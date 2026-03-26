class Validation():
    def __init__(  
        self, 
        length: int = 8, 
        require_num: bool = True,
        require_upper: bool = True,
        require_symbol: bool = True,
        require_lower: bool = True,
        common_passwords: set = None
        ):
        self.length = length
        self.require_num = require_num
        self.require_upper = require_upper
        self.require_symbol = require_symbol
        self.require_lower = require_lower
        self.common_passwords = common_passwords
        