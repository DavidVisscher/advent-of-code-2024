"""
Advent of Code 2024 Day 2
=========================
"""


from typing import List
from enum import Enum
from pathlib import Path

class Direction(Enum):
    INCREASING = 1
    DECREASING = 2


def read_reports(filepath: Path) -> List[List[int]]:
    """
    Reads the reports from a file.
    """
    out = []
    with open(filepath, 'r') as file:
        for line in file:
            out.append(list(map(int, line.strip().split())))
    return out


def safety_score(reports: List[List[int]], problem_damper: bool = False) -> int:
    """
    Determines the safety score of a list of reports.
    A safety score is the number of safe reports in the list.
    
    If the problem damper is enabled, the report is allowed to contain one erroneous level.
    If we remove that level and the report is then safe, we count it as safe.
    """
    if not problem_damper:
        score = filter(lambda x: x, map(determine_safety, reports))
        return len(list(score))
    else:
        score = 0
        for report in reports:
            for variation in generate_variations(report):
                if determine_safety(variation):
                    score += 1
                    break
        return score

def generate_variations(report: List[int]) -> List[List[int]]:
    """
    Generates all variations of a report by removing one level at a time.
    """
    out = []
    for i in range(len(report)):
        variation = report.copy()
        del variation[i]
        out.append(variation)
    return out
    

def determine_safety(report: List[int]) -> bool:
    """
    Determines the safety of a report.
    
    A report is safe if the difference between consecutive levels is less than 3.
    A report must also be either strictly increasing or strictly decreasing.
    """
    direction = determine_direction(report)
   
    
    for i in range(1, len(report)):
        difference = report[i] - report[i-1]
        
        if direction == Direction.INCREASING:
            if difference > 3 or difference <= 0:
                return False
        else:  # Direction.DECREASING
            if difference < -3 or difference >= 0:
                return False
                
    return True


def determine_direction(report: List[int]) -> Direction:
    """
    Determines the direction of a report.
    
    A report is strictly increasing if the first level is less than the last level.
    A report is strictly decreasing if the first level is greater than the last level.
    """
    if report[0] > report[-1]:
        return Direction.DECREASING
    else:
        return Direction.INCREASING
