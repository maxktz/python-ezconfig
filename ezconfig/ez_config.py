import sys
import json
from typing import Optional, Union
from pathlib import Path
from json import JSONDecodeError
from rich.table import Table, box, Column
from rich.console import Console
from rich.style import StyleType

from . import utils
from .errors import KeyNotFoundError, NoPairError, RequiredParameterError, ValueTypeError
from .key_prompt import KeyPrompt
from .types import ValueType


class EzConfig:
    """Allows super easy access to configuration file
    
    To user, using easy interface,
    and to you, just by 'EzConfig.config' dictionary <3

    Args:
        *key_prompts (KeyPrompt | str), Prompts, to ask user for. Required.
        saving_json (Path | str, optional): path to json file to save config into. Defaults to "config.json".
        show_index (bool, optional): True/False to show numbers column for rows. Defaults to True.
        show_lines (bool, optional): True/False to show separation horizontal lines. Defaults to False.
        clean_console (bool, optional): True/False to clean up console between printing. Defaults to True.
        title (str, optional): The title of the table rendered at the top.. Defaults to None.
        caption (str, optional): The table caption rendered below.. Defaults to None.
        headers (Union[str, str], optional): Column headers, example: ("Key", "Value"). Defaults to None.
        box (box.Box, optional): One of the constants in box.py used to draw the edges (see :ref:`appendix_box`), or ``None`` for no box lines. Defaults to box.ROUNDED.
        style (StyleType, optional): Default style for the table. Defaults to "bold white".
        column_styles (Union[StyleType, StyleType], optional): Union of 2 row styles. Defaults to ("bold cyan", "bold green").
        console (Console, optional): Optional <rich.console.Console> object, if you want to use your custom rich console. Defaults to None.
        configure_text (str, optional): Text that shows up when the configure method is used. Defaults to None.
    """       
    config: dict
    """Dictionary of your json configuration file."""
    def __init__(self,
                 *key_prompts: KeyPrompt | str,
                 saving_json: Path | str = "config.json",
                 show_index: bool = True,
                 show_lines: bool = False,
                 clean_console: bool = True,
                 title: Optional[str] = "[bold green]ezconfig[cyan]([white]{saving_json}[cyan])",
                 caption: Optional[str] = None,
                 headers: Optional[Union[str, str]] = None,
                 box: box.Box = box.ROUNDED,
                 style: Optional[StyleType] = "bold white",
                 column_styles: Union[StyleType, StyleType] = ("bold cyan", "bold green"),
                 console: Optional[Console] = None,
                 configure_text: str = None,
    ) -> None:
        self.key_prompts: list[KeyPrompt] = []
        for p in key_prompts:
            prompt = p if isinstance(p, KeyPrompt) else KeyPrompt(key=str(p))
            if prompt.key.lower() not in [p.key.lower() for p in self.key_prompts]:
                self.key_prompts.append(prompt)
        self.saving_json = Path(saving_json).with_suffix(".json")
        self.headers = headers
        self.title = title
        self.caption = caption
        self.box = box
        self.show_lines = show_lines
        self.show_index = show_index
        self.style = style
        self.column_styles = column_styles
        self.clean_console = clean_console
        self.configure_text = configure_text
        if not configure_text:
            key_color, val_color = column_styles[0], column_styles[1]
            self.configure_text = (
                f"input [{key_color}]KEY[/{key_color}]=[{val_color}]VALUE[/{val_color}] to configure\n"
                f"[white]Or press [bold {val_color}]ENTER[/bold {val_color}] to continue\n"
            )
        self.console = console if isinstance(console, Console) else Console()
        self.config = {}
    
    def _get_config(self) -> dict:
        try:
            file_text = self.saving_json.read_text(encoding='utf-8')
            config = json.loads(file_text)
        except (FileNotFoundError, JSONDecodeError):
            config = {}
        for prompt in self.key_prompts:
            if prompt.key not in config:
                config[prompt.key] = prompt.default_value
            if config[prompt.key] is not None and prompt.value_type:
                config[prompt.key] = prompt.value_type(config[prompt.key])
        return config
    
    def _update_config_file(self) -> bool:
        old_config = self._get_config()
        if self.config != old_config:
            self.saving_json.write_text(json.dumps(self.config, indent=4), encoding='utf-8')
            return True
        return False
    
    def _print_table(self, config: dict):
        caption = self.caption.format(saving_json=self.saving_json) if isinstance(self.caption, str) else None
        title = self.title.format(saving_json=self.saving_json) if isinstance(self.title, str) else None
        columns=[Column(header=self.headers[0] if self.headers else "", style=self.column_styles[0], header_style=self.style),
                 Column(header=self.headers[1] if self.headers else "", style=self.column_styles[1], header_style=self.style)]
        if self.show_index: 
            columns.insert(0, Column(style=self.column_styles[0]))
        table = Table(
            *columns,
            title=title,
            caption=caption,
            box=self.box,
            show_header=True if self.headers else False,
            show_lines=self.show_lines,
            style=self.style,
        )
        for i, prompt in enumerate(self.key_prompts, 1):
            val = utils.parse_output_value(config[prompt.key], prompt.can_be_empty)
            row = (str(i), prompt.key, val) if self.show_index else (prompt.key, val)
            table.add_row(*row)
        self.console.print(table)

    def _parse_input_key(self, key: str) -> str:
        return key.strip().lower()
    
    def _parse_input_value(self, key: str, value: str, value_type: ValueType) -> None | str:
        value = value.strip()
        if value in ("", "~"):
            return None
        if value_type is bool:
            if value.lower() in ("0", "false"):
                return False 
            if value.lower() in ("1", "true"):
                return True
            raise ValueTypeError(key, value, value_type)
        try:
            return value_type(value)
        except (ValueError, TypeError):
            raise ValueTypeError(key, value, value_type)
    
    def _parse_input_data(self, input_data: str) -> Union[str, str]:
        data = input_data.split("=", 1)
        key = self._parse_input_key(data[0])
        value = data[1].strip()
        return key, value
    
    def print_config(self):
        """Prints config table."""    
        self.config = self._get_config()    
        table = self._print_table(self.config)
        self.console.print(table)
    
    def configure(self):
        """Prints configuration table and enables editing mode."""
        self.config = self._get_config()
        warn = "[bold][white]![/bold][yellow]"
        message = ""
        while True:
            if self.clean_console: self.console.clear()
            self._print_table(self.config)
            self.console.print(message)
            message = ""
            
            input_data = self.console.input(self.configure_text).strip()
            if input_data.lower() in ("", "enter"):
                for prompt in self.key_prompts:
                    if not prompt.can_be_empty and self.config[prompt.key] is None:
                        message = f"{warn} {RequiredParameterError(prompt.key)}"
                        break
                else:
                    return
                continue
            elif input_data.lower() in ("exit", "q", "quit"):
                sys.exit(0) 
            try:
                key, value = self._parse_input_data(input_data)
            except IndexError:
                message = f'{warn} {NoPairError()}'
                continue
            for index, prompt in enumerate(self.key_prompts, 1):
                if key in (str(index), prompt.key.lower()):
                    try:
                        value = self._parse_input_value(prompt.key, value, prompt.value_type)
                    except ValueTypeError as error:
                        message = f'{warn} {error}'
                        break
                    self.config[prompt.key] = value
                    break
            else:
                message = f'{warn} {KeyNotFoundError(key)}'
            self._update_config_file()