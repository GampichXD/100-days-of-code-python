# Professional Portfolio Project - GUI
# Typing Speed Test desktop app
# Author : Abraham
import tkinter as tk
from tkinter import messagebox
import time

# Sample text to type
sample_text = (
    "The quick brown fox jumps over the lazy dog. "
    "This sentence contains every letter in the English alphabet."
)

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")

        self.start_time = None

        # Sample text display
        self.sample_label = tk.Label(root, text="Type the following text:", font=("Arial", 14))
        self.sample_label.pack(pady=10)

        self.text_display = tk.Text(root, height=5, wrap="word", font=("Courier", 14), bg="#f0f0f0")
        self.text_display.insert("1.0", sample_text)
        self.text_display.config(state="disabled")
        self.text_display.pack(padx=20, pady=10, fill="x")

        # Typing area
        self.input_field = tk.Text(root, height=5, wrap="word", font=("Courier", 14))
        self.input_field.pack(padx=20, pady=10, fill="x")
        self.input_field.bind("<FocusIn>", self.start_timer)

        # Done button
        self.done_button = tk.Button(root, text="Done", font=("Arial", 12), command=self.calculate_speed)
        self.done_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        end_time = time.time()
        typed_text = self.input_field.get("1.0", "end-1c")
        time_taken = (end_time - self.start_time) / 60  # minutes

        word_count = len(typed_text.split())
        wpm = round(word_count / time_taken) if time_taken > 0 else 0

        # Accuracy calculation
        accuracy = self.calculate_accuracy(sample_text, typed_text)

        self.result_label.config(
            text=f"⏱Typing Speed: {wpm} WPM\n🧮Accuracy: {accuracy:.2f}%"
        )
        self.start_time = None  # reset for next try

    def calculate_accuracy(self, original, typed):
        original_words = original.strip().split()
        typed_words = typed.strip().split()

        correct = 0
        for o, t in zip(original_words, typed_words):
            if o == t:
                correct += 1

        accuracy = (correct / len(original_words)) * 100 if original_words else 0
        return accuracy

# Run the app
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()
