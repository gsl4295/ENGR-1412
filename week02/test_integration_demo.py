import unittest
from week02.integration_demo import Function

class TestA(unittest.TestCase):
    def test_linear(self):
        f = Function("(x)", (0, 10))
        f.dx_optimizer()
        self.assertEqual(f.area_under_curve, 50.0)
        pass
