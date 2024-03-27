from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests
import sys
from PyQt5.QtWidgets import QApplication

class UI(QMainWindow):
    def __init__(self, api):
        super(UI, self).__init__()
        self.api = api
        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"MainWindow")
        self.resize(511, 738)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.setCentralWidget(self.centralwidget)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(260, 160, 171, 51))
        self.submit_button.setFont(font)
        self.submit_button.clicked.connect(self.submit)

        self.question_text = QTextEdit(self.centralwidget)
        self.question_text.setObjectName(u"question_text")
        self.question_text.setGeometry(QRect(20, 80, 411, 81))
        self.question_text.setFont(font)

        self.copy_button = QPushButton(self.centralwidget)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setGeometry(QRect(20, 630, 171, 41))
        self.copy_button.setFont(font1)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        self.result_text = QTextEdit(self.centralwidget)
        self.result_text.setObjectName(u"result_text")
        self.result_text.setGeometry(QRect(20, 250, 411, 371))
        self.result_text.setFont(font1)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(270, 630, 161, 41))
        self.save_button.setFont(font1)
        self.save_button.clicked.connect(self.save_to_file)

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.copy_button.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save to File", None))

    def submit(self):
        # Get the question from the text box
        question = self.question_text.toPlainText().strip()

        # Generate a response using the OpenAI Chat API
        response = self.api.generate_response(question)

        # Check if the API request was successful
        if response.status_code == 200:
            response_json = response.json()

            # Check if 'choices' is in the response
            if 'choices' in response_json:
                # Check if 'message' and 'content' are in the first choice
                if 'message' in response_json['choices'][0] and 'content' in response_json['choices'][0]['message']:
                    # Extract the generated response from the API response
                    generated_text = response_json['choices'][0]['message']['content']
                    self.result_text.setPlainText(generated_text)
                else:
                    # Show an error message if 'message' or 'content' is not in the first choice
                    QMessageBox.critical(self, 'Error', 'Unexpected response from OpenAI Chat API: Missing "message" or "content"')
            else:
                # Show an error message if 'choices' is not in the response
                QMessageBox.critical(self, 'Error', 'Unexpected response from OpenAI Chat API: Missing "choices"')
        else:
            # Show an error message if the API request fails
            QMessageBox.critical(self, 'Error', 'Failed to generate response from OpenAI Chat API')

    def copy_to_clipboard(self):
        # Get the response text
        response = self.result_text.toPlainText()

        # Copy the response to the clipboard
        QApplication.clipboard().setText(response)

    def save_to_file(self):
        # Get the question and response text
        question = self.question_text.toPlainText().strip()
        response = self.result_text.toPlainText().strip()

        # Open a file dialog
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')

        # Save the question and response to the file
        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write(f"Question: {question}\n\n")
                    file.write(f"Response: {response}\n")

                QMessageBox.information(self, 'Success', 'File saved successfully')
            except Exception as e:
                # Show an error message if the file saving fails
                QMessageBox.critical(self, 'Error', f'Failed to save file: {str(e)}')
    
    def run(self):
        app = QApplication([])
        self.show()
        sys.exit(app.exec_())
