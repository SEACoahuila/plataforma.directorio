#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Para publicar en la web, es una rama del dominio
SITEURL = 'http://www.seacoahuila.org.mx/directorio'

# Usar URLs absolutos, debe ser Falso
RELATIVE_URLS = False
