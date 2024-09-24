from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt  # Qt 모듈에서 Qt 임포트


class ContentArea(QWidget):
    def __init__(self):
        super().__init__()
        self.content_layout = None
        self.content_widget = None
        self.title_label = None
        self.title_layout = None
        self.layout = None
        self.title_widget = None
        self.init_ui()

    def init_ui(self):
        # 전체 레이아웃 설정
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)  # 여백 설정
        self.layout.setSpacing(0)  # 위젯 간의 간격을 0으로 설정

        # 타이틀 위젯 생성
        self.title_widget = QWidget(self)
        self.title_widget.setObjectName("titleWidget")  # 객체 이름 설정
        self.title_layout = QVBoxLayout()
        self.title_layout.setContentsMargins(20, 20, 20, 20)
        self.title_layout.setSpacing(0)
        self.title_widget.setLayout(self.title_layout)

        # 타이틀 라벨 추가
        self.title_label = QLabel("현재 페이지 타이틀", self)
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        font = QFont('Inter', 16)  # 글꼴 설정 (Inter, 16pt)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_layout.addWidget(self.title_label)

        # 콘텐츠 위젯 생성
        self.content_widget = QWidget(self)
        self.content_widget.setObjectName("contentWidget")  # 객체 이름 설정
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(10)
        self.content_widget.setLayout(self.content_layout)

        # 콘텐츠 영역에 라벨 추가 (예시용)
        content_label = QLabel("콘텐츠 영역", self)
        self.content_layout.addWidget(content_label)

        # 전체 레이아웃에 위젯 추가 (stretch factor 적용)
        self.layout.addWidget(self.title_widget, stretch=1)
        self.layout.addWidget(self.content_widget, stretch=9)

        # 레이아웃을 적용
        self.setLayout(self.layout)

        # ContentArea에 객체 이름 할당
        self.setObjectName("contentArea")

        # 배경 스타일링 활성화
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.title_widget.setAttribute(Qt.WA_StyledBackground, True)
        self.content_widget.setAttribute(Qt.WA_StyledBackground, True)

        # 스타일 시트를 수정하여 위젯 자체에 적용
        self.setStyleSheet("""
            QWidget#contentArea {
                background-color: #ffffff;  /* 콘텐츠 영역 배경: 흰색 */
            }
            QWidget#titleWidget {
                background-color: #f0f0f0;  /* 타이틀 영역 배경: 연한 회색 */
                border-bottom: 1px solid #cccccc;  /* 하단 경계선 */
            }
            QWidget#contentWidget {
                background-color: #ffffff;  /* 콘텐츠 영역 배경: 흰색 */
            }
        """)

    def set_title(self, title):
        """타이틀 라벨의 텍스트를 업데이트하는 메서드"""
        self.title_label.setText(title)
