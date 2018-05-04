# Base
import pytest
from tests import test_one
from tests import test_two

print('Base')
t1 = test_one.Test_One()
t1.test_thing_one()
t2 = test_two.Test_Two()
t2.test_also()
