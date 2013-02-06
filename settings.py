#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Phil Adams'
SITENAME = u'philadams.net'
SITEURL = 'http://philadams.net'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = '/Users/phil/Code/pelican-themes/seahorse'

# URIs
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
