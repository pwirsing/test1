# Test
import pytest
# sfrom context import sample

class Test_One:
    """test class"""

    def test_thing_one(self):
        print("name:", __name__)
        assert 1

    def test_method_trial(self):
        print(' or ', __name__)
        assert False
        
