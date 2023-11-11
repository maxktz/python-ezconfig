from typing import Any


def float_to_str(value: float):
    if value == round(value):
        return str(round(value))
    return str(value)

def parse_output_value(value: Any, can_be_none: bool = True) -> str:
    if value is None:
        return f"[bold green]~[/bold green]" if can_be_none else f"[bold yellow]~[/bold yellow]"
    if isinstance(value, float):
        return float_to_str(value)
    if value is False:
        return f"[bold yellow]{value}[/bold yellow]"
    return str(value)