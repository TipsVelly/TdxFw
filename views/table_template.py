# table_template.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QScrollArea, QGridLayout
)
from PyQt5.QtCore import Qt, pyqtSignal

class TableTemplate(QWidget):
    property_clicked = pyqtSignal(str)  # Property 클릭 시 시그널

    def __init__(self):
        super().__init__()
        self.property_count = 1  # Property 번호를 위한 카운터
        self.max_fields_per_row = 2  # 한 줄에 최대 2개의 필드
        self.init_ui()

    def init_ui(self):
        # 메인 레이아웃 설정
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        # 서치 필드 영역 설정
        self.search_area_widget = QWidget()
        self.search_area_layout = QGridLayout()
        self.search_area_layout.setSpacing(10)
        self.search_area_widget.setLayout(self.search_area_layout)

        # 첫 번째 Property 추가
        self.add_property_field()

        # 테이블 영역 설정 (예시로 빈 위젯 추가)
        self.table_area_widget = QWidget()
        self.table_area_widget.setStyleSheet("background-color: #f0f0f0;")
        self.table_area_widget.setFixedHeight(300)  # 예시 높이

        # 메인 레이아웃에 위젯 추가
        self.main_layout.addWidget(self.search_area_widget)
        self.main_layout.addWidget(self.table_area_widget)

        self.setLayout(self.main_layout)

    def add_property_field(self):
        # 현재 필드 수에 따라 위치 결정
        field_index = self.property_count - 1
        row = field_index // self.max_fields_per_row
        col = (field_index % self.max_fields_per_row) * 2  # 라벨과 필드를 위해 *2

        # Property 라벨 생성
        property_label = QLabel(f"Property {self.property_count}")
        property_label.setFixedWidth(75)
        property_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # 서치 필드 생성
        search_field = QLineEdit()
        search_field.setFixedSize(175, 32)

        # Property 클릭 시 시그널 연결
        property_label.mousePressEvent = lambda event, label=property_label: self.on_property_clicked(label.text())

        # 레이아웃에 추가
        self.search_area_layout.addWidget(property_label, row, col)
        self.search_area_layout.addWidget(search_field, row, col + 1)

        # 필드가 최대 개수에 도달하면 ADD 버튼 추가
        if (self.property_count % (self.max_fields_per_row)) == 0:
            add_button = QPushButton("+")
            add_button.setFixedSize(34, 34)
            add_button.clicked.connect(self.add_property_field)
            add_label = QLabel("ADD")
            add_label.setFixedWidth(50)
            add_layout = QVBoxLayout()
            add_layout.addWidget(add_button)
            add_layout.addWidget(add_label)
            add_widget = QWidget()
            add_widget.setLayout(add_layout)
            self.search_area_layout.addWidget(add_widget, row, col + 2)

        self.property_count += 1

    def on_property_clicked(self, property_name):
        # Property 클릭 시 시그널 방출
        self.property_clicked.emit(property_name)
