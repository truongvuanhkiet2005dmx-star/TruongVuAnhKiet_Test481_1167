import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        if not text: return ""
        if key <= 1: return text
        
        # Mã hóa: Đọc theo cột
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
        
        # 1. Tính số hàng và số cột
        num_cols = int(key)
        num_rows = math.ceil(len(text) / num_cols)
        
        # 2. Tính số "ô trống" (shaded boxes) ở hàng cuối cùng
        num_shaded_boxes = (num_cols * num_rows) - len(text)
        
        # 3. Tạo ma trận để chứa các ký tự
        matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
        
        # 4. Điền bản mã vào ma trận theo CỘT
        # Đây là bước quan trọng nhất mà code cũ của bạn làm sai
        curr_char_idx = 0
        for col in range(num_cols):
            for row in range(num_rows):
                # Nếu ô này là ô trống ở cuối ma trận thì bỏ qua không điền
                if row == num_rows - 1 and col >= num_cols - num_shaded_boxes:
                    continue
                
                if curr_char_idx < len(text):
                    matrix[row][col] = text[curr_char_idx]
                    curr_char_idx += 1
        
        # 5. Đọc ma trận theo HÀNG để lấy lại bản rõ ban đầu
        decrypted_text = []
        for row in range(num_rows):
            for col in range(num_cols):
                decrypted_text.append(matrix[row][col])
                
        return ''.join(decrypted_text)