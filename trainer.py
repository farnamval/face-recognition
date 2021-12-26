import cv2
import os
from glob import glob
import numpy
import image_resizing


def train_recognizer(faces_path, databases_path, recognizer_name, face_width=500, face_height=500):
    if recognizer_name != 'LBPH' and recognizer_name != 'Fisher':
        print(" Incorrect recognizer name! Choose between 'LBPH' or 'Fisher'")
        return None

    if recognizer_name == 'LBPH':
        recognizer = cv2.face.LBPHFaceRecognizer_create()
    else:
        recognizer = cv2.face.FisherFaceRecognizer_create()
    print(' Training recognizer...')

    faces = []
    ids = []

    people_faces = os.listdir(faces_path)
    id_number = 1
    for person in people_faces:
        photos_paths = []
        for extension in ['jpg', 'jpeg', 'png']:
            photos_paths.extend(glob(faces_path + '\\' + person + '\\**.' + extension))
        photos_paths.sort()

        for photo_path in photos_paths:
            gray_face = cv2.imread(photo_path, cv2.IMREAD_GRAYSCALE)
            if recognizer_name == 'Fisher':
                gray_face = image_resizing.resize_image(gray_face, face_width, face_height, False)

            faces.append(gray_face)
            ids.append(id_number)
        id_number += 1

    recognizer.train(faces, numpy.array(ids))
    if not os.path.exists(databases_path):
        os.mkdir(databases_path)
    recognizer.write(databases_path + '\\' + recognizer_name + '_database.yml')

    print(' Train was successful')
    return None
