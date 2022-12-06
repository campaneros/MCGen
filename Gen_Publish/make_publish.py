#! /usr/bin/env python

import os
import sys
import optparse
import datetime
import subprocess
import io
import fnmatch
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input_f")
parser.add_argument("--dev", action = "store_true")
input_f = parser.parse_args().input_f
inputname = input_f.split(".")[0]


submit_list = []

listfile = open(input_f,'r')

list_ls = listfile.readlines()
listfile.close()

patter="*.list"


submit_crab_sh=open("submit_crab.sh","w")
submit_crab_sh.write("#!/bin/bash\n")
submit_crab_sh.write("source /cvmfs/cms.cern.ch/cmsset_default.sh\n")
submit_crab_sh.write("cmsenv\n")


os.system('cmsenv')
os.system('export LHAPDF_DATA_PATH="/cvmfs/sft.cern.ch/lcg/external/lhapdfsets/current:/cvmfs/sft.cern.ch/lcg/releases/MCGenerators/lhapdf/6.3.0-3c8e0/x86_64-centos7-gcc8-opt/share/LHAPDF"')
os.system('export HERWIGPATH="../../../HerwigInstallation/share/Herwig"')


for list_l in list_ls:
  list_l = list_l.strip().replace(" ",",").replace("\t",",").split(",")
  if len(list_l) != 5:
    exit_argumenterr()
  process = list_l[0]
  inputs = list_l[1]
  output= list_l[2]
  script = list_l[3]
  nevents = list_l[4]
  print(nevents)


  

  
  command = "python make_GEN.py -i" +inputs+"/"+process+"/split/"+process+".list -o "+output+"/"+process+ " -s "+script+" -n "+nevents
  print (command)
  os.system(command)
  

  print ("mkdir -p "+process)
  os.system("mkdir -p "+process)
  list_old=open(output+"/"+process+"/"+process+".list",'r')
  print("opening "+output+"/"+process+"/"+process+".list")
  list_new=open(process+"/"+process+"_crab.list",'w+')
  list_root=list_old.readlines()
  for root_file in list_root:
	list_new.write("root://xrootd-cms.infn.it//"+root_file+"\n")
	print("root://xrootd-cms.infn.it//"+root_file) 
  os.system("cp skeleton/submit_crab.py "+process+"/submit_crab.py")
  os.system("cp skeleton/Publish.py "+process+"/Publish.py")
  os.system("sed -i 's|###REQUESTNAME###|"+process+"_GEN_v2|g' "+process+"/submit_crab.py")
 # os.system("sed -i 's|###INPUTDATASET###|open(\""+process+"_crab.list\").readlines()|g' "+process+"/submit_crab.py")
  f=open(process+"/submit_crab.py",'rt')
  data=f.read()
  data=data.replace("###INPUTDATASET###","open('"+process+"_crab.list').readlines()")
  f.close()
  f=open(process+"/submit_crab.py",'wt')
  f.write(data)
  f.close()
  os.system("sed -i 's|###OUTPUTPRIMARYDATASET###|RunIISummer20UL18_"+process+"_POWHEG-HerwigV7|g' "+process+"/submit_crab.py") 
  

  submit_crab_sh.write("cd "+process+"/\n")
  submit_crab_sh.write("crab submit -c submit_crab.py\n")
  submit_crab_sh.write("cd ../\n")

submit_crab_sh.close()
os.system("chmod +x submit_crab.sh")
#os.system("source submit_crab.sh")
 











