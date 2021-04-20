import os
from shutil import copytree
import subprocess

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
