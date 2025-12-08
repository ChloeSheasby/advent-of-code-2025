import pytest

from challenges.day_05 import part_one, part_two


class TestDay03():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
        )
    
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 3

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 14

        result = part_two(self.data)

        assert expected == result
