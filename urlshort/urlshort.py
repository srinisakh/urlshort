from flask import (
    Flask, abort, request, jsonify, url_for,
    render_template, redirect
)
from utils import hash_utils as hu
import models

app = Flask(__name__)


def get_id_from_db(long_url):
    lu = models.LongUrl(long_url)
    models.db.session.add(lu)
    models.db.session.commit()
    return lu.id


def get_url_from_db(id):
    lu = models.LongUrl.query.get(id)
    return lu.long_url


@app.route('/shorten', methods=['GET', 'POST'])
def shorten_url():
    long_url = request.args.get("long_url")
    id = get_id_from_db(long_url)

    vals = dict(long_url=long_url,
                short_url=url_for(".navigate_to",
                                  code=hu.shorturl_from_id(id),
                                  _external=True))
    if "is_form" in request.args:
        return render_template("index.html", **vals)

    return jsonify(**vals)


@app.route('/<code>', methods=['GET'])
def navigate_to(code):
    id = hu.shorturl_to_id(code)
    long_url = get_url_from_db(id)
    return redirect(long_url)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


def create_app():
    models.db.init_app(app)
    app.config.from_pyfile("urlshort.cfg")
    return app
