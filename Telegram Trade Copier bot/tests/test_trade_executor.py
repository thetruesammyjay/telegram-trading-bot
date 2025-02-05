from unittest.mock import patch
from bot.trade_executor import execute_trade

@patch("requests.post")
def test_execute_trade(mock_post):
    mock_post.return_value.status_code = 200
    ca = "0x123456789abcdef1234567890abcdef12345678"
    execute_trade(ca)
    mock_post.assert_called_once()