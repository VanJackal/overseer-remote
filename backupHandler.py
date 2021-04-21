import os
from shutil import copytree, disk_usage, rmtree
import subprocess
import re

def execBackup(backupDir, sourceDirs, backupCmds):
    """
    executes a backup of the source directories and run additional backup commands

    backupDir - full path to current backup directory
    sourceDirs - list of directories to be backed up
    backupCmds - list of addtional commands to be executed for backing up data
    """
    backupDirs(backupDir, sourceDirs)
    execBackupCmds(backupDir, backupCmds)

def backupDirs(backupDir, sourceDirs):
    """
    copies the backup source directories to the backup directory

    backupDir - full backup path
    sourceDirs - list of directories to back up
    """
    subprocess.run(f"mkdir -p {backupDir}".split(" "))
    for directory in sourceDirs:
        cmd = f"cp -r {directory} {backupDir}".split(" ")
        subprocess.run(cmd)

def execBackupCmds(backupDir, backupCmds):
    """
    runs the given backup commands, the commmands should all have a {backupDir} marker so the command will backup to the correct directory

    backupDir - full backup path
    backupCmds - list of commands to be executed
    """
    for cmd in backupCmds:
        cmd = cmd.format(backupDir = backupDir).split(" ")
        subprocess.run(cmd)

def getDiskUsage(backupParentDir):
    """
    returns the current disk usage and size of the backup directory in a dictionary

    backupParentDir - parent dir of all backups
    """
    usage = disk_usage(backupParentDir)._asdict()
    currentUsage = subprocess.run(['du', '-s', backupParentDir], stdout = subprocess.PIPE).stdout
    q = re.compile(r"(\d+)(?:.*$)")
    usage['backups'] = int(q.search(str(currentUsage)).group(1))
    return usage

def purgeOld(date,parentDir):
    """
    removes any backups older than a given date in the form YYYYMMDD

    date - int representation of a date in form YYYYMMDD
    parentDir - Backup Parent directory
    """
    files = os.listdir(parentDir)
    for file in files:
        try:
            if int(file[:-2]) < date:
                path = f"{parentDir}{file}"
                rmtree(path)
        except:
            pass

def syncBackup(dest, parentDir):
    """
    syncs the backup directory to a given destination

    dest - string destination using format -> user@host:directory
    parentDir - backup parent directory
    """
    subprocess.run(['rsync', '-r', parentDir, dest])
