from imu_show_design import *

from SerialWidget import *
import time
import sys

import logo
import base64
import os

class myWindow(QtWidgets.QWidget, Ui_imu_show):
  isConnect = False
  dCubeColor = {"top" : "red", "bottom" : "green", "left" : "blue", "right" : "yellow", "front" : "cyan", "back" : "pink"}
  dAngle = {"pitch" : 0.0, "roll" : 0.0, "yaw" : 0.0}
  angleBufLen = 50
  aAngleX = [0 for i in range(0, angleBufLen)]
  aAngleY = [0 for i in range(0, angleBufLen)]
  aAngleZ = [0 for i in range(0, angleBufLen)]
  angleCount = 0
  
  def __init__(self):
    super(myWindow, self).__init__()
    self.setupUi(self)

    self.lPorts = None
    self.strReceive = ""

    tmp = open('imu_show_logo_2017413.png', 'wb+')
    tmp.write(base64.b64decode(logo.img))
    self.label_logo.setPixmap(QtGui.QPixmap("imu_show_logo_2017413.png"))
    tmp.close()
    os.remove('imu_show_logo_2017413.png')

    self.serial = SerialWidget()
    for baud in self.serial.lBaud:
      self.comboBox_baud.addItem(str(baud))
    self.onRefreshCom()

  def begin(self):
    print('myWindow begin')
    self.openGLWidget_imu.paintFunc = self.paintAxis

  def paintAxis(self):
    self.openGLWidget_imu.rotate(-self.dAngle["pitch"], 0, 0, 1)
    self.openGLWidget_imu.rotate(-self.dAngle["roll"],  1, 0, 0)
    self.openGLWidget_imu.rotate(-self.dAngle["yaw"],   0, 1, 0)
    self.openGLWidget_imu.fillCubeColor(-0.225, -0.075, -0.375, 0.450, 0.15, 0.750, self.dCubeColor)
    self.openGLWidget_imu.axis(2)

  def onConnect(self):
    if self.isConnect == False:
      if self.comboBox_com.count():
        for port in self.lPorts:
          if port.portName() == self.comboBox_com.currentText():
            if self.serial.open(port, int(self.comboBox_baud.currentText()), self.onPortReceive) == True:
              self.isConnect = True
              self.pushButton_connect.setText("disconnect")
            else:
              QtWidgets.QMessageBox.information(self, "error", "open faild")
      else:
        QtWidgets.QMessageBox.information(self, "information", "please refresh com")
    else:
      self.isConnect = False
      self.pushButton_connect.setText("connect")
      self.serial.close()

  def onPortReceive(self):
    # print("onPortReceive" + " " + str(time.time()))
    receive = self.serial.serialPort.readAll()
    for count in range(len(receive)):
      try:
        self.strReceive += receive[count]
      except:
        self.strReceive += " "
    receiveLen = len(self.strReceive)
    if receiveLen:
      if receiveLen > 2048:
        self.strReceive = self.strReceive[receiveLen - 2048: ]
      self.textBrowser_receive.setText(self.strReceive)
      self.textBrowser_receive.moveCursor(QtGui.QTextCursor.End)

      #update display
      try:
        rPitch = self.strReceive.rindex("pitch:")
        rEnd = self.strReceive.rindex("\n")
        if rEnd > rPitch:
          strAtti = self.strReceive[rPitch: rEnd]
          lStrAtti = strAtti.split(" ", 3)
          if len(lStrAtti) == 4:
            self.aAngleX[self.angleCount] = float(lStrAtti[0][len("pitch:"): len(lStrAtti[0])])
            self.aAngleY[self.angleCount] = float(lStrAtti[1][len("roll:"): len(lStrAtti[1])])
            self.aAngleZ[self.angleCount] = float(lStrAtti[2][len("yaw:"): len(lStrAtti[2])])
            if (max(self.aAngleX) - min(self.aAngleX)) > 1.5:
              self.dAngle["pitch"] = self.aAngleX[self.angleCount]
            if (max(self.aAngleY) - min(self.aAngleY)) > 1.5:
              self.dAngle["roll"] = self.aAngleY[self.angleCount]
            if (max(self.aAngleZ) - min(self.aAngleZ)) > 2.0:
              self.dAngle["yaw"] = self.aAngleZ[self.angleCount]
            self.angleCount += 1
            if self.angleCount == self.angleBufLen:
              self.angleCount = 0
            self.openGLWidget_imu.paintGL()
      except:
        pass

  def onRefreshCom(self):
    self.comboBox_com.clear()
    self.lPorts = self.serial.scan()
    if len(self.lPorts):
      for port in self.lPorts:
        self.comboBox_com.addItem(port.portName())

  def onComboBaudChanged(self):
    if self.isConnect:
      self.serial.serialPort.setBaudRate(int(self.comboBox_baud.currentText()))

app = QtWidgets.QApplication(sys.argv)
app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
window = myWindow()
window.begin()
window.show()
sys.exit(app.exec_())
