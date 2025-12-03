"""
Django settings for biocazadores project.
"""

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Carga variables de .env si existen (para local)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "fallback_secret_key")

# IMPORTANTE: En producción idealmente esto debe ser False, pero para debuguear déjalo en True por ahora
DEBUG = True

# 1. CORRECCIÓN: Unificamos los hosts permitidos
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "web-production-a5582.up.railway.app", "*"]

# 2. CORRECCIÓN CRÍTICA: Esto arregla la pantalla amarilla (Error 403)
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-a5582.up.railway.app'
]

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'core',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biocazadores.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'biocazadores.wsgi.application'
ASGI_APPLICATION = 'biocazadores.asgi.application'

# 3. CORRECCIÓN BASE DE DATOS: Híbrida (SQLite local / Postgres Railway)
DATABASES = {
    'default': dj_database_url.config(
        # Si no encuentra DATABASE_URL (ej. en local), usa db.sqlite3
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
   # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
   # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
   # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
   # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "core/static")
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'