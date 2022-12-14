from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "###REQUESTNAME###"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "Publish.py"
#config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 4

config.Data.userInputFiles = ###INPUTDATASET### 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputPrimaryDataset = "###OUTPUTPRIMARYDATASET###"
#config.Data.outputDatasetTag = "###INPUTDATASETTAG###"
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_IT_Rome"
config.Site.whitelist = ["T2_IT_Rome"]
