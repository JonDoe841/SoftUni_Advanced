def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power-1)


import unittest

class Tests(unittest.TestCase):
   def test(self):
      func = recursive_power
      res = func(2, 10)
      self.assertEqual(res, 1024)

if __name__ == '__main__':
   unittest.main()