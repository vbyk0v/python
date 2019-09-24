import subprocess
import os


class RunCommand:

    def exec(self, command, output):
        result = subprocess.call(command,
                                shell=True,
                                stdout=subprocess.PIPE)
        result = result.stdout
        if output:
            if os.name == 'nt':
                result = str(result.decode("866"))
                print(result)
            else:
                result = str(result).encode('utf-8')
                print(result)
            return str(result)
        elif not output:
            pass



