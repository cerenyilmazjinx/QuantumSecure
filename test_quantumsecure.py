# test_quantumsecure.py
"""
Tests for QuantumSecure module.
"""

import unittest
from quantumsecure import QuantumSecure

class TestQuantumSecure(unittest.TestCase):
    """Test cases for QuantumSecure class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumSecure()
        self.assertIsInstance(instance, QuantumSecure)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumSecure()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
