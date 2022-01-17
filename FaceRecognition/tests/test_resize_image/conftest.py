import pytest
from os import path, remove


@pytest.fixture(autouse=True)
def delete_test_picture():
    if path.isfile("FaceRecognition\\tests\\test_resize_image\\test_picture.jpg"):
        remove("FaceRecognition\\tests\\test_resize_image\\test_picture.jpg")
