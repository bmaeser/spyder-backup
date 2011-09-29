import logging
from errors import MissingParameterError

logging.basicConfig(format='%(levelname)s:%(message)s')

class Backup(object):
    
    def __init__(self, name="", config={}, targets={}, tempdir=""):
        self.name = name
        self.targets = targets
        self.config = config
        self.tempdir = tempdir
        
    def add_target(self, name, target):
        self.targets[name] = target
        
    def del_target(self, name):
        del self.targets[name]

    def compress(self):
        pass
        #todo
        
    def fetch(self):
        print "fetch"
        #todo!
        
    def push(self, target_name):
        print target_name
        #todo
    
    def push_all(self):
        for target in self.targets.keys():
            self.push(target)
        
    def check_config(self):

        check_ok = True

        if self.name == "":
            logging.warning('This backup has no name!')
            check_ok = False

        if len(self.targets) == 0:
            logging.warning('Backup %s has no targets specified', self.name)
            check_ok = False

        if len(self.config) == 0:
            logging.warning('Backup %s has no configuration specified',
                self.name)
            check_ok = False

        if self.tempdir=="":
            logging.warning('Backup %s has no temp directory specified',
                self.name)
            check_ok = False

        return check_ok

    def del_tempfile(self):
        pass
        #TODO
    
    def run(self):
        if not self.check_config():
            logging.error('Backup %s could not be started because of ' \
                'insufficient configuration', self.name)
            return False

        for n,t in self.targets.iteritems():
            if not t.check_config():
                logging.error('Target %s of Backup %s could not be started ' \
                    'because of insufficient configuration', n, self.name)
                return False

        if self.fetch():
            if self.push_all():
                return True
        return False

    
class RemoteBackup(Backup):
    
    def __init__(self, ssh_config={}, *args, **kwargs):
        self.ssh_config = ssh_config
        super(RemoteBackup, self).__init__(*args, **kwargs)
        
    def check_config(self):
        
        check_ok = super(RemoteBackup, self).check_config()

        for p in ['username', 'password', 'host', 'port', 'keyfile']:
        
            if p not in self.ssh_config:
                check_ok = False
                logging.warning('Backup %s has no %s specified', self.name, p)
        
        return check_ok
        
    
class FSBackup(Backup):
    
    def check_config(self):
        
        if 'path' not in self.config:
            return false
        
        returnsuper(Backup, self).check_config()

class PostgresBackup(Backup):
    pass

class MySQLBackup(Backup):
    pass
