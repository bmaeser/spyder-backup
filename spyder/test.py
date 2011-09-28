from backup import Backup, RemoteBackup

b = Backup()
b.add_target('some', 'asdf')
b.fetch()
b.check_config()
