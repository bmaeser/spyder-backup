from backup import Backup, RemoteBackup
from target import Target

b = RemoteBackup(name="testname")
b.tempdir = "some dir"
#ssh_conf = {
#	"username": "berni",
#	"password": "mypass",
#	"host": "localhost",
#	"port": 22,
#	"keyfile": "/home/berni/.ssh/idrsa.pub"
#}
#b.ssh_config = ssh_conf

target = Target()

b.add_target('eins', target)
#b.fetch()
b.check_config()
#b.push_all()
#print b.run()