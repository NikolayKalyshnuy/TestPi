from machine import Pin, Timer, PWM
from rp2 import PIO, StateMachine, asm_pio
import aiogram
# from gtts import gTTS


# tts = gTTS('hello')
led = PWM(Pin(25))
led.freq(1000)
led.duty_u16()
tim = Timer()
duty = 0


def tick(timer):
    global led
    global duty
    if duty == 65000:
        duty = 0
    else:
        duty = 65000
    led.duty_u16(duty)


tim.init(mode=Timer.PERIODIC, callback=tick, period=500)
#sdfghm