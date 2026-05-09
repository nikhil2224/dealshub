from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('deals/', views.all_deals, name='all_deals'),
    path('deals/<slug:slug>/', views.deal_detail, name='deal_detail'),
    path('category/<slug:slug>/', views.category_deals, name='category_deals'),
    path('stores/', views.all_stores, name='all_stores'),
    path('store/<slug:slug>/', views.store_deals, name='store_deals'),
    path('search/', views.search, name='search'),
    path('go/<int:deal_id>/', views.track_click, name='track_click'),
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms, name='terms'),
    path('affiliate-disclaimer/', views.affiliate_disclaimer, name='affiliate_disclaimer'),
]
