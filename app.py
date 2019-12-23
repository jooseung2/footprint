#!flask/bin/python
from flask import Flask, jsonify, abort, request
import json
import werkzeug
import os

app = Flask(__name__)

@app.route('/newJournal/<journal_id>', methods=['POST'])
def newJournal(journal_id):
    if request.method == 'POST':
        # curl -Ffile=@P1100939.jpg -Fdata="@newjournal.json" http://localhost:5000/newJournal/haha

        imagefile = request.files['file']
        print(request.files['file'])
        print(request.files['data'])

        hahah = json.loads(request.files['data'].read().decode('utf-8'))
        print(hahah)
        print(hahah['title'])

        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(filename)
        return "Image Uploaded successfully"



if __name__ == '__main__':
    app.run(debug=True)