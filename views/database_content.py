# views/database_content.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class DatabaseContent(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("데이터베이스 페이지 내용이 여기에 표시됩니다.")
        layout.addWidget(label)
        self.setLayout(layout)
