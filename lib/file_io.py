# lib/file_io.py

from pathlib import Path

def write_file(file_name, file_content):
    """Write content to a file with the .txt extension."""
    # Convert file_name to string and add .txt extension if not present
    if not str(file_name).endswith('.txt'):
        file_name = file_name.with_suffix('.txt')
    # Write the content to the file
    with open(file_name, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append content to an existing file with the .txt extension."""
    # Convert file_name to string and add .txt extension if not present
    if not str(file_name).endswith('.txt'):
        file_name = file_name.with_suffix('.txt')
    # Append the content to the file
    with open(file_name, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """Read the content of a file with the .txt extension."""
    # Convert file_name to string and add .txt extension if not present
    if not str(file_name).endswith('.txt'):
        file_name = file_name.with_suffix('.txt')
    # Read the content from the file
    with open(file_name, 'r') as f:
        return f.read()
