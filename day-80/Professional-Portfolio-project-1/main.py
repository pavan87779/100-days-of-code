MORSE_CODE_DICT = {

'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',

'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',

'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',

'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',

'4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',

'9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',

'/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'

}



def string_to_morse_code(text):

    text = text.upper()

    morse_code = [MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT]

    return ' '.join(morse_code)




input_string = input("Enter the string to convert to Morse Code: ")
morse_code = string_to_morse_code(input_string)
print("Morse Code: ", morse_code)