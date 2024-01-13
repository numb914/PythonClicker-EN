import mouse
import time
import keyboard
key = input('Set the key for the limited clicker').lstrip()
key1 = input('Set the key to activate the unlimited clicker').lstrip()
key2 = input('Set the key to deactivate the unlimited clicker').capitalize().lstrip()
delay = input('Set the delay for the unlimited clicker').lstrip()
print('Скрипт активирован')
if ',' in delay:
    delay = float(delay.replace(',', '.'))
while True:
    while keyboard.is_pressed(key):
        mouse.click('left')
        time.sleep(0.01)
    if keyboard.is_pressed(key1):
        while True:
            mouse.click('left')
            time.sleep(delay - 0.01)
            if keyboard.is_pressed(key2):
                break
            if keyboard.is_pressed(key1):
                continue
            time.sleep(0.01)
    time.sleep(0.01)