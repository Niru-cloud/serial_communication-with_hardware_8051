import serial
import sys
print("WELCOME TO SERIAL COMMUNICATION USING PYTHON")

def send_data():
  port="COM3"
  serial_port = serial.Serial(port, 9600)
  if serial_port.is_open:
   print(port,"Port is open")
   temp=input("ENTER THE DATA YOU WANT TO SEND AND PRESS ENTER:")
   b=temp.encode('utf-8')
   serial_port.write(b)
   print("Data Sent Successfully...!")
def receive_data():
  port="COM3"
  serial_port = serial.Serial(port, 9600)
  if serial_port.is_open:
    print(port,"port is open")
    print("Waiting for incoming data.....")
    while True:
      byte_data= serial_port.read()
      print (byte_data.decode('utf-8'),end="")

try:
  send_data()
  receive_data()
except serial.SerialException:
 try:
   port="COM3"
   serial.Serial(port, 9600).close()
   print("Port is closed")
   serial_port = serial.Serial(port,9600)
   print("Port is open again")
   send_data()
   receive_data()
 except:
  print("unable to open port")
  sys.exit()

