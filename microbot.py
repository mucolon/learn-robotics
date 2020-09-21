from microbit import i2c, display, Image


class MotoBit():
    '''Initialize moto:bit hardware.
    '''
    I2C_ADDR = 0x59         # 89
    CMD_ENABLE = 0x70       # 112
    CMD_SPEED_LEFT = 0x21   # 33
    CMD_SPEED_RIGHT = 0x20  # 32

    def __init__(self):
        # cool code that you'll write
        # lol I can't give you all the answers
        pass

    def enable(self):
        '''Enable motor driver.
        '''
        i2c.write(self.I2C_ADDR, bytes([self.CMD_ENABLE, 0x01]))

    def disable(self):
        '''Disable motor driver.
        '''
        i2c.write(self.I2C_ADDR, bytes([self.CMD_ENABLE, 0x00]))

    def drive(self, speed_left, speed_right):
        '''Drive motors continuously based on 100 point scale.
        Args:
            speed_left (int|float): Motor power value. [-100, 100]
            speed_right (int|float): Motor power value. [-100, 100]
        '''
        speeds = [speed_left, speed_right]
        for i in range(2):
            speeds[i] = round(speeds[i] * 1.275 + 127.5)
            if speeds[i] < 0:
                speeds[i] = 0
            elif speeds[i] > 255:
                speeds[i] = 255
        i2c.write(self.I2C_ADDR, bytes([self.CMD_SPEED_LEFT, speeds[0]]))
        i2c.write(self.I2C_ADDR, bytes([self.CMD_SPEED_RIGHT, speeds[1]]))


display.show(Image.HAPPY, clear=True, delay=2000)
bot = MotoBit()
bot.enable()
bot.drive(50, 50)
