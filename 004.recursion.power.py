# Use recusion to raise power
import unittest

def power(a,x):
    if x==0 :
        return 1
    if x>0:
        return power(a,x-1) * a  
    else:
        return power(a,x+1)/a

class test_power(unittest.TestCase):
    def test_basic(self):
        for i,o in [([1,1],1),([1,0],1),([2,2],4),([2,10],1024),([2,-1],0.5),([-1,3],-1)]:
            self.assertEqual(power(i[0],i[1]),o,msg=f"For {i}, it should be {o}")

if __name__ == '__main__':
    unittest.main()