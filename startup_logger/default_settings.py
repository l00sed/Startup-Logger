import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ADDITIONAL_APPS = [
    'ideas',
    'livereload',
]
ADDITIONAL_MIDDLEWARE = [
    'livereload.middleware.LiveReloadScript',
]
TEMPLATE_BASE = [
    os.path.join(BASE_DIR, 'templates'),
]
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
