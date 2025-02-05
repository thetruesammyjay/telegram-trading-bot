import re 
from bot.trade_executor import execute_trade
from config.constants import CA_REGEX_PATTERN

def handle_message(update, context):
    message = update.message.text
    if "Entry signal" in message:
        ca = extract_ca(message)
        if ca:
            execute_trade(ca)

def extract_ca(message):
    match = re.search(CA_REGEX_PATTERN, message)
    return match.group(1) if match else None