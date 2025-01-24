def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"





import unittest

class PersonTests(unittest.TestCase):
   def test(self):
      dict = {"name": "George", "town": "Sofia", "age": 20}
      result = get_info(**dict)
      self.assertEqual(result, "This is George from Sofia and he is 20 years old")

if __name__ == "__main__":
   unittest.main()




#print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))