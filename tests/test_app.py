import unittest
from src.app import hello

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, DevOps!")

if __name__ == '__main__':
    unittest.main()