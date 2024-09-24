from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

class HoverButton(QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        icon = QIcon(icon_path)
        self.setIcon(icon)
        self.setIconSize(QSize(24, 24))
        self.setFixedSize(30, 30)
        self.setStyleSheet("background-color: #2c66af; border: none;")

    def enterEvent(self, event):
        self.setCursor(QCursor(Qt.PointingHandCursor))  # 마우스 포인터 변경
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.unsetCursor()  # 커서 기본 상태로 복구
        super().leaveEvent(event)

class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # 로고 이미지 추가
        logo_label = QLabel(self)
        pixmap = QPixmap("images/logo.png")  # 로고 이미지 경로
        logo_label.setPixmap(pixmap)

        # 로고 왼쪽 여백 추가
        layout.addSpacing(20)
        layout.addWidget(logo_label)

        # 중간에 공간 추가
        layout.addStretch(1)

        # Bell 버튼 추가
        bell_button = HoverButton("images/HeaderBell.png", self)
        layout.addWidget(bell_button)

        # Personal 버튼 추가
        personal_button = HoverButton("images/HeaderPersonal.png", self)
        layout.addWidget(personal_button)

        # 배경색 설정 (파란색)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#2c66af'))
        self.setPalette(palette)

        self.setLayout(layout)
