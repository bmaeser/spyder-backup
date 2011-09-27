from errors import MissingParameterError

class Backup(object):
    
    def __init__(self, config={}, targets={}, tempdir=""):
        self.targets = targets
        self.config = config
        self.tempdir = tempdir
        
    def add_target(self, name, target):
        self.targets[name] = target
        
    def del_target(self, name):
        del self.targets[name]
        
    def fetch(self):
        print "fetch"
        #todo!
        
    def push(self, target_name):
        print "push"
        #todo
    
    def push_all(self):
        print "push all"
        #todo
        
    def check_config(self):
        valid = True
        essential_
        
        print "check config"
        raise MissingParameterError('you did something very stupid')
        #todo
    
    def run(self):
        print "run"
        #todo
    
class RemoteBackup(Backup):
    
    def __init__(self, ssh_config={}):
        self.ssh_config = ssh_config
        super(RemoteBackup, self).__init__()
        
    def check_config(self):
        for p in ['username', 'password', 'host', 'port', 'keyfile']:
            if p not in self.ssh_config:
                return False
                break
        return super(RemoteBackup, self).check_config()
        
    
class FsBackup(Backup):
    
    pass