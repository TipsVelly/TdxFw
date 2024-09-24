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
        right_pixmap = QPixmap('images/SNBArrowRight.png')
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
                border-right: 1px solid #000010;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.menu_name)  # 메뉴 이름과 함께 시그널 emit

    # enterEvent와 leaveEvent는 제거합니다.


class SideMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.menu_buttons = []  # 버튼들을 저장할 리스트
        self.init_ui()

    def init_ui(self):
        self.menu_layout = QVBoxLayout()
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setSpacing(0)

        # 메뉴 버튼 추가 함수 호출
        self.add_menu_button('Home', 'SNBHomeIcon')
        self.add_menu_button('Database', 'SNBTemplateGen')
        self.add_menu_button('OData', 'SNBTemplateGen')
        self.add_menu_button('Template', 'SNB_Menu-2')
        self.add_menu_button('Menu', 'SNBMenuIcon')
        self.add_menu_button('User', 'SNB_Menu-1')
        self.add_menu_button('Settings', 'SNB_Menu')

        # 남는 공간을 빈칸으로 채움
        self.menu_layout.addStretch(1)

        # 레이아웃을 적용
        self.setLayout(self.menu_layout)

        # 사이드 메뉴의 최소 크기를 설정
        self.setMinimumSize(200, 400)
        self.setFixedWidth(200)  # 사이드 메뉴의 너비를 고정

        # SideMenu에 객체 이름 할당
        self.setObjectName("sideMenu")

        # 배경 스타일링 활성화
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 스타일 시트를 사용해 SideMenu에만 스타일 적용
        self.setStyleSheet("""
            QWidget#sideMenu {
                background-color: #ffffff;  
                border-right: 1px solid #000010;    /* 사이드메뉴 경계선 */
            }
        """)

    def add_menu_button(self, menu_name, icon_name):
        button = MenuButton(menu_name, icon_name, self)
        self.menu_layout.addWidget(button)
        self.menu_buttons.append(button)  # 버튼을 리스트에 추가
