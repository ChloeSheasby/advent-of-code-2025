import pytest

from challenges.day_09 import part_one, part_two


class TestDay09():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3")
        
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 50

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 24

        result = part_two(self.data)

        assert expected == result
