# views/template_dialog.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class TemplateDialog(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        # 다이얼로그 크기 설정
        self.setWindowTitle("템플릿 보기")
        self.setFixedSize(1100, 700)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 이미지를 QLabel에 추가
        label = QLabel()
        pixmap = QPixmap(self.image_path).scaled(1050, 650, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        # 레이아웃에 이미지 라벨 추가
        layout.addWidget(label)

        # 레이아웃을 다이얼로그에 설정
        self.setLayout(layout)
