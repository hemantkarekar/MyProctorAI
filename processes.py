from flask import flash
import psutil

def check_and_alert_blacklisted_processes():
    while True:
        for proc in psutil.process_iter():
            try:
                blacklist = ["Teams", "Zoom"]
                procName = proc.name()
                flag = 0
                for i in blacklist:
                    if(i in procName):
                        flag = 1
                        break
                if(flag == 1):
                    return True
                else:
                    return False
            except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                pass