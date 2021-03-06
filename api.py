#!/usr/bin/python3
"""
API endpoints
"""
import os
from urllib.request import urlopen
from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import requests
import shutil
import urllib

app = Flask(__name__)
api = Api(app)
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp', 'jfif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadImage(Resource):
    #Upload image files to server
    def get(self):
        return {'Welcome': 'car_detector'}

    def post(self):
        if request.method == 'POST':
            file = request.files['file']
        if 'file' not in request.files:
            return {'No':'File'}
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return {'File': 'uploaded success'}
        else:
            return {'Image types allowed':'png, jpg, jpeg, webp, jfif'}


class DownloadImage(Resource):
    #Download image via URL
    def post(self, img_url, imagefile):
        pass

class addID(Resource):
    #add uuid4 to files
    def get(self):
        pass

class Predict(Resource):
    #Give predictions from db by id
    def get(self):
        pass

api.add_resource(UploadImage, '/upload', endpoint='upload image file')
api.add_resource(DownloadImage, '/download', endpoint='download image from URL into a file')
api.add_resource(addID, '/uploads/<int:id>', endpoint='add uuid4 to img files')
api.add_resource(Predict, '/predictions/<int:id>', endpoint='predictions')


if __name__ == "__main__":
    app.run(debug=True)
