import subprocess
import os
#1st trial
f122nm=100e-6
f355nm=0.3
z_width=2.3e-3
y_width=2.3*10e-3
z_center=3.3e-3
y_center=0
t_laser=1.35e-6
##1st trial
#f122nm=100e-6
#f355nm=0.3
#z_width=2.e-3
#y_width=2.*8.73e-3
#z_center=2.e-3
#y_center=0

#f122nm=100e-6
#f355nm=0.3
#z_width=1.75e-3
#y_width=1.75*10e-3
#z_center=2.8e-3
#y_center=0

#f122nm=5e-6
#f355nm=0.006
#z_width=1.e-3
#y_width=5e-3
#z_center=2e-3
#y_center=0
#detune=100e9

detune=0
fout = "detune_scan.txt"

def calcrateeq(f122nm,f355nm,z_width,y_width,z_center,y_center,f_width=300e9,f_detune=0,f_t_laser=t_laser,fin="",fout=""):
	if (fin==""):
		subprocess.call( ["./bin/RateEquation_rootfileInput "+ str(f122nm)+" "+ str(f355nm)+" "+ str(z_width)+" "+str(y_width)+" "+str(z_center)+" "+ str(y_center)+" "+str(f_width)+" "+str(f_detune) + str(f_t_laser)],shell=True)
	else:
		fprocess="./bin/RateEquation_rootfileInput "+ str(f122nm)+" "+ str(f355nm)+" "+ str(z_width)+" "+str(y_width)+" "+str(z_center)+" "+ str(y_center)+" "+str(f_width)+" "+str(f_detune)+" "+str(f_t_laser) +"	"+fin+" "+str(fout)
		subprocess.call( [fprocess],shell=True)

#def WriteResult(fdetune):
#	fin= open("eff_temp.txt")
#	data=fin.read()
#	data_list = data.split() 
#	with open(fout, 'a') as f:
#		print(str(fdetune)+"	"+data_list[0], file=f)
#
#def LoopDetune():
#	for ndetune in range(-300,300,15):
#		fdetune  = ndetune*1e9
#		calcrateeq(f122nm,f355nm,z_width,y_width,z_center,y_center,500e9,fdetune)
#		#calcrateeq(f122nm,f355nm,z_width,y_width,z_center,y_center,753e9,fdetune)
#		WriteResult(fdetune)

if __name__ == '__main__':
	#if os.path.isfile(fout):
	#	subprocess.check_call("mv " + fout + " old.txt",shell = True)
	#LoopDetune()
	calcrateeq(f122nm,f355nm,z_width,y_width,z_center,y_center,500e9,detune)
