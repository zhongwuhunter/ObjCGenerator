import os,sys


class GDFolderManager:
    moduleName = ''
    path = ''
    viewPath =''
    binderPath = ''
    viewModelPath = ''


    def __init__(self, path, moduleName):
        self.path = path
        self.moduleName = moduleName

    def createFolder(self):
        basePath = self.path + self.moduleName
        self.viewPath = basePath + '/View/'
        self.binderPath = basePath + '/Binder/'
        self.viewModelPath = basePath + '/ViewModel/'
        paths = [basePath, self.viewPath, self.viewModelPath, self.binderPath]
        for folderPath in paths:
            folder = os.path.exists(folderPath)
            if not folder:
                os.makedirs(folderPath)

            print("创建目录成功" + folderPath);








