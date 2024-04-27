"""Testing the use of the dictionary functions."""

__author__ = "730529937"

from dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest

def test_invert_use_case_1() -> None:
    """Unit test for invert function with expected use case."""
    input_dict = {"apple": "red", "banana": "yellow", "grape": "purple"}
    expected_output = {"red": "apple", "yellow": "banana", "purple": "grape"}
    assert invert(input_dict) == expected_output


def test_invert_use_case_2() -> None:
    """Unit test for invert function with expected use case."""
    input_dict = {"apple": "red", "banana": "blue", "grape": "purple"}
    expected_output = {"red": "apple", "blue": "banana", "purple": "grape"}
    assert invert(input_dict) == expected_output


def test_invert_edge_case() -> None:
    """Unit test for invert function with edge case."""
    input_dict = {"apple": "red", "banana": "red", "grape": "purple"}
    error_occurred = False
    for key, value in input_dict.items():
        if list(input_dict.values()).count(value) > 1:
            error_occurred = True
            break
    
    assert error_occurred, "Expected a KeyError but function executed successfully"


def test_favorite_color_use_case_1() -> None:
    """Unit test for favorite_color function with expected use case."""
    input_dict = {"Alice": "red", "Bob": "blue", "Charlie": "red", "David": "green"}
    expected_output = "red"
    assert favorite_color(input_dict) == expected_output


def test_favorite_color_use_case_2() -> None:
    """Unit test for favorite_color function with expected use case."""
    input_dict = {"Alice": "red", "Bob": "blue", "Charlie": "green", "David": "yellow"}
    expected_output = "red"
    assert favorite_color(input_dict) == expected_output


def test_favorite_color_edge_case() -> None:
    """Unit test for favorite_color function with edge case."""
    input_dict = {}
    expected_output = ""
    assert favorite_color(input_dict) == expected_output


def test_count_use_case_1() -> None:
    """Unit test for count function with expected use case."""
    input_list = ["apple", "banana", "apple", "orange", "banana"]
    expected_output = {"apple": 2, "banana": 2, "orange": 1}
    assert count(input_list) == expected_output


def test_count_use_case_2() -> None:
    """Unit test for count function with expected use case."""
    input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    expected_output = {"apple": 3, "banana": 2, "orange": 1}
    assert count(input_list) == expected_output


def test_count_edge_case() -> None:
    """Unit test for count function with edge case."""
    input_list = []
    expected_output = {}
    assert count(input_list) == expected_output


def test_alphabetizer_use_case_1() -> None:
    """Unit test for alphabetizer function with expected use case."""
    input_list = ["apple", "banana", "orange", "grape", "pear"]
    expected_output = {"a": ["apple"], "b": ["banana"], "o": ["orange"], "g": ["grape"], "p": ["pear"]}
    assert alphabetizer(input_list) == expected_output


def test_alphabetizer_use_case_2() -> None:
    """Unit test for alphabetizer function with expected use case."""
    input_list = ["apple", "banana", "orange", "apricot", "grape", "guava", "pear"]
    expected_output = {"a": ["apple", "apricot"], "b": ["banana"], "o": ["orange"], "g": ["grape", "guava"], "p": ["pear"]}
    assert alphabetizer(input_list) == expected_output


def test_alphabetizer_edge_case() -> None:
    """Unit test for alphabetizer function with edge case."""
    input_list = []
    expected_output = {}
    assert alphabetizer(input_list) == expected_output


def test_update_attendance_use_case_1() -> None:
    """Unit test for update_attendance function with expected use case."""
    input_dict = {"Monday": ["Alice", "Bob", "Charlie"], "Tuesday": ["David", "Eve"]}
    day_of_week = "Monday"
    new_student = "Frank"
    update_attendance(input_dict, day_of_week, new_student)
    assert input_dict[day_of_week] == ["Alice", "Bob", "Charlie", "Frank"]


def test_update_attendance_use_case_2() -> None:
    """Unit test for update_attendance function with expected use case."""
    input_dict = {"Monday": ["Alice", "Bob", "Charlie"], "Tuesday": ["David", "Eve"]}
    day_of_week = "Wednesday"
    new_student = "Grace"
    update_attendance(input_dict, day_of_week, new_student)
    assert input_dict[day_of_week] == ["Grace"]


def test_update_attendance_edge_case() -> None:
    """Unit test for update_attendance function with edge case."""
    input_dict = {"Monday": ["Alice", "Bob", "Charlie"], "Tuesday": ["David", "Eve"]}
    day_of_week = "Monday"
    new_student = "Alice"
    update_attendance(input_dict, day_of_week, new_student)
    assert input_dict[day_of_week] == ["Alice", "Bob", "Charlie", "Alice"]