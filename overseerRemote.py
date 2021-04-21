#!/bin/python
import backupHandler as bh
import configHandler
from flask import Flask, request

ch = configHandler.ConfigHandler()

app = Flask(__name__)

@app.route('/config', methods = ['PUT', 'GET'])
def config():
    """
    sets or gets the config of the remote
    """
    if request.method == 'PUT':
        config = request.get_json()
        ch.setConfig(config)
        return {'success':True}
    elif request.method == 'GET':
        return ch.getConfig()

@app.route('/backup/start', methods=['POST'])
def backupStart():
    """
    starts a backup, takes in a uid of the backup to be created
    """
    data = request.get_json()
    bh.execBackup(ch.getBackupDir(data["uid"]), ch.getSourceDirs(), ch.getBackupCmds())
    return {'success':True}

@app.route('/backup/usage', methods=['GET'])
def getUsage():
    """
    get current disk usage statistics
    """
    parentDir = ch.getBackupParent()
    return bh.getDiskUsage(parentDir)

@app.route('/backup/sync', methods=['POST'])
def syncBackups():
    """
    sync backup parent dir to the given host/dir
    """
    data = request.get_json()
    bh.syncBackup(data['dest'], ch.getBackupParent())
    return {'success':True}

@app.route('/backup/purge', methods=['POST'])
def purge():
    """
    purges backups older than a given date (YYYYMMDD)
    """
    data = request.get_json()
    bh.purgeOld(data['date'],ch.getBackupParent())
    return {'success':True}
