from PyQt5.QtSerialPort import *

class SerialWidget(QSerialPort, QSerialPortInfo):
  lBaud = [115200, 9600, 57600, 512000, 921600]
  
  def __init__(self):
    self.serialPort = QSerialPort()
    self.serialInfo = QSerialPortInfo()

  def scan(self):
    return self.serialInfo.availablePorts()

  def open(self, info, baud, slot):
    self.serialPort.close()
    self.serialPort.setPort(info)
    self.serialPort.setBaudRate(baud)
    self.serialPort.setParity(QSerialPort.NoParity)
    self.serialPort.setDataBits(QSerialPort.Data8)
    self.serialPort.setStopBits(QSerialPort.OneStop)
    self.serialPort.setFlowControl(QSerialPort.NoFlowControl)
    self.serialPort.readyRead.connect(slot)
    if self.serialPort.open(QSerialPort.ReadWrite) == True:
      self.serialPort.read(1)
      if self.serialPort.error():
        print("serial port error")
      return True
    return False

  def close(self):
    self.serialPort.close()
    self.serialPort.readyRead.disconnect()
