#!/usr/bin/python3
""" __init__.py - storage"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
