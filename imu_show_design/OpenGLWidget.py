from PyQt5.QtWidgets import *

from OpenGL.GL import *
from OpenGL.GLU import *

import matplotlib._color_data

def colorToData(name):
  return int((matplotlib._color_data.CSS4_COLORS[name]).strip("#"), 16)  #去除库文件颜色数据中的“#”字符并由16进制字符转数字

class OpenGLWidget(QOpenGLWidget):
  SIDE_X = 0
  SIDE_Y = 1
  SIDE_Z = 2

  def __init__(self, parent):
    QOpenGLWidget.__init__(self, parent)
    self.paintFunc = None

  def paintGL(self):
    if self.paintFunc != None:
      self.makeCurrent()
      self.loadIdentity()
      self.setMatrixModeView()
      self.clear()
      self.paintFunc()
      self.flush()

  def initializeGL(self):
    print('OpenGLWidget initializeGL')
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

  def loadIdentity(self):
    glLoadIdentity()

  def setMatrixModeView(self):
    glMatrixMode(GL_MODELVIEW)

  def clear(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  #清空缓存

  def flush(self):
    glFlush()  #刷新显示

  def setColor(self, color):
    var1 = colorToData(color)
    glColor3ub(var1 >> 16, (var1 & 0x00ff00) >> 8, var1 & 0x0000ff)

  def setLookAt(self, x0, y0, z0, x1, y1, z1, x2, y2, z2):
    gluLookAt(x0, y0, z0, x1, y1, z1, x2, y2, z2)  #视线源点，视线目标点，视线方向

  def rotate(self, r, x, y, z):
    glRotatef(r, x, y, z)  #旋转图形，分别填入角度、x、y、z轴选择

  def cube(self, x, y, z, l, w, h, width, color):
    self.line(x, y, z, x + l, y, z, width, color)
    self.line(x, y + w, z, x + l, y + w, z, width, color)
    self.line(x, y, z + h, x + l, y, z + h, width, color)
    self.line(x, y + w, z + h, x + l, y + w, z + h, width, color)

    self.line(x, y, z, x, y + w, z, width, color)
    self.line(x + l, y, z, x + l, y + w, z, width, color)
    self.line(x, y, z + h, x, y + w, z + h, width, color)
    self.line(x + l, y, z + h, x + l, y + w, z + h, width, color)

    self.line(x, y, z, x, y, z + h, width, color)
    self.line(x + l, y, z, x + l, y, z + h, width, color)
    self.line(x, y + w, z, x, y + w, z + h, width, color)
    self.line(x + l, y + w, z, x + l, y + w, z + h, width, color)

  def fillRect(self, x, y, z, l, w, side, color):
    self.setColor(color)
    side = side % 3
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    if side == 0:
      glVertex3f(x + l, y, z)
      glVertex3f(x + l, y, z + w)
      glVertex3f(x, y, z + w)
    elif side == 1:
      glVertex3f(x + l, y, z)
      glVertex3f(x + l, y + w, z)
      glVertex3f(x, y + w, z)
    elif side == 2:
      glVertex3f(x, y + l, z)
      glVertex3f(x, y + l, z + w)
      glVertex3f(x, y, z + w)
    glEnd()

  def fillCube(self, x, y, z, l, w, h, color):
    dColor = {"top" : color, "bottom" : color, "left" : color, "right" : color, "front" : color, "back" : color}
    self.fillCubeColor(x, y, z, l, w, h, dColor)

  def fillCubeColor(self, x, y, z, l, w, h, dColor):
    self.fillRect(x, y, z + h, l, w, self.SIDE_Y, dColor["back"])
    self.fillRect(x, y, z, l, h, self.SIDE_X, dColor["bottom"])
    self.fillRect(x, y, z, w, h, self.SIDE_Z, dColor["left"])
    self.fillRect(x, y, z, l, w, self.SIDE_Y, dColor["front"])
    self.fillRect(x + l, y + w, z + h, -l, -h, self.SIDE_X, dColor["top"])
    self.fillRect(x + l, y + w, z + h, -w, -h, self.SIDE_Z, dColor["right"])

  def line(self, x0, y0, z0, x1, y1, z1, w, color):
    glLineWidth(w)
    self.setColor(color)
    glBegin(GL_LINES)
    glVertex3f(x0, y0, z0)
    glVertex3f(x1, y1, z1)
    glEnd()

  def axis(self, w):
    self.line(-0.9, 0, 0, 0.9, 0, 0, w, "red")
    self.line(0.9, 0, 0, 0.85, 0.05, 0, w, "red")
    self.line(0.9, 0, 0, 0.85, -0.05, 0, w, "red")
    self.line(0, -0.9, 0, 0, 0.9, 0, w, "green")
    self.line(0, 0.9, 0, 0.05, 0.85, 0, w, "green")
    self.line(0, 0.9, 0, -0.05, 0.85, 0, w, "green")
    self.line(0, 0, -0.9, 0, 0, 0.9, w, "blue")
    self.line(0, 0, 0.9, 0, 0.05, 0.85, w, "blue")
    self.line(0, 0, 0.9, 0, -0.05, 0.85, w, "blue")
