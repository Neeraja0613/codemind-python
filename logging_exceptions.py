import logging

logging.basicConfig(level=logging.ERROR)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:
    logging.error("An exception occurred", exc_info=True)
