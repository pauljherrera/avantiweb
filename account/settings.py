from django.conf import settings

settings.configure(EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend')