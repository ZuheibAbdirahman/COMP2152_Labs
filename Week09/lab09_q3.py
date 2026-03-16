import unittest

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def is_valid_ip(ip_string):
    """Check if a string is a valid IPv4 address."""
    if not isinstance(ip_string, str) or ip_string == "":
        return False
    
    parts = ip_string.split(".")
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if part != str(num):
            return False
    
    return True

def fizzbuzz(n):
    """Return Fizz/Buzz/FizzBuzz or the number as string."""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

class TestCelsius(unittest.TestCase):
    """Test cases for celsius_to_fahrenheit function."""
    
    def test_freezing(self):
        """Test that 0°C equals 32°F"""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
    
    def test_boiling(self):
        """Test that 100°C equals 212°F"""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
    
    def test_negative(self):
        """Test that -40°C equals -40°F (crossover point)"""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

class TestValidIP(unittest.TestCase):
    """Test cases for is_valid_ip function."""
    
    def test_valid(self):
        """Test a valid IP address"""
        self.assertTrue(is_valid_ip("192.168.1.1"))
    
    def test_invalid_octet(self):
        """Test IP with octet > 255"""
        self.assertFalse(is_valid_ip("256.1.1.1"))
    
    def test_too_few_parts(self):
        """Test IP with only 3 parts"""
        self.assertFalse(is_valid_ip("1.2.3"))
    
    def test_empty(self):
        """Test empty string"""
        self.assertFalse(is_valid_ip(""))

class TestFizzBuzz(unittest.TestCase):
    """Test cases for fizzbuzz function."""
    
    def test_fizz(self):
        """Test number divisible by 3 only"""
        self.assertEqual(fizzbuzz(3), "Fizz")
    
    def test_buzz(self):
        """Test number divisible by 5 only"""
        self.assertEqual(fizzbuzz(5), "Buzz")
    
    def test_fizzbuzz(self):
        """Test number divisible by both 3 and 5"""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    
    def test_number(self):
        """Test number not divisible by 3 or 5"""
        self.assertEqual(fizzbuzz(7), "7")

if __name__ == "__main__":
    unittest.main()