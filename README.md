[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/13.2.0)](https://pypi.org/project/python-ezconfig) [![PyPI version](https://badge.fury.io/py/python-ezconfig.svg)](https://badge.fury.io/py/python-ezconfig) 

[![my telegram](https://img.shields.io/badge/my-telegram-blue)](https://t.me/zrxmax) [![xcrypto telegram](https://img.shields.io/badge/xcrypto%20+=%20dev-telegram-blue)](https://t.me/+vx4yLtrRcvAyZWM0)

![Logo](https://i.imgur.com/mbH37Fx.png)

[English readme](https://github.com/textualize/rich/blob/master/README.md)

### `ezconfig` is a Python library for easy formatting config file right from the terminal.

Press `ENTER` and run your code, **or change varialables right there!** 

ezconfig can also use different variable types, use different styles, and highlight mistakes, if there are any.

![da](https://i.imgur.com/oF4ArPE.jpg)

## Installing

Requires Python 3.7 or later.

Install with pip or your favorite PyPI package manager.

```sh
pip install python-ezconfig
```

## Get started with 2 lines of code

```python
from ezconfig import EzConfig

ez = EzConfig("VAR1", "VAR2", ...)
ez.configure()

print(ez.config)
# {'VAR1': ..., 'VAR2': ...}
```

## Advanced usage

If you want to set **default value**, or prevent the user from leaving the **variable empty**, or set **value type** (instance) - use KeyPrompt

```python
from ezconfig import EzConfig, KeyPrompt

ez = EzConfig(
    KeyPrompt("DELAY", value_type=float, default_value=5),
    KeyPrompt("LINK", value_type=str, can_be_empty=False),
    KeyPrompt("USE_PROXY", value_type=bool, can_be_empty=False),
    KeyPrompt("USE_CACHE", value_type=bool, can_be_empty=False, default_value=False),
)
ez.configure()
```
If user will input string value in DELAY, then he will get this warning:

![](https://i.imgur.com/PhDSCwq.jpg)
And it works with many other types, such as `int`, `bool`, `float`, `str`...

As well, if you pass argument `can_be_empty=False`, the user will not be able to run your script without filling this field.

![](https://i.imgur.com/AFr112n.jpg)

Then you can access this variables
```python
print(ez.config['DELAY'])
# 28     # Note, you get a right types, int, not "28"
print(ez.config['USE_PROXY'])
# False
print(type(ez.config['USE_PROXY']))
# bool
```

Note: You always able to access configuration from config file as well

![](https://i.imgur.com/bt5VbhD.png)
you can change this file by passing `saving_json={file}` to `EzConfig()`

## Documentation

#### class - `ezconfig.EzConfig`

    Allows super easy access to configuration file

    To user, using easy interface,
    and to you, just by 'EzConfig.config' dictionary <3

    Arguments:
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

EzConfig class methods:

`ezconfig.EzConfig.configure()` - Main method, prints configuration table and enables editing mode.

`ezconfig.EzConfig.print_config()` - Just prints config table, nothing more.



#### class - `ezconfig.KeyPrompt`

    Defines a key-value prompt for EzConfig.

    Arguments:
        key (str): Key name, must be str.
        default_value (str, optional): Will be default value if there are no saved values. Defaults to None.
        can_be_empty (bool, optional): True/False. Defaults to True.
        value_type (ValueType, optional): Value will be passed instance. Defaults to str.

there is no methods for this class.

##### That's all, thank you for your attention <3, here u can buy me a coffee
Any crypto network: `0x753846BF882046c5Edc3cefED30A4E6Bf8F99999`
<p><a href="https://www.buymeacoffee.com/zrxmax"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="zrxmax" /></a><a href="https://ko-fi.com/zrxmax"> <img align="left" src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" height="50" width="210" alt="zrxmax" /></a></p><br><br></p>