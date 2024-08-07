from dundie.core import load

def test_load():
    """Test load Function"""
    assert len(load('test/assets/people.csv')) == 2
    assert (load("test/assets/people.csv"))[0][0] == 'j' 
    