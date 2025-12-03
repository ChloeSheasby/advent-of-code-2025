import pytest

from challenges.day_03 import part_one, part_two


class TestDay03():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
    
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 357

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 3121910778619

        result = part_two(self.data)

        assert expected == result
