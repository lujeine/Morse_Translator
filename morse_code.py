import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load dot and dash sound files
dot_sound = pygame.mixer.Sound("dot.mp3")
dash_sound = pygame.mixer.Sound("dash.mp3")

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

DOT_DURATION = 0.1  # Duration of a dot in seconds
DASH_DURATION = 0.3  # Duration of a dash in seconds


def play_dot():
    dot_sound.play()
    time.sleep(DOT_DURATION)
    dot_sound.stop()


def play_dash():
    dash_sound.play()
    time.sleep(DASH_DURATION)
    dash_sound.stop()


def play_morse_code(message):
    for char in message:
        if char == '.':
            play_dot()
        elif char == '-':
            play_dash()
        elif char == ' ':
            time.sleep(DOT_DURATION)  # Gap between parts of the same letter
        elif char == '/':
            time.sleep(DASH_DURATION)  # Gap between letters
        time.sleep(DOT_DURATION)  # Gap between symbols


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += '/ '
    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    i = 0
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher
