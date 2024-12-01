"""
Advent of Code 2024 Day 1
=========================
"""

from pathlib import Path
from typing import Tuple, List


def parse_lists(file_path: Path) -> Tuple[List[int], List[int]]:
    """
    Reads the input file and returns two lists of integers.

    The input file should contain pairs of numbers separated by three spaces.
    Each pair should be on a new line.

    Args:
        file_path: Path to the input file

    Returns:
        A tuple containing two lists:
        - The first list contains the left numbers from each pair
        - The second list contains the right numbers from each pair

    Example input file:
        3   4
        4   3
        2   5
    """
    left, right = [], []

    with open(file_path, "r") as file:
        while line := file.readline():
            l_part, r_part = line.split("   ")
            left.append(int(l_part))
            right.append(int(r_part))

    return left, right


def find_distances(left: List[int], right: List[int]) -> List[int]:
    """
    Finds the distances between corresponding numbers in two lists after sorting.

    The function sorts both input lists independently and then calculates the
    absolute difference between corresponding positions.

    Args:
        left: First list of integers
        right: Second list of integers. Must be same length as left list.

    Returns:
        A list containing the absolute differences between corresponding
        numbers after sorting both input lists.

    Example:
        left = [3, 4, 2]
        right = [4, 3, 5]
        Returns: [1, 0, 1]  # After sorting: [2-3, 3-3, 4-5]
    """
    distances = []
    l_sorted = sorted(left)
    r_sorted = sorted(right)

    # Check that the lists are the same length
    if len(l_sorted) != len(r_sorted):
        raise ValueError("Lists must be the same length")

    # Create pairs of left and right numbers
    for index, l in enumerate(l_sorted):
        r = r_sorted[index]
        distances.append(abs(l - r))

    return distances


def find_similarity_score(left: List[int], right: List[int]) -> int:
    """
    Finds the similarity score between two lists by counting occurrences.

    For each number in the left list, counts how many times it appears in the right list
    and adds that number multiplied by the original number to the score.

    Args:
        left: First list of integers
        right: Second list of integers

    Returns:
        An integer representing the similarity score between the two lists

    Example:
        left = [1, 2, 3]
        right = [2, 2, 4] 
        Returns: 4  # (1*0 + 2*2 + 3*0)
    """
    score = 0

    for index, l in enumerate(left):
        r_occurrences = right.count(l)
        score += l * r_occurrences

    return score


if __name__ == "__main__":
    left, right = parse_lists(Path("day1/main_input.txt"))
    distances = find_distances(left, right)
    print(f"Sum of distances: {sum(distances)}")

    score = find_similarity_score(left, right)
    print(f"Similarity score: {score}")
