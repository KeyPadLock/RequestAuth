import RPi.GPIO as GPIO
import time

PIN_COM = 8
PIN0 = 10
PIN1 = 12
PIN2 = 16
PIN3 = 18
PIN4 = 22
PIN5 = 24
PIN6 = 26
PIN7 = 29
PIN8 = 32
PIN9 = 36
PIN_STR = 38
PIN_PND = 40
PIN_LEDR = 3
PIN_LEDG = 5
PIN_LOCK = 7

CODE_LEN = 4
BLINK_DUR = 1

def keypad_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    #Setup Outputs
    GPIO.setup(PIN_COM, GPIO.OUT)
    GPIO.output(PIN_COM, GPIO.HIGH)
    #Setup Inputs
    GPIO.setup(PIN0, GPIO.IN)
    GPIO.setup(PIN1, GPIO.IN)
    GPIO.setup(PIN2, GPIO.IN)
    GPIO.setup(PIN3, GPIO.IN)
    GPIO.setup(PIN4, GPIO.IN)
    GPIO.setup(PIN5, GPIO.IN)
    GPIO.setup(PIN6, GPIO.IN)
    GPIO.setup(PIN7, GPIO.IN)
    GPIO.setup(PIN8, GPIO.IN)
    GPIO.setup(PIN9, GPIO.IN)
    GPIO.setup(PIN_STR, GPIO.IN)
    GPIO.setup(PIN_PND, GPIO.IN)
    #Setup LEDs
    GPIO.setup(PIN_LEDR, GPIO.OUT)
    GPIO.setup(PIN_LEDG, GPIO.OUT)
    GPIO.output(PIN_LEDR, GPIO.LOW)
    GPIO.output(PIN_LEDG, GPIO.LOW)
    #Setup Solenoid
    GPIO.setup(PIN_LOCK, GPIO.OUT)
    GPIO.output(PIN_LOCK, GPIO.LOW)

def blink_green():
    GPIO.output(PIN_LEDG, GPIO.HIGH)
    time.sleep(BLINK_DUR)
    GPIO.output(PIN_LEDG, GPIO.LOW)
    print("Unlocked")
    GPIO.output(PIN_LOCK, GPIO.HIGH)
    a = read_keypad()
    print("Locked")
    GPIO.output(PIN_LOCK, GPIO.LOW)
    time.sleep(1)

def blink_red():
    GPIO.output(PIN_LEDR, GPIO.HIGH)
    time.sleep(BLINK_DUR)
    GPIO.output(PIN_LEDR, GPIO.LOW)

def read_keypad():
    while(True):
        if(GPIO.input(PIN0) == GPIO.HIGH):
            return('0')
        if(GPIO.input(PIN1) == GPIO.HIGH):
            return('1')
        if(GPIO.input(PIN2) == GPIO.HIGH):
            return('2')
        if(GPIO.input(PIN3) == GPIO.HIGH):
            return('3')
        if(GPIO.input(PIN4) == GPIO.HIGH):
            return('4')
        if(GPIO.input(PIN5) == GPIO.HIGH):
            return('5')
        if(GPIO.input(PIN6) == GPIO.HIGH):
            return('6')
        if(GPIO.input(PIN7) == GPIO.HIGH):
            return('7')
        if(GPIO.input(PIN8) == GPIO.HIGH):
            return('8')
        if(GPIO.input(PIN9) == GPIO.HIGH):
            return('9')
        if(GPIO.input(PIN_STR) == GPIO.HIGH):
            return('*')
        if(GPIO.input(PIN_PND) == GPIO.HIGH):
            return('#')

def get_code():
    #Get Code
    code = ""
    while(len(code) < CODE_LEN):
        inChar = read_keypad()
        if(inChar == "*"):
            print("Cleared")
            code = ""
        elif(str.isdigit(inChar)):
            print(inChar)
            code = code + inChar
        time.sleep(1)
    return code
    
    
