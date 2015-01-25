import subprocess
import os

AUTOTEST_ENVIRONMENT = '%CD%\\environment\\sdk\\platform-tools;%CD%\\environment\\sdk\\tools;%CD%\\environment\\nodejs;%CD%\\environment\\jdk\\bin'

os.system('setx -m JAVA_HOME %CD%\environment\jdk')
os.system('setx -m ANDROID_HOME %CD%\environment\sdk')
os.system('setx -m AUTOTEST_ENVIRONMENT ' + AUTOTEST_ENVIRONMENT)

result = subprocess.check_output('reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path', shell=True)
result = result[result.index('REG_EXPAND_SZ') + 13:].strip()
if '%AUTOTEST_ENVIRONMENT%' not in result:
    os.system('setx -m PATH ' + '\"'+ '%AUTOTEST_ENVIRONMENT%;' + result + '\"')

raw_input('...')

