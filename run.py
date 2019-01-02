from flask import Flask
from flask_restful import Resource, Api
import psycopg2

app = Flask(__name__)
api = Api(app)

# from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# DB_HOST = os.environ.get('DB_HOST')
# DB_NAME = os.environ.get('DB_NAME')
# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')

# connection = psycopg2.connect('host=' + DB_HOST + ' port=5432 dbname=' + DB_NAME ' user=' + DB_USER ' password=' + DB_PASSWORD)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')