import unittest
from console import Console

class TestConsole(unittest.TestCase):

    def setUp(self):
        # Initialize the Console instance
        self.console = Console()

    def test_add_farm(self):
        # Test the add_farm method
        result = self.console.add_farm(1, 'Wheat', 10)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
