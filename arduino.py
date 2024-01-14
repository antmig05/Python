import pyfirmata

comport = 'COM3'

board = pyfirmata.Arduino(comport)

led1 = board.get_pin('d:9:o')
led2 = board.get_pin('d:10:o')
led3 = board.get_pin('d:11:o')
led4 = board.get_pin('d:12:o')
led5 = board.get_pin('d:13:o')

def led(l):
    if l == 0:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
    elif l ==1:
        led1.write(1)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
    elif l ==2:
        led1.write(1)
        led2.write(1)
        led3.write(0)
        led4.write(0)
        led5.write(0)
    elif l == 3:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(0)
        led5.write(0)
    elif l == 4:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(0)
    elif l == 5:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(1)