
###############################################################################
###
###  Filename    : UVFLG_SCANS_inputs.py
###  FileType    : Python source file
###  Author      : Kaspars Prusis
###  Date        : 09/08/2018
###  Description : This is an input file for script AIPS_UVFLG.py
###  for setting all the variables (AIPS user number,inname, and SCAN numbers
###  for UVFGL)
###
###############################################################################

AIPS_user_number = 2
AIPS_name = '0635+5157_8'
AIPS_klass = 'SPLAT'
AIPS_disk = 2
AIPS_seq = 1
target = '0635+5157'             # Main observable source
flag_list = '0631+5311'          # Source for which to do flagging of scans
start_scan = 34  		 # Scan to start flagging with
end_scan = 260  		 # End scan to flag 
interval = 4    		 # Interval between scans to be flagged (every fourth need to be flagged)
stokes = 'FULL'                  # Flag  Stokes parameters (RR, LL, RL, LR, FULL, CROSS)
antennas = [1, 0]                # Flag scans containing antenna number   
baselines = [0]                  # Flag scans with all baselines containing antennas set in "antennas" parameter
ifs = 0                          # IFs for which to flag scans (default "0" - all IFs) 
outfgver = 1                     # Version of Flag table (FG) in which to write flags generated
opcode = 'FLAG'                  
reason = 'LO_DROPOUT'
log_dir = '/home/lofar/kaspars/scripts/AIPS_scripts/flaging/UVFLG_SCAN'

###############################################################################
###
###  Extra settings 
###
###############################################################################
###
###  There are ocasions when using this script there are some unflagged data
###  at the beginning and end of the scans left after the flagging (even if
###  the scan times to be flagged are set correctly). At the moment of writing
###  this script I did not understand why this happens but I found a solution
###  to flag extra time during the start and end of the scan.
###  So the following two setting are - how much before the start and after 
###  the scan to flag.
###  This works because there are some time between the scans when nothing 
###  is observed and you can flag it. BUT be carefull not to add too big
###  extra time to be flagged so you do not flag data from the next or the 
###  previous scan (time between scans ir e-MERLIN varies from ~7 for PH-Cal
###  to ~30 sec the main source)

start_time_offset = 5    # Extra seconds to take before the start of the scan
end_time_offset = 5      # Extra seconds to flag after the end of scan
