import os
from codes.show import Camera
from codes.calibrate import Calibration
from codes.do_sampling import Smp
from codes.tune_model_pars import Tuning
from codes.get_eye_track import EyeTrack
from codes.get_model import Modeling
from codes.see_data import See


# *********************** PARAMETERS ***********************
NUMBER = 16
CAMERA_ID = 2

# *********************** SEE CAMERA ***********************
# Camera().raw(CAMERA_ID)
# Camera().features(CAMERA_ID)

# *********************** CALIBRATION **********************
# NAME = "Mostafa Lotfi"
# GENDER = "M"
# AGE = 25
# Descriptions = "3 monitors"
# CALIBRATION_GRID = 2, 10
# INFO = (NAME, GENDER, AGE, Descriptions)
# Calibration().et(NUMBER, CAMERA_ID, INFO, CALIBRATION_GRID)
# Calibration().boi(NUMBER, CAMERA_ID, 20)

# # *********************** SAMPLING *************************
# Smp().sampling(NUMBER, CAMERA_ID)

# # *********************** TESTING **************************
# Smp().testing(NUMBER, CAMERA_ID)

# # ********************* SEE FEATURES ***********************
# See().data_features(NUMBER, "et")
# See().data_features(NUMBER, "boi")
# See().data_features(NUMBER, "smp")
# See().data_features(NUMBER, "tst")

# # *********************** MODELING *************************
# Tuning().boi_mdl(NUMBER, 2, 2, 1, 1, delete_files=True)
# Tuning().et_mdl(NUMBER, 2, 2, 1, 1, delete_files=True)

# # *********************** GET PIXELS ***********************
# EyeTrack().get_pixels(NUMBER)

# # ******************* GET TESTING PIXELS *******************
# EyeTrack().get_pixels(NUMBER, True, delete_files=True)

# # ******************** GET FIXATIONS ***********************
# EyeTrack().get_fixations(NUMBER)

# # ***************** GET TESTINGT FIXATIONS *****************
# EyeTrack().get_fixations(NUMBER, True)

# ***************** SEE SAMPLING PIXELS ********************
See().pixels(NUMBER)

# ***************** SEE TESTING PIXELS *********************
See().pixels_test(NUMBER)

# ***************** CREATE PUBLIC MODELS *******************
# mdl = Modeling()
# mdl.create_boi()
# mdl.create_et()
# mdl.train_boi(subjects=[1], n_epochs=2, patience=1)
# mdl.train_et(subjects=[1], n_epochs=2, patience=1)