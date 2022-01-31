import GPS
import os

# Sets alire environment variables for GNAT studio
# Put this file under `.gnatstudio\plug-ins`
#
# see: https://docs.adacore.com/live/wave/gps/pdf/gps_ug/GPS.pdf
# and: https://github.com/valexey/gnatstudio_alire_integration/blob/master/alire.py

def load_env(_, gps_file):
    stream = os.popen('cd ' + gps_file.directory() + ' && alr printenv')
    output = stream.read()
    if "export ALIRE=" not in output:
        return
    
    print('Alire project found!')
    lines = output.splitlines()
    for line in lines:
        if "GPR_PROJECT_PATH" in line:
            res = line.split('=')[1].split('"')[1]
            print('GPR_PROJECT_PATH is: ' + res)
            GPS.setenv("GPR_PROJECT_PATH", res)
    
GPS.Hook("project_changing").add(load_env)
