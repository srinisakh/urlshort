from flask import (
    Flask, abort, request, jsonify, url_for,
    render_template, redirect
)
import validators

from utils import hash_utils as hu
import models

app = Flask(__name__)


def get_id_from_db(long_url):
    """
    Adds the id to the database and returns the id

    :param long_url: Adds the long url to the db and returns
    auto-incremented corresponding id
    :return: Id that is just committed to the db that corresponds
    to the long_url
    """
    lu = models.LongUrl(long_url)
    models.db.session.add(lu)
    models.db.session.commit()
    return lu.id


def get_url_from_db(id):
    """
    Returns URL previously associated with id

    :param id: previously stored id
    :return: URL that corresponds to the id requested
    """
    lu = models.LongUrl.query.get(id)
    return lu.long_url if lu else None


@app.route('/shorten', methods=['POST'])
def shorten_url():
    """
    API end-point for processing the URL shortening requests.

    :return: Returns either JSON or redirects to html page with
    result containing the shortened URL
    """
    long_url = request.args.get("long_url")
    try:
        if validators.url(long_url):
            id = get_id_from_db(long_url)

            vals = dict(long_url=long_url,
                        short_url=url_for(".navigate_to",
                                          code=hu.shorturl_from_id(id),
                                          _external=True))
            if request.accept_mimetypes.accept_html:
                return render_template("index.html", **vals)
            else:
                return jsonify(**vals)
        else:
            abort(400)
    except Exception:
        abort(400)


@app.route('/<code>', methods=['GET'])
def navigate_to(code):
    """
    Navigates to url from the short url code

    :param code: Encoded URL code
    :return: redirect to the URL
    """
    id = hu.shorturl_to_id(code)
    long_url = get_url_from_db(id)
    return redirect(long_url) if long_url else abort(404)


@app.route('/', methods=['GET'])
def index():
    """
    Home page

    :return: render the index page
    """
    return render_template("index.html")


def create_app(cfg_file=None):
    models.db.init_app(app)
    app.config.from_pyfile(cfg_file or "urlshort.cfg")
    return app
