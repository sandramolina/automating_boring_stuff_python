#! python3

"""
    bulletPointAdder.py - Adds Wikipedia bullet points to the start
    of each line of text on the clipboard.
"""

import pyperclip
# Paste text from the clipboard:
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = f'* {lines[i]}'

text = '\n'.join(lines)

# Copy the new text to the clipboard.
pyperclip.copy(text)
