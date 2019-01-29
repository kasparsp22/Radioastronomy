####################################################################
#                                                                  #
#           This script interacts with AIPS and does UVFLG         #
#           on user specified scans 				   #
#								   #
#           Workflow:						   #
# 	    1) User sets SCAN number from which to start 	   #
#	       ("start_scan" parameter)	  			   #
#	    2) User specifies after how many scans to	 	   #
#	       repeat flagging ("interval" parameter)  		   #
#	    3) Script  opens NX table and gets the TIMERANGE	   #
#	       for the scanns needed to be flagged		   #
#	    4) Script calls UVFLG and flags those scans            #                                      						     #
####################################################################


import AIPS
from AIPS import AIPS, AIPSDisk
from AIPSTask import AIPSTask, AIPSList, AIPSMessageLog
from AIPSData import AIPSUVData, AIPSImage, AIPSCat
import time, sys, os, numpy as np
import re
from time import gmtime, strftime, localtime
ti = time.time()    # To time the script


###############################################################################
###############################################################################
## Main UVFLG script
###############################################################################
###############################################################################

logfile = 'UVFLG_SCANS_log.txt'
lf = open(logfile,"w")

version_number = '1.0'
version_date = "26/09/18"

print >> lf, '\nStarted running UVFLG_SCANS version  %s' % (version_number), 'on %s' % strftime("%d-%b-%y"), 'at:', strftime("%H:%M:%S", localtime()),'\n'


print '\n Started running UVFLG_SCANS version  %s' % (version_number), 'on %s' % strftime("%d-%b-%y"), 'at:', strftime("%H:%M:%S", localtime()),'\n'


try:
    execfile("UVFLG_SCANS_inputs.py")

except:
    print "\n Could not find UVFLG_SCANS_inputs.py!"
    print " Make sure input file is in the same folder as this script (UVFLG_SCANS.py)"
    print " Aborting!"
    sys.exit(0)

## Test to see whether all variables have been set:

try:

    AIPS_user_number
    AIPS_name
    AIPS_klass
    AIPS_disk
    AIPS_seq
    flag_list
    start_scan
    end_scan
    interval
    stokes
    baselines
    ifs
    outfgver
    opcode
    reason
    data_dir

except:
    print " Please check you\'ve set all the variables in the input file."
    print " ABORTING AIPS_UVFLG!\n"
    sys.exit(0)

# Exporting DATADIR
os.environ ["DATADIR"] = data_dir
AIPS.userno = AIPS_user_number

# Setting UVFLG known parameters
uvflg = AIPSTask("uvflg")
uvflg.default
uvflg.inname = AIPS_name
uvflg.indisk = AIPS_disk
uvflg.inclass = AIPS_klass
uvflg.inseq = AIPS_seq
uvflg.sources[1:] = flag_list
uvflg.stokes = stokes
uvflg.outfgver = outfgver
uvflg.opcode = opcode
uvflg.reason = reason

## Get SCAN information (Timeranges, etc.) from LISTR
AIPS.userno = AIPS_user_number
listr = AIPSTask('listr')
listr.default
listr.inname = AIPS_name
listr.indisk = AIPS_disk
listr.inclass = AIPS_klass
listr.inseq = AIPS_seq
listr.optype = 'SCAN'
listr.docrt = -3
listr.outprint = 'DATADIR:DATA_SCANS.txt'
#listr.inp()
listr.go()

timearray = []
timearrayc = []

# Read in timeranges etc. from file to array
with open("DATA_SCANS.txt","r") as f:
   scans = f.read().splitlines()
for i in xrange(2 + start_scan,2 + start_scan + end_scan):   # "2 +" because we have 3 header lines that we do not need 
   scan_data = scans[i].split()   # Split string in array elements by whitespace
   if scan_data[1] != '0635+5157' and scan_data[1] != '0631+5311':   # If sources are not Main source and PH-Cal stop flagging and write data to log file
      print >>lf, 'Different source (%s) found in scan %d. Stopping flagging here!\n' % (scan_data[1], i-2)
      print 'Different source (%s) found in scan %d. Stopping flagging here!\n ' % (scan_data[1], i-2)
      break
   else:       
      print 'Flagging SCAN %s \n' % scan_data[0] 
      #array = re.split('[/:]',scan_data[4])+ re.split('[/:]',scan_data[6])
      #uvflg.timerang = scan_data[4].replace("/", " ").replace(":"," ") + " " + scan_data[6].replace("/"," ").replace(":"," ")  # creating string format for TIMERANGE parameter for UVFLG from SCAN file
      type(uvflg.timerang)
      print (uvflg.inp())
      break


lf.close()


