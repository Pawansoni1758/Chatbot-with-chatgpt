from PyQt6.QtWidgets import QTextEdit, QMainWindow, QLineEdit, QPushButton, QApplication
import sys
from backend import ChatBot
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = ChatBot()

        self.setMinimumSize(600, 470)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 450, 350)
        self.chat_area.setReadOnly(True)

        # Add search area widget
        self.search_area = QLineEdit(self)
        self.search_area.setGeometry(10, 370, 450, 40)
        self.search_area.returnPressed.connect(self.send_message)

        # Add send button
        self.button = QPushButton("send", self)
        self.button.setGeometry(470, 370, 50, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.search_area.text().strip()
        self.chat_area.append(f"<p style = 'color:#333333'>Me: {user_input}</p>")
        self.search_area.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style = 'color:#333333, background-color: #E9E9E9'>"
                              f" Bot: {response}</p>")


app = QApplication(sys.argv)
chatbot_window = ChatbotWindow()
sys.exit(app.exec())
