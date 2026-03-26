class Validation():
    def __init__(  
        self, 
        length: int = 8, 
        require_num: bool = True,
        require_upper: bool = True,
        require_symbol: bool = True,
        require_lower: bool = True,
        common_passwords: set[str] = None
        ):
        self.length = length
        self.require_num = require_num
        self.require_upper = require_upper
        self.require_symbol = require_symbol
        self.require_lower = require_lower
        self.common_passwords = common_passwords
        

    def validate(self, password: str) -> list[str]:
        errors = []

        if len(password) < self.length:
            errors.append(f"Password must be at least {self.min_length} characters")
        
        if self.require_num and not any (c.isdigit() for c in password):
            errors.append("Password must contain a number")

        if self.require_upper and not any (c.isupper() for c in password):
            errors.append("Password must contain an uppercase letter")
        
        if self.require_symbol and not any (not c.isalnum() for c in password):
            errors.append("Password must contain a special character")

        if self.require_lower and not any (c.islower() for c in password):
            errors.append("Password must contain a lowercase letter")

        if password in self.common_passwords:
            errors.append()

        return errors