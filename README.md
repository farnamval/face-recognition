# Face Recognition
Face Recognition using cv2. Program has 3 commands:
- CD (Collect Data) - save monochromatic cropped faces from people-folder to faces-folder
- TR (Train Recognizer) - with using faces from faces-folder, train to predict person with Fisher and LBPH recognizers and save databases to databases-folder
- RP (Recognize People) - predict people on the pictures from source-folder using databases created after Train Recognizer

# Used Packages
- numpy
- opencv-contrib-python
