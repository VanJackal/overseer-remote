#!/bin/python
import backupHandler as bh
import configHandler as ch
from flask import Flask, request

backupDir = ch.getBackupDir(2021041901)
sourceDirs = ch.getSourceDirs()
backupCmds = ch.getBackupCmds()

app = Flask(__name__)

bh.execBackup(backupDir, sourceDirs, backupCmds);

"""
TODO
 - Get/Set(PUT) Configs
 - start backup
 - get current disk usage
 - get backups dir size
 - purge old
 - sync backup folder (source -> destination)
"""

@app.route('/config', methods = ['PUT', 'GET'])
def config():
    if request.method == 'PUT':
        config = request.get_json()
        ch.setConfig(config)
        return {'success':True}
    elif request.method == 'GET':
        return ch.getConfig()
