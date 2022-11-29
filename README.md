# Instructions to Generate Monte Carlo

## LeptoQuark Analysis

Follow the guide [Generator file](https://github.com/CMSROMA/LQGen) to generate the Gen level files.

Once you have the Gen files, you can follow the [this guide](https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-production-private) and download the [github repository](https://gitlab.cern.ch/cms-exo-mci/EXO-MCsampleProductions).
Once you cloned the repository 

```
cd EXO-MCsampleProductions
python setup.py
```

*** When you execute the setup.py command from the previous guide the default repository for MiniAODv1 and NanoAODv2 will be generated, to have the MiniAODv2 and NanoAODv9 follow this instruction***

```
cd FullSimulation/RunIISummer20UL18
scram project -n MiniAOD__CMSSW_10_6_20 CMSSW CMSSW_10_6_20
scram project -n NanoAODv9__CMSSW_10_6_20 CMSSW CMSSW_10_6_20
```
