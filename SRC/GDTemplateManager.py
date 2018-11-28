import os,sys,re,traceback
from datetime import datetime
from string import Template


class GDTemplateManager:
    templatePath = ''
    targetPaths = None
    targetNames = None

    def __init__(self, templatePath, targetPaths, targetNames):
        self.templatePath = templatePath
        self.targetPaths = targetPaths
        self.targetNames = targetNames

    def generate(self):
        self.replace()

    def replace(self):
        self.replaceType('Controller')
        self.replaceType('View')
        self.replaceType('Binder')
        self.replaceType('ViewModel')

    def replaceType(self, type):
        hTmplPath = self.templatePath + type + '.h'
        mTmplPath = self.templatePath + type + '.m'
        hTragetPath = self.targetPaths[type] + self.targetNames[type] + '.h'
        mTragetPath = self.targetPaths[type] + self.targetNames[type] + '.m'
        className = self.targetNames[type]
        self.replaceTemplate(hTmplPath, hTragetPath, className, self.targetNames)
        self.replaceTemplate(mTmplPath, mTragetPath, className, self.targetNames)



    def replaceTemplate(self,templatePath, targetPath, className, targetNames):
        class_file = open(targetPath, 'w')

        lines = []
        # 读取模板文件
        template_file = open(templatePath, 'r')
        tmpl = Template(template_file.read())
        # 模板替换

        view = targetNames['View']
        viewModel = targetNames['ViewModel']
        binder = targetNames['Binder']

        lines.append(tmpl.substitute
            (
            CLASSNAME = className,
            VIEWNAME = view,
            VIEWMODELNAME = viewModel,
            BINDERNAME = binder
        ))

        class_file.writelines(lines)
        class_file.close()
        template_file.close()
        print('替换完成 ', targetPath)

















