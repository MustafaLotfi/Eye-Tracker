import cv2
import pickle
import tuning_parameters as tp
from base import eyeing as ey


subjects_dir = "../subjects/"
target_fol = "data-et-clb/"
# target_fol = "data-boi/"

target_dir = subjects_dir + f"{tp.NUMBER}/" + target_fol

x1, x2, y = ey.load(target_dir, ["x1", "x2", "y"])

print(x1.shape, x2.shape, y.shape)

i = 0
for img in x1:
    print(f"{i}, {y[i]}")
    cv2.imshow("Eyes Image", img)
    q = cv2.waitKey(200)
    if q == ord('q'):
        break
    i += 1

