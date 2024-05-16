"""
Utilities.py: Utility functions for handling various tasks related to dictionaries, integers, and RGB values.

Dan Mailman

09-May-24

Functions:
- ExitOnNoDictVal(s, d, n) -> object: Exits if the key is not found in the dictionary and returns the value.
- ExitOnNoIntVal(s, d, n): Exits if the key is not found in the dictionary or if the value is not an integer.
- ExitOnNoRGBVal(s, d, n): Exits if the key is not found in the dictionary or if the value is not a valid RGB tuple.

Usage:
- You can use these functions to handle dictionary lookups, integer conversions, and RGB value validations in your code.

Example:
- [Include example usage scenarios or code snippets]

"""
from typing import Tuple
def ExitOnNoDictVal(key: str, d: dict, n: str) -> object:
    """Exit if key is not found in the dictionary. return val"""
    val = d.get(key)
    assert val is not None, f'ERR: {n}: "{key}" not found.'
    return val
def ExitOnNoIntVal(key: str, d: dict, n: str) -> int:
    """Exit if the key is not found in the dictionary, return the integer value."""
    val = d.get(key)
    assert val is not None, f'ERR: {n}: "{key}" not found.'
    try:
        nRet = int(val)
    except ValueError:
        exit(f'ERR: {n}: Value {val} for key "{key}" is not an integer.')
    return nRet
def ExitOnNoRGBVal(key: str, d: dict, n: str) -> Tuple[int, int, int]:
    """Exit if the key is not found in the dictionary, return the RGB value as a tuple of integers."""
    val: Tuple[int, int, int] = d.get(key)
    assert val is not None, f'ERR: {n}: "{key}" not found.'
    if not isinstance(val, tuple) or len(val) != 3 or not all(isinstance(x, int) and 0 <= x <= 255 for x in val):
        exit(f'ERR: {n}: Value {val} for key "{key}" is not a valid RGB tuple.')
    return val
def ExitOnNoStrVal(key: int, d: dict, n: str) -> str:
    """Exit if the key is not found in the dictionary, return the string value."""
    val = d.get(key)
    assert val is not None, f'ERR: {n}: "{key}" not found.'
    if not isinstance(val, str):
        exit(f'ERR: {n}: Value {val} for key "{key}" is not a string.')
    return val
def ExitOnNoStrForRGB(key: Tuple[int, int, int], d: dict, n: str) -> str:
    """Exit if the key is not found in the dictionary, return the string value."""
    val = d.get(key)
    assert val is not None, f'ERR: {n}: {key} not found.'
    if not isinstance(val, str):
        exit(f'ERR: {n}: Value {val} for key {key} is not a string.')
    return val

if __name__ == "__main__":
    my_dict = {'a': '1', 'b': '2', 'c': '3'}
    assert ExitOnNoDictVal('a', my_dict, 'my_dict') == '1'

    my_dict = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    assert ExitOnNoRGBVal('red', my_dict, 'my_dict') == (255, 0, 0)

    my_dict = {'x': 'abc'}
    try:
        ExitOnNoIntVal('x', my_dict, 'my_dict')
    except SystemExit as e:
        assert str(e) == f'ERR: my_dict: Value abc for key "x" is not an integer.'
    my_dict_str = {'a': '1', 'b': '2', 'c': '3'}
    assert ExitOnNoStrVal('a', my_dict_str, 'my_dict_str') == '1'

    my_dict_invalid = {'x': 123}
    try:
        ExitOnNoStrVal('x', my_dict_invalid, 'my_dict_invalid')
    except SystemExit as e:
        assert str(e) == 'ERR: my_dict_invalid: Value 123 for key "x" is not a string.'

    my_dict_rgb = {(255, 0, 0): 'red', (0, 255, 0): 'green', (0, 0, 255): 'blue'}
    assert ExitOnNoStrForRGB((255, 0, 0), my_dict_rgb, 'my_dict_rgb') == 'red'
    try:
        ExitOnNoStrForRGB((255, 255, 255), my_dict_rgb, 'my_dict_rgb')
    except SystemExit as e:
        assert str(e) == 'ERR: my_dict_rgb: (255, 255, 255) not found.'
