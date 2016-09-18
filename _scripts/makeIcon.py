import scipy.misc as sm
import Tkinter
import tkFileDialog
import numpy as np


class IconGen:
    def __init__(self, size = 19):
        Tkinter.Tk().withdraw()
        self.name = tkFileDialog.askopenfilename()
        self.size = size
        self.fix()
        self.save()

    def fix(self ):
        try:
            im = sm.imread(self.name , mode = "RGBA")
        except TypeError:
            im = sm.imread(self.name)

        dim = im.shape[ : 2]
        im = im[(dim[0] - min(dim))/2 : (dim[0] + min(dim))/2, (dim[1] - min(dim))/2 : (dim[1] + min(dim))/2 ,:]

        self.im = sm.imresize(im, size = (self.size,self.size))

        xi = range(self.size)
        xi, yi = np.meshgrid(xi, xi)
        r = np.sqrt((xi - self.size/2)**2 + (yi - self.size/2)**2)
        outside = r > self.size/2
        x, y =  np.where(outside)
        self.im[x ,y , :] =  0

    def save(self):
        index = self.name.rfind(".")
        output = ".".join([self.name[0 : index], "png"])
        sm.imsave(output, self.im)

IconGen()
