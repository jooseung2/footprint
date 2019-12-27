#!flask/bin/python
from flask import Flask, jsonify, abort, request
import json
import werkzeug
import os
from PIL import Image

from constants import POST, BAD_REQUEST, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import s3

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/newJournal/<journal_id>", methods=[POST])
def newJournal(journal_id):
    # curl -Ffile=@P1100939.jpg -Fdata="@newjournal.json" http://localhost:5000/newJournal/haha
    if request.method == POST:
        if "file" not in request.files or "data" not in request.files:
            return abort(BAD_REQUEST, "Image or entries are not attached")

        imagefile = request.files["file"]
        try:
            entries = json.loads(request.files["data"].read().decode("utf-8"))
            if "title" not in entries:
                return abort(BAD_REQUEST, "missing a title")
            if "text" not in entries:
                return abort(BAD_REQUEST, "missing a text")
            if "lon" not in entries or "lat" not in entries:
                return abort(BAD_REQUEST, "missing a location information")
            if "time" not in entries:
                return abort(BAD_REQUEST, "missing time value")

        except json.JSONDecodeError:
            return abort(BAD_REQUEST, "Invalid entries format")

        if imagefile and allowed_file(imagefile.filename):
            image = Image.open(imagefile)
            image.show()

            filename = werkzeug.utils.secure_filename(imagefile.filename)
            imagefile.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "Image Uploaded successfully\n"

        return "why are you here"

    else:
        return "haha"


if __name__ == "__main__":
    app.run(debug=True)
