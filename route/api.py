from flask import jsonify, Blueprint, Response

from utils import get_posts_all, get_post_by_pk

api_route = Blueprint('api_route', __name__)


@api_route.route("/api/posts")
def get_posts_json_page() -> tuple | Response:
    data: list[dict] | None = get_posts_all()
    return jsonify(data)


@api_route.route("/api/posts/<int:post_id>")
def get_post_json_page(post_id) -> Response:
    post: dict | None = get_post_by_pk(post_id)
    return jsonify(post)
