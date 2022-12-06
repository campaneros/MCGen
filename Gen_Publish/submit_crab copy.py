from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "SingleLQ_umuLQumu_M3000_Lambda1p0_GEN_v2"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "Publish.py"
#config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 4

config.Data.userInputFiles = open('SingleLQ_umuLQumu_M3000_Lambda1p0_crab.list').readlines() 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputPrimaryDataset = "RunIISummer20UL18_SingleLQ_umuLQumu_M3000_Lambda1p0_POWHEG-HerwigV7"
#config.Data.outputDatasetTag = "###INPUTDATASETTAG###"
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_IT_Rome"
config.Site.whitelist = ["T2_IT_Rome"]
