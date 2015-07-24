#! python3
# sshlogin.py - a program to automatically login to ssh

import pexpect

PROMPT = ['# ', '>>> ', '> ", ', '\$ ']
def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey= 'Are you sure you want to continue connecting'
    ConnStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(ConnStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = '10.0.0.73'
    user = 'mnobile'
    password = 'Palmer33'
    child = connect(user, host, password)
    send_command(child, 'ls ~')

if __name__ == '__main__':
    main()
