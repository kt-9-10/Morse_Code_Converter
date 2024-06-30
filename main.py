MORSE_CODE_RULES = {
    'a': '·−', 'b': '−···', 'c': '−·−·', 'd': '−··', 'e': '·', 'f': '··−·',
    'g': '−−·', 'h': '····', 'i': '··', 'j': '·−−−', 'k': '−·−', 'l': '·−··',
    'm': '−−', 'n': '−·', 'o': '−−−', 'p': '·−−·', 'q': '−−·−', 'r': '·−·',
    's': '···', 't': '−', 'u': '··−', 'v': '···−', 'w': '·−−', 'x': '−··−',
    'y': '−·−−', 'z': '−−··',
    '0': '−−−−−', '1': '·−−−−', '2': '··−−−', '3': '···−−', '4': '····−',
    '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·',
    '.': '·−·−·−', ',': '−−··−−', '?': '··−−··', "'": '·−−−−·', '!': '−·−·−−',
    '/': '−··−·', '(': '−·−−·', ')': '−·−−·−', '&': '·−···', ':': '−−−···',
    ';': '−·−·−·', '=': '−···−', '+': '·−·−·', '-': '−····−', '_': '··−−·−',
    '"': '·−··−·', '$': '···−··−', '@': '·−−·−·',
    ' ': '  '
}

while True:

    converted_text = ''
    input_text = input('Please enter the text you want to encode to Morse code: \n')
    if input_text == '':
        break
    else:
        for key in input_text.lower():
            try:
                converted_text += MORSE_CODE_RULES[key]

            except KeyError:
                converted_text = 'Invalid character included.'
                break

            else:
                converted_text += ' '

        print(f'Result:\n{converted_text}\n')
