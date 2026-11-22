"""Mirrors Identity's settings/debug.py: same settings, different WSGI entry point."""
from config.settings import *  # noqa: F401,F403

WSGI_APPLICATION = "config.wsgi.application"
