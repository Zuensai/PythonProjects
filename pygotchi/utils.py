# utils.py
import sys
import select

def get_input_nonblocking():
    """
    Checks for user input without blocking.
    Returns the string if input is available, otherwise None.
    """
    i, _, _ = select.select([sys.stdin], [], [], 0)
    if i:
        return sys.stdin.readline().strip()
    return None
