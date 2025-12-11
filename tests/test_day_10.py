import pytest

from challenges.day_10 import part_one, part_two


class TestDay10():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data = (
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")
        
    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 7

        result = part_one(self.data)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 33

        result = part_two(self.data)

        assert expected == result
