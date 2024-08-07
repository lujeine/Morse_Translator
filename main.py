from tkinter import *
from tkinter import messagebox
from morse_code import encrypt, decrypt, play_morse_code

# Create a GUI window
window = Tk()

from_language = StringVar(window)
to_language = StringVar(window)

from_language.set("lang-code")
to_language.set("lang-code")

# Store the Morse code message
morse_message = ""


# Function to clear both the text areas
def clear_all():
    from_language_field.delete(1.0, END)
    to_language_field.delete(1.0, END)


# perform conversion from one language to another
def convert():
    global morse_message
    message = from_language_field.get("1.0", "end")[:-1]

    if from_language.get() == to_language.get():
        messagebox.showerror("Can't Be same Language")
        return
    elif from_language.get() == "Eng" and to_language.get() == "Morse":
        morse_message = encrypt(message)
        to_language_field.insert('end -1 chars', morse_message)
    elif from_language.get() == "Morse" and to_language.get() == "Eng":
        result = decrypt(message)
        to_language_field.insert('end -1 chars', result)
    else:
        messagebox.showerror("Please choose valid language code..")
        return


# play the Morse code sound
def play_sound():
    play_morse_code(morse_message)


# Driver code
if __name__ == "__main__":
    window.configure(background='white')
    window.geometry("600x500")
    window.title("Morse Translator")

    from_language_field = Text(window, height=5, width=40, font="lucida 13")
    to_language_field = Text(window, height=5, width=40, font="lucida 13")

    from_language_field.grid(row=1, column=1, padx=30, pady=30)
    to_language_field.grid(row=2, column=1, padx=30, pady=30)

    languageCode_list = ["Eng", "Morse"]

    FromLanguage_option = OptionMenu(window, from_language, *languageCode_list)
    ToLanguage_option = OptionMenu(window, to_language, *languageCode_list)

    FromLanguage_option.grid(row=1, column=2, ipadx=10)
    ToLanguage_option.grid(row=2, column=2, ipadx=10)

    convert_button = Button(window, text="Convert", bg="white", fg="black",
                            command=convert, width=20, height=2)

    clear_button = Button(window, text="Clear", bg="white",
                          fg="black", command=clear_all, width=20, height=2)

    play_button = Button(window, text="Play Sound", bg="white", fg="black",
                         command=play_sound, width=20, height=2)

    convert_button.grid(row=3, column=1, pady=10)
    clear_button.grid(row=4, column=1, pady=10)
    play_button.grid(row=5, column=1, pady=10)

    window.mainloop()
