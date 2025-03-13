import os
os.system('rd /s /q "app\\__pycache__"')
os.system('rd /s /q "__pycache__"')
os.system('rd /s /q "app\\func\\__pycache__"')
try:
    os.system('python bot.py')
except KeyboardInterrupt:
    pass