#!/usr/bin/env python
# encoding: utf-8
'''
@author: slyb
@license: (C) Copyright 2017-2020, 天津定智科技有限公司.
@contact: slyb@tju.edu.cn
@file: ID_DEFINE.py.py
@time: 2019/6/16 15:23
@desc:
'''
db_manufacture='manufacture'
db_management='management'
db_produce='produce'
db_price='price'
db_temp='lyb_temp'
# host_name='127.0.0.1'
# user_name='root'
# passwd_name='12345678'
host_name='121.196.217.197'
user_name='jingyi'
passwd_name='jingyi123'

local_host_name='127.0.0.1'
local_user_name='root'
local_passwd_name=''

import wx
MENU_CHECK_IN = wx.NewIdRef()
MENU_CHECK_OUT = wx.NewIdRef()
MENU_STYLE_DEFAULT = wx.NewIdRef()
MENU_STYLE_XP = wx.NewIdRef()
MENU_STYLE_2007 = wx.NewIdRef()
MENU_STYLE_VISTA = wx.NewIdRef()
MENU_STYLE_MY = wx.NewIdRef()
MENU_USE_CUSTOM = wx.NewIdRef()
MENU_LCD_MONITOR = wx.NewIdRef()
MENU_HELP = wx.NewIdRef()
MENU_DISABLE_MENU_ITEM = wx.NewIdRef()
MENU_REMOVE_MENU = wx.NewIdRef()
MENU_TRANSPARENCY = wx.NewIdRef()
MENU_NEW_FILE = 10005
MENU_SAVE = 10006
MENU_OPEN_FILE = 10007
MENU_NEW_FOLDER = 10008
MENU_COPY = 10009
MENU_CUT = 10010
MENU_PASTE = 10011
COLUMN_WIDTH=[270,150,100,120,200,70,70,200,120,260,    120,120,120,120,120,120,    70,70,70,60,70,70]#这是下单界面中各列的宽度列表
COLUMN_WIDTH_UNDER_TECH_REVIEW=[270,150,100,120,200,100,100,200,120,260,    120,120,120,120,120,120,    70,70,70,60,70,70]#这是下单界面中各列的宽度列表
INIT_STATE_FOLD_FLAG=0#下单界面左面板的状态标志，初始状态：显示订单检索面板
NEWCONTRACT_STATE_FOLD_FLAG=1#下单界面左面板的状态标志，新建合同状态：显示新建合同面板
ORDERMAN_STAFF_ID_PASSWORD_DICT = {'SN123':'12345678','SN234':'23456789'}#工厂下单员字典，登录时用于检索密码是否正确，并根据密码锁定下单员ID
ORDERMAN_STAFF_PASSWORD_ID_DICT=dict(zip(ORDERMAN_STAFF_ID_PASSWORD_DICT.values(),ORDERMAN_STAFF_ID_PASSWORD_DICT.keys()))
ORDERMAN_STAFF_ID_NAME_DICT={'SN123':'张三','SN234':'李四'}
CONTRACT_STATE_DICT={'0':"草稿",'5':"待技术审核",'8':"技审驳回",'10':"待价格审核",'13':"价格审核驳回",'15':"待财务审核",'25':"等待排产",'30':"生产中"}
COPPER_SERIAL_DICT={'铜条玻璃1':'1系','铜条玻璃2':'1系','铜条玻璃3':'2系','铜条玻璃4':'2系','铜条玻璃5':'3系','铜条玻璃6':'3系','铜条玻璃7':'4系',}
ANTIQUE_SERIAL_DICT={"金色":'1系',"银色":'2系',"黑蓝色":'3系',}
PROCESSING=0
TECH_REVIEW=1
TECH_REJECT=2
PRICE_REVIEW=3
PRICE_REJECT=4
FINANCIAL_REVIEW=5
NEW_STATE=1
OLD_STATE=0
MIN_DIDDLE_WIDHT=30
PLACE_ORDER=0
CHECK_ORDER=1
ORDER_TYPE=["普通","加急","售后","补充"]#存储订单类型名
ORDER_TYPE_DATE=[15,10,5,5]#存储订单类型对应的加工日期
TITLE_DOOR_TYPE_NAME=["普通门","抽屉","玻璃门","网格门","真百叶门","假百叶门","平板","特殊"]
SUB_DOOR_TYPE_NAME=[["普通柜门","回型柜门","高柜门","三合一门","移门"],["普通抽屉","半造型抽屉"],
                    ["整框玻璃门","四格玻璃门","六格玻璃门","八格玻璃门","上半四格玻璃门","上半六格玻璃门","上半八格玻璃门"],
                    ["网格门","上半网格门","下半网格门","上下半网格门"],["真百叶门","上半真百叶门","下半真百叶门","上下半真百叶门"],
                    ["假百叶门","上半假百叶门","下半假百叶门","上下半假百叶门"],["平板"],["炕围"]]
DOOR_TYPE_NEED_MIDDLE=["高柜门","上半四格玻璃门","上半六格玻璃门","上半八格玻璃门","上半网格门","下半网格门","上下半网格门","上半真百叶门","下半真百叶门","上下半真百叶门","上半假百叶门","下半假百叶门","上下半假百叶门"]
OPEN_DIRECTION_CHOICES = ["左开","右开","上开","下开","不开","对开","上下对开","单左开","单右开","单上开","单下开","开孔"]
GLASS_TYPE_CHOICES=["普通玻璃","铜条玻璃"]
COPPER_GLASS_TYPE_CHOICES=["铜条玻璃1","铜条玻璃2","铜条玻璃3","铜条玻璃4","铜条玻璃5","铜条玻璃6","铜条玻璃7",]
DOOR_WITHOUT_HINGE=["普通抽屉","半造型抽屉","炕围"]
TEXTURE_LIST=["无纹","有纹"]
MEKE_PRICE_COLUMN_NAME=[["套系",60],["门型",90],["颜色",80],["高",35],["宽",35],["数量",30],["基材",80],["套色",30],["双面",30],
                        ["玻璃类型",60],["基础\r\n单价",30],["复杂度\r\n加收",50],["膜皮\r\n加价",30],["双面\r\n加价",30],["横纹\r\n加价",30],
                        ["基材\r\n加价",30],["套色\r\n加价",30],["玻璃门\r\n工艺加收",50],["普通玻璃\r\n加价",50],["铜条玻璃\r\n加价",50],
                        ["真百叶\r\n工艺加收",50],["真百叶\r\n高度加收",50],["真百叶\r\n宽度加收",50],["假百叶\r\n工艺加收",50],
                        ["网格门\r\n加收",50],["网格门\r\n高度加收",50],["网格门\r\n宽度加收",50],["三合一门\r\n加收",50],
                        ["拉直器\r\n加收",50],["仿古\r\n加收",30],["条子\r\n加收",30],["附件\r\n复杂度加收",65],
                        ["附件\r\n拼接加收", 50],["罗马柱\r\n非标加收",50],["圆弧廊桥\r\n加收",50],["整套组件\r\n基础价格",50],
                        ["五金件",50],["合计",72]]
ID_NEW_ORDER=wx.NewId()
ID_NEW_DOOR=wx.NewId()
ID_DEL_DOOR=wx.NewId()
ID_REALTIME_ORDER=wx.NewId()
ID_SETUP_STOCK_THRESHOLD=wx.NewId()
ID_WINDOW_LEFT=wx.NewId()
ID_WINDOW_BOTTOM=wx.NewId()
ALPHA_ONLY = 1
DIGIT_ONLY = 2
FLOAT_ONLY = 3
SIGNED_FLOAT_ONLY = 4
EXPRESS_ONLY=5
ORDER_PLACER=9
MANAGER=5
PAGE_NAME=["订单管理","排产计划管理","产能计划管理","库存管理","等待价格审核订单","等待财务审核订单","数据集管理"]
MACHINE_NAME=[['SC01','1号轧机'],['SC02','5号轧机'],['SC03','6号轧机'],['SC04','2号轧机'],
              ['SC05','3号轧机'],['SC06','4号轧机'],['SC07','7号轧机'],['SC08','8号轧机'],
              ['SC09','9号轧机'],['SC10','10号轧机'],['SC11','11号轧机'],['SC12','12号轧机'],
              ['SC13','13号轧机'],['SC14','14号轧机'],['SC15','15号轧机']]
COLUMN_NAME=['生产线名称',"9月2日A班","9月2日B班","9月3日A班","9月3日B班","9月4日A班","9月4日B班",
             "9月5日A班","9月5日B班","9月6日A班","9月6日B班","9月7日A班","9月7日B班",
             ]
PRODUCT_NAME=["A1","B0","B1","B31.0","B31.2","B31.4","B31.6","B5","B7","B8","B9"]
PRODUCT2COLOUR={'A1':wx.RED,'B0':wx.Colour(67,120,189),'B1':wx.Colour(10,100,100),'B31.0':wx.Colour(46,189,30),'B31.2':wx.BLUE,'B31.4':wx.BLACK,'B31.6':wx.Colour(120,34,223),
                'B5':wx.Colour(210,120,67),'B7':wx.GREEN,'B8':wx.Colour(57,125,132),'B9':wx.Colour(165,34,78)}
MACHINE2PRODUCT={'SC01':['A1','B0','B31.2','B9'],'SC02':['A1','B0','B31.2','B31.6'],'SC03':['A1','B0','B31.2','B31.6'],
                 'SC04':['B1','B5','B7','B31.4'],'SC05':['B1','B5','B7','B31.4'],'SC06':['B1','B5','B7','B31.4'],
                 'SC07':['B1','B5','B7','B31.4'],'SC08':['B1','B5','B7','B31.4'],'SC09':['B31.2'],'SC10':['B31.2'],
                 'SC11':['B31.2'],'SC12':['B31.2'],'SC13':['B31.2'],'SC14':['B31.2'],'SC15':['B31.0','B31.2'],
                 }
PRODUCT_STATE={10:"已排产，待生产",20:"正在生产",30:"已完工"}
MACHINE_LIST=["SC01","SC02","SC03","SC04","SC05","SC06","SC07","SC08","SC09","SC10","SC11","SC12","SC13","SC14","SC15"]
SCHEDULE_DAYS=10
GROUP_NAME=['A班','B班']
MACHINE_CAPACITY=[6]*len(MACHINE_LIST)
VALUE = [18, 18, 30, 6, 60, 30, 12, 30, 30, 0, 6]#用于计算最晚排产日期
TODAY='0000-00-00'