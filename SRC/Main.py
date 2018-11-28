
from GDFolderManager import  *

from  GDFileManager import  *

from  GDTemplateManager import  *




class GDObjCGenerator:
    moduleName = ''
    path = ''
    tag = ''
    folderManager = None
    fileManager = None

    def __init__(self, path, moduleName, tag):
        self.path = path
        self.moduleName = moduleName
        self.tag = tag


    def createFolder(self):
        self.folderManager = GDFolderManager(self.path, self.moduleName)
        self.folderManager.createFolder()

    def createFile(self):
        viewPath = self.folderManager.viewPath;
        binderPath = self.folderManager.binderPath;
        viewModelPath = self.folderManager.viewModelPath;
        self.fileManager = GDFileManager(viewPath, binderPath, viewModelPath, self.moduleName, self.tag)
        self.fileManager.build()

    def generate(self):
        templatePath = './Template/'
        targetPaths = { 'View':self.folderManager.viewPath,
                        'Controller': self.folderManager.viewPath,
                        'Binder' : self.folderManager.binderPath,
                        'ViewModel': self.folderManager.viewModelPath
                        }
        targetNames = self.fileManager.classNames()
        templateManager = GDTemplateManager(templatePath, targetPaths, targetNames)
        templateManager.generate()


    def start(self):
        self.createFolder()
        self.createFile()
        self.generate()


def start():
    basePath = '/Users/tiger/Desktop/'
    moduleName = 'Notice'
    tag = 'PT'

    codeGenerator = GDObjCGenerator(basePath, moduleName, tag)
    codeGenerator.start()


start()
