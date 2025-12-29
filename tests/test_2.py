import sys
import os
import pytest
from unittest.mock import MagicMock, patch
import tkinter as tk

# Add the project root to the Python path to allow imports from Product_realize
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Product_realize.gui_crolling_like_v3 import MainApp, items, frame_li, frame_dict

@pytest.fixture
def app():
    """Fixture to create and tear down the MainApp instance."""
    # Mock tkinter's mainloop and other problematic methods for testing
    with patch('tkinter.Tk.mainloop', return_value=None), \
         patch('tkinter.Tk.geometry', return_value=None):
        
        # Reset frame_dict for each test
        _frame_dict = {}
        application = MainApp(items, frame_li, _frame_dict)
        
        # Replace tkraise on each frame instance with a unique mock
        for frame in application.frame_dict.values():
            frame.tkraise = MagicMock()

        yield application
        # Destroy the root window after the test
        application.root.destroy()

def test_app_initialization(app):
    """Test if the MainApp initializes correctly."""
    assert app.root.title() == '유튜브 댓글 크롤링 / 좋아요 click'
    assert app.items == items
    # Check if all frames are created
    for frame_name in frame_li:
        assert frame_name in app.frame_dict
        assert isinstance(app.frame_dict[frame_name], tk.Frame)
    # Check that the initial frame was raised
    app.frame_dict['초기화면'].tkraise.assert_called_once()


def test_change_frame(app):
    """Test the change_frame method."""
    # Reset mock from initialization to have a clean state for this test
    app.frame_dict['초기화면'].tkraise.reset_mock()

    # Test changing to another frame
    app.change_frame('유튜브 댓글 크롤링')
    app.frame_dict['유튜브 댓글 크롤링'].tkraise.assert_called_once()
    app.frame_dict['초기화면'].tkraise.assert_not_called()

    # Test changing to a non-existent frame
    app.change_frame('없는 프레임')
    # No new tkraise calls should be made to the last correct frame
    app.frame_dict['유튜브 댓글 크롤링'].tkraise.assert_called_once()


@patch('threading.Thread')
@patch('Product_realize.gui_crolling_like_v3.youtube_comment_crolling_v1.main')
def test_crolling_frame_change(mock_crolling_main, mock_thread, app):
    """Test the crolling_FrameChange method."""
    test_url = "http://test.url"
    
    app.crolling_FrameChange(test_url)

    # 1. Check if it changes to the '대기화면'
    app.frame_dict['대기화면'].tkraise.assert_called_once()

    # 2. Check if a thread was created with the correct target and args
    mock_thread.assert_called_once()
    args, kwargs = mock_thread.call_args
    assert kwargs['target'] == mock_crolling_main
    assert kwargs['args'] == (test_url, app.change_frame)

    # 3. Check if the thread was started
    mock_thread.return_value.start.assert_called_once()


@patch('threading.Thread')
@patch('Product_realize.gui_crolling_like_v3.youtube_comment_like_v2.main')
def test_like_frame_change(mock_like_main, mock_thread, app):
    """Test the like_FrameChange method."""
    test_url = "http://like-test.url"
    test_id = "test_id"
    test_pass = "test_pass"

    app.like_FrameChange(test_url, test_id, test_pass)

    # 1. Check if it changes to the '대기화면'
    app.frame_dict['대기화면'].tkraise.assert_called_once()

    # 2. Check if a thread was created with the correct target and args
    mock_thread.assert_called_once()
    args, kwargs = mock_thread.call_args
    assert kwargs['target'] == mock_like_main
    assert kwargs['args'] == (test_url, test_id, test_pass, app.change_frame)
    
    # 3. Check if the thread was started
    mock_thread.return_value.start.assert_called_once()
