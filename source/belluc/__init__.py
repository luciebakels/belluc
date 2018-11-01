import numpy as np
from astropy.io import fits


class FitsFile:
	def __init__(self, fname):
		self.fname = fname
		self.file = None

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