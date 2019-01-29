####################################################################
#                                                                  #
#           This script interacts with AIPS and does UVFLG         #
#           on user specified baselines, channels, antennas, etc   #
#                                                                  #
####################################################################
import AIPS
from AIPS import AIPS, AIPSDisk
from AIPSTask import AIPSTask, AIPSList, AIPSMessageLog
from AIPSData import AIPSUVData, AIPSImage, AIPSCat
import time, sys, os, numpy as np
from time import gmtime, strftime, localtime
ti = time.time()    # To time the script


###############################################################################
###############################################################################
## Main UVFLG script
###############################################################################
###############################################################################

version_number = '1.0'
version_date = "09/08/18"


print '\n Started running AIPS_UVFLG version  %s' % (version_number), 'on %s' % strftime("%d-%b-%y"), 'at:', strftime("%H:%M:%S", localtime()),'\n'


try:
    execfile("AIPS_UVFLG_inputs.py")

except:
    print "\n Could not find AIPS_UVFLG_inputs.py!"
    print " Make sure input file is in the same folder as this script (AIPS_UVFLG.py)"
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
    Stokes
    baselines
    ifs
    num_chan_per_if
    channels
    outfgver
    opcode
    reason

except:
    print " Please check you\'ve set all the variables in the input file."
    print " ABORTING AIPS_UVFLG!\n"
    sys.exit(0)

## Read parameters from input file to local variable
AIPS.userno = AIPS_user_number
uvflg = AIPSTask('uvflg')
uvflg.default
uvflg.inname = AIPS_name
uvflg.indisk = AIPS_disk
uvflg.inclass = AIPS_klass
print dir(uvflg.intext)
uvflg.sources[1:] = flag_list
uvflg.stokes = Stokes
uvflg.opcode = opcode
uvflg.reason = reason
uvflg.outfgver = outfgver
uvflg.inseq = AIPS_seq

antennas = map(int, baselines[0].split('-'))   # map converts str array to int array
uvflg.antennas[1:] = antennas                  # antennas array is passed to an uvflg.antennas parameter
uvflg.baseline[1] = int(list(baselines[0])[2]) # need to set only one of the antennas
uvflg.inp()

'''
prtab = AIPSTask('prtab')
prtab.inname = AIPS_name
prtab.indisk = AIPS_disk
prtab.inclass = AIPS_klass
prtab.inseq = AIPS_seq
prtab.inext = 'FG'
prtab.outprint = 'PRTAB_OUTPUT'
prtab.go()
'''

### Flagging of data
### Setting of all the channels and IFS

num_element = 0;

for i in range(len(baselines)):
    for k in range(len(ifs)):
        #print "IF -> %d" % ifs[k]
        for z in range (num_chan_per_if[k]):
            uvflg.bif = ifs[k]
            #print "BIF -> %d" % uvflg.bif
            uvflg.eif = uvflg.bif
            #print "EIF -> %d" % uvflg.eif
            uvflg.bchan = channels[num_element]
            #print "BCHAN -> %d" % uvflg.bchan
            uvflg.echan = uvflg.bchan
            #print "ECHAN -> %d" % uvflg.echan
            num_element+=1
            uvflg.inp()
            uvflg.go()
