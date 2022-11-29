from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "###REQUESTNAME###"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab.py"
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 4

#config.Data.inputDataset = "/RunIISummer20UL18_SingleLQ_ueLQue_M1000_Lambda1p0_POWHEG-HerwigV7/mcampana-crab_SingleLQ_ueLQue_M1000_Lambda1p0_GEN-e2c4cde2cf98d6ed3c1aae393da41da3/USER" 
#config.Data.userInputFiles=["/RunIISummer20UL18_SingleLQ_ueLQue_M1000_Lambda1p0_POWHEG-HerwigV7/mcampana-crab_SingleLQ_ueLQue_M1000_Lambda1p0_GEN-e2c4cde2cf98d6ed3c1aae393da41da3/USER"]
#config.Data.userInputFiles = open('SingleLQ_ueLQue_M1000_Lambda0p1_crab.list').readlines()
config.Data.userInputFiles = open('###REQUESTNAME###_crab.list').readlines()
config.Data.outputPrimaryDataset = "###INPUTDATASETTAG###_###REQUESTNAME###"
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputDatasetTag = "RunIISummer20UL18_SIM"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_IT_Rome"
config.Site.whitelist = ['T2_IT_Rome']
