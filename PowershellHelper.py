Win_IP = ' 1.1.1.1 '

powershell_dict = {'$cred': "$username = 'user';"
                            "$password = '123456;"
                            "$pass = ConvertTo-SecureString -AsPlainText $password -Force;"
                            "$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $username, $pass;",

                   'Enter-PSSesion': "Enter-PSSession 1.1.1.1 -Credential $cred;",
                   'Remove-Variable': "Remove-Variable * -ErrorAction SilentlyContinue;",
                   'Get-ComputerInfo': "Invoke-Command -computername " + Win_IP + " -Credential $cred "
                                       "-scriptblock {Get-ComputerInfo};",
                   'Restart-Computer': "Invoke-Command -computername " + Win_IP + " -Credential $cred "
                                       "-scriptblock {Restart-Computer -force};"}

def get_credentials():
    command = powershell_dict.get('$cred') + powershell_dict.get('Enter-PSSesion')

    print(command)
    # command = "$username = 'psuser';" \
    #           "$password = 'psuser';" \
    #           "$pass = ConvertTo-SecureString -AsPlainText $password -Force;" \
    #           "$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $username, $pass;"
    process = subprocess.Popen(["powershell.exe", str(command)], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    print (result.decode("866"))
    #return str(result)

def get_info():
    command = powershell_dict.get('$cred') + powershell_dict.get('Get-ComputerInfo')
    # print(command)
    process = subprocess.Popen(["powershell.exe", str(command)], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    print (result.decode("866"))


def restart_pc():
    command = powershell_dict.get('$cred') + powershell_dict.get('Restart-Computer')
    print(command)
    process = subprocess.Popen(["powershell.exe", str(command)], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    print (result.decode("866"))

def check_powershell():
    command = "Test-WsMan " + Win_IP
    print(command)
    process = subprocess.Popen(["powershell.exe", str(command)], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    print (result.decode("866"))
    if 'Microsoft' in result:
        print('Ok!')
    else:
        print ('Fail!')
