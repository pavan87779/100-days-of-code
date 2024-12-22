import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def pdf_to_text(pdf_file):
    """
    Extracts text from a PDF file.

    :param pdf_file: Path to the PDF file.
    :return: Extracted text as a string.
    """
    text = ""
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def text_to_speech(text, output_file):
    """
    Converts text to speech and saves it as an audio file.

    :param text: Text to convert.
    :param output_file: Path for the output audio file.
    """
    try:
        tts = gTTS(text)
        tts.save(output_file)
        print(f"Audio file saved as: {output_file}")
    except Exception as e:
        print(f"Error converting text to speech: {e}")

def select_pdf():
    """Opens a file dialog to select a PDF file."""
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        text = pdf_to_text(pdf_path)
        if text.strip():
            save_audio(text)
        else:
            messagebox.showerror("Error", "No text found in the PDF file.")

def save_audio(text):
    """Opens a file dialog to save the audio file."""
    audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if audio_path:
        text_to_speech(text, audio_path)
        messagebox.showinfo("Success", f"Audio file saved as: {audio_path}")

def main():
    root = tk.Tk()
    root.title("PDF to Audiobook")

    canvas = tk.Canvas(root, width=400, height=200)
    canvas.pack()

    label = tk.Label(root, text="Upload a PDF to Convert to Audiobook", font=("Helvetica", 14))
    canvas.create_window(200, 50, window=label)

    upload_btn = tk.Button(root, text="Upload PDF", command=select_pdf, bg="blue", fg="white", font=("Helvetica", 12))
    canvas.create_window(200, 100, window=upload_btn)

    root.mainloop()

if __name__ == "__main__":
    main()
