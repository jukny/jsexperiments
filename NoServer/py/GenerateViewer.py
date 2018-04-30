from .template import template
from os import mkdir, startfile
import os.path as op

def create_structure():
    if not op.exists('./images'):
        mkdir('./images')
    if not op.exists('/html'):
        mkdir('./html')
        mkdir('./html/css')
        mkdir('./html/js')

def setup_imagerepo(name):
    pass