from bot.message_handler import extract_ca

def test_extract_ca():
    message = "Entry signal: Buy 0x1234567890abcdef1234567890abcdef12345678"
    expected_ca = "0x1234567890abcdef1234567890abcdef12345678"
    assert extract_ca(message) == expected_ca

    message_no_ca = "Entry signal: Buy Now!"
    assert extract_ca(messahe_no_ca) is None