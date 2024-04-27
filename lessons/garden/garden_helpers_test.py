"""Testing Garden Functions."""
__author__ = 730529937

import pytest

import garden_helpers

# Unit tests for add_by_kind function
def test_add_by_kind_edge_case():
    """Test adding a new plant kind to an empty dictionary."""
    by_kind = {}
    new_plant_kind = "flower"
    new_plant = "rose"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {"flower": ["rose"]}


def test_add_by_kind_use_case():
    """Test adding a new plant to an existing plant kind."""
    by_kind = {"flower": ["marigold"]}
    new_plant_kind = "flower"
    new_plant = "lily"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {"flower": ["marigold", "lily"]}


# Unit tests for add_by_date function
def test_add_by_date_edge_case():
    """Test adding a plant to a month with no existing plants."""
    garden_by_date = {}
    month = "April"
    plant = "sunflower"
    add_by_date(garden_by_date, month, plant)
    assert garden_by_date == {"April": ["sunflower"]}


def test_add_by_date_use_case():
    """Test adding a plant to a month with existing plants."""
    garden_by_date = {"April": ["marigold"]}
    month = "April"
    plant = "zinnia"
    add_by_date(garden_by_date, month, plant)
    assert garden_by_date == {"April": ["marigold", "zinnia"]}


# Unit tests for lookup_by_kind_of_date function
def test_lookup_by_kind_of_date_edge_case():
    """Test looking up plants of a specific kind in a month with no plants."""
    plants_by_kind = {"flower": ["rose"]}
    plants_by_date = {"April": []}
    kind = "flower"
    month = "April"
    assert lookup_by_kind_of_date(plants_by_kind, plants_by_date, kind, month) == "No flowers to plant in April."


def test_lookup_by_kind_of_date_use_case():
    """Test looking up plants of a specific kind in a month with matching plants."""
    plants_by_kind = {"flower": ["rose", "lily", "marigold"]}
    plants_by_date = {"April": ["rose", "marigold"]}
    kind = "flower"
    month = "April"
    expected_output = "flowers to plant in April: ['rose', 'marigold']"
    assert expected_output in lookup_by_kind_of_date(plants_by_kind, plants_by_date, kind, month)


# Run the tests if this script is executed
if __name__ == "__main__":
    pytest.main()