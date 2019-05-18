import os

from app import create_app

config_name = os.getenv('APP_SETTINGS','development') #default to development
app = create_app(config_name)

if __name__ == '__main__':
    app.run()