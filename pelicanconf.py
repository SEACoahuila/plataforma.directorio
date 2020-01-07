#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web
SITENAME = 'Directorio de Sistemas Estatales Anticorrupción'
SITEURL = 'https://www.seacoahuila.org.mx/directorio'
SITEDESCRIPTION = 'En este micrositio web se publica información sobre los Sistemas Estatales Anticorrupción de México.'

# Autor
AUTHOR = 'SEA Coahuila'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['cpc', 'se']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = ['favicon.ico', 'cpc', 'se', 'robots.txt']

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

# Para desarrollo, NO hay cargas desde Internet
USE_REMOTE_SERVICES = False

# Para desarrollo, NO borrar todo output
DELETE_OUTPUT_DIRECTORY = False

# No eliminar de output los siguientes directorios y archivos
OUTPUT_RETENTION = ['.git', '.gitignore']

# Siempre aprovechar lo que se tenga en caché
LOAD_CONTENT_CACHE = True

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
