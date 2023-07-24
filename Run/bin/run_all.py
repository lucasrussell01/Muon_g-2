import GetIon
import subprocess
import os

f122nm=100e-6
f355nm=0.3
z_width=1.7e-3
y_width=15.5*1.7e-3
z_center=2.8e-3
y_center=0
detune=0

#f122nm=100e-6
#f355nm=0.3
#z_width=2.3e-3
#y_width=23e-3
#z_center=3.3e-3
#y_center=0
#detune=0
fall="result/all.dat"
finput_all="result/all_before_ionization.dat"

#dirname="data/"
dirname="/ghi/fs02/had/g-2/EndToEndSim2022Source/MuYield/" 
prefix="MuYield_220128_2e6_"
surfix=".dat"

out_dirname="result/"
out_surfix="_ionization.dat"

def run_all():
	process = "rm " + fall
	subprocess.call(process,shell=True)
	for i in range(1,100):
	#for i in range(1,2):
	#for i in range(10000,10001):

		i_zero=str(i).zfill(6)

		fname=subprocess.run("find " +dirname+prefix+str(i_zero)+"*"+surfix+" -print" ,shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)

		fin=fname.stdout.rstrip('\n')
		fin=fin.lstrip()
		fout=fin.replace(dirname,out_dirname)
		fout=fout.replace(surfix,out_surfix)

		print("Simulation start: input filename",fin, " output filename is", fout)

		GetIon.calcrateeq(fin,fout)
	
		#process_sub = "cat " + fin + " >> " + finput_all
		#subprocess.call(process_sub,shell=True)
		process = "cat " + fout + " >> " + fall
		subprocess.call(process,shell=True)


if __name__ == '__main__':
	run_all()
