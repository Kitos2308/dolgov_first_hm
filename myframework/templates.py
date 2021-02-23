
import os

from jinja2.enviroment import Environment
from jinja2 import FileSystemLoader

def render(template_name, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    tmpl = env.get_template(template_name)
    return tmpl.render(**kwargs)