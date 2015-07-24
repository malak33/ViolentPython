#! python3
# sshlogin2.py - a program to automatically login to ssh, and run a command or two

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
    print('What is the host IPv4 address you want to connect to?')
    host = input()
    print('What is the user you would like to connect as?')
    user = input()
    print('What is the password of the use you are connecting as?')
    password = input()
    child = connect(user, host, password)
    print('What is the command that you would like to send to the remote machine?')
    commandsender = input()
    send_command(child, commandsender)

if __name__ == '__main__':
    main()