import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import glob
import operator
from operator import itemgetter
from Data import *

class Regression:

    @staticmethod
    def LoadSet(folder):
        data = Regression.LoadData(folder)
        labels = Regression.LoadLabels(folder)
        values =(data, labels)
        return values
    
    @staticmethod
    def LoadData(folder):
        set = []
        path = "dataset\\" + folder + "\\inputs\\*.png"
        for filename in glob.glob(path):
            img = mpimg.imread(filename)#.convert('LA')
            img = Regression.__ConvertToGrayscale(img)
            data = img.reshape(20, 20, 1)
            set.append(data)
        return np.asarray(set)
    
    @staticmethod
    def LoadLabels(folder):
        labels = LoadJson(folder)       
        for key in labels :
            name = key.split('_')[0]
            labels[key] = labels[key] / SpellCooldowns[name]

        sorted_labels = sorted(labels.items(), key=operator.itemgetter(0))
        values = [x[1] for x in sorted_labels]
        return np.asarray(values)
    
    def __ConvertToGrayscale(image):
        return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

    @staticmethod
    def __ImageTest():
        img = mpimg.imread(file)
        print(img)
        print(img.shape)
        plt.imshow(img) # 20 *20 * 3
        imgFlat = img.flatten(order='C')
        print(imgFlat) # 1 * 1200
        plt.show()


if __name__ == "__main__":

    print("Start")
    
    #ImageTest()
    trainSet = Regression.LoadSet("train")
    print(trainSet[1])
    print("End")
