
import spidev

class SPICommunication:
    def __init__(self, bus=0, device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 1000000  # Set SPI communication speed

    def send_data(self, data):
        self.spi.writebytes(data)

    def receive_data(self):
        return self.spi.readbytes(10)  # Read 10 bytes of data

    def close(self):
        self.spi.close()
