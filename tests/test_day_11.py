import pytest

from challenges.day_11 import part_one, part_two


class TestDay11():
    @pytest.fixture(autouse=True)
    def setUp(self) -> None:
        self.data1 = (
            "aaa: you hhh\nyou: bbb ccc\nbbb: ddd eee\nccc: ddd eee fff\nddd: ggg\neee: out\nfff: out\nggg: out\nhhh: ccc fff iii\niii: out")
        
        self.data2 = (
            "svr: aaa bbb\naaa: fft\nfft: ccc\nbbb: tty\ntty: ccc\nccc: ddd eee\nddd: hub\nhub: fff\neee: dac\ndac: fff\nfff: ggg hhh\nggg: out\nhhh: out"
        )

    def test_given_test_input_when_part_one_correct_answer_given(
            self):
        expected = 5

        result = part_one(self.data1)

        assert expected == result

    def test_given_test_input_when_part_two_correct_answer_given(
            self):
        expected = 2

        result = part_two(self.data2)

        assert expected == result
