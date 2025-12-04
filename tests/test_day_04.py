import pytest

from challenges.day_04 import part_one, part_two


class TestDay03():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n"
            "@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n"
            ".@@@@@@@@.\n@.@.@@@.@."
        )
    
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 13

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 43

        result = part_two(self.data)

        assert expected == result
