import os
import sys

from django.conf import settings


_file_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_file_path, 'apps'))

settings.INSTALLED_APPS += (
    'south',
    'pagination',
    'photologue',
    # Project
    'photos',
    'common',
    'generic_views',
    'inventory',
    'assets',
    'dynamic_search',
    'movements',
    'main',
    'web_theme',
)

if getattr(settings, 'DJANGO_INVENTORY_IMPORTER_ACTIVE', False):
    settings.INSTALLED_APPS += (
        'importer',
    )

settings.PROJECT_TITLE = getattr(settings, 'PROJECT_TITLE', 'Django Inventory')
settings.PROJECT_NAME = getattr(settings, 'PROJECT_NAME', 'django_inventory')

settings.LANGUAGES = getattr(settings, 'LANGUAGES', tuple())
settings.LANGUAGES += (
    ('es', 'Spanish'),
    ('en', 'English'),
    ('ru', 'Russian'),
)

settings.MIDDLEWARE_CLASSES = getattr(settings, 'MIDDLEWARE_CLASSES', tuple())
settings.MIDDLEWARE_CLASSES += (
    'pagination.middleware.PaginationMiddleware',
    'common.middleware.login_required_middleware.LoginRequiredMiddleware',
)

settings.TEMPLATE_CONTEXT_PROCESSORS = getattr(settings, 'TEMPLATE_CONTEXT_PROCESSORS', tuple())
settings.TEMPLATE_CONTEXT_PROCESSORS += (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

settings.LOGIN_URL = getattr(settings, 'LOGIN_URL', '/common/login')

# -------- LoginRequiredMiddleware ----------
settings.LOGIN_EXEMPT_URLS = getattr(settings, 'LOGIN_EXEMPT_URLS', tuple())
settings.LOGIN_EXEMPT_URLS = (
    r'^favicon\.ico$',
    r'^about\.html$',
    r'^legal/',  # allow the entire /legal/* subsection
    r'^static/',

    r'^accounts/register/$',
    r'^accounts/register/complete/$',
    r'^accounts/register/closed/$',

    r'^accounts/activate/complete/',
    r'^accounts/activate/(?P<activation_key>\w+)/$',

    r'^password/reset/$',
    r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    r'^password/reset/complete/$',
    r'^password/reset/done/$',
)
# --------- Pagination ------------------
settings.PAGINATION_DEFAULT_PAGINATION = getattr(settings, 'PAGINATION_DEFAULT_PAGINATION', 10)
# --------- Web theme app ---------------
settings.WEB_THEME = getattr(settings, 'WEB_THEME', 'warehouse')
