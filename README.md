# Instructions to Generate Monte Carlo

## LeptoQuark Analysis

Follow the guide [Generator file](https://github.com/CMSROMA/LQGen) to generate the Gen level files.

Once you have the Gen files, you can follow the [this guide](https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-production-private) and download the [github repository](https://gitlab.cern.ch/cms-exo-mci/EXO-MCsampleProductions).
Once you cloned the repository 

```
cd EXO-MCsampleProductions
python setup.py
```

**When you execute the setup.py command from the previous guide the default repository for MiniAODv1 and NanoAODv2 will be generated, to have the MiniAODv2 and NanoAODv9 follow this instruction**

```
cd FullSimulation/RunIISummer20UL18
scram project -n MiniAOD__CMSSW_10_6_20 CMSSW CMSSW_10_6_20
scram project -n NanoAODv9__CMSSW_10_6_20 CMSSW CMSSW_10_6_20
```

Follow the instruction on the guide to create a new csv file (there are also some csv example here). 
###### For SIM step
```
cp skeleton/submit_crab_SIM.py path_to/SIM__CMSSW_10_6_17_patch1/src/skeleton/submit_crab.py
```

**Then create a file with a list of all the root files in the repository create by the config_SIM.py step (one in the folder of every sample). The file list has to be REQUESTNAME.list, where REQUESTNAME is the name given before the comma in the .csv file. The file path in has to be:** ***root://xrootd-cms.infn.it///path_to_single_file***

### NanoAOD modification for LQ
To save the LQ particle in the NanoAOD files do
```
cd NanoAODv9__CMSSW_10_6_20/src
git cms-addpkg PhysicsTools/NanoAOD
cd this_repo
cp genparticles_cff.py path_to/NanoAODv9__CMSSW_10_6_20/src/PhysicsTools/NanoAOD/python/
cp common_cff.py path_to/NanoAODv9__CMSSW_10_6_20/src/PhysicsTools/NanoAOD/python/
cd path_to/NanoAODv9__CMSSW_10_6_20/src
cmsenv
scram b
```

### MiniAOD modification to store PPS info
To Save the PPS information in the MiniAOD
```
cd path_to/MiniAOD__CMSSW_10_6_20/src
git cms-addpkg Validation/CTPPS
cd this_repo
cp CTPPSDirectProtonSimulation.cc path_to/MiniAOD__CMSSW_10_6_20/src/Validation/CTPPS/plugins
cp ctppsDirectProtonSimulation_cfi.py path_to/MiniAOD__CMSSW_10_6_20/src/Validation/CTPPS/python
cp test_addbranches_cfg.py path_to/MiniAOD__CMSSW_10_6_20/src/
cd path_to/MiniAOD__CMSSW_10_6_20/src
cmsenv
scram b
```

modify the test_addbranches_cfg.py with the name of the file you want store the PPS info and then run
```
cmsRun test_addbranches_cfg.py
```

### NanoAOD modification to store PPS info
To store the PPS info in the NanoAOD files
```
cd path_to/NanoAODv9__CMSSW_10_6_20/src
cp nano_cff.py path_to/NanoAODv9__CMSSW_10_6_20/src/PhysicsTools/NanoAOD/python/
cmsenv
scram b
```






