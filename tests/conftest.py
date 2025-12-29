import pytest
from Product_realize.gui_crolling_like_v3 import MainApp

@pytest.fixture
def Mainapp():
    mainapp = MainApp(['유튜브 댓글 크롤링', '유튜브 댓글 좋아요'], ['초기화면', '유튜브 댓글 크롤링', '유튜브 댓글 좋아요', '대기화면', '완료화면'], {})
    return mainapp

