import unittest
from power import power

class PowerTest(unittest.TestCase):
    def cut_rational(self, num, level=10):
        return float(str(num)[:level+2])

    def test_power_0(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(1, 0), 1)
        self.assertEqual(power(200, 0), 1)
        self.assertEqual(power(-2312421, 0), 1)
        self.assertEqual(power(-2312421.432422, 0), 1)
        self.assertEqual(power(2312421.75327, 0.0), 1)
    
    def test_power_1(self):
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(-1, 1), -1)
        self.assertEqual(power(-23, 1), -23)
        self.assertEqual(power(-23.42, 1), -23.42)
        self.assertEqual(power(1, 1), 1)
        self.assertEqual(power(2000, 1), 2000)
        self.assertEqual(power(893423.12, 1), 893423.12)
    
    def test_whole(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(4, 3), 64)
        self.assertEqual(power(-4, 3), -64)
        self.assertEqual(power(-2, 10), 1024)
    
    def test_rational(self):
        self.assertEqual(self.cut_rational(power(0.5, 0.5)), 0.7071067811)
        self.assertEqual(power(1, 2.322321), 1)
        self.assertEqual(self.cut_rational(power(1.00000001, 0.00000001)), 1)
        self.assertEqual(self.cut_rational(power(1.234, 1.5334)), 1.3804563088)
        self.assertEqual(self.cut_rational(power(332.132, -12.46654)), 3.6981033841)
        self.assertEqual(self.cut_rational(power(1.132, 1.46654)), 1.1994107551)
        self.assertEqual(self.cut_rational(power(342.964, 10.663253)), 1.0814253711)
        #self.assertEqual(self.cut_rational(power(0.125, 0.625)), 0.2726269331)
        #self.assertEqual(self.cut_rational(power(0.132, 1.46654)), 0.0513199817)
        #self.assertEqual(self.cut_rational(power(0.132, 0.46654)), 0.3887877403)

if __name__ == "__main__":
    unittest.main()