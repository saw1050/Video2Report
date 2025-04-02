class BaseConfig:
    HOSTNAME = '0.0.0.0'
    PORT = '5000'
    DEVICES = [0]
    MODEL = 'base'
    DATA_DUMP_PATH = './temp'
    DB = 'V2R'
    DB_USER = 'root'
    DB_PWD = 'saw_2022'
    DB_HOST = '172.17.0.2'
    DB_TABLE = 'users'
    SECRET_KEY = 'LIBigLO8l3Iop0'

    
    
class DebugConfig(BaseConfig):
    DEBUG = True
    # NUM_WORK = 1
    ROOT_USER = {'username':'admin', 'password':'77777778'}
    
class ReleasesConfig(BaseConfig):
    DEBUG = False
    # NUM_WORK = 2
    ROOT_USER = {'username':'admin', 'password':'77777778'}
    
config = {
    'default': BaseConfig,
    'current': ReleasesConfig
}