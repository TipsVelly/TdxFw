# header.py

from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon, QCursor
from PyQt5.QtCore import QSize, Qt, QPoint


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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # 부모 윈도우 참조
        self.init_ui()

        # 창 이동을 위한 변수 초기화
        self.old_pos = None

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 레이아웃 여백 제거

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

        # 최소화, 최대화/복원, 닫기 버튼 추가
        minimize_button = HoverButton("images/minimize.png", self)
        minimize_button.clicked.connect(self.parent.showMinimized)
        layout.addWidget(minimize_button)

        # 최대화/복원 버튼
        self.maximize_button = HoverButton("images/maximize.png", self)
        self.maximize_button.clicked.connect(self.toggle_max_restore)
        layout.addWidget(self.maximize_button)

        # 닫기 버튼
        close_button = HoverButton("images/Close.png", self)
        close_button.clicked.connect(self.parent.close)
        layout.addWidget(close_button)

        # 배경색 설정 (파란색)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#2c66af'))
        self.setPalette(palette)

        self.setLayout(layout)
        self.setFixedHeight(50)  # 헤더 높이 고정

    def toggle_max_restore(self):
        """창 최대화 및 복원 토글"""
        if self.parent.isMaximized():
            self.parent.showNormal()
            self.maximize_button.setIcon(QIcon("images/maximize.png"))
        else:
            self.parent.showMaximized()
            self.maximize_button.setIcon(QIcon("images/restore.png"))

    def mousePressEvent(self, event):
        """마우스 클릭 위치 저장"""
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
        event.accept()

    def mouseMoveEvent(self, event):
        """창 이동"""
        if self.old_pos:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.parent.move(self.parent.pos() + delta)
            self.old_pos = event.globalPos()
        event.accept()

    def mouseReleaseEvent(self, event):
        """마우스 버튼을 놓을 때 위치 초기화"""
        self.old_pos = None
        event.accept()
