# INFOS
project = '{{cookiecutter.project}}'
version = '{{cookiecutter.version}}'
release = '{{cookiecutter.version}}'
author = '{{cookiecutter.author}}'
copyright = '{{cookiecutter.author}}'
# SOURCES
language = 'en'
master_doc = 'index'
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
# EXTENSIONS
extensions = []
templates_path = ['templates']
# HTML FILES
html_theme = 'alabaster'
html_static_path = ['static']
# LATEX FILES
latex_elements = {
    'pointsize': '11pt',
    'papersize': 'a4paper',
}
