import unittest

# Its a type of fibonacci series that starts with 2 and 1
# First defined the base cases
# Then just added the previous case to find the sum
def lucas_numbers(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_numbers(n-1) + lucas_numbers(n-2)

class test_lucas_numbers(unittest.TestCase):
    def test_basic(self):
        for i,o in [(0,2),(1,1),(2,3),(3,4),(5,11),(9,76)]:
            self.assertEqual(lucas_numbers(i),o,msg=f"For {i}, it should be {o}")

if __name__ == '__main__':
    unittest.main()