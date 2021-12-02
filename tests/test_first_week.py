import unittest
import pytest
from src.premiereSemaine import sliding_comparer,tuple_list_from_text,generate_direction
from parameterized import parameterized
import os

@pytest.fixture(autouse=True)
def day_two_file():
    output_list = [("a","1"),("b","2"),("c","3")]
    with open("test_day_two.txt", "w") as fp:
        fp.write('\n'.join("{} {}".format(x[0], x[1]) for x in output_list))
    yield
    os.remove("test_day_two.txt")

@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([1, 2, 3], 2),
        ([0, 0, 0], 0),
        ([0, 1, 0], 1),
        ([-1, 0, 1], 2),
    ],
)
def test_sliding_comparer_pytest(test_input, expected):
    assert sliding_comparer(test_input) == expected


def test_tuple_list_from_text(day_two_file):
    results = tuple_list_from_text("test_day_two.txt")
    print("here")
    assert (type(results[0]) == type((1,2))) &  (type(results[0][0])==type("string")) &  (type(results[0][1])==type(1))


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (("forward",1),(1,0)),
        (("down",1),(0,1)),
        (("up",1),(0,-1)),
    ]
)
def test_reading_directions(test_input, expected):
    test_case = ("forward",1)

    assert generate_direction(test_input)==expected


# #using parameterized to test it
# class TestSequence(unittest.TestCase):
#     @parameterized.expand([
#         ["standard",[1,2,3],2],
#         ["all zeros", [0,0,0],0],
#         ["negative and positive", [-1,0,2],2],
#         ["partial increase",[0,0,1],1],
#     ])
#     def test_sliding_comparer_success(self,name,a,b):
#         self.assertEqual(sliding_comparer(a),b)