import pytest

from challenges.day_02 import part_one, part_two


class TestDay02():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 1227775554

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 4174379265

        result = part_two(self.data)

        assert expected == result
