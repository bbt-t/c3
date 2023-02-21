from flask import render_template, Blueprint

from utils import get_posts_by_user

users_route = Blueprint('users_route', __name__)


@users_route.route('/users/<name>')
def user_page(name):
    user_posts = get_posts_by_user(name)
    user_name = user_posts[1]['poster_name']
    return render_template("user-feed.html", posts=user_posts, name=user_name)
