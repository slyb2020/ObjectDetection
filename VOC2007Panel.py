
import matplotlib.pyplot as plt
import wx
import images
import wx.dataview as dv
import wx.lib.scrolledpanel as scrolled
from PictureShowPanel import PictureShowPanel
import cv2
import os
import wx.grid as gridlib

ann_filepath = 'D:/WorkSpace/DataSet/VOC2007/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/Annotations/'
img_filepath = 'D:/WorkSpace/DataSet/VOC2007/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/JPEGImages/'
img_savepath = 'D:/WorkSpace/DataSet/VOC2007/TrafficDatasets/JPEGImages/'
ann_savepath = 'D:/WorkSpace/DataSet/VOC2007/TrafficDatasets/Annotations/'
names = locals()
classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
           'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
           'dog', 'horse', 'motorbike', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor', 'person']
classColour ={'aeroplane':wx.RED,'bicycle':wx.YELLOW,'bird':wx.BLUE,'boat':wx.GREEN,'bottle':wx.Colour(123,53,24),
              'bus':wx.Colour(123,53,124),'car':wx.Colour(123,153,124),'cat':wx.Colour(23,153,24),'chair':wx.Colour(23,53,124),'cow':wx.Colour(53,100,24),'diningtable':wx.Colour(153,100,124),
              'dog':wx.Colour(134,153,192),'horse':wx.Colour(34,153,192),'motorbike':wx.Colour(134,53,192),'pottedplant':wx.Colour(134,153,92),
              'sheep':wx.Colour(223,253,224),'sofa':wx.Colour(23,253,224),'train':wx.Colour(223,253,24),'tvmonitor':wx.Colour(123,253,224),'person':wx.Colour(123,53,224),
              }

class VOC2007Panel(wx.Panel):
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
        self.datasetNB = wx.Notebook(self.datasetProcessingPNL, -1, size=(150 + 28, -1), style=
                             # wx.BK_DEFAULT
                             #wx.BK_TOP
                             wx.BK_BOTTOM
                                     # wx.BK_LEFT
                                     # wx.BK_RIGHT
                                     # | wx.NB_MULTILINE
                                     )
        il = wx.ImageList(16, 16)
        self.datasetNB.AssignImageList(il)
        self.datasetTrain=gridlib.Grid(self.datasetNB, -1)
        self.datasetNB.AddPage(self.datasetTrain, "训练数据集")
        self.datasetTest=gridlib.Grid(self.datasetNB, -1)
        self.datasetNB.AddPage(self.datasetTest, "测试数据集")
        self.CreateDataGrid()
        hbox=wx.BoxSizer()
        vvbox = wx.BoxSizer(wx.VERTICAL)
        dataSetShowPropertyPanel = DataSetShowPropertyPanel(self.datasetProcessingPNL)
        vvbox.Add(dataSetShowPropertyPanel,1,wx.EXPAND)
        self.countDatasetDistributionBTN = wx.Button(self.datasetProcessingPNL,-1,label="统计数据集分布",size=(-1,35))
        vvbox.Add(self.countDatasetDistributionBTN,0,wx.EXPAND)
        self.findOutWrongPictureBTN = wx.Button(self.datasetProcessingPNL,-1,label="找出错误图片",size=(-1,35))
        vvbox.Add(self.findOutWrongPictureBTN,0,wx.EXPAND)
        hbox.Add(vvbox,0,wx.EXPAND)
        hbox.Add(self.datasetNB, 0, wx.EXPAND)
        self.middlePanel = wx.Panel(self.datasetProcessingPNL,-1,size=(200,-1))
        hbox.Add(self.middlePanel,0,wx.EXPAND)
        self.picShowPanel = PictureShowPanel(self.datasetProcessingPNL)
        hbox.Add(self.picShowPanel,1,wx.EXPAND)
        self.datasetProcessingPNL.SetSizer(hbox)
        # self.datasetTrain.SelectBlock(0,0,0,0)
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)

    def OnCellLeftClick(self, event):
        row = event.GetRow()
        self.datasetTrain.SelectBlock(row,0,row,0)
        imgFilename = self.datasetTrain.GetCellValue(row,0)
        annFilename = imgFilename[:-4]+'.xml'
        fp = open(ann_filepath + annFilename)  # 打开Annotations文件
        lines = fp.readlines()
        fp.close()
        self.RefreshMiddlePanel(annFilename,lines)
        self.picShowPanel.imgData = cv2.cvtColor(cv2.imread(img_filepath+imgFilename),cv2.COLOR_BGR2RGB)
        for Object in self.Objects:
            cv2.rectangle(self.picShowPanel.imgData, (Object[1],Object[2]),(Object[3],Object[4]),classColour[Object[0]],2)
        self.picShowPanel.Refresh()
        event.Skip()
    def RefreshMiddlePanel(self,file,lines):
        self.middlePanel.DestroyChildren()
        vbox = wx.BoxSizer(wx.VERTICAL)
        for i in range(0,len(classes)//2*2,2):
            hhbox = wx.BoxSizer()
            BTN = wx.Button(self.middlePanel,-1,label=classes[i], size=(-1,30))
            BTN.SetBackgroundColour(classColour[classes[i]])
            hhbox.Add(BTN,1)
            BTN = wx.Button(self.middlePanel,-1,label=classes[i+1], size=(-1,30))
            BTN.SetBackgroundColour(classColour[classes[i+1]])
            hhbox.Add(BTN,1)

            vbox.Add(hhbox,0,wx.EXPAND)

        self.middlePanel.SetSizer(vbox)
        self.middlePanel.Layout()
        ind_start = []
        ind_end = []
        lines_id_start = lines[:]
        lines_id_end = lines[:]

        # 在xml中找到object块，并将其记录下来
        while "\t<object>\n" in lines_id_start:
            a = lines_id_start.index("\t<object>\n")
            ind_start.append(a)  # ind_start是<object>的行数
            lines_id_start[a] = "delete"

        while "\t</object>\n" in lines_id_end:
            b = lines_id_end.index("\t</object>\n")
            ind_end.append(b)  # ind_end是</object>的行数
            lines_id_end[b] = "delete"

        # names中存放所有的object块
        i = 0
        self.Objects=[]
        for k in range(0, len(ind_start)):
            Object = []
            for j in range(0, len(classes)):
                if classes[j] in lines[ind_start[i] + 1]:
                    Object.append(classes[j])
                    a = ind_start[i]
                    Object.append(int(lines[a+6][9:-8]))
                    Object.append(int(lines[a+7][9:-8]))
                    Object.append(int(lines[a+8][9:-8]))
                    Object.append(int(lines[a+9][9:-8]))
                    # for o in range(ind_end[i] - ind_start[i] + 1):
                    #     name.append(lines[a + o])
                    self.Objects.append(Object)
                    break
            i += 1

        # # xml头
        # string_start = lines[0:ind_start[0]]
        #
        # # xml尾
        # if ((file[2:4] == '09') | (file[2:4] == '10') | (file[2:4] == '11')):
        #     string_end = lines[(len(lines) - 11):(len(lines))]
        # else:
        #     string_end = [lines[len(lines) - 1]]
        #
        #     # 在给定的类中搜索，若存在则，写入object块信息
        # a = 0
        # for k in range(0, len(ind_start)):
        #     if classes1 in names['block%d' % k]:
        #         a += 1
        #         string_start += names['block%d' % k]
        #     # if classes2 in names['block%d' % k]:
        #     #     a += 1
        #     #     string_start += names['block%d' % k]
        #     # if classes3 in names['block%d' % k]:
        #     #     a += 1
        #     #     string_start += names['block%d' % k]
        #     # if classes4 in names['block%d' % k]:
        #     #     a += 1
        #     #     string_start += names['block%d' % k]
        #     # if classes5 in names['block%d' % k]:
        #     #     a += 1
        #     #     string_start += names['block%d' % k]
        #
        # string_start += string_end
        # print(string_start)
        # for c in range(0, len(string_start)):
        #     fp_w.write(string_start[c])
        # fp_w.close()

    def CreateDataGrid(self):
        number = len(os.listdir(img_filepath))
        self.datasetTrain.SetColLabelSize(25)
        self.datasetTrain.SetRowLabelSize(50)
        self.datasetTrain.CreateGrid(number, 1)  # , gridlib.Grid.SelectRows)
        self.datasetTrain.SetColSize(0, 100)
        # self.datasetTrain.SetColSize(1, 75)
        self.datasetTrain.SetColLabelValue(0, '图片名称')
        # self.dataGrid.SetColLabelValue(1, 'Y')
        for i, filename in enumerate(os.listdir(img_filepath)):
            self.datasetTrain.SetCellValue(i,0,filename)


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

