import time,datetime
import random
import wx
from ID_DEFINE import *
import pymysql as MySQLdb

GROUP_NAME=['A班','B班']
for i in range(10 * 2):
    date_str = str(datetime.date.today() + datetime.timedelta(days=int(i / 2)))+" "+GROUP_NAME[i%2]
    print("date_str=",date_str)

# a=[0]*9
# print("a=",a)
# a.pop(-1)
# print("a=",a)
# print"datetime.datetime.now=", datetime.datetime.now()
#
# date1=str(datetime.datetime.now())
# date1=date1[:10]
# print"date1=",date1
# date2="2019-06-28"
# date1 = time.strptime(date1, "%Y-%m-%d")
# date2 = time.strptime(date2, "%Y-%m-%d")
# print"date2=",date2
# print"date1=",date1
# date1 = datetime.datetime(date1[0], date1[1], date1[2])
# date2 = datetime.datetime(date2[0], date2[1], date2[2])
# print"date2=",date2
# print"date1=",date1
# print(date2-date1)
#
date_str = str(datetime.date(2017,1,1)+datetime.timedelta(days=10))
print(date_str)

customerStartTime = datetime.date(2010, 1, 1)
customerEndTime = datetime.date(2010, 1, 2)

print((customerEndTime-customerStartTime).days)

class CustomerSimulator(wx.Dialog):
    def __init__(self,parent,log,customerName, productionName,startDate= datetime.date(2017,1,1),endDate=datetime.date(3000,12,31)):
        self.parent = parent
        self.log = log
        self.productionName=productionName
        self.customerID = 0
        self.customerName = customerName
        self.customerStartTime = startDate
        self.customerEndTime = endDate
        self.customerStorageCapacity=300.
        self.customerConsumeRate = 10.
        self.customerThreshold = 0.3
        self.customerDelayTime = 2
        self.customerHolidayType = 0
        self.initStorage = 0.5*self.customerStorageCapacity
        self.orderDateList = []
        self.orderQuantityList = []


    def RegisterCustomerInfoIntoDB(self):
        try:
            db = MySQLdb.connect(host="%s" % local_host_name, user='%s' % local_user_name, passwd='%s' % local_passwd_name, db='ipms',charset='utf8')
        except:
            pass
            # wx.MessageBox("无法连接IPMS(智能生产管理系统)数据库","错误信息")
            # if log:
            #     log.WriteText("无法连接IPMS(智能生产管理系统)数据库" ,colour=wx.RED)
        cursor = db.cursor()
        sql = "select `客户ID`  from `客户信息表` where `客户名称`='%s' and `订购产品名称`='%s'" %(self.customerName, self.productionName)
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount>0:
            sql = "UPDATE `客户信息表` SET (`起始时间`='%s', `终止时间``='%s',`日消耗量``=%0.2f,`库存量``=%0.2f, `库存下限``=%0.2f)" % (str(self.customerStartTime),str(self.customerEndTime),self.customerConsumeRate,self.customerStorageCapacity,self.customerThreshold)
        else:
            sql = "INSERT INTO `客户信息表`(`客户名称`,`订购产品名称`,`起始时间`,`终止时间`,`日消耗量`,`库存量`,`库存下限`)VALUES ('%s','%s','%s','%s',%0.2f,%0.2f,%0.2f)" % (self.customerName, self.productionName,str(self.customerStartTime),str(self.customerEndTime),self.customerConsumeRate,self.customerStorageCapacity,self.customerThreshold)
        try:
            cursor.execute(sql)
            db.commit()  # 必须有，没有的话插入语句不会执行
        except:
            db.rollback()
        sql =  "select `客户ID`  from `客户信息表` where `客户名称`='%s' and `订购产品名称`='%s'" %(self.customerName, self.productionName)
        cursor.execute(sql)
        self.customerID = cursor.fetchone()[0]
        db.close()
        return(self.customerID)

    def CreateData(self,startDate=datetime.date(2017,1,1),endDate=datetime.date.today()):
        orderFlag = False
        self.orderDateList = []
        self.orderQuantityList = []
        if ((endDate - datetime.date.today()).days)> 0:
            endDate = datetime.date.today()
        days = (endDate-startDate).days+1
        currentStorage=self.initStorage
        for i in range(days):
            currentDate = startDate + datetime.timedelta(days=i)
            currentStorage -= self.customerConsumeRate*(1+(random.random()-0.5)*0.4)
            if currentStorage<=(self.customerThreshold*self.customerStorageCapacity):
                if not orderFlag:
                    orderFlag = True
                    delayDay=0
                    delayDays = self.customerDelayTime+random.randint(0,4)
                else:
                    delayDay+=1
                    if delayDay>=delayDays:
                        orderFlag = False
                        self.orderDateList.append(currentDate)
                        orderQuantity = int(self.customerStorageCapacity - currentStorage)
                        orderQuantity = int(orderQuantity / 5) * 5
                        self.orderQuantityList.append(orderQuantity)
                        currentStorage+=orderQuantity

    def SaveData(self):
        for i,orderDate in enumerate(self.orderDateList):
            self.SaveOrderIntoDB(self.log, orderDate, self.orderQuantityList[i])
            print(orderDate)

    def SaveOrderIntoDB(self,log,orderTime,quantity):
        try:
            db = MySQLdb.connect(host="%s" % local_host_name, user='%s' % local_user_name, passwd='%s' % local_passwd_name, db='ipms',charset='utf8')
        except:
            pass
            # wx.MessageBox("无法连接IPMS(智能生产管理系统)数据库","错误信息")
            # if log:
            #     log.WriteText("无法连接IPMS(智能生产管理系统)数据库" ,colour=wx.RED)
        cursor = db.cursor()
        sql = "INSERT INTO `历史订单表`( `产品名称`, `下单日期`,`产品数量`,`客户企业名称`, `状态`)VALUES ('%s','%s','%s','%s',%s)" % (self.productionName, str(orderTime),str(quantity), self.customerName,0)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()  # 必须有，没有的话插入语句不会执行
        except:
            # Rollback in case there is any error
            db.rollback()
        # 关闭数据库连接
        db.close()


customer1 = CustomerSimulator(None,None,"天津大学","A1")
customer1.CreateData()
print("here",customer1.orderDateList)
customer1.SaveData()

# a = "2017-10-27"
# b=a.split('-')
# print("data=",b)

