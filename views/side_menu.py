from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from widgets.menu_button import MenuButton


class SideMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.menu_layout = None
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
                border-right: 1px solid #cccccc;    /* 사이드메뉴 경계선 */
            }
        """)

    def add_menu_button(self, menu_name, icon_name):
        button = MenuButton(menu_name, icon_name, self)
        self.menu_layout.addWidget(button)
        self.menu_buttons.append(button)  # 버튼을 리스트에 추가
