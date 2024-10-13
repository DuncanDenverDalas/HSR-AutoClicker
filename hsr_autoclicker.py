import time
import threading
import mouse
import keyboard
import pyautogui
from pynput.keyboard import Key, Listener, KeyCode
import pywinauto
import pygetwindow as gw
import pyuac
import PyInstaller

def focus_to_window(window_title = None) :
    window = gw.getWindowsWithTitle(window_title)[0]
    if not window.isActive :
        pywinauto.application.Application().connect(handle=window._hWnd).top_window().set_focus()

class thread(threading.Thread) : 

    autoclickerOn = False
    shouldKus = False

    def __init__(self, thread_name, thread_ID) : 
        threading.Thread.__init__(self) 
        self.thread_name = thread_name 
        self.thread_ID = thread_ID 
 
    def run(self) : 
        while not self.shouldKus :
            time.sleep(0.03)
            self.loop() 

    def loop(self) :
        if not self.autoclickerOn :
            return

        focus_to_window("Honkai: Star Rail")

        pyautogui.tripleClick()
        pyautogui.mouseDown()
        pyautogui.mouseUp(x = mouse.get_position()[0] + 10, y = mouse.get_position()[1] + 10)
        mouse.move(-10, -10, absolute=False, duration=0.00)

thread1 = thread("Loop is looping", 1000)

def keyboardCallback(key):

    print('\nYou Entered {0}'.format( key))
 
    if key == KeyCode.from_char('`') :
        thread1.autoclickerOn = not thread1.autoclickerOn

    if key == Key.end :
        thread1.shouldKus = True
        return False

def main():

    thread1.start()
    with Listener(on_press = keyboardCallback) as listener: 
        listener.join()


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
        main()
    else:        
        main()
