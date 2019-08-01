import pytest
import geo_analysis3 as ga

def test_calculate_distance():
    coord1 = [0,0,0]
    coord2 = [2,0,0]
    expected = 2.0
    observed = ga.calculate_distance(coord1, coord2)
    assert observed == expected 
    
def test_bond_check():
    distance = 1.5
    expected = True
    observed = ga.bond_check(distance)
    assert observed == expected
    
