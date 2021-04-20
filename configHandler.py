import yaml

with open("config.yaml",'r') as f:
    config = yaml.load(f, Loader = yaml.FullLoader)

def getSourceDirs():
    return config['sourceDirs']

def getBackupCmds():
    return config['backupCmds']

def getBackupDir(uid):
    backupParentDir = config['backupParentDir']
    return f"{backupParentDir}/{uid}/"

def getConfig():
    return config

def setConfig(newConfig):
    config = newConfig
    dump = yaml.dump(config)
    with open('config.yaml', 'w') as f:
        f.write(dump)
