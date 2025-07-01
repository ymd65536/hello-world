import unittest
from main import greet

class TestGreet(unittest.TestCase):
    def test_greet_english(self):
        """Test English greeting (default behavior)"""
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("World", "en"), "Hello, World!")
    
    def test_greet_japanese(self):
        """Test Japanese greeting"""
        self.assertEqual(greet("World", "ja"), "こんにちは、Worldさん！")

if __name__ == '__main__':
    unittest.main()
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
