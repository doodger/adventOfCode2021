import unittest
import pytest
from src.premiereSemaine import sliding_comparer
from parameterized import parameterized


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([1, 2, 3], 2),
        ([0, 0, 0], 0),
    ],
)
def test_sliding_comparer_pytest(test_input, expected):
    assert sliding_comparer(test_input) == expected


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
