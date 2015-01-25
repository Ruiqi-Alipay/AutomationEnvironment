import subprocess
import time
import sys

print 'Step 1: check and disconnect existing connection'
cmd = 'adb disconnect'
subprocess.check_output(cmd.split())

time.sleep(2.0)

print 'Step 2: restart adb in usb mode'
cmd = 'adb usb'
result = subprocess.check_output(cmd.split())
print result

time.sleep(5.0)

print 'Step 3: check devices'
cmd = 'adb devices'
result = subprocess.check_output(cmd.split())
print result

if result.index('device') <= 0:
    sys.exit()

print 'Step 4: get cellphone IP'
cmd = 'adb shell ifconfig wlan0'
result = subprocess.check_output(cmd.split())
start = result.index('ip') + 3
end = result.index(' mask')
ip_address = result[start:end]
print 'Cellphone running at: ' + ip_address

print 'Step 5: restart cellphone adb in tcp/ip mode'
cmd = 'adb tcpip 5555'
result = subprocess.check_output(cmd.split())
print result

time.sleep(5.0)

print 'Step 6: make TCP connection'
cmd = 'adb connect ' + ip_address
result = subprocess.check_output(cmd.split())
print result

time.sleep(5.0)

cmd = 'adb devices'
result = subprocess.check_output(cmd.split())
print result

raw_input('Now please remove the cable!')