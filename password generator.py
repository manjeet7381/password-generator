import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.root.configure(bg="#88ebcb")

        self.create_interface()

    def create_interface(self):
        self.length_label = tk.Label(self.root, text="Password Length:", bg="#88ebcb", font=('Arial', 12))
        self.length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.length_entry.insert(0, "12")

        self.num_label = tk.Label(self.root, text="Number of Passwords:", bg="#88ebcb", font=('Arial', 12))
        self.num_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.num_entry = tk.Entry(self.root, width=10)
        self.num_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.num_entry.insert(0, "1")

        self.generate_button = tk.Button(self.root, text="Generate Password(s)", command=self.generate_passwords,
                                         bg="#9bc1cb", font=('Arial', 10))
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.root, text="", bg="#88ebcb", font=('Arial', 12))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_passwords(self):
        try:
            password_length = int(self.length_entry.get())
            num_passwords = int(self.num_entry.get())

            if password_length <= 0 or num_passwords <= 0:
                raise ValueError("Invalid input. Please enter positive integers.")

            generated_passwords = [self.generate_password(password_length) for _ in range(num_passwords)]

            result_text = "\n".join([f"Password {i + 1}: {password}" for i, password in enumerate(generated_passwords)])
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showwarning("Error", f"Invalid input: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()