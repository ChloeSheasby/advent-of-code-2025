# import pytest

# from challenges.day_01 import part_a, part_b, read_puzzle_input_to_arrays


# class TestDay01():
#     @pytest.fixture(autouse=True)
#     def setUp(self) -> None:
#         self.array1 = [3, 4, 2, 1, 3, 3]
#         self.array2 = [4, 3, 5, 3, 9, 3]

#     def test_given_small_input_when_part_a_correct_answer_given(
#             self):
#         expected = 11

#         result = part_a(self.array1, self.array2)

#         assert expected == result

#     def test_given_large_input_when_part_a_correct_answer_given(
#             self):
#         array1, array2 = read_puzzle_input_to_arrays()
#         expected = 2756096

#         result = part_a(array1, array2)

#         assert expected == result

#     def test_given_small_input_when_part_b_correct_answer_given(
#             self):
#         expected = 31

#         result = part_b(self.array1, self.array2)

#         assert expected == result

#     def test_given_large_input_when_part_b_correct_answer_given(
#             self):
#         array1, array2 = read_puzzle_input_to_arrays()
#         expected = 23117829

#         result = part_b(array1, array2)

#         assert expected == result
