#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SEA Coahuila'
SITENAME = 'Sitios Web SEA y CPC'
SITEURL = ''

PATH = 'content'

#Directorios que tienen los articulos
ARTICLE_PATHS = ['cpc', 'se']

TIMEZONE = 'America/Mexico_City'


THEME = "themes/blue-penguin-2"


DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Los articulos van en directorios categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

#Borra toda la salida
#Borra directorios ocultos en output como .git, mantenga en falso
DELETE_OUTPUT_DIRECTORY= False

# Para desarrollo se recomienda usar URLs relativos, debe ser Verdadero
RELATIVE_URLS = True
