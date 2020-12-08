import unittest
import Day4.day4 as day

class Day4Tests(unittest.TestCase):
    def test_day_4_part_one(self):
        self.assertEqual(day.part_one(), 1650)

    def test_day_4_part_two(self):
        self.assertEqual(day.part_two(), 1129)

if __name__ == '__main__':
    unittest.main()        