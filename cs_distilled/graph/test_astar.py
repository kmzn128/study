import unittest
import math
import astar

class TestAster(unittest.TestCase):
    
    def test_astar_find_char(self):
        exp_start = (1,1)
        exp_goal = (8,36)
        ans_s = astar.find_char("S")
        ans_g = astar.find_char("G")
        self.assertEqual(exp_start, ans_s)
        self.assertEqual(exp_goal, ans_g)

    def test_reachable(self):
        a = astar.reachable(0,0)
        b = astar.reachable(1,1)
        c = astar.reachable(2,2)
        e = astar.reachable(8,36)
        self.assertEqual(False, a)
        self.assertEqual(False, b)
        self.assertEqual(True, c)
        self.assertEqual(True, e)
        
    def test_show_next_step(self):
        a = astar.show_next_step((1,1))
        b = astar.show_next_step((2,3))
        self.assertSetEqual({(2,1),(1,2)}, a)
        self.assertSetEqual({(2,2),(1,3),(3,3)}, b)
    
    def test_calc_distance(self):
        a = astar.calc_distance((8,35))
        b = astar.calc_distance((7,35))
        self.assertEqual(1, a)
        self.assertEqual(math.sqrt(2), b)
        

if __name__ == "__main__":
    unittest.main()
    