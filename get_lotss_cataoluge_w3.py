import pyvo as vo
import os
import glob
import numpy as np
import argparse

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
    #msfiles = targetdatadir + '/PP1_av_corr.ms'
    print msfiles
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
    print ref_dir
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
    
    print radeg
    print dedeg
    mypos = ( radeg, dedeg )

    ## this is the tier 1 database to query
    url = 'http://vo.astron.nl/lbcs/lobos/cone/scs.xml'
    t = vo.conesearch( url, pos=mypos, radius=10 )

    tb = t.votable.to_table()
    ## find unresolved

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
    #print tb_sorted
    #print P_count
    len_array = len(tb_sorted)
    for i in range ((len_array-P_count)):
        len_array-=1
        tb_sorted.remove_row(len_array) 
    #b_sorted.add_row('L332093',205.73033333333299,54.242361111111101,2457100.5,'00:57:021','PXX-PXXXX',18)

    ########### Create output table with 'raj2000' 'decj2000' 'ObsID' columns ##########
    tb_out_0 = tb_sorted['raj2000','decj2000','ObsID']
    tb_out = tb_out_0['raj2000','decj2000']
    ########### Add and remove duplicats #################################
    print 2222222222222222222222222222222222
    #tb_out_1 = np.append(tb_out,np.array([(205.73033333333299,54.242361111111100)], dtype =tb_out.dtype ))
    tb_out_1 = np.array(tb_out)
    result=[idx for idx, item in enumerate(tb_out_1) if item in tb_out_1[:idx]]
    print result
    tb_out_0.remove_rows(result)
    print tb_out_0          
    
    ########## Return output file ###############################
    outfile = 'lotss_targets.csv'
    #tb_out.write(outfile, format='ascii.csv')    
       

    #tb_uniq = tb_out['raj2000','decj2000']
  
    
    
if __name__ == "__main__":
    main()
