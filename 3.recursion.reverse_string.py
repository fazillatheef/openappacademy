# Reverse a string using recursion
import unittest

def reverse_string(s):
    if s == "":
        return ""
    return s[-1:] + reverse_string(s[:-1])

class test_reverse_string(unittest.TestCase):
    def test_basic(self):
        for i,o in [("[1,2]","]2,1["),("Malayalam","malayalaM"),("Fazil","lizaF")]:
            self.assertEqual(reverse_string(i),o,msg=f"For {i}, it should be {o}")

if __name__ == '__main__':
    unittest.main()