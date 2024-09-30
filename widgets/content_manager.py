# widgets/content_manager.py

from views.home_content import HomeContent
from views.database_content import DatabaseContent
from views.odata_content import ODataContent
from PyQt5.QtWidgets import QWidget


# 기타 콘텐츠 위젯 임포트

def get_content_widget(menu_name):
    if menu_name == 'Home':
        return HomeContent()
    elif menu_name == 'Database':
        return DatabaseContent()
    elif menu_name == 'OData':
        return ODataContent()
    else:
        return QWidget()  # 기본 빈 위젯 또는 에러 메시지를 표시하는 위젯을 반환
