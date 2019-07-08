import datetime

class Logger:

    INFO = 'INFO'
    DEBUG = 'DEBUG'
    ERROR = 'ERROR'
    FATAL = 'FATAL'

    def set_log_file(self, filename):
        self.filename = filename
        with open(self.filename, 'w') as file:
            file.write("==MegaLogger 3000==\n")

    def log(self, message, level):
        time = str(datetime.datetime.now())
        string = time + '|' + level + '|' + message
        with open(self.filename, 'a') as file:
            file.write('%s\n' % string)
        print(string)

if __name__ == '__main__':
    logger = Logger()
    logger.set_log_file("123")
    logger.log('Message', Logger.INFO)

    for i in range(10):
        try:
            a = '2'
            b = 2
            c = a + b
        except BaseException as err:
            logger.log(str(err), Logger.ERROR)
