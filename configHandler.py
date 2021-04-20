import yaml

class ConfigHandler:
    """
    object to handle persistant config throughout flask calls
    """
    def __init__(self):
        with open("config.yaml",'r') as f:
            self.config = yaml.load(f, Loader = yaml.FullLoader)

    def getSourceDirs(self):
        return self.config['sourceDirs']

    def getBackupCmds(self):
        return self.config['backupCmds']

    def getBackupDir(self,uid):
        """
        returns the full backup path given a uid (datecode) of the backup

        uid - int date code of form YYYYMMDD
        """
        backupParentDir = self.config['backupParentDir']
        sid = self.config['sid']
        return f"{backupParentDir}/{uid}/{sid}/"

    def getBackupParent(self):
        return self.config['backupParentDir']

    def getConfig(self):
        return self.config

    def setConfig(self, newConfig):
        """
        sets the config var and file to a given newConfig dict

        newConfig - dict of config variables
        """
        self.config = newConfig
        dump = yaml.dump(self.config)
        with open('config.yaml', 'w') as f:
            f.write(dump)
