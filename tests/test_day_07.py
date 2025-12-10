import pytest

from challenges.day_07 import part_one, part_two


class TestDay07():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            ".......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n...............\n")
    
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 21

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 40

        result = part_two(self.data)

        assert expected == result
