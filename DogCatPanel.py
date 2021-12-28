import matplotlib.pyplot as plt
import wx
import images
import wx.dataview as dv
import wx.lib.scrolledpanel as scrolled
from PictureShowPanel import PictureShowPanel
import cv2
import os


class MyButton(wx.Button):
    def __int__(self,parent,id,size):
        wx.Button.__init__(self, parent,id,size=size)
        self.type = ""
        self.name = ""

class TestingDataSetShowPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        wsizer = wx.WrapSizer(orient=wx.HORIZONTAL)
        max = 100
        count = 0
        while count < max:
            count += 1
            for img16 in os.listdir('D:\\WorkSpace\\DataSet\\DogCat\\test\\')[5*(count-1):5*count]:
                bmp = wx.Image('D:\\WorkSpace\\DataSet\\DogCat\\test\\' + img16).Scale(width=32, height=32, quality=wx.IMAGE_QUALITY_BOX_AVERAGE).ConvertToBitmap()
                label = img16.split('.')[-2]
                btn = MyButton(self, -1, size=(32, 32))
                btn.type = "TEST"
                btn.name = label
                btn.SetBitmap(bmp)
                btn.SetToolTip(label)
                wsizer.Add(btn)
        self.SetSizer(wsizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()

class TrainingDataSetShowPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        wsizer = wx.WrapSizer(orient=wx.HORIZONTAL)
        max = 100
        count = 0
        while count < max:
            count += 1
            for img16 in os.listdir('D:\\WorkSpace\\DataSet\\DogCat\\train\\')[5*(count-1):5*count]:
                bmp = wx.Image('D:\\WorkSpace\\DataSet\\DogCat\\train\\' + img16).Scale(width=32, height=32, quality=wx.IMAGE_QUALITY_BOX_AVERAGE).ConvertToBitmap()
                label = img16.split('.')[-3]
                id = img16.split('.')[-2]
                btn = MyButton(self, -1, size=(32, 32))
                btn.type = "TRAIN"
                btn.name = label+'.'+id
                btn.SetBitmap(bmp)
                btn.SetToolTip(label)
                wsizer.Add(btn)
        self.SetSizer(wsizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()
class ErrorDataSetShowPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        wsizer = wx.WrapSizer(orient=wx.HORIZONTAL)
        max = 100
        count = 0
        while count < max:
            count += 1
            for img16 in os.listdir('D:\\WorkSpace\\DataSet\\DogCat\\error\\')[5*(count-1):5*count]:
                bmp = wx.Image('D:\\WorkSpace\\DataSet\\DogCat\\error\\' + img16).Scale(width=32, height=32, quality=wx.IMAGE_QUALITY_BOX_AVERAGE).ConvertToBitmap()
                label = img16.split('.')[-3]
                id = img16.split('.')[-2]
                btn = MyButton(self, -1, size=(32, 32))
                btn.type = "TRAIN"
                btn.name = label+'.'+id
                btn.SetBitmap(bmp)
                btn.SetToolTip(label)
                wsizer.Add(btn)
        self.SetSizer(wsizer)
        self.SetAutoLayout(1)
        self.SetupScrolling()


class DogCatPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent=parent
        self.notebook=wx.Notebook(self, -1, size=(21, 21), style=
                             # wx.BK_DEFAULT
                             #wx.BK_TOP
                             # wx.BK_BOTTOM
                                  wx.BK_LEFT
                                  #wx.BK_RIGHT
                                  # | wx.NB_MULTILINE
                                  )
        il = wx.ImageList(16, 16)
        self.notebook.AssignImageList(il)
        self.datasetProcessingPNL=wx.Panel(self.notebook, -1)
        self.notebook.AddPage(self.datasetProcessingPNL, "数据集处理")
        hbox=wx.BoxSizer()
        hbox.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(hbox)
        self.datasetNB = wx.Notebook(self.datasetProcessingPNL, -1, size=(4 * 128 + 28, -1), style=
                             # wx.BK_DEFAULT
                             #wx.BK_TOP
                             wx.BK_BOTTOM
                                     # wx.BK_LEFT
                                     # wx.BK_RIGHT
                                     # | wx.NB_MULTILINE
                                     )
        il = wx.ImageList(16, 16)
        self.datasetNB.AssignImageList(il)
        self.datasetTrain=TrainingDataSetShowPage(self.datasetNB)
        self.datasetNB.AddPage(self.datasetTrain, "训练数据集")
        self.datasetTest=TestingDataSetShowPage(self.datasetNB)
        self.datasetNB.AddPage(self.datasetTest, "测试数据集")
        self.datasetError=ErrorDataSetShowPage(self.datasetNB)
        self.datasetNB.AddPage(self.datasetError, "出错数据集")
        hbox=wx.BoxSizer()
        vvbox = wx.BoxSizer(wx.VERTICAL)
        self.datasetSelectCOMBO = wx.ComboBox(self.datasetProcessingPNL,-1,"猫狗大战数据集",size=(-1,35), choices=["猫狗大战数据集"])
        vvbox.Add(self.datasetSelectCOMBO,0,wx.TOP|wx.BOTTOM|wx.EXPAND,5)
        dataSetShowPropertyPanel = DataSetShowPropertyPanel(self.datasetProcessingPNL)
        vvbox.Add(dataSetShowPropertyPanel,1,wx.EXPAND)
        self.countDatasetDistributionBTN = wx.Button(self.datasetProcessingPNL,-1,label="统计数据集分布",size=(-1,35))
        self.countDatasetDistributionBTN.Bind(wx.EVT_BUTTON,self.OnCountDatasetDistributionBTN)
        vvbox.Add(self.countDatasetDistributionBTN,0,wx.EXPAND)
        self.findOutWrongPictureBTN = wx.Button(self.datasetProcessingPNL,-1,label="找出错误图片",size=(-1,35))
        self.findOutWrongPictureBTN.Bind(wx.EVT_BUTTON,self.OnFindOutWrongPictureBTN)
        vvbox.Add(self.findOutWrongPictureBTN,0,wx.EXPAND)
        hbox.Add(vvbox,0,wx.EXPAND)
        hbox.Add(self.datasetNB, 0, wx.EXPAND)
        self.picShowPanel = PictureShowPanel(self.datasetProcessingPNL)
        hbox.Add(self.picShowPanel,1,wx.EXPAND)
        self.datasetProcessingPNL.SetSizer(hbox)
        self.Bind(wx.EVT_BUTTON,self.OnPicButton)
    def OnFindOutWrongPictureBTN(self,event):
        if "proProcessingModel.pt" not in os.listdir("./model/"):
            print("here")
    def OnCountDatasetDistributionBTN(self,event):
        if "temp.jpg" not in os.listdir('./bitmaps/'):
            heights = []
            widths = []
            path = 'D:\\WorkSpace\\DataSet\\DogCat\\train\\'
            for p in os.listdir(path):
                imgPath = os.path.join(path, p)
                imgArray = cv2.imread(imgPath)
                heights.append(imgArray.shape[0])
                widths.append(imgArray.shape[1])
            plt.scatter(widths, heights)
            plt.savefig("./bitmaps/temp.jpg")
        self.picShowPanel.imgData = plt.imread("./bitmaps/temp.jpg")
        self.picShowPanel.imgData = cv2.cvtColor(self.picShowPanel.imgData, cv2.COLOR_BGR2RGB)
        self.picShowPanel.Refresh()
    def OnPicButton(self,event):
        obj = event.GetEventObject()
        objID = event.GetId()
        if obj.type == "TRAIN":
            self.picShowPanel.imgData = cv2.imread('D:\\WorkSpace\\DataSet\\DogCat\\train\\' + obj.name+'.jpg', cv2.IMREAD_UNCHANGED)
        elif obj.type == "TEST":
            self.picShowPanel.imgData = cv2.imread('D:\\WorkSpace\\DataSet\\DogCat\\test\\' + obj.name+'.jpg', cv2.IMREAD_UNCHANGED)
        self.picShowPanel.imgData = cv2.cvtColor(self.picShowPanel.imgData, cv2.COLOR_BGR2RGB)
        self.picShowPanel.Refresh()

class DataSetShowPropertyPanel(wx.Panel):
    def __init__(self, parent):
        self.labelNameList=['猫','狗']
        self.trainImageList = []
        self.testImageList = []
        wx.Panel.__init__(self, parent, -1, size = (170, -1))
        self.SetBackgroundColour(wx.Colour(220,220,220))
        propertyList = dv.DataViewListCtrl(self,size = (-1,200))
        self.propertydata = [
            ['训练集个数', str(len(self.trainImageList))],
            ['测试集个数', str(len(self.testImageList))],
            ['数据类型', 'uint8'],
            ['图像通道数', '3'],
            ['标签个数', str(len(self.labelNameList))]]
        # Give it some columns.
        # The ID col we'll customize a bit:
        propertyList.AppendTextColumn('参数', width=80)
        propertyList.AppendTextColumn('取值', width=90, mode=dv.DATAVIEW_CELL_EDITABLE)

        # Load the data. Each item (row) is added as a sequence of values
        # whose order matches the columns
        for itemvalues in self.propertydata:
            propertyList.AppendItem(itemvalues)

        # Set the layout so the listctrl fills the panel
        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(propertyList, 0, wx.EXPAND)

        labelList = dv.DataViewListCtrl(self)
        self.labeldata = []
        for i,j in enumerate(self.labelNameList):
            labeldata = [j,'6000','1000']
            self.labeldata.append(labeldata)
        labelList.AppendTextColumn('标签', width=80)
        labelList.AppendTextColumn('训练集样本数量', width=90, mode=dv.DATAVIEW_CELL_EDITABLE)
        # labelList.AppendTextColumn('测试集样本数量', width=100, mode=dv.DATAVIEW_CELL_EDITABLE)
        # for itemvalues in self.labeldata:
        #     labelList.AppendItem(itemvalues)
        self.Sizer.Add(labelList, 1, wx.EXPAND)

