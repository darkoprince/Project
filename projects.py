from gpiozero import LED, Button
from signal import pause
from time import sleep
import urllib2

led = LED(17)
button_pressed = Button(2)

def ifttt():
        urllib2.urlopen("https://maker.ifttt.com/trigger/woman_inlabour/with/key/mth3UwjXe5RsyLclHaatC4562E8gL5JIujqqmn2Q0KH").read()


button_pressed.when_pressed = ifttt

button_pressed.when_pressed = led.on
button_pressed.when_released = led.off


def dot():
        led.on()
        sleep(2)
        led.off()
        sleep(0.1)

ifttt()
pause()

