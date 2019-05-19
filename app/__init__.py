from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

#imports to now build functionality
from flask import request, jsonify, abort

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    #import the models
    from models.bucket import BucketList

    #get and create a bucketlist
    @app.route('/bucketlists/', methods=['POST', 'GET'])
    def bucketlists():
        if request.method == "POST":
            name = str(request.data.get('name', '')) # return empty by default
            if name:
                b_list = BucketList(name=name)
                b_list.save()

                #return the response
                response = jsonify({
                    'id': b_list.id,
                    'name': b_list.name,
                    'created_at': b_list.date_created,
                    'updated_at': b_list.date_modified
                })
                response.status_code = 201

                return response
        else:
            # GET request by default
            pass

    return app