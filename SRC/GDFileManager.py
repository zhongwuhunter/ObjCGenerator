import os,sys

class GDFileManager:
    __viewPath = ''
    __binderPath = ''
    __viewModelPath = ''
    __moduleName = ''
    __tag = ''
    def __init__(self, viewPath, binderPath, viewModelPath, moduleName, tag) :
        self.viewPath = viewPath
        self.binderPath = binderPath
        self.viewModelPath = viewModelPath
        self.moduleName = moduleName
        self.tag = tag


    def build(self):
        self.buildControllerFile()
        self.buildViewFile()
        self.buildBinderFile()
        self.buildViewModelFile()



    def classNames(self):
        viewName = self.tag + self.moduleName + 'View'
        controllerName = self.tag + self.moduleName + 'Controller'
        viewModelName = self.tag + self.moduleName + 'ViewModel'
        binderName = self.tag + self.moduleName + 'Binder'

        result = {'View':viewName, 'Controller':controllerName,
                  'ViewModel':viewModelName, 'Binder':binderName}
        return  result


    def buildControllerFile(self):
        hPath = self.viewPath + self.tag + self.moduleName + 'Controller.h'
        mPath = self.viewPath + self.tag + self.moduleName + 'Controller.m'
        self.createFile([hPath, mPath])


    def buildViewFile(self):
        hPath = self.viewPath + self.tag + self.moduleName + 'View.h'
        mPath = self.viewPath + self.tag + self.moduleName + 'View.m'
        self.createFile([hPath, mPath])



    def buildBinderFile(self):
        hPath = self.binderPath + self.tag + self.moduleName + 'Binder.h'
        mPath = self.binderPath + self.tag + self.moduleName + 'Binder.m'
        self.createFile([hPath, mPath])

    def buildViewModelFile(self):
        hPath = self.viewModelPath + self.tag + self.moduleName + 'ViewModel.h'
        mPath = self.viewModelPath + self.tag + self.moduleName + 'ViewModel.m'
        self.createFile([hPath, mPath])



    def createFile(self, paths):
        for path in paths:
            file = open(path, 'w')
            file.close()
            print("创建文件成功" , path)