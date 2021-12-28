import torchvision.models as models
import torch
import os
import random
import torch.utils.data as data
import numpy as np
import torchvision.transforms as T
from PIL import Image
from PIL import ImageFile
from torch import nn
from torch.autograd import Variable
import torch.nn.functional as F
import cv2


class DogCat(data.Dataset):
    def __init__(self, root, transforms=None, train=True, test=False):
        '''
        目标：获取所有图像的地址，并根据训练、验证、测试划分数据
        :param root:
        :param transforms:
        :param train:
        :param test:
        '''
        self.test = test
        self.train = train
        imgs = [os.path.join(root, img) for img in os.listdir(root)]
        imgs = sorted(imgs, key=lambda x: int(x.split('.')[-2]))
        random.shuffle(imgs)
        imgsNum = len(imgs)
        if self.train:
            self.imgs = imgs[:int(0.8 * imgsNum)]
        if self.test:
            self.imgs = imgs[int(0.8 * imgsNum):]
        if transforms is None:
            normalize = T.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
            if self.test:
                self.transforms = T.Compose([
                    T.RandomResizedCrop(224),  # 输入的图像尺寸是224X224
                    T.ToTensor(),  # 数据值从[0,255]范围转为[0,1],相当于除以255的操作
                    normalize
                ])
            elif self.train:
                self.transforms = T.Compose([
                    T.RandomResizedCrop(224),
                    T.RandomHorizontalFlip(),
                    T.ToTensor(),
                    normalize
                ])

    def __getitem__(self, index):
        '''
        返回一张图像的数据
        对于验证集是训练集的一部分，也有标签
        :param index:
        :return:
        '''
        imgPath = self.imgs[index]
        label = 1 if 'dog' in imgPath.split('/')[-1] else 0
        data = Image.open(imgPath)
        data = self.transforms(data)
        return data, label, imgPath  # 需要返回图像的路径

    def __len__(self):
        return len(self.imgs)

class DogCat2(data.Dataset):
    def __init__(self, root, transforms=None, train=False, test=False):
        self.test = test
        self.train = train
        imgs = [os.path.join(root, img) for img in os.listdir(root)]
        imgs = sorted(imgs, key=lambda x: int((x.split('.')[-2]).split('\\')[-1]))

        random.shuffle(imgs)
        imgsNum = len(imgs)
        if self.train:
            self.imgs = imgs[:]
        if self.test:
            self.imgs = imgs[:]
        if transforms is None:
            normalize = T.Normalize(mean = [0.485, 0.456, 0.406],
                                    std = [0.229, 0.224, 0.225])
            if self.test:
                self.transforms = T.Compose([
                    T.RandomResizedCrop(224),
                    T.ToTensor(),
                    normalize
                ])
            elif self.train:
                self.transforms = T.Compose([
                    T.RandomResizedCrop(224),
                    T.RandomHorizontalFlip(),
                    T.ToTensor(),
                    normalize
                ])
    def __getitem__(self, index):
        imgPath = self.imgs[index]
        label = 1 if 'dog' in imgPath.split('/')[-1] else 0
        data = Image.open(imgPath)
        data = self.transforms(data)
        return data, label, imgPath

    def __len__(self):
        return len(self.imgs)

def train():
    trainset = DogCat('D:\\WorkSpace\\DataSet\\DogCat\\train\\')
    trainloader = torch.utils.data.DataLoader(dataset=trainset, batch_size=20, shuffle=True)
    ImageFile.LOAD_TRUNCATED_IMAGES = True  # 在处理图像数据的时候，如果Image.open()报错，则不保存图像

    device = torch.device('cpu') if torch.cuda.is_available() else torch.device('cpu')
    model = models.resnet152(pretrained=True)
    model.fc.out_features = 2
    # torch.manual_seed(1)
    learningRate = 1e-3
    optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)
    criterion = nn.CrossEntropyLoss()
    numEpoches = 1
    model = torch.load('./model/preProcessingModel2.pt')
    model.to(device)

    for epoch in range(numEpoches):
        print('current epoch = %d' % epoch)
        for i, (images, labels, imgPath) in enumerate(trainloader):
            model.train()
            # images = images.cuda()
            # labels = labels.cuda()
            outputs = model(images)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if i % 100 == 0:
                print('current loss = %.5f' % loss.item())
    print("finish training")
    torch.save(model,'./../model/preProcessingModel3.pt')

def FindOutWrongPicture(modelPath):
    testset2 = DogCat2('D:\\WorkSpace\\DataSet\\DogCat\\test\\', test=True)
    testloader2 = torch.utils.data.DataLoader(dataset=testset2, batch_size=1)
    device = torch.device('cpu') if torch.cuda.is_available() else torch.device('cpu')
    invalidImages = []
    model = torch.load(modelPath)
    model.to(device)
    for images, labels,imgPath in testloader2:
        model.eval()
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        outputs = F.softmax(outputs,dim=1)
        outputs = torch.max(outputs,1)
        values,predicts = outputs
        for value in values:
            if(value<=0.5):
                invalidImages.append(imgPath)
                file = imgPath[0]
                print(file)
                filename = file.split('\\')[-1]
                print(filename)
                imgArray = cv2.imread(file)
                cv2.imwrite("D:\\WorkSpace\\DataSet\\DogCat\\error\\" + filename, imgArray)
    print(len(invalidImages))


if __name__ == '__main__':
    FindOutWrongPicture('./../model/preProcessingModel3.pt')