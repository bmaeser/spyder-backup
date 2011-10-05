import logging

class Source(object):

	def __init__(self, tempdir, name, config):
        """ Constructor

        Arguments:
        name -- give this source a name. will be used to generate a proper filename
        tempdir -- the directory where we can store temporary data
        config -- a dictionary containing all needed data
        """

		self.temdir = tempdir
		self.name = name
		self.config = config

	def fetch():
        """ Fetches the data and stores the data in tempdir/filename.
        This function should be overwritten by the actual implementations.

        Returns True on success, False on failure.

        """

        return False

	def check_config():
		return True


	def _compress():
		return True

class RemoteSource(Source):

	def __init__(self):
		super(RemoteSource, self).__init__(*args, **kwargs)


class FSSource(Source):
	pass


class PostgreSQLSource(Source):
	pass

class MySQLSource(Source):
	pass