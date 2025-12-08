import pytest

from challenges.day_06 import part_one, part_two


class TestDay03():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
        )
    
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 4277556

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 3263827

        result = part_two(self.data)

        assert expected == result
