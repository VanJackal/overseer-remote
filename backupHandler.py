import os
from shutil import copytree, disk_usage, rmtree
import subprocess
import re

def execBackup(backupDir, sourceDirs, backupCmds):
    backupDirs(backupDir, sourceDirs)
    execBackupCmds(backupDir, backupCmds)

def backupDirs(backupDir, sourceDirs):
    for directory in sourceDirs:
        copytree(directory,backupDir,dirs_exist_ok=True)

def execBackupCmds(backupDir, backupCmds):
    for cmd in backupCmds:
        cmd = cmd.format(backupDir = backupDir).split(" ")
        subprocess.run(cmd)

def getDiskUsage(backupParentDir):
    usage = disk_usage(backupParentDir)._asdict()
    currentUsage = subprocess.run(['du', '-s', backupParentDir], capture_output = True).stdout
    q = re.compile(r"(\d+)(?:.*$)")
    usage['backups'] = int(q.search(str(currentUsage)).group(1))
    return usage

def purgeOld(date,parentDir):
    files = os.listdir(parentDir)
    for file in files:
        try:
            if int(file[:-2]) < date:
                path = f"{parentDir}{file}"
                rmtree(path)
        except:
            pass

def syncBackup(dest, parentDir):
    subprocess.run(['rsync', '-r', parentDir, dest])
