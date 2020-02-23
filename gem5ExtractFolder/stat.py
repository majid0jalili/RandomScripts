import os
import re
import csv


def serachFileKeys(path, keys, name):
    foundVal = []
    for k in keys:
        foundVal.append(0)
        searchfile = open(path, "r")
        for line in searchfile:
            if k in line: 
                res = (line.split())
                foundVal[-1] = (int(res[1]))
                break
        searchfile.close()
    return foundVal

def serachFolderKeys(path, keys):
    foundVal = []
    entries = os.listdir(path)
    apps=["apps"]
    apps.extend(keys)
    writeToCSV(apps)
    for entry in entries:
        if( entry[-4:]==".txt"):
            result=[]
            path1 = path+"/"+entry
            result.append(entry[0:-4])
            result.extend(serachFileKeys(path1, keys, entry[0:-4]))
            print(result)
            writeToCSV(result)
    return foundVal              

def writeToCSV(result):
    with open("./m5out/output.csv", 'a') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(result)


myPath = "./m5out"
keys=["system.switch_cpus.numCycles", "system.switch_cpus.commit.loads",
      "system.cpu.dcache.overall_accesses::.switch_cpus.data", "system.cpu.dcache.demand_misses::.switch_cpus.data", 
      "system.cpu.l2cache.overall_accesses::.switch_cpus.data", "system.cpu.l2cache.demand_misses::.switch_cpus.data", 
      "system.l3.overall_accesses::.switch_cpus.data", "system.l3.demand_misses::.switch_cpus.data", 
      "system.l3.DataMeta::0", "system.l3.DataMeta::1", "system.l3.DataMeta::2", "system.l3.DataMeta::3",
      "system.l3.MetaReq_accesses::total", "system.l3.MetaReq_misses::total",
      "system.mem_ctrls1.num_reads::total", "system.mem_ctrls1.num_writes::total"


       ]


if os.path.exists("./m5out/output.csv"):
  os.remove("./m5out/output.csv")
else:
  print("The file does not exist")


l1 = serachFolderKeys('./m5out', keys)
#print(l1)
