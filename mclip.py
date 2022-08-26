#! python3
# mclip.py - a multi-clipboard program

import sys
import pyperclip

# To run: python3 mclip.py hello this way you are giving the word to be found

TEXT = {
    'agree': """Yes, that sounds fine to me""",
    'busy': """Sorry, can we do this later?""",
    'hello': """Hellooooo!!!!!!!""",
    "fede": "Hola Fede!"
}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

# first command line arg is the keyphrase
keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for %s copied into the clipboard' % (keyphrase))
else:
    print(f'There is no text for %s' % (keyphrase))

