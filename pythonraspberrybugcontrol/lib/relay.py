import signal
import sys
try:
    import smbus
    smbusavailable = True
except ImportError:
    smbusavailable = False

class Relay(object):

    bus = None
    logger = None
    global smbusavailable

    def __init__(self, busnumber=1, logger=None):
        self.logger = logger
        self.DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        if smbusavailable:
            self.bus = smbus.SMBus(busnumber) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
            self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
        else:
            self.protocolstate("SMBUS Python Library is not available. Simulating only")

    def on_1(self):
        self.protocolstate("on", [1,])
        self.DEVICE_REG_DATA &= ~(0x1<<0)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def on_2(self):
        self.protocolstate("on", [2,])
        self.DEVICE_REG_DATA &= ~(0x1<<1)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def on_3(self):
        self.protocolstate("on", [3,])
        self.DEVICE_REG_DATA &= ~(0x1<<2)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def on_4(self):
        self.protocolstate("on", [4,])
        self.DEVICE_REG_DATA &= ~(0x1<<3)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def off_1(self):
        self.protocolstate("off", [1,])
        self.DEVICE_REG_DATA |= (0x1<<0)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def off_2(self):
        self.protocolstate("off", [2,])
        self.DEVICE_REG_DATA |= (0x1<<1)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def off_3(self):
        self.protocolstate("off", [3,])
        self.DEVICE_REG_DATA |= (0x1<<2)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def off_4(self):
        self.protocolstate("off", [4,])
        self.DEVICE_REG_DATA |= (0x1<<3)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def allon(self):
        self.protocolstate("on", range(1,4))
        self.DEVICE_REG_DATA &= ~(0xf<<0)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def alloff(self):
        self.protocolstate("off", range(1,4))
        self.DEVICE_REG_DATA |= (0xf<<0)
        if smbusavailable: self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def protocolstate(self, message, ports=[]):
        m = []
        if ports:
            m.append("Ports")
            m.append(', '.join(str(x) for x in ports))
            m.append(":")
        m.append(message)
        message = " ".join(m)

        if self.logger:
            self.logger.debug(message)
        else:
            print message

if __name__=="__main__":
    relay = Relay()
    # Called on process interruption. Set all pins to "Input" default mode.
    def endProcess(signalnum = None, handler = None):
        relay.ALLOFF()
        sys.exit()

    signal.signal(signal.SIGINT, endProcess)

    while True:
        ct = raw_input("input: ")
        if ct == '1on':
            relay.on_1()
        elif ct == '2on':
            relay.on_2()
        elif ct == '3on':
            relay.on_3()
        elif ct == '4on':
            relay.on_4()
        elif ct == '1off':
            relay.off_1()
        elif ct == '2off':
            relay.off_2()
        elif ct == '3off':
            relay.off_3()
        elif ct == '4off':
            relay.off_4()
        elif ct == 'allon':
            relay.allon()
        elif ct == 'alloff':
            relay.alloff()