# views/home_content.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy


class HomeContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 수평 레이아웃 (버튼 2개를 가로로 나란히 배치)
        hbox = QHBoxLayout()

        # 버튼 1 생성 및 크기 설정
        button1 = QPushButton("Button 1", self)
        button1.setFixedSize(150, 150)
        button1.setStyleSheet("margin-bottom: 30px;")  # 하단 마진 설정

        # 버튼 2 생성 및 크기 설정
        button2 = QPushButton("Button 2", self)
        button2.setFixedSize(150, 150)
        button2.setStyleSheet("margin-bottom: 30px;")  # 하단 마진 설정

        # 버튼 사이에 간격을 50px 주는 스페이서 추가
        spacer = QSpacerItem(50, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # 수평 레이아웃에 버튼과 스페이서 추가
        hbox.addWidget(button1)
        hbox.addItem(spacer)
        hbox.addWidget(button2)

        # 수직 레이아웃 (수평 레이아웃을 중앙에 배치)
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # 위쪽 여백
        vbox.addLayout(hbox)  # 버튼들이 들어간 수평 레이아웃
        vbox.addStretch(1)  # 아래쪽 여백

        # 최종 레이아웃을 설정
        self.setLayout(vbox)

        # 스타일 시트를 사용하여 배경색을 설정
        self.setStyleSheet("""
            QWidget {
                background-color: #8F9197;  /* 배경색 설정 */
            }
        """)
