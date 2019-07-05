from flask import render_template, request, Blueprint
from flaskblog.models import Post
import logging

main = Blueprint('main', __name__)

logger = logging.getLogger('flaskblog')

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    logger.info('Home page')
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    logger.info('About page')
    return render_template('about.html', title='About')