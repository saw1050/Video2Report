from app import app
from config import config

cfg = config['current']

if __name__ == '__main__':
    app.run(port=cfg.PORT, debug=cfg.DEBUG, threaded=True)
