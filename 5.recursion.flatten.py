# flatten multi dimension arrays into a 1 dimension array
import unittest

def flatten(l):
    if type(l)!= list:
        return [l]
    else:
        result=[]
        for e in l:
            result += flatten(e)
        return result 

class test_flatten(unittest.TestCase):
    def test_basic(self):
        for i,o in [([1,2,3],[1,2,3]),([1,[2],3],[1,2,3]),([[1,2],3],[1,2,3]),([[]],[]),([],[]),([1,[],3],[1,3])]:
            self.assertEqual(flatten(i),o,msg=f"For {i}, it should be {o}")

if __name__ == '__main__':
    unittest.main()