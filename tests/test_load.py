<<<<<<< HEAD
import pytest

from dundie.core import load
from dundie.database import EMPTY_DB, connect

from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test function load function."""
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test function load function."""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"


@pytest.mark.unit
def test_db_schema():
    load(PEOPLE_FILE)
    db = connect()
    assert db.keys() == EMPTY_DB.keys()
=======
from dundie.core import load

def test_load():
    """Test load Function"""
    assert len(load('test/assets/people.csv')) == 2
    assert (load("test/assets/people.csv"))[0][0] == 'j' 
    
>>>>>>> 199ecad93caddf53d4240b3a889817690898ae9c
