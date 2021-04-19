import os
from shutil import copytree
import subprocess

sourceDirs = [
        "/home/jackal/Projects/Overseer/sampleData/"
        ]
backupCmds = [
        "mongodump -o {backupDir}mongodump"
        ]

def execBackup(backupDir):
    backupDirs(backupDir)
    execBackupCmds(backupDir)

def backupDirs(backupDir):
    for directory in sourceDirs:
        copytree(directory,backupDir,dirs_exist_ok=True)

def execBackupCmds(backupDir):
    for cmd in backupCmds:
        cmd = cmd.format(backupDir = backupDir).split(" ")
        subprocess.run(cmd)
