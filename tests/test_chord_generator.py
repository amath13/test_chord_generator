import pytest
import sys
import os

# Append the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import your functions and variables from the module
from chord_generator import calculate_interval, chords

@pytest.fixture
def get_chords_Cmin():
    return [48, 51, 55]

@pytest.fixture
def get_chords_Emaj():
    return [52, 56, 59]

def test_pick_not_in_chord():
    not_chord = 'Cmin42'
    assert not_chord not in chords

def test_calculate_interval(get_chords_Cmin, get_chords_Emaj):
    interval = calculate_interval(get_chords_Cmin[0], get_chords_Emaj[0])
    assert interval == 4
