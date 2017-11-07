from vsblog import create_app
from vsblog import models
from vsblog.config import DevConfig

from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

app = create_app(DevConfig)
manager = Manager(app)
migrate = Migrate(app,models.db)

manager.add_command('server',Server(port=8010))
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
	return dict(app = app,
				db = models.db,
				User = models.User,
				Post = models.Post,
				Tag = models.Tag,
				Comment = models.Comment,
				Role = models.Role
				)

if __name__ == '__main__':
	manager.run()