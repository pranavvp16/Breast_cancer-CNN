from config import config 
from imutils import paths
import random
import shutil
import os 

imagePaths = list(paths.list_images(config.ORIG_INPUT_DATASET))
random.seed(42)
random.shuffle(imagePaths)

i = int(len(imagePaths)*config.TRAIN_SPLIT)
trainPaths = imagePaths[:i]
testPaths = imagePaths[i:]

i = int(len(trainPaths)*config.VAL_SPLIT)
valPaths = imagePaths[:i]
trainPaths = imagePaths[i:]

dataset = [
    ("training",trainPaths,config.TRAIN_PATH),
    ("validation",valPaths,config.VAL_PATH),
    ("test",testPaths,config.TEST_PATH)
]

#Looop over the dataset list 
for(dtype, imagePaths ,baseOutput) in dataset:
    print("INFO[] building '{}' split",format(dtype))

    if not os.path.exists(baseOutput):
        print("INFO[] creating '{}' directory as it not existed",format(baseOutput))
        os.makedirs(baseOutput)
    
    for inputPaths in imagePaths:
        filename = inputPaths.split(os.path.sep)[-1]
        label=filename[-5:-4]
        
        labelPath = os.sep.join([baseOutput,label])

        if not os.path.exists(labelPath):
            print("INFO[] creating '{}' directory",format(labelPath))
            os.makedirs(labelPath)
        
        p = os.path.sep.join([labelPath,filename])
        shutil.copy2(inputPaths,p)


