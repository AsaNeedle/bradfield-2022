import unittest
from utf_converter import utf_converter

class TestUTFConverter(unittest.TestCase):
  
    def test_cases(self):
      test_string = [240, 159, 145, 190]
      utf32_byte_array = utf_converter(test_string)
      self.assertEqual(utf32_byte_array, [128126]), 

      test_cases = [
        'hello, world!',
        'Gödel',
        '開発者',
        '🥶',
        '1 + 2 = 3'
      ]
      for case in test_cases:
        test_string = list(bytes(case, 'utf8'))
        expected = [ord(c) for c in case]
        actual = utf_converter(test_string)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
