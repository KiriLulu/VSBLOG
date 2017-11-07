class Config(object):
	SECRET_KEY = 'KiriLulu19950928'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	
	@staticmethod
	def init_app(app):
		pass
	
class DevConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'stmp.qq.com'
	MAIL_USE_TLS = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1:3306/vsdb?charset=utf8'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	
class ProdConfig(Config):
	pass
	
class TestConfig(Config):
	pass 
	
