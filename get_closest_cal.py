

###########################################################
#### Script finds closest calibrator to a given target ####

import numpy as np
import astropy
from astropy.coordinates import SkyCoord



def astropy_sep (tra1,tdec1,tra2,tdes2):
    sc1 = SkyCoord(tra1,tdec1,frame = 'fk5', unit='degree')
    sc1 = SkyCoord(tra2,tdec2,frame = 'fk5', unit='degree')
    return((sc1.speration(sc2)).degree)

######################## MAIN ##############################

target_dir  = '/data/scratch/lb_bw/'
target_file = 'lbcs_manual_target_list.txt'
calib_dir   = './'
calib_file  = 'lotss_targets.csv'

targets = np.loadtxt(target_dir + target_file,skiprows=1, delimiter=',',dtype ='str'  )
print targets
calibr = np.loadtxt(calib_dir + calib_file,skiprows=1, delimiter=',',dtype ='str'  )
print calibr
print 111222222222333333333333333333333333

content = []
targets_1 = []
delta_dist_0 = 1000
calibrator = None
for i in targets:       ### Removing 'deg' from lists
    targets_1.append([i[0].replace('deg',''),i[1].replace('deg',''),i[2]])
for i in targets_1:
    for j in calibr:
        delta_dist_1 =abs(float(i[0])-float(j[0])) + abs(float(i[1]) - float(j[1]))   #### Calculete absoluted distance difference between target and calibratoe
        #print delta_dist_1
        #print delta_dist_1
        if delta_dist_1 < delta_dist_0:   ### Selecting calibrator with the lowest difference 
            delta_dist_0 = delta_dist_1
            calibrator =j[2]
        outdata =  {
        "Target": i[2],
        "Calibrator": calibrator,   
              }      
    #outdata['Target'].append(i[2])
    content.append(outdata)
print '###############'
print delta_dist_0
print '###############'
#print targets_1
print '########################'
#print content


