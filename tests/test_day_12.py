import pytest

from challenges.day_12 import part_one, part_two


class TestDay12():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "0:\n###\n##.\n##.\n\n1:\n###\n##.\n.##\n\n2:\n.##\n###\n##.\n\n3:\n##.\n###\n##.\n\n4:\n###\n#..\n###\n\n5:\n###\n.#.\n###\n\n\n4x4: 0 0 0 0 2 0\n12x5: 1 0 1 0 2 2\n12x5: 1 0 1 0 3 2")

    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 2

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 2

        result = part_two(self.data)

        assert expected == result
