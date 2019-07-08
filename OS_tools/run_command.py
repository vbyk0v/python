import OS_tools.classes as classes


r = classes.RunCommand()


def check_python():
    result = r.exec(command='python -V', output=True)
    if 'ython' in result:
        print("Pyton installed")
        return True
    else:
        print('Python not installed')
        return False

def check_python_module(module = ''):
    result = r.exec(command='pip3 list', output=True)
    if str(module) in result:
        print(module + " installed")
        return True
    else:
        print(module + ' not installed')
        return False

def check_python_missing_modules(modules_list):
    result = r.exec(command='pip3 list', output=True)
    missing_modules = []
    installed_modules = []
    for module in range(0, len(modules_list)):
        if modules_list[module] in result:
            installed_modules.append(modules_list[module])
        else:
            missing_modules.append(modules_list[module])
    print('installed_modules:', installed_modules)
    print('missing_modules:', missing_modules)
    return missing_modules


def install_missing_modules():

    modules_to_install = check_python_missing_modules(modules_list=modules)

    for module in range (0, len(modules_to_install)):
        r.exec(command='pip3 install ' + str(modules_to_install[module]), output=True)

    check_python_missing_modules(modules_to_install)



modules = ['pip', 'six', 'rsa']

install_missing_modules()

#check_python()
#check_python_module(module='pip')