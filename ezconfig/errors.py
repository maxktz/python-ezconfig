from .utils import parse_output_value

class KeyNotFoundError(BaseException):
    def __str__(self):
        return f'cannot find any key relating to "{self.args[0]}"'

class RequiredParameterError(BaseException):
    def __str__(self):
        return f'parameter {self.args[0]} is required'

class NoPairError(BaseException):
    def __str__(self):
        return f'please provide a key=value pair, not only key'

class ValueTypeError(BaseException):
    def __init__(self, key: str, value: str, type) -> None:
        super().__init__(key, value, type)
        self.key = key
        self.value = value
        self.type = type
    
    def __str__(self):
        return f'value {self.key} should be instance of {self.type.__name__}, not "{parse_output_value(self.value)}"'