import unittest
import pytest
from src.premiereSemaine import (
    sliding_comparer,
    tuple_list_from_text,
    generate_direction_part_one,
    generate_direction_part_two,
    accumulate_binary,
    gamma_to_epsilon,
    list_of_bit_to_int,
    day_3_io,
    validate_card,
    oxygen_rate,
    accumulate_binary_oxygen,
    carbon_rate
)
from parameterized import parameterized
import os


@pytest.fixture(autouse=True)
def day_two_file():
    output_list = [("a", "1"), ("b", "2"), ("c", "3")]
    with open("test_day_two.txt", "w") as fp:
        fp.write("\n".join("{} {}".format(x[0], x[1]) for x in output_list))
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
    assert (
        (type(results[0]) == type((1, 2)))
        & (type(results[0][0]) == type("string"))
        & (type(results[0][1]) == type(1))
    )


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (("forward", 1), (1, 0)),
        (("down", 1), (0, 1)),
        (("up", 1), (0, -1)),
    ],
)
def test_reading_directions_part_one(test_input, expected):

    assert generate_direction_part_one(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((("forward", 5), 0), (5, 0, 0)),
        ((("forward", 5), 1), (5, 5, 1)),
        ((("down", 5), 5), (0, 0, 10)),
        ((("up", 10), 5), (0, 0, -5)),
        ((("forward", 10), -5), (10, -50, -5)),
    ],
)
def test_reading_directions_part_two(test_input, expected):

    assert generate_direction_part_two(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], ([1, 0, 0])),
        ([[1, 1, 0], [1, 0, 1], [0, 0, 1], [0, 0, 1]], ([0, 0, 1])),
    ],
)
def test_accumulating_binary(test_input, expected):

    assert accumulate_binary(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([0, 0, 0, 0], ([1, 1, 1, 1])),
        ([1, 1, 0, 0], ([0, 0, 1, 1])),
        ([1, 0, 1, 1, 0], [0, 1, 0, 0, 1]),
    ],
)
def test_gamma_to_epsilon(test_input, expected):

    assert gamma_to_epsilon(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [([1, 0], (2)), ([1, 0, 1, 1, 0], (22)), ([0, 1, 0, 0, 1], 9)],
)
def test_list_of_bit_to_int(test_input, expected):
    assert list_of_bit_to_int(test_input) == expected


def test_day_three_part_one_integration():
    # tests if the proper gamma rate is obtained
    arr = day_3_io("../src/day3test.txt")

    total = accumulate_binary(arr)
    gamma = total
    epsilon = gamma_to_epsilon(total)

    assert list_of_bit_to_int(gamma) * list_of_bit_to_int(epsilon) == 198


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([[1, 1, 0], [1, 1, 1], [0, 1, 1]], [1, 1, 1]),
        ([[1, 1, 1], [1, 1, 0], [0, 1, 1]], [1, 1, 1]),
        ([[0, 1, 1], [1, 1, 0], [1, 1, 1]], [1, 1, 1]),
    ],
)
def test_oxygen_rate(test_input, expected):
    assert oxygen_rate(test_input) == expected

def test_day_three_part_two_integration():
    # tests if the proper gamma rate is obtained
    arr = day_3_io("../src/day3test.txt")


    oxygen = list_of_bit_to_int(oxygen_rate(arr))
    carbon = list_of_bit_to_int(carbon_rate(arr))


    assert (oxygen == 23) & (carbon == 10 )




@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            False,
        ),
        (
            [
                [1, 0, 0],
                [0, 0, 1],
                [0, 1, 0],
            ],
            False,
        ),
        (
            [
                [1, 1, 1],
                [0, 0, 0],
                [0, 0, 0],
            ],
            True,
        ),
        (
            [
                [1, 0, 0],
                [1, 0, 0],
                [1, 0, 0],
            ],
            True,
        ),
        (
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ],
            True,
        ),
    ],
)
def test_day_four_validate_grids(test_input, expected):
    assert validate_card(test_input) == expected


@pytest.mark.parametrize(
    "i_card,i_number, expected",
    [
        (
            [
                [10, 7, 9],
                [99, 65, 11],
                [78, 36, 24],
            ],
            65,
            (1, 1),
        ),
        (
            [
                [10, 7, 9],
                [99, 65, 11],
                [78, 36, 24],
            ],
            11,
            (2, 1),
        ),
        (
            [
                [10, 7, 9],
                [99, 65, 11],
                [78, 36, 24],
            ],
            299,
            (-1, -1),
        ),
    ],
)
def test_day_four_check_new_number(i_card, i_number, expected):
    assert validate_card(i_card, i_number) == expected
