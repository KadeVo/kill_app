import psutil
import time
import os
import signal



def monitor_applications():
  monitor_applications = ['ProtonVPN.exe']
  maxtime = 7200
  for x in psutil.process_iter(attrs=['pid', 'name', 'create_time']):
    try:
      if x.info['name'] in monitor_applications:
        runtime = time.time - x.info['create_time']
      
        if runtime >= maxtime:
          os.kill(x.info['pid'], signal.SIGKILL)
          print(f"Killed {x.info['name']} because it was alive for {runtime}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass
    
monitor_applications()
