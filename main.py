import webbrowser
import pyautogui
import time
browser_destination = 'C:\\Users\\vlad1\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe'
browser = webbrowser.BackgroundBrowser(browser_destination)
webbrowser.register('Yandex', None, browser)
webbrowser.get('yandex').open_new_tab('https://music.yandex.ru/radio/activity')
time.sleep(5)
pyautogui.press('space')
pyautogui.press('0')
for i in range(10):
    pyautogui.press('+')
    time.sleep(5)
a = 10
if a == 10:
    a += 1
    print(a)
else:
    print("неудача")
