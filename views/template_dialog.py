# views/template_dialog.py

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QWidget,
    QLineEdit, QComboBox, QCheckBox, QPushButton, QSizePolicy
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal


class TemplateDialog(QDialog):
    # "Apply" 버튼 클릭 시 데이터를 전달하는 시그널 정의
    apply_clicked = pyqtSignal(dict)

    def __init__(self, image_path, data=None, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.data = data.copy() if data else {
            "ViewName": "",
            "URLPattern": "",
            "Title": "",
            "ProxyApply": False,
            "ODataSet": ""
        }
        self.init_ui()

    def init_ui(self):
        # 다이얼로그 속성 설정
        self.setWindowTitle("템플릿 다이얼로그")
        self.setFixedSize(1100, 700)

        # 다이얼로그의 전체 높이의 5%를 헤더 높이로 설정
        header_height = int(700 * 0.05)  # 35px

        # 메인 수직 레이아웃 생성
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 헤더 레이아웃 생성
        header_widget = QWidget()
        header_widget.setFixedHeight(header_height)
        header_widget.setStyleSheet("background-color: #2c66af;")

        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(10, 0, 10, 0)
        header_label = QLabel("템플릿 다이얼로그")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        header_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header_label)

        header_widget.setLayout(header_layout)
        main_layout.addWidget(header_widget)

        # 콘텐츠 수평 레이아웃 생성 (좌측과 우측 레이아웃 배치)
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(10)

        # 좌측 레이아웃 생성 (템플릿 미리보기)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        # '템플릿 미리보기' 라벨 추가
        left_title_label = QLabel("템플릿 미리보기")
        left_title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        left_title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        left_layout.addWidget(left_title_label)

        # 이미지 라벨 생성 및 설정
        image_label = QLabel()
        pixmap = QPixmap(self.image_path).scaled(770, 558, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("border: 1px solid #ccc;")
        left_layout.addWidget(image_label)

        # 좌측 레이아웃에 남은 공간을 채워 아래쪽 여백을 없앰
        left_layout.addStretch()

        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setFixedWidth(780)
        left_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # 우측 레이아웃 생성 (파일설정)
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)

        # '파일설정' 라벨 추가
        right_title_label = QLabel("파일설정")
        right_title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        right_title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        right_layout.addWidget(right_title_label)

        # 설정 정보 표시용 위젯 생성 및 레이아웃 설정
        right_widget = QWidget()
        right_widget.setStyleSheet("background-color: #f0f0f0;")
        right_widget_layout = QVBoxLayout()
        right_widget_layout.setContentsMargins(0, 0, 0, 0)
        right_widget_layout.setSpacing(2)  # 라벨과 컨트롤 간 간격 2px

        # Function to create label and input with minimal spacing
        def create_field(label_text, widget):
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 1)
            layout.setSpacing(1)
            label = QLabel(label_text)
            label.setStyleSheet("font-size: 14px;")
            layout.addWidget(label)
            layout.addWidget(widget)
            return layout

        # ViewName
        self.view_name_input = QLineEdit()
        self.view_name_input.setText(self.data.get("ViewName", ""))
        view_name_layout = create_field("ViewName:", self.view_name_input)
        right_widget_layout.addLayout(view_name_layout)

        # URL Pattern
        self.url_pattern_input = QLineEdit()
        self.url_pattern_input.setText(self.data.get("URLPattern", ""))
        url_pattern_layout = create_field("URL Pattern:", self.url_pattern_input)
        right_widget_layout.addLayout(url_pattern_layout)

        # Title
        self.title_input = QLineEdit()
        self.title_input.setText(self.data.get("Title", ""))
        title_layout = create_field("Title:", self.title_input)
        right_widget_layout.addLayout(title_layout)

        # Proxy Apply
        self.proxy_checkbox = QCheckBox()
        self.proxy_checkbox.setChecked(self.data.get("ProxyApply", False))
        proxy_label = QLabel("프록시 적용 여부:")
        proxy_label.setStyleSheet("font-size: 14px;")
        proxy_layout = QHBoxLayout()
        proxy_layout.setContentsMargins(0, 0, 0, 1)
        proxy_layout.setSpacing(1)
        proxy_layout.addWidget(proxy_label)
        proxy_layout.addWidget(self.proxy_checkbox)
        proxy_layout.addStretch()
        proxy_container = QWidget()
        proxy_container.setLayout(proxy_layout)
        right_widget_layout.addWidget(proxy_container)

        # ODataSet
        self.odata_select = QComboBox()
        self.odata_select.addItems(["Option 1", "Option 2", "Option 3"])  # 예시 데이터
        self.odata_select.setCurrentText(self.data.get("ODataSet", "Option 1"))
        odata_layout = create_field("ODataSet:", self.odata_select)
        right_widget_layout.addLayout(odata_layout)

        # 설정 위젯 레이아웃 설정
        right_widget.setLayout(right_widget_layout)
        right_widget.setFixedWidth(240)
        right_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # 우측 레이아웃에 설정 위젯 추가
        right_layout.addWidget(right_widget)

        # 우측 레이아웃에 남은 공간을 채워 'Apply' 버튼을 하단에 배치
        right_layout.addStretch()

        # Apply 버튼
        apply_button = QPushButton("Apply")
        apply_button.setStyleSheet("background-color: #2c66af; color: white; font-weight: bold;")
        apply_button.setFixedHeight(40)
        apply_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        apply_button.clicked.connect(self.on_apply)
        right_layout.addWidget(apply_button)

        # 우측 컨테이너 위젯 생성 및 레이아웃 설정
        right_container_widget = QWidget()
        right_container_widget.setLayout(right_layout)
        right_container_widget.setFixedWidth(240)
        right_container_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # 콘텐츠 레이아웃에 좌우 위젯 추가
        content_layout.addWidget(left_widget)
        content_layout.addWidget(right_container_widget)

        # 메인 레이아웃에 콘텐츠 레이아웃 추가
        main_layout.addLayout(content_layout)

        # 다이얼로그의 메인 레이아웃 설정
        self.setLayout(main_layout)

    def on_apply(self):
        # 필드에서 데이터 수집
        data = {
            "ViewName": self.view_name_input.text(),
            "URLPattern": self.url_pattern_input.text(),
            "Title": self.title_input.text(),
            "ProxyApply": self.proxy_checkbox.isChecked(),
            "ODataSet": self.odata_select.currentText()
        }
        # 데이터를 시그널을 통해 전달
        self.apply_clicked.emit(data)
        # 다이얼로그 닫기
        self.accept()
