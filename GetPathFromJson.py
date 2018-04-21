import os
import json

projectPath="E:\Projects\WebstormProjects\DanQing"

staticsPath=projectPath+"\static"

imagesPath=staticsPath+"\images"
jsonPath=staticsPath+"\json"

imageData={}

def initImageData(imagePath):
    dirs=os.listdir(imagePath)
    for d in dirs:
        childDir=os.path.join(imagePath,d)
        if(os.path.isdir(childDir)):
            imageData[d]=[]
            imgs=os.listdir(childDir)
            for i in imgs:
                imageData[d].append({"src":'/static/images/'+d+'/'+i})
    print(imageData)

def saveToJson(imageData):
    for key,val in imageData.items():
        childPath=os.path.join(jsonPath,key+'.json')
        with open(childPath,'w') as f:
            json.dump({'images':val},f)
            print(key+'.json 加载完成')


initImageData(imagesPath)
saveToJson(imageData)