from flask import Flask, request, jsonify
# Đảm bảo đường dẫn import này đúng với cấu trúc thư mục của bạn
from cipher.ecc import ECCCipher 

app = Flask(__name__)

# Khởi tạo thuật toán ECC
ecc_cipher = ECCCipher()

# ==========================================
# ECC CIPHER ENDPOINTS (Chỉ giữ lại phần này)
# ==========================================

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys_api():
    # Gọi hàm tạo key từ class ECCCipher
    message = ecc_cipher.generate_keys()
    return jsonify({'message': message})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_api():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Thực hiện ký số
    signature_hex = ecc_cipher.sign_message(message)
    if signature_hex:
        return jsonify({'signature': signature_hex})
    return jsonify({'error': 'Keys not found. Please generate keys first.'}), 404

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_api():
    data = request.json
    message = data.get('message')
    signature_hex = data.get('signature')
    
    if not message or not signature_hex:
        return jsonify({'error': 'Missing data (message or signature)'}), 400
    
    # Thực hiện kiểm tra chữ ký
    is_verified = ecc_cipher.verify_signature(message, signature_hex)
    return jsonify({'is_verified': is_verified})

# Chạy Server
if __name__ == "__main__":
    # Debug=True giúp bạn thấy lỗi cụ thể nếu code có vấn đề
    app.run(host="0.0.0.0", port=5000, debug=True)