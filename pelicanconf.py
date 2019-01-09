#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web
SITEURL = 'http://www.seacoahuila.org.mx/directorio'
SITENAME = 'Directorio SEA'
SITEDESCRIPTION = 'En este micrositio web se publica información sobre los Sistemas Estatales Anticorrupción de México.'

# Autor
AUTHOR = 'SEA Coahuila'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['cpc', 'se']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = ['favicon.ico', 'cpc', 'se']

# Los artículos van en directorios por categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Tema
THEME = "themes/bootstrap-4"

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Para desarrollo, los vinculos son relativos
RELATIVE_URLS = True

# Para desarrollo, se desactiva la paginacion
DEFAULT_PAGINATION = False

# Para desarrollo, se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Para desarrollo, recomendado mantener en falso
DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = True
OUTPUT_RETENTION = ['.git', '.gitignore']
USE_REMOTE_SERVICES = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
