from flask import Flask, request, render_template, jsonify
import boto3
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# S3 Client
s3_client = boto3.client(
    's3',
    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    region_name=app.config['AWS_REGION']
)

# File size limit (5MB)
MAX_FILE_SIZE = 5 * 1024 * 1024

def allowed_file_size(filesize):
    return int(filesize) <= MAX_FILE_SIZE

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file_size(request.content_length):
        return jsonify({'error': 'File exceeds 5MB limit'}), 400
    
    try:
        # Upload the file to S3
        s3_client.upload_fileobj(
            file,
            app.config['AWS_S3_BUCKET'],
            file.filename,
            ExtraArgs={"ACL": "public-read"}  # Make file publicly readable
        )
        return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
