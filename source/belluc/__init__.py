import numpy as np
from astropy.io import fits


class FitsFile:
    def __init__(self, fname):
        self.fname = fname
        self.file = None
        self.ra = None
        self.dec = None

    def openFile(self):
        if self.file is None:
            self.file = fits.open(self.fname)
        else:
            return 0

    def closeFile(self):
        if self.file is None:
            return 0
        else:
            self.file.close()
            self.file = None

    def printNumberHDUs(self):
        self.openFile()
        
        num_hdus = len(self.file)
        print("This file has {} HDUs.".format(num_hdus))        

        self.closeFile()
    
    def checkRA(self):
        if self.ra is not None:
            return 0

        self.openFile()
        
        self.ra = self.file[0].header["RA"]        
        
        self.closeFile()

    def checkDec(self):
        if self.dec is not None:
            return 0

        self.openFile()
        
        self.dec = self.file[0].header["DEC"]        
        
        self.closeFile() 

    def printRA(self):
        self.checkRA()
        print('RA: ', self.ra)

    def printDEC(self):
        self.checkDec()
        print('DEC: ', self.dec)