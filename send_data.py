import bluetooth
import time


bd_addr = "C4:8E:8F:BC:5A:18"
port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))


def data(map_environment, bot_coordinates):
    sock.send("map: " + str(map_environment) + "\n" + "bot coordinates: " + str(bot_coordinates))
    time.sleep(5)
