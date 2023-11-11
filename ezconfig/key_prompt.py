from typing import Optional
from .types import ValueType

class KeyPrompt:
    """Defines a key-value prompt for EzConfig.

    Args:
        key (str): Key name, must be str
        default_value (str, optional): Will be default value if there are no saved values. Defaults to None.
        can_be_empty (bool, optional): True/False. Defaults to True.
        value_type (ValueType, optional): Value will be passed instance. Defaults to str.
    """        
    def __init__(self,
                 key: str,
                 default_value: Optional[str] = None,
                 can_be_empty: bool = True,
                 value_type: Optional[ValueType] = str,
    ) -> None:
        self.key = key
        self.default_value = default_value
        self.can_be_empty = can_be_empty
        self.value_type = value_type