from typing import Optional


class KeyPrompt:
    """Defines a key-value prompt for EzConfig.

    Args:
        key (str): Key name, must be str
        default_value (str, oprional): Will be default value if there is no saved values. Defaults to None.
        can_be_empty (bool, optional): True/False. Defaults to True.
        value_type (str | int | float, optional): Value will be always formated by passed instance. Defaults to str.
    """        
    def __init__(self,
                 key: str,
                 default_value: Optional[str] = None,
                 can_be_empty: bool = True,
                 value_type: Optional[str | int | float] = str,
    ) -> None:
        self.key = key
        self.default_value = default_value
        self.can_be_empty = can_be_empty
        self.value_type = value_type