import RPi.GPIO as GPIO
import time

PIN_COM = 13
PIN0 = 11
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

PIN_ARR = [PIN0, PIN1, PIN2, PIN3, PIN4, PIN5, PIN6, PIN7, PIN8, PIN9, PIN_STR, PIN_PND]

CODE_LEN = 4
BLINK_DUR = 1

def keypad_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    #Setup Outputs
    GPIO.setup(PIN_COM, GPIO.OUT)
    GPIO.output(PIN_COM, GPIO.HIGH)
    #Setup Inputs
    for pin in PIN_ARR:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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
    time.sleep(1)
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
        for i,pin in enumerate(PIN_ARR):
            if(GPIO.input(pin) == GPIO.HIGH):
                if(i == 10):
                    return('*')
                elif(i == 11):
                    return('#')
                else:
                    return(str(i))

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
        time.sleep(0.5)
    return code
    
    
