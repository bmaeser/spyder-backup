import logging
from errors import MissingParameterError

class Target(object):
    
    def __init__(self, config={}):
        self.config = config
        
        
    def check_config(self):
        return False
        #todo!

class FTPTarget(Target):
	pass

class FSTarget(Target):
	pass

class SSHTarget(Target):
	pass

class S3Target(Target):
	pass

