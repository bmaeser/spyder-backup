import logging
from datetime import date




class Backup(object):

    def __init__(self, name, sources={}, targets={}, statusfile=None,
            logfile=None):
        self.name = name
        self.sources = sources
        self.targets = targets
        self.statusfile = statusfile
        self.logfile = logfile
        self.__fetched_files = []

        #if logfile provided, use logfile, print to stout if not
        if self.logfile is not None:
            logging.basicConfig(
                filename=self.logfile,
                format= "%(asctime)s [%(levelname)-8s] %(message)s")
        else:
            logging.basicConfig(format= "%(asctime)s [%(levelname)-8s] %(message)s")

    def fetch(self):
        for s,t in self.sources.iteritems():
            pass
            #TODO

    def push(self):
        for n,t in self.targets.iteritems():
            pass
            #TODO

    def check_configs(self):
        """ Checks the if all sources and targets are FORMAL ok.
        It will cry (log) a lot if some information is missing.

        Returns True if everthing seems to be ok.
        """

        check_ok = True

        #check all targets
        if len(self.targets) == 0:
            logging.warning('Backup %s has no targets specified', self.name)
            check_ok = False
        else:
            for n,t in self.targets.iteritems():
                if not t.check_config():
                    logging.error('Target %s of Backup %s could not be ' \
                        'started because of insufficient configuration', n,
                        self.name)
                    check_ok = False

        #check all sources
        if len(self.sources) == 0:
            logging.warning('Backup %s has no sources specified', self.name)
            check_ok = False
        else:
            for n,s in self.sources.iteritems():
                if not s.check_config():
                    logging.error('Source %s of Backup %s could not be ' \
                        'started because of insufficient configuration', n,
                        self.name)
                    check_ok = False
        return check_ok

    def __writestatus(self, statuscode):
        """ helper function to write a statuscode into the statusfile

        Arguments: 
        statuscode -- a String, representing the actuall status. one of:
            0 = everything ok
            1 = backup is in progress
            2 = something bad happend, backup failed!
        """
        if self.statusfile is not None:
            f = open(self.statusfile, 'w')
            f.write(statuscode)
            f.close()

    def run(self):
        """ Runs the backup.
        Actually this function does:
        1.) check if all sources seem to be sufficient configured
        2.) check if all targets seem to be sufficient configured 
        3.) try to fetch the data from the source
        4.) try to push the data to all targets
        
        Returns True if successfull, False if not.  
        """

        self.__writestatus('1')

        if not self.check_configs():
            logging.error('Backup %s could not be started because of ' \
                'insufficient configuration', self.name)
            self.__writestatus('2')
            return False
        
        if self.fetch():
            if self.push():
                self.__writestatus('0')
                return True


        self.__writestatus(2)
        return False

    def add_target(self, name, target):
        """ Ads a new target to the target dictionary

        Arguments:
        name -- the targets name
        target -- the actual target-object (Subclass of targets.Target)
        """
        self.targets[name] = target

    def del_target(self, name):
        """ Deletes a target from the target dictionary

        Arguments:
        name -- the targets name
        """
        del self.targets[name]

    def add_source(self, name, source):
        """ Ads a new source to the source dictionary

        Arguments:
        name -- the source's name
        target -- the actual source-object (Subclass of source.Source)
        """
        self.sources[name] = source

    def del_source(self, name):
        """ Deletes a target from the target dictionary

        Arguments:
        name -- the source's name
        """
        del self.sources[name]

    



class Backuppp(object):
    
    def __init__(self, name, config={}, targets={}, tempdir=""):
        """ Constructor

        Arguments:
        name -- the name (identifier) of this backup
        config -- a dictionary containing all needed data
        targets -- a dictionary containing all targets
        tempdir -- the directory where we can store temporary data
        """

        self.name = name
        self.targets = targets
        self.config = config
        self.tempdir = tempdir

        today = date.today()
        print self.name

        self.filename = "asdf"

        #self.filename = self.name + "_" + date.today().isoformat()
        
    def add_target(self, name, target):
        """ Ads a new target to the target dictionary

        Arguments:
        name -- the targets name
        target -- the actual target-object (Subclass of targets.Target)
        """

        self.targets[name] = target
        
    def del_target(self, name):
        """ Deletes a target from the target dictionary

        Arguments:
        name -- the targets name
        """
        del self.targets[name]

    def compress(self):
        """ Creates a tar.gz of the backupfile and deletes the original"""
        pass
        #todo
        
    def fetch(self):
        """ Performs the Backup and stores the data in tempdir/filename.
        This function should be overwritten by the actual implementations.

        Returns True on success, False on failure.

        """
        return False

        
    def push(self, target_name):
        """ Pushes the file (filename) to the named target.

        Arguments:
        target_name -- the name of the target to push to
        """
        print target_name
        #todo
    
    def push_all(self):
        """ Pushes the file (filename) to ALL targets in the target dictionary
        """
        for target in self.targets.keys():
            self.push(target)
        
    def check_config(self):
        """ Checks the if this Backup is FORMAL ok.
        It will cry (log) a lot if some information is missing.

        Returns True if everthing seems to be ok.

        This function should be overwritten by the actual implementation.
        """

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
        """ Deletes the temporary file in tempdir/filename"""
        pass
        #TODO
    
    def run(self):
        """ Runs the backup.
        Actually this function does:
        1.) check if the backup seems to be sufficient configured
        2.) check if all targets seem to be sufficient configured 
        3.) try to fetch the data from the source
        4.) try to push the data to all targets
        
        Returns True if successfull, False if not.  
        """
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
        """ Constructor

        Arguments:
        ssh_config -- a dictionary containing all needed data
        and everything needed by the superclass
        """
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
