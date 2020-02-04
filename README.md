# abyss_CNN suite.
### Erik Muller jan 2020.
python code to form input image set, build CNN and run CNN prediction on an input image.

### Dependencies (for detector.py / CNN_helper.py):
+ cv2 (openCV)
+ Tensorflow
+ numpy

Additional dependencies (for make_imageset.py, train_abyss_CNN.py)
+ glob
+ pickle
+ matplotlib

### OVERVIEW:
  Three scripts (detector.py, make_imageset and train_abyss_CNN),
  and one library CNN_helper. The root directory containing the trained model
  is specified in CNN_helper, as is the size of the images used to train the
  CNN (32 is good, 64 is better, 128 is okay, but starts to become slow.)

  'detector.py' script loads a previously-saved CNN trained model ( with
  train_abyss_CNN), and predicts if an input image is contains a lens flare
  (returns 1) or does not (not-flared; returns 0).

  'make_imageset.py' builds a new pickle file holding the training image data
  to be used by train_abyss_CNN.

  'train_abyss_CNN' trains a new CNN model, used by detector.py

  File CNN_helper contains the directory path to the model, which must be
  in the same directory as the test images. The image to be tested by
  detector.py is given relative to the path of the model.

  USAGE:
  Python detector.py <filename> (python 2.7+, python 3.x)
  where filename is the path to target file,
  appended to the 'rootDir' variable set in CNN_helper

  E.g. if a CNN model is located at ./training, and the images are stored
  in ./training/images, such as ./training/images/G0055569.JPG
  specify rootDIr =  './training/' in CNN_helper
  CNN_helper also contains an imageSize variable, this size must match the model
  otherwise an error will be generated.

  EXAMPLE:
  Python detector.py good/G0055569.JPG
------
------

### CNN TRAINING (python 3.x only):
### Preparation of image set.

    To build a bespoke model predictor, images must be appropraitely sized,
    filtered and smoothed, then stacked consistently with tensorflow
    expectation.

    The make_imageset.py will do this, again with CNN_helper depencencies.
    The desired image size is specified in CNN_helper; imageSize = <pixels>,
    where <pixels> indicates the number of pixels along a side of the resulting
    images. Pixel length is best kept as a power of two to improve efficiency,
    but it is not very important. Note that training of the CNN is proportional
    to <pixels> x ¬10, a practical limit for a low-end laptop is pixels =  256.

    The rootDir variable in CNN_helper should be set to the path (relative or
    absolute) of the training image data. The images must be stored in to
    directories: 'good' and 'flare', which contain the relevant images.

    OUTPUT:
    The result of executing make_imageset is a pickle file, containing two
    lists of processed 'good' and 'flared' images. The pickle file is saved at
    the path given in <rootDir>.

    EXAMPLE:
    make_imageset.py
------
### Training the CNN.

    A model is necessary to make predictions, and the train_abyss_CNN.py script
    will build a 5-layer neural network (configurable in CNN_helper), via
    tensorflow. Tensorflow expects a specific format and structure of the images
    and their labels, and make_imageset.py (above) takes an file path to build
    the necessary image format and save it as a pickle file. The pickel file is
    retrived with train_abyss_CNN, correctly parsed and handed to tensorflow.

    The expected pickle file must exist at the rootDir, and be
    called 'flaretraining.pkl'. Note that the version of python used to build
    the pickel file must be the same as the version used to unpack it (i.e. do
    not use python 3.3 to run 'make_imageset.py', then python 3.3 to run
    'train_abyss_CNN.py')
------
