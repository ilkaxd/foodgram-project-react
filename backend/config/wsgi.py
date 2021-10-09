import os
import sys

from django.core.wsgi import get_wsgi_application

from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTING_MODULE'))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, "..")))

application = get_wsgi_application()
