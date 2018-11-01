import argparse
import numpy as np
#import sys
#sys.path.append("/home/luciebakels/Code/codingWorkshop2018/belluc/source/")

from belluc import *

#fitsfile = "/home/luciebakels/Code/codingWorkshop2018/SciCoder-2018-Perth/Data Files/spectra/spec-10000-57346-0002.fits"

parser = argparse.ArgumentParser(description="This program does stuff", usage="name_of_script ...", epilog="this is text added to the end of the help")

parser.add_argument("-f", "--files", dest="files",default=None,help="url file name",nargs="+")
parser.add_argument("-n", "--nfiles", dest="nfiles",default=None,help=".txt file containing fitsfiles", required=False)

args = parser.parse_args()

filename = args.files

nfile = np.genfromtxt(args.nfiles, dtype=None)

for i in range(len(nfile)):
	fitsfile = nfile[i].decode('utf-8')
	ff = FitsFile(fitsfile)
	ff.printNumberHDUs()


