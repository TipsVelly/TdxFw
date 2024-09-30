from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout
from PyQt5.QtGui import QPixmap, QCursor, QFont
from PyQt5.QtCore import Qt, pyqtSignal, QSize


class MenuButton(QWidget):
    clicked = pyqtSignal(str)  # 메뉴 이름을 전달하는 시그널로 변경

    def __init__(self, menu_name, icon_name, parent=None):
        super().__init__(parent)
        self.menu_name = menu_name  # 메뉴 이름을 인스턴스 변수로 저장
        self.setObjectName('menuButton')  # 객체 이름 설정
        self.init_ui(menu_name, icon_name)
        self.init_style()  # 스타일 초기화

    def init_ui(self, menu_name, icon_name):
        # 레이아웃 설정
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0)  # 좌우 여백 조정
        layout.setSpacing(5)  # 위젯 간 간격

        # 좌측 아이콘
        left_icon_label = QLabel(self)
        pixmap = QPixmap(f'images/{icon_name}.png')
        left_icon_label.setPixmap(pixmap)
        left_icon_label.setFixedSize(20, 20)
        left_icon_label.setScaledContents(True)

        # 메뉴 이름 라벨
        text_label = QLabel(menu_name, self)
        text_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # 글꼴 설정
        font = QFont('Sans-Serif', 10)
        font.setBold(True)
        font.setPixelSize(14)
        text_label.setFont(font)
        text_label.setFixedHeight(22)  # 라벨 높이 설정

        # 우측 아이콘
        right_icon_label = QLabel(self)
        right_pixmap = QPixmap('../images/SNBArrowRight.png')
        right_icon_label.setPixmap(right_pixmap)
        right_icon_label.setFixedSize(15, 15)
        right_icon_label.setScaledContents(True)

        # 레이아웃에 위젯 추가
        layout.addWidget(left_icon_label)
        layout.addWidget(text_label)
        layout.addStretch(1)  # 남은 공간 채우기
        layout.addWidget(right_icon_label)

        self.setLayout(layout)

        # 버튼 높이 설정
        self.setFixedHeight(40)

        # 사이즈 정책 설정 (가로로 확장)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # 마우스 포인터 변경
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def init_style(self):
        self.setAttribute(Qt.WA_StyledBackground, True)  # 배경 스타일링 활성화
        self.setStyleSheet("""
            QWidget#menuButton {
                background-color: transparent;
            }
            QWidget#menuButton:hover {
                background-color: #EAF0F7;
                border-right: 1px solid #cccccc;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.menu_name)  # 메뉴 이름과 함께 시그널 emit
