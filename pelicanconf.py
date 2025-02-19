AUTHOR = 'Siméon'
SITETITLE = 'Poisson of Interest'
SITEURL = ""

PATH = "content"

STATIC_PATHS = ['images', 'extras']

THEME = 'themes/flex'

SITELOGO = "images/logo.jpg"

SITESUBTITLE = "Distributing Fascinating Fish"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

OUTPUT_PATH = 'docs'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

# Blogroll
'''LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)'''

# Social widget
SOCIAL = (
    #("You can add links in your config file", "#"),
    #("Another social link", "#"),
    ("twitter", "https://x.com/PoissonInterest"), 
)

COPYRIGHT_NAME = "Poisson of Interest. All rights reserved."
COPYRIGHT_YEAR = 2025

TWITTER_USERNAME = "PoissonInterest"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
