def test(Mainapp):
    assert '초기화면' in Mainapp.frame_dict
    assert '완료화면' in Mainapp.frame_dict
    assert '유튜브 댓글 크롤링' in Mainapp.frame_dict
    assert '유튜브 댓글 좋아요' in Mainapp.frame_dict
    assert '대기화면' in Mainapp.frame_dict

    assert '유튜브 댓글 좋아요' in Mainapp.combobox['values']
    assert '유튜브 댓글 크롤링' in Mainapp.combobox['values']

    Mainapp.root.destroy()

    


