from typing import Any


def float_to_str(value: float):
    if value == round(value):
        return str(round(value))
    return str(value)

def parse_output_value(value: Any, can_be_none: bool = True) -> str:
    if value is None:
        return f"[bold green]~" if can_be_none else f"[bold yellow]~"
    if type(value) is float:
        return float_to_str(value)
    return str(value)