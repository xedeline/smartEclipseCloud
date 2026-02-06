# test_smarteclipse.py
"""
Tests for smartEclipse module.
"""

import unittest
from smarteclipse import smartEclipse

class TestsmartEclipse(unittest.TestCase):
    """Test cases for smartEclipse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = smartEclipse()
        self.assertIsInstance(instance, smartEclipse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = smartEclipse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
