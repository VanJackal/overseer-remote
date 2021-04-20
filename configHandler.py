import yaml

class ConfigHandler:
    def __init__(self):
        with open("config.yaml",'r') as f:
            self.config = yaml.load(f, Loader = yaml.FullLoader)

    def getSourceDirs(self):
        return self.config['sourceDirs']

    def getBackupCmds(self):
        return self.config['backupCmds']

    def getBackupDir(self,uid):
        backupParentDir = self.config['backupParentDir']
        sid = self.config['sid']
        return f"{backupParentDir}/{uid}/{sid}/"

    def getBackupParent(self):
        return self.config['backupParentDir']

    def getConfig(self):
        return self.config

    def setConfig(self, newConfig):
        self.config = newConfig
        dump = yaml.dump(self.config)
        with open('config.yaml', 'w') as f:
            f.write(dump)
