import bluetooth
import re
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print "Accepted connection from ", address
map_width = 13
map_environment = [[0.00 for i in range(map_width)] for j in range(map_width)]

while True:
    data = client_sock.recv(1024)
    row = 0
    column = 0
    for prob in re.findall(r"[-+]?\d*\.\d+|\d+", data):
        map_environment[row][column] = float(prob)
        column += 1
        if column == map_width:
            column = 0
            row += 1
        if row == map_width:
            break
    for x in map_environment:
       print x
    print data[-1]
    print ""