# lab11_q2_complete.py

class PasswordChecker:
    def __init__(self):
        """Initialize the password checker with common weak passwords"""
        self.common_passwords = [
            "password", "123456", "12345678", "qwerty", "abc123",
            "monkey", "letmein", "dragon", "baseball", "master",
            "admin", "root", "welcome", "password123", "admin123"
        ]
        self.history = []  # List to store (password, result) tuples
    
    def check_common(self, password):
        """Check if password is in the common passwords list"""
        return password.lower() in self.common_passwords
    
    def check_strength(self, password):
        """Check password strength criteria and return dictionary"""
        has_length = len(password) >= 8
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        
        return {
            "length": has_length,
            "digit": has_digit,
            "special": has_special
        }
    
    def evaluate(self, password):
        """Evaluate password strength and return rating"""
        # Check if it's a common password first
        if self.check_common(password):
            result = "WEAK (common password)"
        else:
            # Get strength criteria
            strength = self.check_strength(password)
            # Count how many criteria pass
            criteria_count = sum(strength.values())
            
            if criteria_count <= 1:
                result = "WEAK"
            elif criteria_count == 2:
                result = "MEDIUM"
            else:  # criteria_count == 3
                result = "STRONG"
        
        # Store in history
        self.history.append((password, result))
        return result


def main():
    print("=" * 60)
    print("  Q2: PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    print()
    
    # Create a password checker
    checker = PasswordChecker()
    
    # Test passwords
    test_passwords = ["admin", "hello", "hello123", "MyP@ss99", "p@ssw0rd!", "root"]
    
    print("--- Checking Passwords ---")
    for pwd in test_passwords:
        result = checker.evaluate(pwd)
        print(f"  {pwd:12} → {result}")
    
    print()
    print("--- Check History ---")
    for pwd, result in checker.history:
        print(f"  {pwd:12} : {result}")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()