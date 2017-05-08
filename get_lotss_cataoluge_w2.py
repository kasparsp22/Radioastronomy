import pyvo as vo
import os
import glob
import numpy as np
import argparse

np.set_printoptions(threshold ='nan')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument( '-t',dest='targetdatadir',type=str,help='targetdata directory')
    parser.add_argument( '-r',dest='myrad',type=float,help='radius to search in degrees, default 2',default=2.0 )

    args = parser.parse_args()
    targetdatadir = args.targetdatadir
    targetdatadir = './test_data'
    myrad = args.myrad 
    ## get a list of measurement sets
    msfiles = glob.glob(targetdatadir+'/*.ms')

    '''
    ss = "taql 'select REFERENCE_DIR from %s/FIELD' > reference_dir.txt"%(msfiles[0])
    os.system( ss )
    print ss
    '''
    ## get the reference direction
    with open( 'reference_dir.txt', 'r' ) as f:
	lines = f.readlines()
    f.close()
    #os.system( 'rm reference_dir.txt' )
    ref_dir = lines[2].rstrip('\n').rstrip(']').strip('[')
    ## convert to degrees
    ra_tmp = ref_dir.split(',')[0]
    rah = float( ra_tmp.split('h')[0] )
    ram = float( ra_tmp.split('h')[1].split('m')[0] )
    ras = float( ra_tmp.split('m')[1] )
    radeg = 15 * ( ( ras/60. + ram )/60. + rah ) 
    dec_tmp = ref_dir.split(',')[1]
    ded = float( dec_tmp.split('d')[0] )
    dem = float( dec_tmp.split('d')[1].split('m')[0] )
    des = float( dec_tmp.split('m')[1] )
    dedeg = ( ( des/60. + dem )/60. + ded )
    
    mypos = ( radeg, dedeg )

    ## this is the LOFAR lbcs database to query
    url = 'http://vo.astron.nl/lbcs/lobos/cone/scs.xml'
    t = vo.conesearch( url, pos=mypos, radius=10 )
    tb = t.votable.to_table()

    #### Workaround to sort and pick good calibrator info from tb array ###########
    counts=[]
    P_count  = 0                        
    for i in tb:
        b = i[5].count('P')      #### Count of 'P' - good baselines       
        counts.append(b)
        if b >=2:
            P_count = P_count + 1    #### To determine how many sources to take
    print 'Good sources - ' + str(P_count)   
    inds = np.argsort(counts)
    tb_sorted =tb[inds[::-1]]
    len_array = len(tb_sorted)
    for i in range ((len_array-P_count)):
        len_array-=1
        tb_sorted.remove_row(len_array)
    ########### Create output table with 'raj2000' 'decj2000' 'ObsID' columns ########## 
    tb_out_0 = tb_sorted['raj2000','decj2000','ObsID'] 
    tb_out = tb_out_0['raj2000','decj2000']   ######### Array for finding duplicates

    ########### Remove duplicats #################################
    tb_out_1 = np.array(tb_out)
    result=[idx for idx, item in enumerate(tb_out_1) if item in tb_out_1[:idx]]
    print len(result)
    print len(tb_out_0)
    tb_out_0.remove_rows(result)
    print len(tb_out_0)              

    ########## Return output file ###############################
    outfile = 'lotss_targets.csv'
    tb_out_0.write(outfile, format='ascii.csv')    
  

if __name__ == "__main__":
    main()
