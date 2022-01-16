from FaceRecognition.apps.recognitionService.source.id_checker import check_ids
import pytest


@pytest.mark.parametrize("people, confidence, number_of_ids, expected_result",
                         [([1, 2], [1, 1], 3, [1, 2]),
                          ([1, 1, 2], [1, 2, 2], 3, [1, 0, 2]),
                          ([1, 1, 2], [3, 2, 2], 3, [0, 1, 2]),
                          ([1, 1, 2], [2, 2, 3], 3, [1, 1, 2]),
                          ([1, 1, 1], [2, 3, 3], 3, [1, 0, 0]),
                          ([1, 1, 2, 2], [3, 2, 2, 3], 3, [0, 1, 2, 0])])
def test_check_ids_good(people, confidence, number_of_ids, expected_result):
    assert check_ids(people, confidence, number_of_ids) == expected_result


@pytest.mark.parametrize("people, confidence, number_of_ids, expected_exception",
                         [([1, 2, 2], [1, 2, 3], 2, IndexError),
                          ([1, 2, 2], [1, 2], 3, IndexError)])
def test_check_ids_error(people, confidence, number_of_ids, expected_exception):
    with pytest.raises(expected_exception):
        check_ids(people, confidence, number_of_ids)
