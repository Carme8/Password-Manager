import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("1000x400")
        self.root.configure(bg='#ececec')

        # KEY CRYPTOGRAPHY
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        # LAYOUT
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter your password:", bg='#ececec', fg='black', font=("JetBrainsMonoNL-Thin", 14)).pack(pady=10)

        self.password_entry = tk.Entry(self.root, show='*', width=30, font=("JetBrainsMonoNL-Thin", 14))
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Encrypt", command=self.encrypt_password, bg='#5c5c5c', fg='black', font=("JetBrainsMonoNL-Thin", 12)).pack(pady=10)
        tk.Button(self.root, text="Decrypt", command=self.decrypt_password, bg='#5c5c5c', fg='black', font=("JetBrainsMonoNL-Thin", 12)).pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", bg='#ececec', fg='black', font=("JetBrainsMonoNL-Thin", 12))
        self.result_label.pack(pady=20)

        # BUTTONS RESET AND EXIT
        button_frame = tk.Frame(self.root, bg='#ececec')
        button_frame.pack(pady=10)

        # BUTTONS RESET
        tk.Button(button_frame, text="Reset", command=self.reset, bg='#5c5c5c', fg='black', font=("JetBrainsMonoNL-Thin", 12)).pack(side=tk.LEFT, padx=5)

        # BUTTONS EXIT
        tk.Button(button_frame, text="Exit", command=self.exit_app, bg='#5c5c5c', fg='black', font=("JetBrainsMonoNL-Thin", 12)).pack(side=tk.LEFT, padx=5)

    def encrypt_password(self):
        password = self.password_entry.get()
        if password:
            encrypted_password = self.cipher_suite.encrypt(password.encode())
            self.result_label.config(text=f"Encrypted password: {encrypted_password.decode()}")
        else:
            messagebox.showwarning("Warning!", "Enter a password before encrypting.")

    def decrypt_password(self):
        password = self.result_label.cget("text").split(": ")[-1]
        if password:
            decrypted_password = self.cipher_suite.decrypt(password.encode()).decode()
            self.result_label.config(text=f"Decrypted password: {decrypted_password}")
        else:
            messagebox.showwarning("Warning!", "No encrypted password to decrypt.")

    def reset(self):
        self.password_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
