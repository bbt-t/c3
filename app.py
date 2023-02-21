import os

from flask import Flask

from route.api import api_route
from route.main import main_route
from route.posts import post_route
from route.search import search_route
from route.users import users_route


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY=os.getenv('SECRET_KEY'),
)

for r in (main_route, search_route, users_route, post_route, api_route):
    app.register_blueprint(r)


if __name__ == "__main__":
    app.run()


