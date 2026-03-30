import tkinter as tk
from tkinter import messagebox
# Giả sử file chứa class của bạn tên là transposition_cipher.py
from transposition_cipher import TranspositionCipher 

class TranspositionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transposition Cipher Tool")
        self.root.geometry("400x450")
        self.cipher = TranspositionCipher()

        # Label & Entry cho Message
        tk.Label(root, text="Văn bản (Message):", font=('Arial', 10, 'bold')).pack(pady=5)
        self.txt_input = tk.Text(root, height=5, width=40)
        self.txt_input.pack(pady=5)

        # Label & Entry cho Key
        tk.Label(root, text="Khóa (Key - Số nguyên):", font=('Arial', 10, 'bold')).pack(pady=5)
        self.entry_key = tk.Entry(root, width=10)
        self.entry_key.insert(0, "2") # Mặc định key = 2
        self.entry_key.pack(pady=5)

        # Frame chứa nút bấm
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Mã hóa", bg="#4CAF50", fg="white", width=12, command=self.handle_encrypt).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Giải mã", bg="#2196F3", fg="white", width=12, command=self.handle_decrypt).pack(side=tk.LEFT, padx=5)

        # Kết quả
        tk.Label(root, text="Kết quả (Result):", font=('Arial', 10, 'bold')).pack(pady=5)
        self.txt_output = tk.Text(root, height=5, width=40, bg="#f0f0f0")
        self.txt_output.pack(pady=5)

    def get_params(self):
        text = self.txt_input.get("1.0", tk.END).strip()
        try:
            key = int(self.entry_key.get())
            return text, key
        except ValueError:
            messagebox.showerror("Lỗi", "Key phải là một số nguyên!")
            return None, None

    def handle_encrypt(self):
        text, key = self.get_params()
        if text and key:
            result = self.cipher.encrypt(text, key)
            self.display_result(result)

    def handle_decrypt(self):
        text, key = self.get_params()
        if text and key:
            result = self.cipher.decrypt(text, key)
            self.display_result(result)

    def display_result(self, result):
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranspositionApp(root)
    root.mainloop()