# views/content_area.py

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt  # Qt 모듈에서 Qt 임포트


class ContentArea(QWidget):
    def __init__(self):
        super().__init__()
        self.current_content_widget = None  # 현재 표시 중인 콘텐츠 위젯
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
        self.title_label = QLabel("현재 페이지 타이틀", self.title_widget)
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        font = QFont('Inter', 16)  # 글꼴 설정 (Inter, 16pt)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_layout.addWidget(self.title_label)

        # 콘텐츠 영역에 스크롤을 추가 (스크롤 가능하게 설정)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget(self.scroll_area)
        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)

        # 전체 레이아웃에 위젯 추가 (stretch factor 적용)
        self.layout.addWidget(self.title_widget, stretch=1)
        self.layout.addWidget(self.scroll_area, stretch=9)

        # 레이아웃을 적용
        self.setLayout(self.layout)

        # ContentArea에 객체 이름 할당
        self.setObjectName("contentArea")

        # 배경 스타일링 활성화
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.title_widget.setAttribute(Qt.WA_StyledBackground, True)
        self.scroll_area_widget.setAttribute(Qt.WA_StyledBackground, True)

        # 스타일 시트를 수정하여 위젯 자체에 적용
        self.setStyleSheet("""
      
            QWidget#titleWidget {
                background-color: #ffffff;  /* 타이틀 영역 배경: 연한 회색 */
                border-bottom: 1px solid #cccccc;  /* 하단 경계선 */
                }
                
            QWidget#contentArea{
                background-color : #000000;                            
            }
       
        """)

    def set_title(self, title):
        """타이틀 라벨의 텍스트를 업데이트하는 메서드"""
        self.title_label.setText(title)

    def set_content_widget(self, widget):
        """콘텐츠 영역의 위젯을 업데이트하는 메서드"""
        # 기존 콘텐츠 위젯 제거
        if self.current_content_widget is not None:
            self.scroll_area_layout.removeWidget(self.current_content_widget)
            self.current_content_widget.deleteLater()
            self.current_content_widget = None
        # 새로운 콘텐츠 위젯 추가
        self.current_content_widget = widget
        self.scroll_area_layout.addWidget(self.current_content_widget)
