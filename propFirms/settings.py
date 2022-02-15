import cloudinary
from pathlib import Path


API_Key = os.get.environ(PFIRM_CLOUDINARY_API_KEY)
API_Secret_key = so.get.environ(PFIRM_CLOUDINARY_SECRET_KEY)


cloudinary.config(cloud_name='pfirm',
                  api_key=API_Key,
                  api_secret=API_Secret_key,
                  api_proxy='http://proxy.server:3128',
                  secure = True
                  )


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = Path(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.get.environ(Propfirms_Secret_Key)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.propfirms.co.uk', 'propfirms.co.uk']

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',       # installed for SEO
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # local apps

    'company.apps.CompanyConfig',
    'users.apps.UsersConfig',
    'staffs.apps.StaffsConfig',
    'firms.apps.FirmsConfig',
    'competition.apps.CompetitionConfig',
    'brokers.apps.BrokersConfig',
    'analytics.apps.AnalyticsConfig',
    'updates.apps.UpdatesConfig',

    # third party apps

    'cloudinary',
    'crispy_forms',
    'ckeditor',
    'djmoney',
    'phonenumber_field',
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'propfirms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'propfirms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': hidden_username,
        'USER': hidden_user,
        'PASSWORD': 'hidden_password,
        'HOST': hidden_host,

        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = '/home/propfirms/propfirms/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/propfirms/propfirms/static'
STATIC_URL = '/static/'



CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
        'width': 1024,
        'height': 300,
    },
}


BOOTSTRAP4 = {
    'include_jquery': True,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'



AUTH_USER_MODEL = 'users.User'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

#stops Relaying disallowed as webmaster@localhost
DEFAULT_FROM_EMAIL = ''

"""
# Email is sent using the SMTP HOST and Port Specified here

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = admin_email
EMAIL_HOST_PASSWORD = HOST_PASSWORD
EMAIL_USE_TLS =  False
EMAIL_USE_SSL = True
EMAIL_PORT = 465

#stops Relaying disallowed as webmaster@localhost
DEFAULT_FROM_EMAIL = ''
"""

LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = '/'
