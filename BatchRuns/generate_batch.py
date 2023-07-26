import os
import numpy as np


def CreateJob(name, runID, macro, VUVfile, UNBfile):

    if os.path.exists(name): os.system('rm %(name)s' % vars()) 

    os.system('echo "#!/bin/bash" >> %(name)s' % vars())

    os.system('echo "cd /home/had/lrussell" >> %(name)s' % vars())
    os.system('echo "source .bashrc_kamioka" >> %(name)s' % vars())
    os.system('echo "cd laserionization_highstat" >> %(name)s' % vars())
    os.system('echo "python3 bin/batch_run.py --runID=%(runID)s  --VUV=%(VUVfile)s --UNB=%(UNBfile)s" >> %(name)s' % vars())
    os.system('echo "cd /home/had/lrussell/ToRFQstudy/run" >> %(name)s' % vars())
    os.system('echo "python3 prep_g4.py --runID=%(runID)s --fin=%(macro)s" >> %(name)s' % vars())
    os.system('echo "source /home/had/lrussell/.bashrc" >> %(name)s' % vars())
    os.system('echo "../bin/Linux-g++/musrSim %(runID)s.mac" >> %(name)s' % vars())
    os.system('chmod +x %(name)s' % vars())
    print(f"Created job: {name}")


def SubmitJob(name):

    os.system(f'bsub -q s ./{name}')
    print(f"Submitted job: {name}")


def VUVconfig(name, E=100e-6, z_width=2.3e-3, y_width=23e-3, z_pos=3.3e-3, y_pos=0e-3, linewidth=500e9, freq=0, center_t=5e-9, FWHM_t=2e-9):

    name = "/home/had/lrussell/laserionization_highstat/" + name
    if os.path.exists(name): os.system('rm %(name)s' % vars()) 
    os.system(f'echo "{E}" >> {name}')
    os.system(f'echo "{z_width}" >> {name}')
    os.system(f'echo "{y_width}" >> {name}')
    os.system(f'echo "{z_pos}" >> {name}')
    os.system(f'echo "{y_pos}" >> {name}')
    os.system(f'echo "{linewidth}" >> {name}')
    os.system(f'echo "{freq}" >> {name}')
    os.system(f'echo "{center_t}" >> {name}')
    os.system(f'echo "{FWHM_t}" >> {name}')


def UNBconfig(name, E=0.3, z_width=2.3e-3, y_width=23e-3, z_pos=3.3e-3, y_pos=0e-3, linewidth=500e9, freq=0, center_t=5e-9, FWHM_t=2e-9):

    name = "/home/had/lrussell/laserionization_highstat/" + name
    if os.path.exists(name): os.system('rm %(name)s' % vars()) 
    os.system(f'echo "{E}" >> {name}')
    os.system(f'echo "{z_width}" >> {name}')
    os.system(f'echo "{y_width}" >> {name}')
    os.system(f'echo "{z_pos}" >> {name}')
    os.system(f'echo "{y_pos}" >> {name}')
    os.system(f'echo "{linewidth}" >> {name}')
    os.system(f'echo "{freq}" >> {name}')
    os.system(f'echo "{center_t}" >> {name}')
    os.system(f'echo "{FWHM_t}" >> {name}')


def vary_z_pos():
    n_runID = 11000 #start at 11000 then increment
    for z in np.arange(1e-3, 10.5e-3, 0.25e-3):
        # declare relevant vars
        runID = str(n_runID).zfill(5)
        #print(runID)
        VUVcfg = f'VUV_run{runID}.txt'
        UNBcfg = f'UNB_run{runID}.txt'       
        runname = runID + ".sh"
        macro = f'MuYield_000001_ionization_run{runID}.dat'
        # generate configs
        VUVconfig(VUVcfg, z_pos=z)
        UNBconfig(UNBcfg, z_pos=z)
        print(f"Generated configs for z_pos = {z}")
        # Create the job
        CreateJob(runname, runID, macro, VUVcfg, UNBcfg)
        # Submit the job
        SubmitJob(runname)
        # Increase runID by 1 for next value
        n_runID+=1

def vary_y_pos():
    n_runID = 12000 #start at 12000 then increment
    for y in np.arange(-23e-3, 24e-3, 1e-3):
        # declare relevant vars
        runID = str(n_runID).zfill(5)
        #print(runID)
        VUVcfg = f'VUV_run{runID}.txt'
        UNBcfg = f'UNB_run{runID}.txt'       
        runname = runID + ".sh"
        macro = f'MuYield_000001_ionization_run{runID}.dat'
        # generate configs
        VUVconfig(VUVcfg, y_pos=y)
        UNBconfig(UNBcfg, y_pos=y)
        print(f"Generated configs for y_pos = {y}")
        # Create the job
        CreateJob(runname, runID, macro, VUVcfg, UNBcfg)
        # Submit the job
        SubmitJob(runname)
        # Increase runID by 1 for next value
        n_runID+=1

def vary_z_size():
    n_runID = 13000 #start at 13000 then increment
    for z in np.arange(0, 7.5e-3, 0.1e-3):
        # declare relevant vars
        runID = str(n_runID).zfill(5)
        #print(runID)
        VUVcfg = f'VUV_run{runID}.txt'
        UNBcfg = f'UNB_run{runID}.txt'       
        runname = runID + ".sh"
        macro = f'MuYield_000001_ionization_run{runID}.dat'
        # generate configs
        VUVconfig(VUVcfg, z_width=z)
        UNBconfig(UNBcfg, z_width=z)
        print(f"Generated configs for z size = {z}")
        # Create the job
        CreateJob(runname, runID, macro, VUVcfg, UNBcfg)
        # Submit the job
        SubmitJob(runname)
        # Increase runID by 1 for next value
        n_runID+=1

def vary_y_size():
    n_runID = 14000 #start at 14000 then increment
    for y in np.arange(18e-3, 28.5e-3, 0.5e-3):
        # declare relevant vars
        runID = str(n_runID).zfill(5)
        #print(runID)
        VUVcfg = f'VUV_run{runID}.txt'
        UNBcfg = f'UNB_run{runID}.txt'       
        runname = runID + ".sh"
        macro = f'MuYield_000001_ionization_run{runID}.dat'
        # generate configs
        VUVconfig(VUVcfg, y_width=y)
        UNBconfig(UNBcfg, y_width=y)
        print(f"Generated configs for y size = {y}")
        # Create the job
        CreateJob(runname, runID, macro, VUVcfg, UNBcfg)
        # Submit the job
        SubmitJob(runname)
        # Increase runID by 1 for next value
        n_runID+=1

def vary_E_VUV():
    n_runID = 15000 #start at 15000 then increment
    for e in np.arange(80e-6, 122e-6, 2e-6):
        # declare relevant vars
        runID = str(n_runID).zfill(5)
        #print(runID)
        VUVcfg = f'VUV_run{runID}.txt'
        UNBcfg = f'UNB_run{runID}.txt'       
        runname = runID + ".sh"
        macro = f'MuYield_000001_ionization_run{runID}.dat'
        # generate configs
        VUVconfig(VUVcfg, E=e)
        UNBconfig(UNBcfg)
        print(f"Generated configs for VUV E = {e}")
        # Create the job
        CreateJob(runname, runID, macro, VUVcfg, UNBcfg)
        # Submit the job
        SubmitJob(runname)
        # Increase runID by 1 for next value
        n_runID+=1

def vary_E_UNB():
    n_runID = 16000 #start at 16000 then increment
    for e in np.arange(0.24, 0.37, 0.01):
        # declare relevant vars
        runID = str(n_runID).zfill(5)
        #print(runID)
        VUVcfg = f'VUV_run{runID}.txt'
        UNBcfg = f'UNB_run{runID}.txt'       
        runname = runID + ".sh"
        macro = f'MuYield_000001_ionization_run{runID}.dat'
        # generate configs
        VUVconfig(VUVcfg)
        UNBconfig(UNBcfg, E=e)
        print(f"Generated configs for UNB E = {e}")
        # Create the job
        CreateJob(runname, runID, macro, VUVcfg, UNBcfg)
        # Submit the job
        SubmitJob(runname)
        # Increase runID by 1 for next value
        n_runID+=1


vary_z_pos()
vary_y_pos()
vary_z_size()
vary_y_size()
vary_E_UNB()
vary_E_VUV()


