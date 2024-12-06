"""
Advent of Code 2024 Day 2
=========================

Test suite for day2.py
"""

from day2 import determine_safety, Direction, determine_direction, read_reports, safety_score
from pathlib import Path


def test_determine_safety():
    """
    Tests the whole example given in the problem statement.
    """
    assert determine_safety([7, 6, 4, 2, 1]) is True
    assert determine_safety([1, 2, 7, 8, 9]) is False
    assert determine_safety([9, 7, 6, 2, 1]) is False
    assert determine_safety([1, 3, 2, 4, 5]) is False
    assert determine_safety([8, 6, 4, 4, 1]) is False
    assert determine_safety([1, 3, 6, 7, 9]) is True

def test_determine_direction():
    """
    Tests the direction determination function.
    """
    assert determine_direction([7, 6, 4, 2, 1]) == Direction.DECREASING
    assert determine_direction([1, 2, 7, 8, 9]) == Direction.INCREASING

def test_read_reports():
    """
    Tests the report reading function.
    """
    reports = read_reports(Path('day2/test_reports.txt'))
    assert reports == [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

def test_safety_score():
    """
    Tests the safety score function.
    """
    reports = read_reports(Path('day2/test_reports.txt'))
    assert safety_score(reports) == 2

def test_safety_score_with_problem_damper():
    """
    Tests the safety score function with the problem damper enabled.
    """
    reports = read_reports(Path('day2/test_reports.txt'))
    assert safety_score(reports, problem_damper=True) == 4

def test_main():
    """
    Tests the main function.
    """
    assert safety_score(read_reports(Path('day2/reports.txt'))) == 534 
    assert safety_score(read_reports(Path('day2/reports.txt')), problem_damper=True) == 577