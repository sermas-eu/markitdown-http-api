import logging
import json
import os
import io
import flask_cors
from flask import Flask, request, make_response
from werkzeug import exceptions
from waitress import serve
from markitdown_http_api import config
from markitdown import MarkItDown

config.load_env()

logger = logging.getLogger(__name__)
logger.info("Starting markitdown API")

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024 * 1024
flask_cors.CORS(app)

skip_llm = False if os.environ.get("OPENAI_API_KEY") else True


@app.before_request
def log_request_info():
    app.logger.info("%s %s", request.method, request.path)
    app.logger.debug("Headers: %s", request.path)


def _get_content_from_request():
    if "file" not in request.files:
        raise exceptions.BadRequest("No file attached")
    content = request.files["file"]
    if not content.filename:
        raise exceptions.BadRequest("No file selected")
    return content


@app.route("/status", methods=["GET"])
def hello_world():
    return {"status": "ok"}, 200


@app.errorhandler(404)
def page_not_found(e):
    app.logger.error("No handler found for %s", request.path)
    return {
        "error": True,
        "message": "Could not find a handler for " + request.path,
    }, 404


@app.route("/", methods=["POST"])
def markitdown():

    content = _get_content_from_request()

    md = MarkItDown()
    result = md.convert_stream(
        io.BytesIO(content.stream.read()), file_extension=".pdf", url=content.filename
    )

    response = make_response(result.text_content, 200)
    response.mimetype = "text/plain"

    return response


if __name__ == "__main__":
    serve(app, listen="*:5012")
