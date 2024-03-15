# Owleye
## Intro
Owleye gives you the posibiliy to transform your webcam to an eye tracker. Owleye is a subsection of my master thesis: "Driver's Hazard Perception Assessment in a Driving Simulator".
At first, you should calibrate your camera, then the program tells you which point you are looking on your monitor. Indeed, this is a top-table eye tracker.
___
## Installation

### 1.Use source code:

Open terminal, download the repo:
`git clone <repo address>`

(or just download the zip file)

Go to the project directory:
`cd Owleye`

make a virtual environment:
`python -m venv env` or `virtualenv env`

activate the virtual environment:

Windows:
`.\env\Scripts\activate`

Linux:
`source env/bin/activate`

Install required libraries:
`pip install -r requirements.txt`

### 2. Use .exe file

Download the release file. It is tested on Windows 10.

## Usage

If you are using the source code, after activating the virtual environment, run main.py:
`python main.py`

or if you have downloaded the Owleye.exe, run it.

In the opened window, there are some parameters that you can change:

![Screenshot 2024-03-13 013738](https://github.com/MustafaLotfi/Owleye/assets/53625380/9e0996ed-560b-4329-b101-1496e51ffb17)



## Method

While the camera is streaming, Owleye gets the images and extracts head and eyes features. Then it feeds this data to the neural networks models to calculate the user's eye view point.

### Input

Owleye receives the user's images during time and extracts their face 478 landmarks/keypoints using Mediapipe library. It's done by canonical face model which is in the world coordinates. Then Owleye extracts below data using the landmarks:
- **Head rotation and position vectors:** (r1, r2, r3), (x, y, z) are calculated using Opencv library
- **Left and right eyes iris:** (xl, yl), (xr, yr). These are calculated respect to the eyes
- **Eyes images:** Two images are concatenated together in rows.

Now, an input of one image (two eyes) and one vector (10 scalar) is ready to calculate the target.

### Output

The output of Owleye is a vector of user's eye view points on screen during time.

### Dataset

221000 samples (eye images and vectors) are collected from 20 male subjects. The subjects were told look at the red point.

### Modeling

Two Convolutional Neural Network (CNNs) models are used to predict the user's eye view point in the horizonal and vertical directions on the monitor.

### Fine-tuning

There are two CNN models that

### Calibration
The calibration process consists of looking at a white point in a black screen for a certain time. Then, the point's position changes and the user must look at it again. This process is repeated until the calibration ends. During this procedure, Owleye collects data (input and output). It means each sample data entails one image, one vector and one location point.


## Limitations and future works
**1) Recunstructing whole code:** The structure of the code is terrible. Owleye is made in 2021. Therefore, a lot of things have changed since then. The structure of the code totally can be redesigned to reach a better performance. The code can be more object oriented. the libraries (mediapipe and tensorflow) have changed a lot. So, the algorithm can be rewritten considering the changes.

**2) Changing the calibration algorithm:** The calibration duration time is really long. Using methods like image morphing makes it unnecessary to collect images from all positions and angles.

**3) Changing the fine-tuning method:** In the current method, to retrain the algorithm, we considered to just change the weights in the last layer of the network. In this way, the network keeps the original shape of itself and just changes the last layer's weights to customize the network for each subject. But, this fine-tuning process can be improved by implementing better solutions.
