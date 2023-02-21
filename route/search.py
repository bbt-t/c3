from flask import request, render_template, Blueprint

from utils import search_for_posts
search_route = Blueprint('search_route', __name__)


@search_route.route('/search/')
def search_page() -> str:
    s = str(request.args.get("s"))
    posts: list = search_for_posts(s)
    posts_len = len(posts)
    return render_template("search.html", posts=posts, s=s, posts_len=posts_len)
