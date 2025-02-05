from unittest.mock import patch
from bot.bot import start_bot

@patch("telegram.ext.Updater")
def test_start_bot(mock_updater):
    start_bot()
    mock_updater.assert_called_once()