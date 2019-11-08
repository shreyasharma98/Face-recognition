# Face-recognition

Real Time Face Recognition in Python using Opencv and Haarcascade.

### Prerequisites

Numpy</br>
OpenCV
Haarcascades : https://github.com/opencv/opencv/tree/master/data/haarcascades

### Installing

Install Numpy via anaconda:
conda install numpy

Install OpenCV via anaconda:
conda install -c menpo opencv

### Haarcascades
Cascade classifiers are trained on a few hundred sample images of image that contain the object we want to detect, and other images that do not contain those images.. 
#### Haar Feature Selection
There are some common features that we find on most common human faces :
  a dark eye region compared to upper-cheeks
  a bright nose bridge region compared to the eyes
  some specific location of eyes, mouth, nose…
The characteristics are called Haar Features. The feature extraction process will look like this :
<img src="https://maelfabien.github.io/assets/images/haar.jpg" />

# FACE RECOGNITION
## Detection
Detecting Faces in the image using frontalface Haarcascade.
<img src="detect.png" />
## Recognition
  > Detect the faces and Make the dataset of the them : create_dataset.py
  > Train the Machine and create .Yml file of the dataset : train.py
  > Final Recognition : Face_recognition.py
 Result: 
 <img src="recognise.png" />
