# notes_deleter
A DL Based classifier to delete only the images of notes after exams.\
**Android App coming soon**

Model Used: Inception V3

## Why use Google's Inception?

Traditional machine learning approach uses feature extraction for images using Global descriptors such as Local Binary Patterns, Histogram of Oriented Gradients, Color Histograms etc.  These are hand-crafted features that requires domain level expertise.

But in Deep Neural Networks! Instead of using hand-crafted features, Deep Neural Nets automatically learns these features from images in a hierarchical fashion. Lower layers learn low-level features such as Corners, Edges whereas middle layers learn color, shape etc. and higher layers learn high-level features representing the object in the image.

Thus, we can use a **Convolutional Neural Network** as a Feature Extractor by taking the activations available before the last fully connected layer of the network (i.e. before the final softmax classifier). These activations will be acting as the feature vector for a machine learning classifier which further learns to classify it. This type of approach is well suited for Image Classification problems, where instead of training a CNN from scratch (which is time-consuming and tedious), **a pre-trained CNN could be used as a Feature Extractor**.
Which is exactly why we will be using Google's Inception model.



## How To:

 * Create your own notes data set with atleast 700- 1000 images
 * Currently I'm not doing any preprocessing but if you have a slow system then it is recommended to reshape your image into a smaller one. a 200 * 200 or 50 * 50 perhaps.
 * Place the image dataset in the folder -  **"training_dataset"**
 * Run the bat/sh file to train the network
 * To test your NN use - `python classify.py myimage.jpg`

## To-do

* Make it better
* Add image preprocessing
* transfer model for android
* Make android app that automatically deletes file based on this backend
### Stuff used to make this:

 * [Tensorflow Image Recognition](https://www.tensorflow.org/tutorials/image_recognition)
 * [Classify Image](https://github.com/tensorflow/models/blob/master/tutorials/image/imagenet/classify_image.py/)
 * [Image Classifier in 5 minutes](https://www.youtube.com/watch?v=QfNvhPx5Px8)
 * [Flower Recognition using Deep Learning] (https://gogul09.github.io/software/flower-recognition-deep-learning)