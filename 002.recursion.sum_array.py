# Sum an array using recursion
import unittest

def sum_array(n):
    if len(n)== 0:
        return 0
    else:
        return sum_array(n[1:]) + n[0]

class test_sum_array(unittest.TestCase):
    def test_basic(self):
        for i,o in [([1,1],2),([1,2,3,4],10),([-1,-1],-2),([3],3),([-1,0,1],0),([],0)]:
            self.assertEqual(sum_array(i),o,msg=f"For {i}, it should be {o}")

if __name__ == '__main__':
    unittest.main()