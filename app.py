from flask import Flask,jsonify
import pymysql
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import Users,UserRegistration,UserLogin
from resources.admin import AddVacantRoles

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['PREFERRED_URL_SCHEME']='https'
app.config['JWT_SECRET_KEY']='sportsresourceapikey'
api = Api(app)
jwt = JWTManager(app)

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401

api.add_resource(Users,'/user')
api.add_resource(UserRegistration,'/userreg')
api.add_resource(UserLogin,'/userlogin')
api.add_resource(AddVacantRoles,'/addvacantroles')


if __name__=='__main__':
    app.run(port="5000",debug=True)