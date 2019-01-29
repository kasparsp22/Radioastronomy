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
#	    4) Script calls UVFLG and flags those scans            #
#           run script with parseltongue UVFLG_SCANS.py            #
#           after the script has ended log file                    #
#           UVFLG_SCANS_log.txt is created                         #
#                                                                  #
####################################################################

########################## README ##################################
###            
### This script was developed to flag e-MERLIN data phase reference
### scans for LO telescope because it is off source every second
### PH-Cal scan (it is too slow that is why it is left on a target
### every second PH-Cal scan)
### This script is partially automatic, because it does not know the 
### sequence of the bad scans (every fourth, third scan), nor does it
### know with which to start (start flagging with first, second, etc
### scan). 
### So it is NEEDED and I did use it together with SPFLG because
### with SPFG you can see at which scan the bad data scans start
### and you can see the sequence (every fourth, third scan is bad)
### so use this script together with SPFLG.
### As the sequence of bad skans might change, CAREFULLY look on all 
### the data you want to use this script on with SPFLG and only then
### after you are shure about the sequence run the script !!! 
###
### Usually the sequence of bad scans might change after another source
### is obeserved in a scan. The script is aware of that and will stop
### working when it will see different source that the one in flag_list
### and will write that scan number in the log file.
### So when that happens go to log file, see the scan at which it
### stopped working and use SPFLG to look at the sequence of bad 
### scans after that scan and adjust the parameters start_scan
### and interval and rerun the script! 
###
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
########################## Main UVFLG script ##################################
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
    target
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
    log_dir
    start_time_offset
    end_time_offset

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
uvflg.sources[1] = flag_list
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
for i in xrange(2 + start_scan,2 + end_scan + 1):   # "2 +" because we have 3 header lines that we do not need; "+1" because to include end scan in flagging
   scan_data = scans[i].split()   # Split string in array elements by whitespace
   if scan_data[1] != target and scan_data[1] != flag_list:   # If sources are not Main source and PH-Cal stop flagging and write data to log file
      print >>lf, '  Different source (%s) found in SCAN %d!! Stopping flagging here!\n' % (scan_data[1], i-2)
      print 'Different source (%s) found in SCAN %d!! Stopping flagging here!\n ' % (scan_data[1], i-2)
      print >> lf, '*************************************************************************'
      break
   else:           
      if (i-2) == start_scan or (i-2) == inter + interval:
         time_array = re.split('[/:]',scan_data[4]) + re.split('[/:]', scan_data[6])  # Splitting out TIMERANG from DATA_SCANS.txt file
         time_array_int = [int(x) for x in time_array]  # Converting array of strings to array of ints needed for calculations

         start_time_in_sec = time_array_int[0] * 86400 + time_array_int[1] * 3600 + time_array_int[2] * 60 + time_array_int[3]
         end_time_in_sec = time_array_int[4] * 86400 + time_array_int[5] * 3600 + time_array_int[6] * 60 + time_array_int[7]
        
         # The following changes in TIMERANGE are due to some errors with flagging when
         # the data appears still not flagged for some seconds even if the scan
         # timerange is set correctly. So to deal with that I increase flagging TIMERANGE by
         # subtracting ectra seconds from the start of the scan and adding to the end of the scan

         start_time_in_sec -= start_time_offset
         end_time_in_sec += end_time_offset
         
         # Setting uvflg.timerang parameter to new timerange values
         uvflg.timerang[1] = start_time_in_sec // 86400
         uvflg.timerang[2] = (start_time_in_sec - uvflg.timerang[1] * 86400) // 3600
         uvflg.timerang[3] = (start_time_in_sec - uvflg.timerang[1] * 86400 - uvflg.timerang[2] * 3600) // 60
         uvflg.timerang[4] = start_time_in_sec - uvflg.timerang[1] * 86400 - uvflg.timerang[2] * 3600 - uvflg.timerang[3] * 60
        
         uvflg.timerang[5] = end_time_in_sec // 86400
         uvflg.timerang[6] = (end_time_in_sec - uvflg.timerang[5] * 86400) // 3600
         uvflg.timerang[7] = (end_time_in_sec - uvflg.timerang[5] * 86400 - uvflg.timerang[6] * 3600) // 60
         uvflg.timerang[8] = end_time_in_sec - uvflg.timerang[5] * 86400 - uvflg.timerang[6] * 3600 - uvflg.timerang[7] * 60   
         
         print 'Flagging SCAN %s with timerange %s ' % (i-2, ' '.join(time_array)) 
         print >> lf,'  Flagging SCAN %s with timerange %s' % (i-2, ' '.join(time_array))    
         inter = (i-2)
         #uvflg.inp()
         #break
         uvflg.go()

lf.close()

