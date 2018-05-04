# Test
import pytest

class Test_Two:
    """test class"""

    def test_thing_two(self):
        print( __name__)
        assert 1

    def test_also(self):
        print('and this as well')
        assert 'test' in __name__

        
