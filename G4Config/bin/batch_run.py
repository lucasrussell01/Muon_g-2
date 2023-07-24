import GetIon
import subprocess
import os
import argparse



fall="result/all.dat"
finput_all="result/all_before_ionization.dat"

#dirname="data/"
dirname="/ghi/fs02/had/g-2/EndToEndSim2022Source/MuYield/" 
prefix="MuYield_220128_2e6_"
surfix=".dat"


parser = argparse.ArgumentParser(description="Run batch G4 preparation")
parser.add_argument('--runID', required=True, type=int, help="ID for the run")
parser.add_argument('--VUV', required=False, type =str, default="VUVparam.txt",help="VUV config file")
parser.add_argument('--UNB', required=False, type =str, default="Unboundparam.txt",help="Unbound config file")

args = parser.parse_args()

runID = str(args.runID).zfill(5)

out_dirname="result/"
out_prefix = "MuYield_"
out_surfix=f"_ionization_run{runID}.dat"

filename1 = args.VUV 
filename2 = args.UNB

def run_all():
    process = "rm " + fall
    subprocess.call(process, shell=True)
    for i in range(1, 2):

        i_zero=str(i).zfill(6)
        fname=subprocess.run("find " +dirname+prefix+str(i_zero)+"*"+surfix+" -print" ,shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
        
        fin=fname.stdout.rstrip('\n')
        fin=fin.lstrip()
        fout=f"{out_dirname}{out_prefix}{i_zero}{out_surfix}"
        print(f"Simulation start: input filename: {fin} output filename is {fout}")
            
        GetIon.calcrateeq(fin,fout, filename1, filename2)

        process = "cat " + fout + " >> " + fall
        subprocess.call(process,shell=True)


if __name__ == '__main__':
	run_all()
