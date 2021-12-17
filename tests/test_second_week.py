import unittest
import pytest
from src.deuxiemeSemaine import thermal_line_horizontal_vertical, thermal_line_coordinator, fishy, many_fishy, counter_fishy, how_many_unique, decode
from collections import Counter
from functools import reduce
from parameterized import parameterized
import os


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            "0,9 -> 5,9",
            Counter(
                {
                    (0, 9): 1,
                    (1, 9): 1,
                    (2, 9): 1,
                    (3, 9): 1,
                    (4, 9): 1,
                    (5, 9): 1,
                }
            ),
        ),
(
            "5,9 -> 0,9",
            Counter(
                {
                    (0, 9): 1,
                    (1, 9): 1,
                    (2, 9): 1,
                    (3, 9): 1,
                    (4, 9): 1,
                    (5, 9): 1,
                }
            ),
        ),
        (
            "7,0 -> 7,4",
            Counter(
                {
                    (7, 0): 1,
                    (7, 1): 1,
                    (7, 2): 1,
                    (7, 3): 1,
                    (7, 4): 1,
                }
            ),
        ),
(
            "7,4 -> 7,0",
            Counter(
                {
                    (7, 0): 1,
                    (7, 1): 1,
                    (7, 2): 1,
                    (7, 3): 1,
                    (7, 4): 1,
                }
            ),
        ),
    ],
)
def test_hydrothermal(test_input, expected):
    assert thermal_line_horizontal_vertical(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            "0,9 -> 5,9",
            Counter(
                {
                    (0, 9): 1,
                    (1, 9): 1,
                    (2, 9): 1,
                    (3, 9): 1,
                    (4, 9): 1,
                    (5, 9): 1,
                }
            ),
        ),
(
            "5,9 -> 0,9",
            Counter(
                {
                    (0, 9): 1,
                    (1, 9): 1,
                    (2, 9): 1,
                    (3, 9): 1,
                    (4, 9): 1,
                    (5, 9): 1,
                }
            ),
        ),
        (
            "7,0 -> 7,4",
            Counter(
                {
                    (7, 0): 1,
                    (7, 1): 1,
                    (7, 2): 1,
                    (7, 3): 1,
                    (7, 4): 1,
                }
            ),
        ),
(
            "7,4 -> 7,0",
            Counter(
                {
                    (7, 0): 1,
                    (7, 1): 1,
                    (7, 2): 1,
                    (7, 3): 1,
                    (7, 4): 1,
                }
            ),
        ),
(
            "0,0 -> 3,3",
            Counter(
                {
                    (0, 0): 1,
                    (1, 1): 1,
                    (2, 2): 1,
                    (3, 3): 1,
                }
            ),
        ),
(
            "3,3 -> 0,0",
            Counter(
                {
                    (0, 0): 1,
                    (1, 1): 1,
                    (2, 2): 1,
                    (3, 3): 1,
                }
            ),
        ),
(
            "2,0 -> 0,3",
            Counter(
                {
                    (2, 0): 1,
                    (1, 1): 1,
                    (0, 2): 1
                }
            ),
        ),
(
            "0,2 -> 2,0",
            Counter(
                {
                    (2, 0): 1,
                    (1, 1): 1,
                    (0, 2): 1
                }
            ),
        ),
    ],
)
def test_hydrothermal_diagonal(test_input, expected):
    assert thermal_line_coordinator(test_input) == expected



@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [
                Counter(
                    {
                        (0, 9): 1,
                        (1, 9): 1,
                        (2, 9): 1,
                        (3, 9): 1,
                        (4, 9): 1,
                        (5, 9): 1,
                    }
                ),
                Counter({(1, 8): 1,
                         (1, 9): 1,
                         (1, 10): 1
                         }),
            ],
            Counter(
                {
                    (0, 9): 1,
                    (1, 9): 2,
                    (2, 9): 1,
                    (3, 9): 1,
                    (4, 9): 1,
                    (5, 9): 1,
                    (1, 8): 1,
                    (1, 10): 1
                }
            ),

        ),

    ],
)
def test_add_hydrothermal(test_input, expected):
    assert (test_input[0]+test_input[1]) == expected





@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [
                Counter(
                    {
                        (0, 9): 1,
                        (1, 9): 1,
                        (2, 9): 1,
                        (3, 9): 1,
                        (4, 9): 1,
                        (5, 9): 1,
                    }
                ),
                Counter({(1, 8): 1,
                         (1, 9): 1,
                         (1, 10): 1
                         }),
            ],
            Counter(
                {
                    (0, 9): 1,
                    (1, 9): 2,
                    (2, 9): 1,
                    (3, 9): 1,
                    (4, 9): 1,
                    (5, 9): 1,
                    (1, 8): 1,
                    (1, 10): 1
                }
            ),

        ),

    ],
)
def test_add_hydrothermal(test_input, expected):
    assert (test_input[0]+test_input[1]) == expected

@pytest.mark.parametrize("test_input, expected",
        [
            (2,[1]),
            (1,[0]),
            (0,[6,8])
        ]                         )
def test_fishy_reproduction(test_input,expected):
    assert fishy(test_input) == expected

@pytest.mark.parametrize("test_input, expected",
        [
            ([3,4,3,1,2],[2,3,2,0,1]),
            ([6,0,6,4,5,6,0,1,1,2,6,7,8,8,8], [5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8])
        ]
)
def test_many_fishy_reproduction(test_input,expected):
    assert counter_fishy(test_input,1).sort() == expected.sort()
    # assert many_fishy(test_input).sort() == expected.sort()


def test_day_five_one_integration():

    with open("../src/day5test.txt") as f:
        thermal_vents = [thermal_line_horizontal_vertical(line.strip()) for line in f]

    total = sum(thermal_vents, Counter() )

    assert sum([1 for i in total.items() if i[1]!=1]) == 5

def test_day_six_one_integration():

    fishes = [3,4,3,1,2]

    # for i in range(18):
    #     fishes = fishy(fishes)
    test = (counter_fishy(fishes,256))

    assert fishes.sort() == [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8].sort()

@pytest.mark.parametrize("test_input, expected",
    [
        (["fdgacbe", "cefdb cefbgd", "gcbe"], 2 ),
        (["fdgacbe", "cefdb cefbgd", "gcbe", "fg", "fgae"], 4 )
    ]
)
def test_how_many_unique(test_input, expected):
    assert how_many_unique(test_input) == expected

def test_day_six_one_integration():
    pre = []
    post = []
    with open("../src/day8test.txt") as f:
        for line in f:
            t_pre,t_post = line.strip().split('| ')
            pre.append(t_pre.split())
            post.append(t_post.split())
    result = sum(map(how_many_unique,post))
    assert result == 26

@pytest.mark.parametrize("test_input, expected",
    [
        ((["acedgfb", "cdfbe" ,"gcdfa" ,"fbcad" ,"dab" ,"cefabd" ,"cdfgeb" ,"eafb" ,"cagedb", "ab"],
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"]), 5353  ),

    ]
)
def test_decode(test_input, expected):
    assert decode(test_input) == expected
