import sys, getopt
import numpy as np;
import re
import glob, os

def findinFile(filename, str):
	mynum=0;
	with open(filename, "r") as ins:
		array = 0
		for line in ins:
			if str in line:
				mynum=([int(s) for s in line.split() if s.isdigit()])[0]
		ins.close()
	return mynum;


def PrefetcherACCCoverage(filename):
	L2keys=["system.cpu.l2cache.prefetcher.usefulP", "system.cpu.l2cache.prefetcher.num_hwpf_issued", "system.cpu.l2cache.demand_misses::total"]
	L3keys=["system.l3.prefetcher.usefulP", "system.l3.prefetcher.num_hwpf_issued",  "system.l3.demand_misses::total"]

	L2Prefertcher = np.zeros(3)
	L3Prefertcher = np.zeros(3)

	i=0
	for str in L3keys:
		L3Prefertcher[i]=(findinFile(filename, str))
		i=i+1
	i=0
	for str in L2keys:
		L2Prefertcher[i]=(findinFile(filename, str))
		i=i+1	

	#print ("L2 ", L2Prefertcher[0]/L2Prefertcher[1], L2Prefertcher[0]/(L2Prefertcher[2]+L2Prefertcher[0]))
	#print ("L3 ", L3Prefertcher[0]/L3Prefertcher[1], L3Prefertcher[0]/(L3Prefertcher[2]+L3Prefertcher[0]))

	print filename[:-4], L2Prefertcher[0]/L2Prefertcher[1], L2Prefertcher[0]/(L2Prefertcher[2]+L2Prefertcher[0]), L3Prefertcher[0]/L3Prefertcher[1], L3Prefertcher[0]/(L3Prefertcher[2]+L3Prefertcher[0])


def Cycle(file):
	c= findinFile(file, "system.switch_cpus.numCycles")
	print file[:-4], c

def Misses(filename):
	ConfusionKeys=["system.cpu.dcache.ConfusionMatrix_0::0", "system.cpu.dcache.ConfusionMatrix_0::1", "system.cpu.dcache.ConfusionMatrix_0::2", "system.cpu.dcache.ConfusionMatrix_0::3", "system.cpu.dcache.ConfusionMatrix_1::0", "system.cpu.dcache.ConfusionMatrix_1::1", "system.cpu.dcache.ConfusionMatrix_1::2", "system.cpu.dcache.ConfusionMatrix_1::3", "system.cpu.dcache.ConfusionMatrix_2::0", "system.cpu.dcache.ConfusionMatrix_2::1", "system.cpu.dcache.ConfusionMatrix_2::2", "system.cpu.dcache.ConfusionMatrix_2::3", "system.cpu.dcache.ConfusionMatrix_3::0", "system.cpu.dcache.ConfusionMatrix_3::1", "system.cpu.dcache.ConfusionMatrix_3::2", "system.cpu.dcache.ConfusionMatrix_3::3"]
	LPSeq=["system.cpu.dcache.PacketCount::sequentioal", "system.cpu.dcache.PacketCount::LP"]
	Confusion = np.zeros((4,4))
	i=0
	j=0
	for str in ConfusionKeys:
		Confusion[i,j]=(findinFile(filename, str))
		j=j+1
		if(j==4):
			j=0
			i=i+1
	
	ActualNotL1=np.sum(Confusion[:,1:])
	PrednotL1=np.sum(Confusion[1:,1:])

	ActualNotL2=np.sum(Confusion[:,2:])
	PrednotL2=np.sum(Confusion[2:,2:])
	
	ActualNotL3=np.sum(Confusion[:,3:])
	PrednotL3=np.sum(Confusion[3:,3:])

	Seq=findinFile(filename, LPSeq[0])
	Seq =Seq*1.0
	LP=findinFile(filename, LPSeq[1])
	print filename[:-4], PrednotL1/ActualNotL1, PrednotL2/ActualNotL2, PrednotL3/ActualNotL3, LP/Seq

	

	#print findinFile(file, "system.switch_cpus.numCycles")	

def main(argv):
	inputfile = ''
	outputfile = ''
	os.chdir(".")
	try:
		opts, args = getopt.getopt(argv,"hcpm",["help=", "cycles=","prefetcher=", "-misses"])
	except getopt.GetoptError:
		print 'test.py -h <help> -c <cycles> -p <prefetcher> -m <misses>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		if opt in ("-c", "--cycles"):
			print "Applications Cycles"
			for file in glob.glob("*.txt"):	
				Cycle(file)
		if opt in ("-p", "--prefetcher"):
			print "Applications L2Accuracy L2Coverage L3Accuracy L3Coverage"
			for file in glob.glob("*.txt"):
				PrefetcherACCCoverage(file)
		if opt in ("-m", "--misses"):
			print "Applications L1MissPrediction L2MissPrediction L3MissPrediction PLInc"
			for file in glob.glob("*.txt"):
				Misses(file)		

   
   

if __name__ == "__main__":
   main(sys.argv[1:])



