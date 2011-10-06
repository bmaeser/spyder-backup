import logging
import os.path
from datetime import date

#logging.basicConfig(format='%(levelname)s:%(message)s')

class Source(object):

    def __init__(self, name="", config={}, tempdir="/tmp", filename=""):
        """ Constructor

        Arguments:
        name -- give this source a name. will be used to generate a proper
                filename and for logging
        tempdir -- the directory where we can store temporary data.
                defaults to "/tmp"
        filename -- the filename where the fetched data should be stored
                will be automatically created if no one is provided.
        config -- a dictionary containing all needed data for the source 
        """

        self.name = name
        self.tempdir = tempdir
        self.config = config

        # create a good filename: filename_YYYY-MM-DD.tar.gz
        if not filename == "":
            self.filename = filename
        else:
            self.filename = self.name+"_"+date.today().isoformat()+".tar.gz"



    def fetch(self):
        """ PLACEHOLDER
        Fetches the data and stores the data in tempdir/filename.
        This function should be overwritten by the actual implementations.

        Returns True on success, False on failure.
        """

        return False

    def get_filepath(self):
        return os.path.join(self.tempdir, self.filename)

    def check_config(self):
        """ Checks the if this Source is FORMAL ok.
        It will cry (log) a lot if some information is missing.

        Returns True if everthing seems to be ok.

        This function should be overwritten by the actual implementation.
        """

        check_ok = True

        if self.name == "":
            logging.warning('This Source has no name!')
            check_ok = False

        # if self.filename == "":
        #     logging.warning('Source %s has no filename!', self.name)
        #     check_ok = False

        if len(self.config) == 0:
            logging.warning('Source %s has no configuration specified',
                self.name)
            check_ok = False

        # if self.tempdir=="":
        #     logging.warning('Source %s has no temp directory specified',
        #         self.name)
        #     check_ok = False

        return check_ok

class RemoteSource(Source):

    def __init__(self, ssh_config={}, *args, **kwargs):
        """ Constructor

        Arguments:
        ssh_config -- a dictionary containing all needed data
        and everything needed by the superclass
        """
        self.ssh_config = ssh_config
        super(RemoteSource, self).__init__(*args, **kwargs)


class FSSource(Source):
    pass


class PostgreSQLSource(Source):
    pass

class MySQLSource(Source):
    pass
