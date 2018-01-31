import os
import sys
import time
import string

from OpenGL.GL import *       #组件
from OpenGL.GLU import *      #组件
from OpenGL.GLUT import *     #组件
from OpenGL.WGL import *      #组件
import matplotlib._color_data;  #组件


def colorToData(name):
  return int((matplotlib._color_data.CSS4_COLORS[name]).strip("#"), 16)  #去除库文件颜色数据中的“#”字符并由16进制字符转数字


lStr = []
def _initStr():  #初始化字库
  global lStr
  lStr = glGenLists(128)
  wglUseFontBitmaps(wglGetCurrentDC(), 0, 128, lStr)

def _showStr(x, y, str, color):
  global lStr
  glPushAttrib(GL_ALL_ATTRIB_BITS)  #保存设置
  var1 = colorToData(color)
  glColor3ub(var1 >> 16, (var1 & 0x00ff00) >> 8, var1 & 0x0000ff)
  glLoadIdentity()
  glRotatef(0, 1, 1, 1)  #旋转图形，分别填入角度、x、y、z轴选择  
  glRasterPos3f(x, y, 0)  #设置源点
  for i in str:
    glCallList(ord(i) + lStr)  #写字
  glPopAttrib()  #恢复设置

class Graphics2D:

  def __init__(self):

    self.lastColor = 0xffffff
    self.lastLineWidth = 1

  def clear(self):
    glClear(GL_COLOR_BUFFER_BIT)  #清空缓存

  def flush(self):
    glutSwapBuffers()  #刷新显示

  def setLineWidth(self, w):
    glLineWidth(w)  #设置线宽
    self.lastLineWidth = w

  def setColor(self, color):
    self.setColor(color)  #设置图形颜色
    self.lastColor = color

  def line(self, x0, y0, x1, y1, w, color):
    glLineWidth(w)
    self.setColor(color)
    glBegin(GL_LINES)  #画线操作
    glVertex2f(x0, y0)  #相对于窗口中心的顶点1
    glVertex2f(x1, y1)  #相对于窗口中心的顶点2
    glEnd()


class Graphics3D:

  SIDE_X = 0
  SIDE_Y = 1
  SIDE_Z = 2
  GLMODE_VIEW       = GL_MODELVIEW
  GLMODE_PROJECTION = GL_PROJECTION

  def __init__(self):
    self.lastColor = 0xffffff
    self.lastLineWidth = 1

  def clear(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  #清空缓存

  def flush(self):
    glutSwapBuffers()  #刷新显示

  def loadIdentity(self):
    glLoadIdentity()  #重新定义画笔到坐标系中心

  def setLineWidth(self, w):
    glLineWidth(w)
    self.lastLineWidth = w

  def setColor(self, color):
    var1 = colorToData(color)
    glColor3ub(var1 >> 16, (var1 & 0x00ff00) >> 8, var1 & 0x0000ff)
    self.lastColor = var1

  def setTranslate(self, x, y, z):
    glTranslatef(x, y, z)

  def setMatrixMode(self, mode):
    glMatrixMode(mode)

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

  def showStr(self, x, y, str, color):
    _showStr(x, y, str, color)

  def showStrPixel(self, x, y, str, color):
    wx = glutGet(GLUT_WINDOW_WIDTH) / 2  #获取窗口宽度
    wy = glutGet(GLUT_WINDOW_HEIGHT) / 2  #获取窗口高度
    if wx == 0:
      wx = 10
    if wy == 0:
      wy = 10
    wx = (x - wx) / wx
    wy = (wy - y) / wy
    _showStr(wx, wy, str, color)


class Windows:

  def __init__(self, name, w, h, x = 0, y = 0, func = 0, is3D = 0, idleFunc = 0, keyFunc = 0):
    glutInit(sys.argv)  #初始化组件
    if is3D == 0:
      glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  #设置显示模式
    else:
      glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  #设置显示模式
    glutInitWindowPosition(x, y)  #设置窗口位置
    glutInitWindowSize(w, h)  #设置窗口大小，单位像素
    glutCreateWindow(name)  #设置窗口名字，加 b"XXXX" 格式化
    if func == 0:
      glutDisplayFunc(self.displayFunc)  #设置显示函数
    else:
      glutDisplayFunc(func)
    if idleFunc != 0:
      glutIdleFunc(idleFunc)  #设置空闲函数
    glEnable(GL_DEPTH_TEST)  #开启深度测试
    _initStr()
    if keyFunc != 0:
      glutKeyboardFunc(keyFunc)  #设置按键处理函数
    glutMainLoop()  #进入循环

  def displayFunc(self):
    pass

  
