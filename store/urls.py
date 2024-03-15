from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _


urlpatterns = [

    path(_(''), views.home, name='home'),
    path(_('about/'), views.about, name='about'),
    path(_('product/<int:pk>/'), views.product, name='product'),
    path(_('category/<slug:category_slug>/'), views.category, name='category'),
    path(_('contact/'), views.ContactView.as_view(), name='contact-page'),
    path(_('thankyou/'), views.thankyou, name='thank-you'),
    path(_('sale/'), views.sale, name='sale'),
    path(_('search/results/'), views.search_results, name='search_results'),

]