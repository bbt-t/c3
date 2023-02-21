import json
import logging
from functools import cache
from json import JSONDecodeError


def load_json_file(file_name: str) -> list[dict] | None:
    try:
        with open(file_name, "rb") as file:
            posts: list[dict] = json.load(file)
        return posts
    except FileNotFoundError:
        logging.critical(f"file {file_name} does not exist")
    except JSONDecodeError:
        logging.critical("failed to read file")


@cache
def get_posts_all() -> list[dict] | None:
    """
    Get all posts from a file.
    :return: data
    """
    result: list[dict] = load_json_file('data/posts.json')
    return result


@cache
def get_bookmarks() -> list[dict] | None:
    """
    Get all bookmarks from a file.
    :return: data
    """
    result: list[dict] = load_json_file('data/bookmarks.json')
    return result


@cache
def get_all_comments() -> list[dict] | None:
    """
    Get all comments from a file.
    :return: data
    """
    result: list[dict] = load_json_file('data/comments.json')
    return result


def get_posts_by_user(user_name: str) -> list:
    """
    Gets all posts by name.
    :param user_name: username to search for posts
    :return: data
    """
    posts: list[dict] = get_posts_all()

    if not (user_posts := [p for p in posts if p.get('poster_name') == user_name]):
        logging.info("user does not exist")

    return user_posts


def get_comments_by_post_id(post_id: int) -> list | None:
    """
    Gets post comments.
    :param post_id: post id
    :return: data
    """
    posts = get_posts_all()

    for post in posts:
        if post.get('pk') == post_id:
            break
    else:
        logging.info("Такого поста не существует")
        return None

    comments: list[dict] = load_json_file('data/comments.json')
    comments_by_post_id = [c for c in comments if c.get('post_id') == post_id]

    return comments_by_post_id


def search_for_posts(query: str) -> list:
    """возвращает список постов по ключевому слову"""
    posts: list[dict] = get_posts_all()
    return [p for p in posts if query.lower() in p.get('content').lower()]


def get_post_by_pk(pk: int) -> dict | None:
    """
    Gets one post by its id.
    :param pk: post id
    :return: data
    """
    posts: list[dict] = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post


def comments_count(post_data: list, comments_data: list) -> list:
    """
    Counts the number of likes.
    :param post_data: posts info
    :param comments_data: comments info
    :return:
    """
    result = []
    for post in post_data:
        for comment in comments_data:
            pk_temp = post.get('pk')
            if comment.get('post_id') == pk_temp:
                result.append(post['pk'])
            post['comments']: int = result.count(pk_temp)

    return result
