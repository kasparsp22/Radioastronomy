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
lf = open(logfile,"a+")

version_number = '1.0'
version_date = "26/09/18"

print >> lf, '*************************************************************************'
print >> lf, '\n  Started running UVFLG_SCANS version  %s' % (version_number), 'on %s' % strftime("%d-%b-%y"), 'at:', strftime("%H:%M:%S", localtime()),''


print '\n  Started running UVFLG_SCANS version  %s' % (version_number), 'on %s' % strftime("%d-%b-%y"), 'at:', strftime("%H:%M:%S", localtime()),'\n'



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
    antennas
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

print >>lf, '  Flagging source(s) %s for antennas %s. Reason -> %s' %(' '.join(flag_list),', '.join(map(str,antennas)),reason)
print 'All data will be applied to AIPS file %s. %s FG table %d' %(AIPS_name, AIPS_klass, outfgver)
print >> lf, '  All data will be applied to AIPS file %s. %s FG table %d' %(AIPS_name, AIPS_klass, outfgver)
print '  Doing SCANS %d - %d; flagging every %d SCAN ' %(start_scan, end_scan, interval)
print >> lf, '  Doing SCANS %d - %d; flagging every %dth SCAN \n' %(start_scan, end_scan, interval)

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
uvflg.antennas[1:] = antennas
uvflg.baseline[1:] = baselines
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
inter = start_scan   # Used as a variable for flagging only every 4th scan

# Read in timeranges etc. from file to array
with open("DATA_SCANS.txt","r") as f:
   scans = f.read().splitlines()

# Extracting info and doing flagging of SCANS
for i in xrange(2 + start_scan,2 + start_scan + end_scan):   # "2 +" because we have 3 header lines that we do not need 
   print i 
   scan_data = scans[i].split()   # Split string in array elements by whitespace
   if scan_data[1] != '0635+5157' and scan_data[1] != '0631+5311':   # If sources are not Main source and PH-Cal stop flagging and write data to log file
      print >>lf, '  Different source (%s) found in SCAN %d!! Stopping flagging here!\n' % (scan_data[1], i-2)
      print 'Different source (%s) found in SCAN %d!! Stopping flagging here!\n ' % (scan_data[1], i-2)
      print >> lf, '*************************************************************************'
      break
   else:           
      if (i-2) == start_scan or (i-2) == inter + interval:
         time_array = re.split('[/:]',scan_data[4]) + re.split('[/:]', scan_data[6])
         uvflg.timerang[1:] = [int(x) for x in time_array]   # Converting all array elements that are strings to integers, needed for timerang parameter
         
         # The following changes in TIMERANGE are due to some errors with flagging when
	 # the data appears still not flagged for some seconds even if the scan
         # timerange is set correctly. So to deal with that I increase flagging TIMERANGE
         # 
         #uvflg.timerang[4] = uvflg.timerang[4] - 5  ## Increase lower limit of flag by 5 sec
         #uvflg.timerang[8] = uvflg.timerang[8] + 5  ## Increase upper limit of flg by 5 sec
         print 'Flagging SCAN %s with timerange %s ' % (scan_data[0], ' '.join(time_array)) 
         print >> lf,'  Flagging SCAN %s with timerange %s' % (scan_data[0], ' '.join(time_array))    
         inter = (i-2)
         #uvflg.inp()
         #break
         #uvflg.go()
lf.close()


