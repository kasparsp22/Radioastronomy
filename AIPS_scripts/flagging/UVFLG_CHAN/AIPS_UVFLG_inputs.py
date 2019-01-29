
###############################################################################
###
###  Filename    : AIPS_UVFLG_inputs.py
###  FileType    : Python source file
###  Author      : Kaspars Prusis
###  Date        : 09/08/2018
###  Description : This is an input file for script AIPS_UVFLG.py
###  or setting all the variables (AIPS user number,inname, etc.,
###  and all parameters for UVFGL)
###
###############################################################################

AIPS_user_number = 2
AIPS_name = 'ALL_3'
AIPS_klass = 'UVCOP'
AIPS_disk = 2
AIPS_seq = 1
flag_list = ['1331+305']


######## Flagging for 1331+305 after PCAL #######

################### Stokes RL ###################
#################################################

'''
Stokes = 'RL'
baselines = ['1-6']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 3, 8, 6, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            105, 107, 109,
            52, 101, 102, 104, 105, 106, 107, 110,
            101, 104, 106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged
reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-7']
ifs = [5]                # array of IFS for which flagging is needed
num_chan_per_if = [1]     # number of channels that need to be flagged per IF
channels = [52]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged
reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-8']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 2, 8, 4, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            105, 109,
            52, 101, 102, 104, 105, 106, 107, 110,
            106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-9']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 3, 8, 6, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            105, 107, 109,
            52, 101, 102, 104, 105, 106, 107, 110,
            101, 104, 106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['5-6']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [4]     # number of channels that need to be flagged per IF

channels = [106, 107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['5-8']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [3]     # number of channels that need to be flagged per IF

channels = [107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['5-9']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [8]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 103, 106, 107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['6-8']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [3]     # number of channels that need to be flagged per IF

channels = [107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['6-9']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [9]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 103, 104, 106, 107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-5']

ifs = [5]                # array of IFS for which flagging is needed
num_chan_per_if = [1]     # number of channels that need to be flagged per IF

channels = [100]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-6']

ifs = [5, 6]                # array of IFS for which flagging is needed
num_chan_per_if = [1, 3]     # number of channels that need to be flagged per IF

channels = [100, 100, 102, 103]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-8']

ifs = [5]                # array of IFS for which flagging is needed
num_chan_per_if = [1]     # number of channels that need to be flagged per IF

channels = [100]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['1-9']

ifs = [5, 6]                # array of IFS for which flagging is needed
num_chan_per_if = [1, 3]     # number of channels that need to be flagged per IF

channels = [100, 100,  102, 103]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

'''
Stokes = 'RL'
baselines = ['5-9']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [1]     # number of channels that need to be flagged per IF

channels = [104]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_RL'
'''

################### Stokes LR ###################
#################################################

Stokes = 'LR'
baselines = ['7-9']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [2]     # number of channels that need to be flagged per IF

channels = [107, 108]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged
reason = 'WRONG_DATA_LR'

'''
Stokes = 'LR'
baselines = ['1-5']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [3, 3, 9, 9, 5, 5]     # number of channels that need to be flagged per IF

channels = [102, 107, 110,
            105, 107, 109,
            52, 100, 101, 102, 104, 105, 106, 107, 110,
            100, 101, 102, 103 104, 106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged
reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['1-6']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 3, 9, 4, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            105, 107, 109,
            52, 100, 101, 102, 104, 105, 106, 107, 110,
            52, 100, 101, 102, 104, 105, 106, 107, 110,
            106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109, 110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged
reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['1-7']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 1, 8, 4, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            109,
            52, 101, 102, 104, 105, 106, 107, 110,
            106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged
reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['1-8']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 2, 8, 4, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            105, 109,
            100, 101, 102, 104, 105, 106, 107, 110,
            106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['1-9']

ifs = [3, 4, 5, 6, 7, 8]                # array of IFS for which flagging is needed
num_chan_per_if = [5, 3, 8, 9, 5, 5]     # number of channels that need to be flagged per IF

channels = [100, 101, 102, 107, 110,
            105, 107, 109,
            52, 101, 102, 104, 105, 106, 107, 110,
            100, 101, 102, 103, 104, 106, 107, 108, 109,
            101, 103, 107, 109, 110,
            100, 102, 105, 109,  110]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['2-5']

ifs = [5, 6]                # array of IFS for which flagging is needed
num_chan_per_if = [4, 1]     # number of channels that need to be flagged per IF

channels = [99, 100, 101,
            109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['2-6']

ifs = [5, 6, 7]                # array of IFS for which flagging is needed
num_chan_per_if = [4, 3, 1]     # number of channels that need to be flagged per IF

channels = [100, 101, 107, 108, 
            107, 108, 109,
            105]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['2-9']

ifs = [5, 6, 7]                # array of IFS for which flagging is needed
num_chan_per_if = [4, 3, 1]     # number of channels that need to be flagged per IF

channels = [100, 101, 107, 108, 
            107, 108, 109,
            105]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['5-6']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [4]     # number of channels that need to be flagged per IF

channels = [106, 107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['5-7']

ifs = [5, 6]                # array of IFS for which flagging is needed
num_chan_per_if = [3, 4]     # number of channels that need to be flagged per IF

channels = [100, 101, 102,
            106, 107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['5-8']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [4]     # number of channels that need to be flagged per IF

channels = [106, 107, 108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['5-9']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [2]     # number of channels that need to be flagged per IF

channels = [108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['6-7']

ifs = [5, 6]                # array of IFS for which flagging is needed
num_chan_per_if = [3, 2]     # number of channels that need to be flagged per IF

channels = [100, 101, 102,
            108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['6-8']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [2]     # number of channels that need to be flagged per IF

channels = [108, 109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['6-9']

ifs = [6]                # array of IFS for which flagging is needed
num_chan_per_if = [1]     # number of channels that need to be flagged per IF

channels = [109]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''

'''
Stokes = 'LR'
baselines = ['7-9']

ifs = [5, 6, 7]                # array of IFS for which flagging is needed
num_chan_per_if = [1, 4, 1]     # number of channels that need to be flagged per IF

channels = [100,
            106, 107, 108, 109,
            105]    # channel numbers in all IFS starting from 'ifs[0]' that need to be flagged

reason = 'WRONG_DATA_LR'
'''




outfgver = 1
opcode = 'FLAG'
