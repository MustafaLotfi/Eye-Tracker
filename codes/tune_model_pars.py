from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.utils import shuffle
from joblib import load as j_load
from joblib import dump as j_dump
import pickle
import numpy as np
import os


def boi(mdl_boi_num, sbj_num):
    path2root = "../"
    subjects_fol = "subjects/"
    models_fol = "models/"
    models_boi_fol = "boi/"
    trained_fol = "trained/"
    data_boi_fol = "data-boi/"
    r_train = 0.85
    n_epochs = 2
    patience = 1
    trainable_layers = 1
    chosen_inputs = [0, 1, 2, 6, 7, 8, 9]

    trained_dir = path2root + models_fol + models_boi_fol + trained_fol
    public_model_dir = trained_dir + f"model{mdl_boi_num}"
    public_scalers_dir = trained_dir + f"scalers{mdl_boi_num}.bin"
    sbj_dir = path2root + subjects_fol + f"{sbj_num}/"

    print("\nLoading subject data in in_blink_out folder...")
    data_boi_dir = sbj_dir + data_boi_fol
    with open(data_boi_dir + "x1.pickle", "rb") as f:
        x1_load = pickle.load(f)
    with open(data_boi_dir + "x2.pickle", "rb") as f:
        x2_load = pickle.load(f)
    with open(data_boi_dir + "y.pickle", "rb") as f:
        y_load = pickle.load(f)
    n_smp, frame_h, frame_w = x1_load.shape[:-1]
    print(f"Sapmles number: {n_smp}")

    print("\nNormalizing data...")
    x2_chs_inp = x2_load[:, chosen_inputs]
    scalers = j_load(public_scalers_dir)
    x1_scaler, x2_scaler = scalers
    x1 = x1_load / x1_scaler
    x2 = x2_scaler.transform(x2_chs_inp)
    scalers_dir = sbj_dir + "scalers-boi.bin"
    j_dump(scalers, scalers_dir)

    print("\nShuffling data...")
    x1_shf, x2_shf, y_shf = shuffle(x1, x2, y_load)

    print("\nSplitting data to train and test...")
    n_train = int(r_train * n_smp)
    x1_train, x2_train = x1_shf[:n_train], x2_shf[:n_train]
    x1_test, x2_test = x1_shf[n_train:], x2_shf[n_train:]
    y_train = y_shf[:n_train]
    y_test = y_shf[n_train:]
    print("Data shapes:")
    print(x1_train.shape, x1_test.shape, x2_train.shape, x2_test.shape,
          y_train.shape, y_test.shape)

    y_train_ctg = to_categorical(y_train)
    y_test_ctg = to_categorical(y_test)

    x_train = [x1_train, x2_train]
    x_test = [x1_test, x2_test]

    print("\nLoading 'blink_out_in' model...")
    cb = EarlyStopping(patience=patience, verbose=1, restore_best_weights=True)
    model = load_model(public_model_dir)

    for layer in model.layers[:-trainable_layers]:
        layer.trainable = False
    print("\nModel summary:")
    print(model.summary())

    print("\nRetraining the model...")
    model.fit(x_train,
              y_train_ctg,
              validation_data=(x_test, y_test_ctg),
              epochs=n_epochs,
              callbacks=cb)
    print("End of retraining...")

    model.save(sbj_dir + "model-boi")


def et(mdl_et_num, sbj_num):
    path2root = "../"
    models_fol = "models/"
    models_et_fol = "et/"
    trained_fol = "trained/"
    subjects_dir = "subjects/"
    data_et_fol = "data-et-clb/"
    sbj_scalers_boi_fol = "scalers-boi.bin"
    sbj_model_boi_fol = "model-boi"
    r_train = 0.85
    n_epochs = 5
    patience = 2
    trainable_layers = 1
    chosen_inputs = [0, 1, 2, 6, 7, 8, 9]

    sbj_dir = path2root + subjects_dir + f"{sbj_num}/"
    trained_dir = path2root + models_fol + models_et_fol + trained_fol

    # ### Retraining 'eye_tracking' model with subject calibration data

    data_et_dir = sbj_dir + data_et_fol
    print(f"\nLoading subject data in {data_et_dir}")
    with open(data_et_dir + "x1.pickle", "rb") as f:
        x1_load = pickle.load(f)
    with open(data_et_dir + "x2.pickle", "rb") as f:
        x2_load = pickle.load(f)
    with open(data_et_dir + "y.pickle", "rb") as f:
        y_load = pickle.load(f)
    n_smp, frame_h, frame_w = x1_load.shape[:-1]
    print(f"Samples number: {n_smp}")

    # Displaying data

    # #### Getting those data that looking 'in' screen

    print("\nNormalizing data...")
    sbj_scalers_boi_dir = sbj_dir + sbj_scalers_boi_fol
    x2_chs_inp = x2_load[:, chosen_inputs]
    x1_scaler_boi, x2_scaler_boi = j_load(sbj_scalers_boi_dir)
    x1_boi = x1_load / x1_scaler_boi
    x2_boi = x2_scaler_boi.transform(x2_chs_inp)

    print("\nLoading in_blink_out model...")
    sbj_model_boi_dir = sbj_dir + sbj_model_boi_fol
    model_boi = load_model(sbj_model_boi_dir)
    print(model_boi.summary())

    print("\nPredicting those data that looking 'in' screen.")
    yhat_boi = model_boi.predict([x1_boi, x2_boi]).argmax(1)

    # Choosing those data
    x1_new = []
    x2_new = []
    y_new = []
    for (x10, x20, y0, yht0) in zip(x1_load, x2_load, y_load, yhat_boi):
        if True:  # yht0 != 1:
            x1_new.append(x10)
            x2_new.append(x20)
            y_new.append(y0)

    x1_new = np.array(x1_new)
    x2_new = np.array(x2_new)
    y_new = np.array(y_new)
    n_smp_new = x1_new.shape[0]
    print(f"New samples: {n_smp_new}")

    # ### Preparing modified calibration data to feeding in eye_tracking model

    print("\nNormalizing modified calibration data to feeding in eye_tracking model...")
    public_scalers_et_dir = trained_dir + f"scalers{mdl_et_num}.bin"
    x2_chs_inp_new = x2_new[:, chosen_inputs]
    scalers_et = j_load(public_scalers_et_dir)
    x1_scaler_et, x2_scaler_et, _ = scalers_et

    x1_nrm = x1_new / x1_scaler_et
    x2_nrm = x2_scaler_et.transform(x2_chs_inp_new)

    y_scalers_et = np.max(y_new, 0)
    y_nrm = y_new / y_scalers_et

    scalers_et[2] = y_scalers_et
    j_dump(scalers_et, sbj_dir + "scalers-et.bin")

    # Shuffling and splitting data to train and test
    x1_shf, x2_shf, y_hrz_shf, y_vrt_shf = shuffle(x1_nrm, x2_nrm, y_nrm[:, 0], y_nrm[:, 1])

    n_train = int(r_train * n_smp_new)
    x1_train, x2_train = x1_shf[:n_train], x2_shf[:n_train]
    x1_test, x2_test = x1_shf[n_train:], x2_shf[n_train:]
    y_hrz_train, y_vrt_train = y_hrz_shf[:n_train], y_vrt_shf[:n_train]
    y_hrz_test, y_vrt_test = y_hrz_shf[n_train:], y_vrt_shf[n_train:]

    x_train = [x1_train, x2_train]
    x_test = [x1_test, x2_test]

    print(x1_train.shape, x1_test.shape, y_hrz_train.shape, y_hrz_test.shape,
          x2_train.shape, x2_test.shape, y_vrt_train.shape, y_vrt_test.shape)

    # Callback for training
    cb = EarlyStopping(patience=patience, verbose=1, restore_best_weights=True)

    print("Loading public eye_tracking models...")
    public_model_et_dir = trained_dir + f"model{mdl_et_num}"
    model_hrz = load_model(public_model_et_dir + "-hrz")
    model_vrt = load_model(public_model_et_dir + "-vrt")

    for (layer_hrz, layer_vrt) in zip(model_hrz.layers[:-trainable_layers], model_vrt.layers[:-trainable_layers]):
        layer_hrz.trainable = False
        layer_vrt.trainable = False

    print(model_hrz.summary())

    print("\nStart of training for model 1 (x-pixels)")
    model_hrz.fit(x_train,
                  y_hrz_train,
                  validation_data=(x_test, y_hrz_test),
                  epochs=n_epochs,
                  callbacks=cb)
    print("End of training")

    print("\nStart of training for model 2 (y-pixels)")
    model_vrt.fit(x_train,
                  y_vrt_train,
                  validation_data=(x_test, y_vrt_test),
                  epochs=n_epochs,
                  callbacks=cb)
    print("End of training")

    print("\nSaving models...")
    model_hrz.save(sbj_dir + "model-et-hrz")
    model_vrt.save(sbj_dir + "model-et-vrt")
