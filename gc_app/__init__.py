from flask import Flask


def create_app(config):
    return Flask(__name__)
