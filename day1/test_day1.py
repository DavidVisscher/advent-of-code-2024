"""
Tests for the functions in day1.py
"""

from pathlib import Path

import pytest

from day1 import parse_lists, find_distances, find_similarity_score


def test_parse_lists():
    left, right = parse_lists(Path("day1/test_input.txt"))
    assert left == [3, 4, 2, 1, 3, 3]
    assert right == [4, 3, 5, 3, 9, 3]


def test_parse_lists_raises_error_if_lists_are_different_lengths():
    with pytest.raises(ValueError):
        find_distances([1, 2], [3, 4, 5])


def test_find_distances():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert find_distances(left, right) == [2, 1, 0, 1, 2, 5]


def test_find_similarity_score():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert find_similarity_score(left, right) == 31


def test_main():
    left, right = parse_lists(Path("day1/main_input.txt"))
    distances = find_distances(left, right)
    assert sum(distances) == 2166959

    score = find_similarity_score(left, right)
    assert score == 23741109
