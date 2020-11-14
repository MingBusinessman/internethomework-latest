from os import path as ospath

import ftplib

class FTPWalk:
    """
    This class is contain corresponding functions for traversing the FTP
    servers using BFS algorithm.
    """

    def __init__(self, connection):
        self.connection = connection

    def listdir(self, _path):
        """
        return files and directory names within a path (directory)
        """

        file_list, dirs, nondirs = [], [], []
        try:
            self.connection.cwd(_path)
        except Exception as exp:
            print ("the current path is : ", self.connection.pwd(), exp.__str__(),_path)
            return [], []
        else:
            self.connection.retrlines('LIST', lambda x: file_list.append(x.split()))
            for info in file_list:
                ls_type, name = info[0], info[-1]
                if ls_type.startswith('d'):
                    dirs.append(name)
                else:
                    nondirs.append(name)
            return dirs, nondirs

    def walk(self, path='/'):
        """
        Walk through FTP server's directory tree, based on a BFS algorithm.
        """
        dirs, nondirs = self.listdir(path)
        yield path, dirs, nondirs
        for name in dirs:
            path = ospath.join(path, name)
            yield from self.walk(path)
            # In python2 use:
            # for path, dirs, nondirs in self.walk(path):
            #     yield path, dirs, nondirs
            self.connection.cwd('..')
            path = ospath.dirname(path)

#连接ftp
x = 148


while x < 151:
    ip = '211.' + '71.' + '149.' + str(x)
    try:
        ftp = ftplib.FTP(ip)
        ftp.connect(ip, port=21)
        ftp.login('', '')
        print(ftp.welcome)
        x = x + 1

        fp = open("static/message.txt", 'w+', encoding='latin1')

        ftpwalk = FTPWalk(ftp)
        try:
            for i in ftpwalk.walk():
                print(i)
                res = str(i).encode('utf-8')
                res.decode('latin1')
                fp.write(res + '\n')
        except:
            print('OK!')
    except:
        x = x + 1
        print('Could not connect FTP server!')

