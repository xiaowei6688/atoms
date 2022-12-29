"""
Django settings for atom project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i+^fumml_w79npry4z9z98+w7&hz9%xxxd1(0wp)8totcj6g9n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'user_plate'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middleware.response_middleware.ResponseMiddleware'
]

ROOT_URLCONF = 'atom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'atom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "user_plate.AtomUser"
# 跨域设置
CORS_ORIGIN_ALLOW_ALL = True

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] '
                          '[%(levelname)s]- %(message)s'}
        },
        'filters': {
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/atom/all.log',  # 日志输出文件
                'maxBytes': 1024 * 1024 * 5,  # 文件大小
                'backupCount': 5,  # 备份份数
                'formatter': 'standard',  # 使用哪种formatters日志格式
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'request_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/atom/request.log',
                'maxBytes': 1024 * 1024 * 5,
                'backupCount': 5,
                'formatter': 'standard'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['default', 'console'],
                'level': 'INFO',
                'propagate': False
            },
            'django.request': {
                'handlers': ['request_handler'],
                'level': 'DEBUG',
                'propagate': False
            },
            'fucha_app': {
                'handlers': ['default', 'console'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }

else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] '
                          '[%(levelname)s]- %(message)s'}
        },
        'filters': {
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/atom/all.log',  # 日志输出文件
                'maxBytes': 1024 * 1024 * 5,  # 文件大小
                'backupCount': 5,  # 备份份数
                'formatter': 'standard',  # 使用哪种formatters日志格式
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'request_handler': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/atom/request.log',
                'maxBytes': 1024 * 1024 * 5,
                'backupCount': 5,
                'formatter': 'standard'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['default', 'console'],
                'level': 'INFO',
                'propagate': False
            },
            'django.request': {
                'handlers': ['request_handler'],
                'level': 'DEBUG',
                'propagate': False
            },
            'fucha_app': {
                'handlers': ['default', 'console'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    # TODO(Rey): 与response_middleware冲突, 暂时不用
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",

    # 登陆认证的全局配置
    "DEFAULT_AUTHENTICATION_CLASSES": ["utils.DRF.authentications.LoginAuth"],
}
