```python
# Import the necessary libraries
import pyperclip  # Library for interacting with clipboard
import os  # Library for interacting with the operating system
import sys  # Library for accessing system-specific parameters and functions

# Check if the script is being run with command-line arguments
if len(sys.argv) > 1:
    # Change the current working directory to the specified path
    os.chdir(sys.argv[1])  # sys.argv[1] is the first command-line argument

# Copy the current working directory to the clipboard
pyperclip.copy(os.getcwd())  # Get the current working directory using os.getcwd()
```