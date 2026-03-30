import sys
import os
import requests
from PyQt5 import QtWidgets

# Ensure path is set so it can find the 'ui' folder
sys.path.append(os.getcwd())
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "./platforms"

# Import the design from the file you just showed me
from ui.ecc import Ui_MainWindow

class ECCClient(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Setup the UI elements (buttons, labels, etc.)
        self.setupUi(self)
        
        # API address (Make sure api.py is running!)
        self.api_url = "http://127.0.0.1:5000/api/ecc"
        
        # Connect the buttons to our logic functions
        self.btnGenerate.clicked.connect(self.generate_keys)
        self.btnSign.clicked.connect(self.sign_message)
        self.btnVerify.clicked.connect(self.verify_signature)
        print("✅ ECC Client Initialized and Connected.")

    def generate_keys(self):
        try:
            response = requests.get(f"{self.api_url}/generate_keys")
            QtWidgets.QMessageBox.information(self, "API", response.json().get('message'))
        except Exception as e:
            print(f"Error: {e}")

    def sign_message(self):
        info = self.txtInformation.toPlainText()
        if not info: return
        try:
            response = requests.post(f"{self.api_url}/sign", json={'message': info})
            self.txtSignature.setPlainText(response.json().get('signature', ''))
        except Exception as e:
            print(f"Sign Error: {e}")

    def verify_signature(self):
        info = self.txtInformation.toPlainText()
        sig = self.txtSignature.toPlainText()
        try:
            response = requests.post(f"{self.api_url}/verify", json={'message': info, 'signature': sig})
            if response.json().get('is_verified'):
                QtWidgets.QMessageBox.information(self, "Success", "Valid! ✅")
            else:
                QtWidgets.QMessageBox.critical(self, "Failed", "Invalid! ❌")
        except Exception as e:
            print(f"Verify Error: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ECCClient()
    print("🚀 Opening ECC Cipher Window...")
    window.show()
    sys.exit(app.exec_())