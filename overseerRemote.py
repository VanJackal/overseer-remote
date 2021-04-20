#!/bin/python
import backupHandler as bh
import configHandler
from flask import Flask, request

ch = configHandler.ConfigHandler()

app = Flask(__name__)

"""
TODO
 x Get/Set(PUT) Configs
 x start backup
 x get current disk usage
 x get backups dir size
 x purge old
 x sync backup folder (source -> destination)
"""

@app.route('/config', methods = ['PUT', 'GET'])
def config():
    if request.method == 'PUT':
        config = request.get_json()
        ch.setConfig(config)
        return {'success':True}
    elif request.method == 'GET':
        return ch.getConfig()

@app.route('/backup/start', methods=['POST'])
def backupStart():
    data = request.get_json()
    bh.execBackup(ch.getBackupDir(data["uid"]), ch.getSourceDirs(), ch.getBackupCmds())
    return {'success':True}

@app.route('/backup/usage', methods=['GET'])
def getUsage():
    parentDir = ch.getBackupParent()
    return bh.getDiskUsage(parentDir)

@app.route('/backup/sync', methods=['POST'])
def syncBackups():
    data = request.get_json()
    bh.syncBackup(data['dest'], ch.getBackupParent())
    return {'success':True}
