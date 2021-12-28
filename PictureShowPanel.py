import wx
import cv2
import imageio
from ID_DEFINE import *

class PictureShowPanel(wx.Panel):
    def __init__(self, parent, imgData=[],size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, -1, size=size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.imgData=imgData

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush("WHITE"))
        dc.Clear()
        x,y = self.GetClientSize()
        if self.imgData!=[]:
            self.imgData = self.imgData.astype('uint8')#时间证明，你给它浮点数，它显示不好，必须给uint8型整数。
            self.img = wx.Image(self.imgData.shape[1], self.imgData.shape[0], self.imgData)
            bmp = self.img.Scale(width=x, height=y, quality=wx.IMAGE_QUALITY_BOX_AVERAGE).ConvertToBitmap()
            dc.DrawBitmap(bmp, 0, 0, True)
