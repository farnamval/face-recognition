from django.conf import settings
import os

haarcascade_path = os.path.join(settings.DATA_ROOT, "haarcascade_frontalface_default.xml")
test_data_root = settings.TEST_DATA_ROOT
buffer_root = settings.MEDIA_ROOT
users_data_root = settings.USERS_DATA_ROOT
people_path = os.path.join(users_data_root, 'People')
faces_path = os.path.join(users_data_root, 'Faces')
source_path = os.path.join(users_data_root, 'Source')
cv2DataBases_path = os.path.join(users_data_root, 'cv2DataBases')
people_path_test = os.path.join(test_data_root, 'People')
faces_path_test = os.path.join(test_data_root, 'Faces')
source_path_test = os.path.join(test_data_root, 'Source')
cv2DataBases_path_test = os.path.join(test_data_root, 'cv2DataBases')
