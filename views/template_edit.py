# views/template_edit.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QSizePolicy, QScrollArea
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TemplateEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 메인 수직 레이아웃 생성
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # 헤더 레이아웃 생성
        header_widget = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(10, 10, 10, 10)
        header_layout.setSpacing(20)  # metadata URL과 EntityType 간 간격을 20px로 설정

        # metadata URL 입력 필드 및 라벨을 수평 레이아웃으로 배치
        metadata_layout = QHBoxLayout()
        metadata_label = QLabel("metadata URL")
        self.metadata_input = QLineEdit()
        self.metadata_input.setFixedWidth(350)  # 너비를 350px로 고정
        metadata_layout.addWidget(metadata_label)
        metadata_layout.addWidget(self.metadata_input)

        # EntityType 선택 필드 및 라벨을 수평 레이아웃으로 배치
        entity_type_layout = QHBoxLayout()
        entity_type_label = QLabel("EntityType")
        self.entity_type_select = QComboBox()
        self.entity_type_select.addItems(["Type1", "Type2", "Type3"])  # 예시 데이터
        self.entity_type_select.setFixedWidth(250)  # 너비를 250px로 고정
        entity_type_layout.addWidget(entity_type_label)
        entity_type_layout.addWidget(self.entity_type_select)

        # Generate 버튼 추가
        generate_button = QPushButton("Generate")
        generate_button.setFixedSize(91, 34)  # 너비를 10px, 높이를 8px로 고정
        generate_button.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid black;
            border-radius: 5px;
            font-weight: bold;
        """)
        generate_button.setCursor(Qt.PointingHandCursor)  # 포인터 커서 설정

        # 헤더 레이아웃에 추가
        header_layout.addLayout(metadata_layout)
        header_layout.addLayout(entity_type_layout)
        header_layout.addStretch()  # 오른쪽으로 밀기
        header_layout.addWidget(generate_button)  # Generate 버튼을 헤더의 최 우측에 배치

        header_widget.setLayout(header_layout)
        self.main_layout.addWidget(header_widget)

        # 콘텐츠 수평 레이아웃 생성 (좌측과 우측 레이아웃 배치)
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(10)

        # 좌측 레이아웃 생성 (UI 로딩 영역)
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)  # 좌우측 레이아웃의 여백을 줄임
        left_layout.setSpacing(10)

        # 스크롤 영역에 콘텐츠 위젯 추가
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        # 실제 UI를 로드하거나 콘텐츠를 추가하는 부분입니다.
        # 여기서는 예시로 간단한 라벨을 추가합니다.
        content_widget = QWidget()
        content_layout_inside = QVBoxLayout()
        content_layout_inside.addWidget(QLabel("Content Area"))
        content_widget.setLayout(content_layout_inside)
        scroll_area.setWidget(content_widget)

        left_layout.addWidget(scroll_area)

        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 좌측 레이아웃의 배경색 설정 제거

        # 우측 레이아웃 생성 (설정 영역)
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)  # 좌우측 레이아웃의 여백을 줄임
        right_layout.setSpacing(10)

        # '{Property} setting' 라벨 추가
        right_title_label = QLabel("{Property} setting")
        right_title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        right_title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        right_layout.addWidget(right_title_label)

        # 설정 정보 표시용 위젯 생성 및 레이아웃 설정
        right_widget = QWidget()
        right_widget_layout = QVBoxLayout()
        right_widget_layout.setContentsMargins(0, 0, 0, 0)
        right_widget_layout.setSpacing(2)  # 라벨과 컨트롤 간 간격 2px

        # Function to create label and input/select with minimal spacing
        def create_field(label_text, widget):
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 1)
            layout.setSpacing(1)
            label = QLabel(label_text)
            label.setStyleSheet("font-size: 14px;")
            layout.addWidget(label)
            layout.addWidget(widget)
            return layout

        # EntityName
        self.entity_name_select = QComboBox()
        self.entity_name_select.addItems(["Entity1", "Entity2", "Entity3"])  # 예시 데이터
        entity_name_layout = create_field("EntityName:", self.entity_name_select)
        right_widget_layout.addLayout(entity_name_layout)

        # Label(Title)
        self.title_input = QLineEdit()
        title_layout = create_field("Label(Title):", self.title_input)
        right_widget_layout.addLayout(title_layout)

        # ControlType
        self.control_type_select = QComboBox()
        self.control_type_select.addItems(["TypeA", "TypeB", "TypeC"])  # 예시 데이터
        control_type_layout = create_field("ControlType:", self.control_type_select)
        right_widget_layout.addLayout(control_type_layout)

        # Enable
        self.enable_select = QComboBox()
        self.enable_select.addItems(["True", "False"])
        enable_layout = create_field("Enable:", self.enable_select)
        right_widget_layout.addLayout(enable_layout)

        # MaxLength
        self.max_length_input = QLineEdit()
        max_length_layout = create_field("MaxLength:", self.max_length_input)
        right_widget_layout.addLayout(max_length_layout)

        # 설정 위젯 레이아웃 설정
        right_widget.setLayout(right_widget_layout)
        right_widget.setFixedWidth(240)
        right_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        right_widget.setStyleSheet("background-color: #FFFFFF;")  # 우측 레이아웃의 배경색을 흰색으로 설정

        # 우측 레이아웃에 설정 위젯 추가
        right_layout.addWidget(right_widget)

        # 우측 레이아웃에 남은 공간을 채워 'Save' 버튼을 하단에 배치
        right_layout.addStretch()

        # Save 버튼
        save_button = QPushButton("저장")
        save_button.setStyleSheet("""
            background-color: #2c66af;
            border: 1px solid black;
            border-radius: 5px;
            font-weight: bold;
            color:#ffffff;
        """)
        save_button.setFixedHeight(40)
        save_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        save_button.setCursor(Qt.PointingHandCursor)  # 포인터 커서 설정
        # save_button.clicked.connect(self.on_save)  # 필요한 경우 시그널 연결
        right_layout.addWidget(save_button)

        # 우측 컨테이너 위젯 생성 및 레이아웃 설정
        right_container_widget = QWidget()
        right_container_widget.setLayout(right_layout)
        right_container_widget.setFixedWidth(240)
        right_container_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        right_container_widget.setStyleSheet("background-color: #FFFFFF;")

        # 콘텐츠 레이아웃에 좌우 위젯 추가
        content_layout.addWidget(left_widget)
        content_layout.addWidget(right_container_widget)

        # 메인 레이아웃에 콘텐츠 레이아웃 추가
        self.main_layout.addLayout(content_layout)



        # 전체 레이아웃 설정
        self.setLayout(self.main_layout)

    def update_data(self, data):
        # 전달받은 데이터를 각 UI 요소에 설정
        self.metadata_input.setText(data.get('metadata_url', ''))
        entity_type = data.get('EntityType', '')
        if entity_type:
            index = self.entity_type_select.findText(entity_type)
            if index != -1:
                self.entity_type_select.setCurrentIndex(index)
        # 우측 설정 필드들에 데이터 설정
        entity_name = data.get('EntityName', '')
        if entity_name:
            index = self.entity_name_select.findText(entity_name)
            if index != -1:
                self.entity_name_select.setCurrentIndex(index)
        self.title_input.setText(data.get('LabelTitle', ''))
        control_type = data.get('ControlType', '')
        if control_type:
            index = self.control_type_select.findText(control_type)
            if index != -1:
                self.control_type_select.setCurrentIndex(index)
        enable = data.get('Enable', '')
        if enable:
            index = self.enable_select.findText(enable)
            if index != -1:
                self.enable_select.setCurrentIndex(index)
        self.max_length_input.setText(data.get('MaxLength', ''))
