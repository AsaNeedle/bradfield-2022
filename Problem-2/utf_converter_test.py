import unittest
from utf_converter import utf_converter

class TestUTFConverter(unittest.TestCase):
  
    def test_given(self):
      test_string = [240, 159, 145, 190]
      utf32_byte_array = utf_converter(test_string)
      self.assertEqual(utf32_byte_array, [128126]), 

if __name__ == '__main__':
    unittest.main()
