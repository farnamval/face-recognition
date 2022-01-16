from FaceRecognition.apps.trainService.Source.image_resizing import resize_image
import pytest
import shutil
import cv2


original_path = "FaceRecognition\\tests\\test_resize_image\\original_picture.jpg"
test_path = "FaceRecognition\\tests\\test_resize_image\\test_picture.jpg"


def create_picture_copy(original, test):
    shutil.copy(original, test)


def test_resize_image_no_parameters():
    create_picture_copy(original_path, test_path)
    test_image = cv2.imread(test_path)
    assert resize_image(test_image).shape == (768, 1365, 3)


@pytest.mark.parametrize("width, height, expected_shape",
                         [(1600, 900, (900, 1600, 3)),
                          (900, 1600, (506, 900, 3))])
def test_resize_image_with_width_and_height(width, height, expected_shape):
    create_picture_copy(original_path, test_path)
    test_image = cv2.imread(test_path)
    assert resize_image(test_image, width, height).shape == expected_shape


@pytest.mark.parametrize("width, height, expected_shape",
                         [(1600, 900, (900, 1600, 3)),
                          (900, 1600, (1600, 900, 3)),
                          (1600, 1600, (1600, 1600, 3))])
def test_resize_image_without_save_scaling(width, height, expected_shape):
    create_picture_copy(original_path, test_path)
    test_image = cv2.imread(test_path)
    assert resize_image(test_image, width, height, False).shape == expected_shape


@pytest.mark.parametrize("width, height, expected_exception",
                         [("900", 1600, TypeError),
                          ("900", "1600", TypeError)])
def test_resize_image_error(width, height, expected_exception):
    create_picture_copy(original_path, test_path)
    test_image = cv2.imread(test_path)
    with pytest.raises(expected_exception):
        resize_image(test_image, width, height, False)
