# Django-etna-backend

A django AuthenticationBackend for ETNA APIs (@school) based on [etnawrapper](https://github.com/tbobm/etnawrapper).

## Usage

See [django: customizing backend](https://docs.djangoproject.com/en/dev/topics/auth/customizing/) for details.

```python
# in your app's settings.py
INSTALLED_APPS = [
    '...',
    'django_etna_backend',
]

AUTHENTICATION_BACKENDS = [
    '...',
    'django_etna_backend.auth.EtnaAuthBackend',
]
```

See [example project](./examples/test/) displaying a basic implementation of this authentication backend.

## Installation

```bash
pip install django_etna_backend
```
