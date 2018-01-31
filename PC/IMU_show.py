import os
import time
import string

from OpenGL.GL import *       #组件
from OpenGL.GLU import *      #组件
from OpenGL.GLUT import *     #组件
from OpenGL.WGL import *      #组件

from matplotlib import * #组件

import df_serial
import df_opengl_graphics;

g2D = df_opengl_graphics.Graphics2D()
g3D = df_opengl_graphics.Graphics3D()
ser = df_serial.DF_Serial()

dColor = {"top" : "red", "bottom" : "green", "left" : "blue", "right" : "yellow", "front" : "cyan", "back" : "pink"}

rotate = 0
lastTick = 0.001

frameTick = 0.001
frameCount = 0
lastFrame = 0

def begin():
  pass

dAngle = {"pitch" : 0.0, "roll" : 0.0, "yaw" : 0.0}
angleBufLen = 50
aAngleX = [0 for i in range(0, angleBufLen)]
aAngleY = [0 for i in range(0, angleBufLen)]
aAngleZ = [0 for i in range(0, angleBufLen)]
angleCount = 0

def graphics():
  global dAngle
  global rotate
  g3D.loadIdentity()
  g3D.setMatrixMode(g3D.GLMODE_VIEW)

  #g3D.rotate(rotate, 1, 1, 1)
  g3D.rotate(-dAngle["pitch"], 0, 0, 1)
  g3D.rotate(-dAngle["roll"],  1, 0, 0)
  g3D.rotate(-dAngle["yaw"],   0, 1, 0)
  g3D.fillCubeColor(-0.15, -0.05, -0.25, 0.3, 0.1, 0.5, dColor)
  g3D.axis(2)

  # time.sleep(0.001)
  # rotate += 1
  # if rotate == 360:
    # rotate = 0

def getNum(str1, str2, str3):
  try:
    start = str1.index(str2)
    try:
      return float(str1[len(str2) : len(str1)])
    except:
      return None
  except:
    return None

def captureMove(arr):
  pass
    
def serialFunc():
  global dAngle
  global lastTick
  
  global aAngleX
  global aAngleY
  global aAngleZ
  global angleCount
  
  global frameTick
  global frameCount
  global lastFrame
  
  tick = time.time()
  
  if ser.isStart:
    try:
      str_read = ser.read().decode()
    except:
      str_read = " "
    #print(str_read)
    if len(str_read) > 0:
      lastTick = tick
      lStr = str_read.split(" ", 3)
      if len(lStr) == 4:
        angleX = getNum(lStr[0], "pitch:", " PITCH:")
        angleY = getNum(lStr[1], "roll:", "ROLL:")
        angleZ = getNum(lStr[2], "yaw:", "YAW:")
        if angleX != None and angleY != None and angleZ != None:
          aAngleX[angleCount] = angleX
          aAngleY[angleCount] = angleY
          aAngleZ[angleCount] = angleZ
          
          #capture move
          if (max(aAngleX) - min(aAngleX)) > 1:
            dAngle["pitch"] = aAngleX[angleCount]
          if (max(aAngleY) - min(aAngleY)) > 1:
            dAngle["roll"] = aAngleY[angleCount]
          if (max(aAngleZ) - min(aAngleZ)) > 2:
            dAngle["yaw"] = aAngleZ[angleCount]
          
          frameCount += 1
          
          angleCount += 1
          if angleCount == angleBufLen:
            angleCount = 0
            
        else:
          print("data error")
      else:
        print("data error")
      
  serHold = 0
  if ser.isStart == 0:
    ser.lPorts = ser.scan()
  elif (tick - lastTick) > 0.03:
    lastTick = tick
    ser.lPorts = ser.scan()
  if ser.lastPortCount != len(ser.lPorts):
    print(ser.lPorts[0][0])
    ser.lastPortCount = len(ser.lPorts)
    i = 0
    for i in range(len(ser.lPorts)):
      if ser.lPort[0] == ser.lPorts[i][0]:
        if ser.isStart == 1:
        
          serHold = 1
    if serHold == 0:
      if ser.ser != None:
        ser.close()
      if len(ser.lPorts):
        ser.portCount = 0
        ser.lPort = ser.lPorts[0]
        print("select com " + ser.lPort[0])
      else:
        ser.lPort = ser.STR_NONE
  
  g3D.showStrPixel(0, 16 * 1, "\"S\":change com, \"B\":change baud, \"O\":open/close com", "white")
  str_portNum = "got " + str(len(ser.lPorts)) + " coms"
  g3D.showStrPixel(0, 16 * 2, str_portNum, "white")
  str_selectCom = "select com :" + ser.lPort[0] + " ( " + ser.str_status + " ) "
  g3D.showStrPixel(0, 16 * 3, str_selectCom, "white")
  str_baud = "baud :" + str(ser.baud)
  g3D.showStrPixel(0, 16 * 4, str_baud, "white")
  str_color = "front :" + dColor["front"] + " back :" + dColor["back"] + \
              " top :" + dColor["top"] + " bottom :" + dColor["bottom"] + \
              " left :" + dColor["left"] + " right :" + dColor["right"]
  g3D.showStrPixel(0, 16 * 5, str_color, "orange")
  
  if (time.time() - frameTick) >= 1:
    frameTick = time.time()
    str_frame = "FPS :" + str(frameCount)
    lastFrame = frameCount
    frameCount = 0
  else:
    str_frame = "FPS :" + str(lastFrame)
  g3D.showStrPixel(0, 16 * 6, str_frame, "cyan")

dKey = {"changeSerial" : "sS", "changeBaud" : "bB", "open" : "oO"}
def keyFunc(key, x, y):
  global dKey
  print("get key ", key)
  str_key = key.decode()  #bytes转string
  if ser.isStart == 0:
    if dKey["changeSerial"].count(str_key) > 0:  
      ser.lPorts = ser.scan()
      if len(ser.lPorts):
        ser.portCount += 1
        if ser.portCount >= len(ser.lPorts):
          ser.portCount = 0
        ser.lPort = ser.lPorts[ser.portCount]
        print("change com")

    if dKey["changeBaud"].count(str_key) > 0:
      ser.baudCount += 1
      if ser.baudCount >= len(ser.lBaud):
        ser.baudCount = 0
      ser.baud = ser.lBaud[ser.baudCount]

  if dKey["open"].count(str_key):
    if ser.isStart == 0:
      ser.open()
    else:
      ser.close()


def idleFunc():
  g3D.clear()
  serialFunc()
  graphics()
  g3D.flush()

df_opengl_graphics.Windows(b"IMU show", 800, 800, 1100, 0, begin, 1, idleFunc, keyFunc)
