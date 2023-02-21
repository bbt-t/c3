from flask import Blueprint, render_template
from utils import get_posts_all, get_all_comments, get_bookmarks, comments_count

main_route = Blueprint('main_route', __name__)


@main_route.route('/')
def page_index() -> str:
    posts, comment, bookmarks = get_posts_all(), get_all_comments(), get_bookmarks()

    comm_count: list[int] = comments_count(posts, comment)
    len_bookmarks: int = len(bookmarks)
    return render_template("index.html", posts=posts, coments=comm_count, len_bookmarks=len_bookmarks)
