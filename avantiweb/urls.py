"""avantiweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from blog.sitemaps import PostSitemap


sitemaps = {
	'post': PostSitemap,
}

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, 
    	name='django.contrib.sitemaps.views.sitemap'),
    url(_(r'^account/'), include('account.urls')),
    url(_(r'^account/'), include('account.urls', namespace='account', app_name='account')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(_(r'^images/'), include('images.urls', namespace='images')),
    url(_(r'^shop/'), include('shop.urls', namespace='shop')),
    url(_(r'^cart/'), include('cart.urls', namespace='cart')),
    url(_(r'^orders/'), include('orders.urls', namespace='orders')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(_(r'^payment/'), include('payment.urls', namespace='payment')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(_(r'^'), include('shop.urls', namespace='shop')),
    url(_(r'^course/'), include('courses.urls', namespace='courses')),
    url(r'^api/', include('courses.api.urls', namespace='api')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
