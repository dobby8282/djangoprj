"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# 프로젝트 루트 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 시크릿 키.
SECRET_KEY = 'django-insecure--t0-qf*ukud$4t=qff=)l$&c=kfty_6m+-d!y*p-p%kd2bez0r'

# SECURITY WARNING: don't run with debug turned on in production!
# 
DEBUG = True

# 프로젝트 접근 가능한 호스트 설정
ALLOWED_HOSTS = []


# Application definition
# 설치된 어플리케이션 목록
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'iris',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # 보안관련
    'django.contrib.sessions.middleware.SessionMiddleware',     # 세션 관리
    'django.middleware.common.CommonMiddleware',                # 공통 미들웨어
    'django.middleware.csrf.CsrfViewMiddleware',                # CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 인증관리
    'django.contrib.messages.middleware.MessageMiddleware',     # 메시지
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # 클릭잭킹 방지 미들웨어
]

# URL 패턴 매핑
ROOT_URLCONF = 'config.urls'

# 템플릿 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   # 템플릿 엔진
        'DIRS': [],                           # 템플릿 디렉토리 설정
        'APP_DIRS': True,                     # 애플릿케이션 디렉토리에서 템플릿 찾도록 설정
        'OPTIONS': {                          # 템플릿 컨텍스트 프로세서 설정
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 웹서버게이트웨이인터페이스. WSGI 서버에게 애플리케이션을 지정하는 역할
WSGI_APPLICATION = 'config.wsgi.application'


# Database 설정
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
# 비밀번호 유효성 검사 설정
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# 국제화(i18n) 설정
LANGUAGE_CODE = 'en-us' # 언어 설정

TIME_ZONE = 'Asia/Seoul'       # 타임존

USE_I18N = True         # 국제화 사용 여부

USE_TZ = True           # 타임존 사용 여부


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# 정적 파일 설정 css, javascript, 이미지 등의 정적파일 관련
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

#  정수 기반의 자동 증가(primary key) 필드
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
