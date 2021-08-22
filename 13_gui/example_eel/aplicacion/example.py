import eel
import eel.browsers

eel.browsers.set_path('chrome', '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe')

my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 3333,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}
eel.init('web')
eel.start('main.html')