from importlib.metadata import files
from pathlib import Path

BASE_DIR = Path(files).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HealthCheckQuiz', 
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

SECRET_KEY = 'your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'quiz.urls'