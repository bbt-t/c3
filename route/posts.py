from flask import render_template, Blueprint

from utils import get_post_by_pk, get_comments_by_post_id

post_route = Blueprint('post_route', __name__)


@post_route.route('/post/<int:post_id>')
def page_posts(post_id) -> str:
    post, comments = get_post_by_pk(post_id), get_comments_by_post_id(post_id)
    comments_len: int = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)
