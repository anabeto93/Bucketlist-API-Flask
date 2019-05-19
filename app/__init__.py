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
    @app.route('/bucketlists', methods=['POST', 'GET'])
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
            bucketlists = BucketList.get_all()

            results = []

            for bl in bucketlists:
                data = {
                    'id': bl.id,
                    'name': bl.name,
                    'created_at': bl.date_created,
                    'updated_at': bl.date_modified
                }

                results.append(data)
            
            response = jsonify(results)
            response.status_code = 200

            return response

    #GET bucketlist by id
    @app.route('/bucketlists/<int:id>', methods=['GET'])
    def get_bucketlist(id, **kwargs):
        bl = get_by_id(id)

        if bl == 404:
            abort(404)
        
        response = serialize_bucketlist(bl, 200)

        return response

    #Update a bucketlist
    @app.route('/bucketlists/<int:id>', methods=['PUT'])
    def update_bucketlist(id, **kwargs):
        bl = get_by_id(id)

        if bl == 404:
            abort(404)

        #get the name sent
        name = str(request.data.get('name', bl.name)) #maintain the current name
        bl.name = name
        bl.save()

        response = serialize_bucketlist(bl, 200)

        return response

    #DELETE a given bucketlist
    @app.route('/bucketlists/<int:id>', methods=['DELETE'])
    def delete_bucketlist(id, **kwargs):
        bl = get_by_id(id)

        if bl == 404:
            abort(404)

        #delete it 
        bl.delete()

        response = jsonify({
            'message': 'bucketlist with id {} deleted successfully'.format(bl.id)
            })
        response.status_code = 200

        return response
    
    def get_by_id(id):
        ''' Get a bucketlist given the id '''
        bl = BucketList.query.filter_by(id=id).first()

        if not bl:
            print('Bucketlist with id: {} not found'.format(id))
            return 404
        
        return bl

    def serialize_bucketlist(bucketlist, status_code):
        response = jsonify({
            'id': bucketlist.id,
            'name': bucketlist.name,
            'created_at': bucketlist.date_created,
            'updated_at': bucketlist.date_modified
        })

        response.status_code = status_code

        return response

    return app