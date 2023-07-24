import argparse
import math

parser = argparse.ArgumentParser(description="Run batch G4 preparation")
parser.add_argument('--runID', required=True, type=int, help="run ID")
parser.add_argument('--fin', required=True, type=str, help="input .dat file")
args = parser.parse_args()

runID = str(args.runID).zfill(5)


with open(f'/home/had/lrussell/laserionization_highstat/result/{args.fin}', 'r') as file:
    n = len(file.readlines())
    n_lim = math.floor(n/100)*100
    print(f"Number of available events: {n}, GEANT4 limit will be {n_lim}")
    

with open('toy.mac', 'r') as file:
    data = file.readlines()
    #print data

data[300] = f'/gun/turtlefilename /home/had/lrussell/laserionization_highstat/result/{args.fin}\n'

data[305] = f'/run/beamOn {n_lim}\n'



with open(f'{runID}.mac', 'w') as file:
    file.writelines(data)


print(f"Saved macro {str(runID)}.mac for run ID: {str(runID)}")
