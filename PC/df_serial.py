import serial
import serial.tools.list_ports as ports

import win32
import win32.win32api as api32


class DF_Serial:

  STR_NONE = ["None", "None"]
  STR_CLOSE = "disconnected"
  STR_OPEN = "connected"

  isStart = 0
  lPorts = [None]
  lPort = STR_NONE
  lastPortCount = 0
  portCount = 0
  lBaud = [9600, 115200]
  baud = lBaud[1]
  baudCount = 1
  str_status = STR_CLOSE
  ser = None

  def __init__(self):
    pass

  def scan(self):
    return list(ports.comports())

  def open(self):
    try:
      self.ser = serial.Serial(self.lPort[0], self.baud, timeout = 0.001)
      self.str_status = self.STR_OPEN
      self.isStart = 1
      rslt = 0
    except:
      api32.MessageBox(0, "open com faild", "error")
      rslt = -1
    print("\nself.ser = ")
    print(self.ser)
    return rslt

  def close(self):
    self.isStart = 0
    if self.ser != None:
      self.ser.close()
      self.str_status = self.STR_CLOSE

  def writeStr(self, strDat):
    if self.isStart:
      self.ser.write(strDat.encode())

  def writeList(self, lDat):
    if self.isStart:
      i = 0
      for i in range(len(lDat)):
        self.ser.write(lDat[i].encode())

  def read(self):
    if self.isStart:
      return self.ser.readall()


