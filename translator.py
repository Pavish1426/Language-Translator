from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

# ---------------- TEXT TO SPEECH ---------------- #

engine = pyttsx3.init()

def speak_text():
    text = output_text.get("1.0", END)

    if text.strip() != "":
        engine.say(text)
        engine.runAndWait()

# ---------------- COPY FUNCTION ---------------- #

def copy_text():
    translated = output_text.get("1.0", END)

    window.clipboard_clear()
    window.clipboard_append(translated)

    messagebox.showinfo("Copied", "Translated text copied!")

# ---------------- TRANSLATE FUNCTION ---------------- #

def translate_text():
    try:
        source_lang = languages[source_language.get()]
        target_lang = languages[target_language.get()]

        input_data = input_text.get("1.0", END)

        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(input_data)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- MAIN WINDOW ---------------- #

window = Tk()
window.title("CodeAlpha Language Translator")
window.geometry("800x500")
window.config(bg="lightblue")

# ---------------- LANGUAGE LIST ---------------- #

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# ---------------- TITLE ---------------- #

title = Label(
    window,
    text="AI LANGUAGE TRANSLATOR",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue"
)

title.pack(pady=10)

# ---------------- INPUT TEXT ---------------- #

input_label = Label(
    window,
    text="Enter Text",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)

input_label.pack()

input_text = Text(
    window,
    height=8,
    width=70,
    font=("Arial", 12)
)

input_text.pack(pady=10)

# ---------------- LANGUAGE SELECTION ---------------- #

frame = Frame(window, bg="lightblue")
frame.pack()

# Source Language

source_language = StringVar()
source_combo = ttk.Combobox(
    frame,
    textvariable=source_language,
    values=list(languages.keys()),
    width=20
)

source_combo.set("English")
source_combo.grid(row=0, column=0, padx=20)

# Target Language

target_language = StringVar()
target_combo = ttk.Combobox(
    frame,
    textvariable=target_language,
    values=list(languages.keys()),
    width=20
)

target_combo.set("Tamil")
target_combo.grid(row=0, column=1, padx=20)

# ---------------- TRANSLATE BUTTON ---------------- #

translate_button = Button(
    window,
    text="Translate",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=translate_text
)

translate_button.pack(pady=15)

# ---------------- OUTPUT TEXT ---------------- #

output_label = Label(
    window,
    text="Translated Text",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)

output_label.pack()

output_text = Text(
    window,
    height=8,
    width=70,
    font=("Arial", 12)
)

output_text.pack(pady=10)

# ---------------- BUTTONS ---------------- #

button_frame = Frame(window, bg="lightblue")
button_frame.pack(pady=10)

copy_button = Button(
    button_frame,
    text="Copy",
    font=("Arial", 11, "bold"),
    bg="orange",
    command=copy_text
)

copy_button.grid(row=0, column=0, padx=10)

speak_button = Button(
    button_frame,
    text="Speak",
    font=("Arial", 11, "bold"),
    bg="purple",
    fg="white",
    command=speak_text
)

speak_button.grid(row=0, column=1, padx=10)

# ---------------- RUN APPLICATION ---------------- #

window.mainloop()