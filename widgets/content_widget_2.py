from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class ContentWidget2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("콘텐츠 2", self)
        layout.addWidget(label)
        self.setLayout(layout)
