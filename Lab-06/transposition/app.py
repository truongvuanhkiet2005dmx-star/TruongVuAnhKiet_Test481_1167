import math
import tkinter as tk
from tkinter import messagebox

# --- PHẦN LOGIC CỦA BẠN ---
class TranspositionCipher:
    def encrypt(self, text, key):
        if not text: return ""
        if key <= 1: return text
        
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        if not text: return ""
        if key <= 1: return text
        
        num_cols = int(key)
        num_rows = math.ceil(len(text) / num_cols)
        num_shaded_boxes = (num_cols * num_rows) - len(text)
        
        matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
        
        curr_char_idx = 0
        for col in range(num_cols):
            for row in range(num_rows):
                if row == num_rows - 1 and col >= num_cols - num_shaded_boxes:
                    continue
                if curr_char_idx < len(text):
                    matrix[row][col] = text[curr_char_idx]
                    curr_char_idx += 1
        
        decrypted_text = []
        for row in range(num_rows):
            for col in range(num_cols):
                decrypted_text.append(matrix[row][col])
                
        return ''.join(decrypted_text)

# --- PHẦN GIAO DIỆN (UI) ---
class TranspositionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transposition Tool - Lab 06")
        self.root.geometry("450x500")
        self.root.configure(bg="#f5f5f5")
        self.cipher = TranspositionCipher()

        # Tiêu đề
        tk.Label(root, text="TRANSPOSITION CIPHER", font=('Helvetica', 14, 'bold'), bg="#f5f5f5", fg="#333").pack(pady=10)

        # Message Input
        tk.Label(root, text="Nhập văn bản:", bg="#f5f5f5").pack(anchor="w", padx=20)
        self.txt_input = tk.Text(root, height=5, width=50)
        self.txt_input.pack(pady=5, padx=20)

        # Key Input
        tk.Label(root, text="Nhập Key (Số nguyên):", bg="#f5f5f5").pack(anchor="w", padx=20)
        self.entry_key = tk.Entry(root, width=10)
        self.entry_key.insert(0, "3")
        self.entry_key.pack(pady=5, padx=20, anchor="w")

        # Buttons
        btn_frame = tk.Frame(root, bg="#f5f5f5")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="MÃ HÓA", bg="#2ecc71", fg="white", font=('bold'), width=15, command=self.do_encrypt).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="GIẢI MÃ", bg="#3498db", fg="white", font=('bold'), width=15, command=self.do_decrypt).pack(side=tk.LEFT, padx=10)

        # Result Output
        tk.Label(root, text="Kết quả:", bg="#f5f5f5").pack(anchor="w", padx=20)
        self.txt_output = tk.Text(root, height=5, width=50, bg="#e8efff")
        self.txt_output.pack(pady=5, padx=20)

    def do_encrypt(self):
        text = self.txt_input.get("1.0", tk.END).strip()
        try:
            key = int(self.entry_key.get())
            res = self.cipher.encrypt(text, key)
            self.show_res(res)
        except:
            messagebox.showerror("Lỗi", "Vui lòng nhập Key là số nguyên!")

    def do_decrypt(self):
        text = self.txt_input.get("1.0", tk.END).strip()
        try:
            key = int(self.entry_key.get())
            res = self.cipher.decrypt(text, key)
            self.show_res(res)
        except:
            messagebox.showerror("Lỗi", "Vui lòng nhập Key là số nguyên!")

    def show_res(self, res):
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, res)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranspositionApp(root)
    root.mainloop()