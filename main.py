# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from views.header import Header
from views.side_menu import SideMenu
from views.content_area import ContentArea
from widgets.content_manager import get_content_widget


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('헤더, 메뉴, 콘텐츠 레이아웃')
        self.setGeometry(100, 100, 1200, 800)

        # 메인 위젯과 레이아웃 설정
        main_widget = QWidget()
        main_layout = QVBoxLayout()  # 메인 수직 레이아웃 (헤더 + 본문)

        # 여백 및 간격 제거
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 상단에 고정된 헤더 추가
        self.header = Header()
        self.header.setFixedHeight(50)  # 헤더 높이를 50px로 고정
        main_layout.addWidget(self.header)

        # 본문(body) 레이아웃 (좌측 메뉴 + 콘텐츠 영역을 수평으로 배치)
        body_layout = QHBoxLayout()

        # 좌측 메뉴 위젯 추가
        self.side_menu = SideMenu()
        self.side_menu.setFixedWidth(200)  # 메뉴 너비를 200px로 고정
        body_layout.addWidget(self.side_menu)

        # 콘텐츠 영역 위젯 추가
        self.content_area = ContentArea()
        # self.content_area.setStyleSheet("background-color: #ffffff;")  # 콘텐츠 영역에 배경색과 경계선 적용
        body_layout.addWidget(self.content_area)

        # 본문 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(body_layout)

        # 메인 위젯에 레이아웃 적용
        main_widget.setLayout(main_layout)

        # 메인 위젯을 QMainWindow의 중앙에 배치
        self.setCentralWidget(main_widget)

        # 스타일 시트를 메인 윈도우에 설정
        self.setStyleSheet("""
        
            #titleWidget {
                background-color: #ffffff;  /* 타이틀 영역 배경: 연한 회색 */
                border-bottom: 1px solid #cccccc;  /* 하단 경계선 */
            }
         
        """)

        # 사이드 메뉴 버튼과 시그널 연결
        self.connect_side_menu_buttons()

    def connect_side_menu_buttons(self):
        for button in self.side_menu.menu_buttons:
            button.clicked.connect(self.handle_menu_button_clicked)

    def handle_menu_button_clicked(self, menu_name):
        self.content_area.set_title(menu_name)
        content_widget = get_content_widget(menu_name)
        if content_widget is not None:
            self.content_area.set_content_widget(content_widget)
        else:
            self.content_area.set_content_widget(QWidget())  # 빈 위젯 설정


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
