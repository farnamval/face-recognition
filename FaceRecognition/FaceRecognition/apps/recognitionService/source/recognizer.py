import cv2
from glob import glob
from . import image_resizing
from . import id_checker
from ..constraits import paths


def recognize_people(databases_path, fisher_database, lbph_database, source_path, face_width, face_height, names):
    detector = cv2.CascadeClassifier(paths.haarcascade_path)
    recognizer_fisher = cv2.face.FisherFaceRecognizer_create()
    recognizer_fisher.read(databases_path + '\\' + fisher_database)
    recognizer_lbph = cv2.face.LBPHFaceRecognizer_create()
    recognizer_lbph.read(databases_path + '\\' + lbph_database)
    font = cv2.FONT_HERSHEY_SIMPLEX

    print(' Starting face recognition...\n'
          ' You can move to the next photo using space bar')

    photos_paths = []
    for extension in ['jpg', 'jpeg', 'png']:
        photos_paths.extend(glob(source_path + '\\**.' + extension))
    photos_paths.sort()

    for photo_path in photos_paths:
        image = cv2.imread(photo_path)
        image = image_resizing.resize_image(image, 1600, 1600)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detected_faces = detector.detectMultiScale(gray, 1.05, 15, minSize=(100, 100))
        faces_lbph = []
        confidences_lbph = []
        faces_fisher = []
        confidences_fisher = []

        for (x, y, w, h) in detected_faces:
            gray_face = gray[y: y + h, x: x + w]
            face, confidence = recognizer_lbph.predict(gray_face)
            faces_lbph.append(face)
            confidences_lbph.append(confidence)

            gray_face = image_resizing.resize_image(gray_face, face_width, face_height, False)
            face, confidence = recognizer_fisher.predict(gray_face)
            faces_fisher.append(face)
            confidences_fisher.append(confidence)

        faces_fisher = id_checker.check_ids(faces_fisher, confidences_fisher, len(names))
        faces_lbph = id_checker.check_ids(faces_lbph, confidences_lbph, len(names))
        counter = 0
        for face in faces_fisher:
            if face == 0:
                faces_fisher[counter] = faces_lbph[counter]
            counter += 1
        face_ids = faces_fisher

        counter = 0
        for (x, y, w, h) in detected_faces:
            if face_ids[counter] != 0:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                person = names[face_ids[counter]]
                cv2.putText(image, str(person), (x + 5, y - 5), font, 1, (25, 153, 0), 2)
            counter += 1

        image = image_resizing.resize_image(image)
        cv2.imshow('Image', image)

        while True:
            if cv2.waitKey(1) & 0xff == 32:
                break

    cv2.destroyAllWindows()
    return None
