# views/odata_content.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt, QSize
from views.template_dialog import TemplateDialog  # 다이얼로그 임포트


class ODataContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 그리드 레이아웃 생성 (한 열에 3개의 이미지 레이블 배치)
        grid_layout = QGridLayout()

        # 이미지 경로 리스트 (여러 개의 이미지 경로를 저장)
        image_paths = [
            'images/NoTemplate.png',  # 이미지 경로를 실제 경로로 수정
            'images/NoTemplate.png',
            'images/NoTemplate.png',
            'images/NoTemplate.png',
            'images/image5.png',
            'images/image6.png',
            'images/image7.png',
            'images/image8.png',
            'images/image9.png',
            'images/image10.png',  # 추가된 이미지
            'images/image11.png'   # 추가된 이미지
        ]

        # 3xN 그리드에 이미지 레이블 추가
        for i, image_path in enumerate(image_paths):
            label = QLabel()
            pixmap = QPixmap(image_path).scaled(250, 250, Qt.KeepAspectRatio)  # 이미지를 250x250로 설정
            label.setPixmap(pixmap)
            label.setFixedSize(250, 250)  # 레이블 크기 설정
            label.setCursor(QCursor(Qt.PointingHandCursor))  # hover 시 포인터로 변경
            label.mousePressEvent = lambda event, p=image_path: self.handle_image_click(p)  # 클릭 시 다이얼로그 띄우기
            row = i // 3
            col = i % 3
            grid_layout.addWidget(label, row, col)

        # 그리드 레이아웃을 담을 위젯
        grid_widget = QWidget()
        grid_widget.setLayout(grid_layout)

        # 그리드 위젯을 콘텐츠로 추가
        main_layout = QVBoxLayout()
        main_layout.addWidget(grid_widget)

        self.setLayout(main_layout)

    def handle_image_click(self, image_path):
        """이미지 레이블 클릭 시 다이얼로그 띄우는 메서드"""
        dialog = TemplateDialog(image_path, self)
        dialog.exec_()  # 다이얼로그 실행
