from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Deal, Store, Category, DealClick, Newsletter, ContactMessage


def get_active_deals():
    """Return queryset of non-expired active deals."""
    return Deal.objects.filter(
        is_active=True,
        expiry_date__gte=timezone.now().date()
    ).select_related('store', 'category')


def homepage(request):
    featured_deals = get_active_deals().filter(is_featured=True)[:8]
    popular_deals = get_active_deals().filter(is_popular=True)[:8]
    recent_deals = get_active_deals()[:12]
    stores = Store.objects.filter(is_active=True)[:8]
    categories = Category.objects.filter(is_active=True)

    # Hot deals (highest discount)
    hot_deals = get_active_deals().order_by('-discount_percent')[:6]

    context = {
        'featured_deals': featured_deals,
        'popular_deals': popular_deals,
        'recent_deals': recent_deals,
        'stores': stores,
        'categories': categories,
        'hot_deals': hot_deals,
    }
    return render(request, 'deals/home.html', context)


def all_deals(request):
    deals = get_active_deals()

    # Filtering
    category_slug = request.GET.get('category')
    store_slug = request.GET.get('store')
    sort_by = request.GET.get('sort', 'newest')
    search_q = request.GET.get('q', '')

    if category_slug:
        deals = deals.filter(category__slug=category_slug)
    if store_slug:
        deals = deals.filter(store__slug=store_slug)
    if search_q:
        deals = deals.filter(
            Q(title__icontains=search_q) |
            Q(description__icontains=search_q) |
            Q(store__name__icontains=search_q) |
            Q(category__name__icontains=search_q)
        )

    # Sorting
    sort_options = {
        'newest': '-created_at',
        'discount_high': '-discount_percent',
        'discount_low': 'discount_percent',
        'price_low': 'new_price',
        'price_high': '-new_price',
        'popular': '-click_count',
    }
    deals = deals.order_by(sort_options.get(sort_by, '-created_at'))


    paginator = Paginator(deals, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': Category.objects.filter(is_active=True),
        'stores': Store.objects.filter(is_active=True),
        'current_category': category_slug,
        'current_store': store_slug,
        'current_sort': sort_by,
        'search_q': search_q,
        'total_deals': deals.count(),
    }
    return render(request, 'deals/all_deals.html', context)


def deal_detail(request, slug):
    deal = get_object_or_404(Deal, slug=slug, is_active=True)
    related_deals = get_active_deals().filter(
        category=deal.category
    ).exclude(pk=deal.pk)[:4]

    context = {
        'deal': deal,
        'related_deals': related_deals,
    }
    return render(request, 'deals/deal_detail.html', context)


def category_deals(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    deals = get_active_deals().filter(category=category)

    sort_by = request.GET.get('sort', 'newest')
    sort_options = {
        'newest': '-created_at',
        'discount_high': '-discount_percent',
        'discount_low': 'discount_percent',
        'price_low': 'new_price',
        'price_high': '-new_price',
    }
    deals = deals.order_by(sort_options.get(sort_by, '-created_at'))

    paginator = Paginator(deals, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'category': category,
        'page_obj': page_obj,
        'current_sort': sort_by,
        'categories': Category.objects.filter(is_active=True),
        'total_deals': deals.count(),
    }
    return render(request, 'deals/category_deals.html', context)


def store_deals(request, slug):
    store = get_object_or_404(Store, slug=slug, is_active=True)
    deals = get_active_deals().filter(store=store)

    sort_by = request.GET.get('sort', 'newest')
    sort_options = {
        'newest': '-created_at',
        'discount_high': '-discount_percent',
        'discount_low': 'discount_percent',
        'price_low': 'new_price',
        'price_high': '-new_price',
    }
    deals = deals.order_by(sort_options.get(sort_by, '-created_at'))

    paginator = Paginator(deals, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'store': store,
        'page_obj': page_obj,
        'current_sort': sort_by,
        'stores': Store.objects.filter(is_active=True),
        'total_deals': deals.count(),
    }
    return render(request, 'deals/store_deals.html', context)


def all_stores(request):
    stores = Store.objects.filter(is_active=True)
    context = {'stores': stores}
    return render(request, 'deals/stores.html', context)


def search(request):
    q = request.GET.get('q', '').strip()
    deals = []
    if q:
        deals = get_active_deals().filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(store__name__icontains=q) |
            Q(category__name__icontains=q)
        )
    paginator = Paginator(deals, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'page_obj': page_obj,
        'search_q': q,
        'total_results': deals.count() if q else 0,
    }
    return render(request, 'deals/search.html', context)


def track_click(request, deal_id):
    """Track affiliate link clicks and redirect."""
    deal = get_object_or_404(Deal, pk=deal_id, is_active=True)
    # Track click
    ip = request.META.get('REMOTE_ADDR')
    ua = request.META.get('HTTP_USER_AGENT', '')
    DealClick.objects.create(deal=deal, ip_address=ip, user_agent=ua)
    deal.click_count += 1
    deal.save(update_fields=['click_count'])
    return render(request, 'deals/redirect.html', {'deal': deal})


def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            obj, created = Newsletter.objects.get_or_create(email=email)
            if created:
                messages.success(request, "🎉 You've subscribed successfully! Get the best deals in your inbox.")
            else:
                messages.info(request, "You're already subscribed. Thank you!")
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect(request.META.get('HTTP_REFERER', '/'))


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "✅ Thank you for contacting us! We'll get back to you within 24 hours.")
        return redirect('contact')
    return render(request, 'deals/contact.html')


def about(request):
    return render(request, 'deals/about.html')


def privacy_policy(request):
    return render(request, 'deals/privacy_policy.html')


def terms(request):
    return render(request, 'deals/terms.html')


def affiliate_disclaimer(request):
    return render(request, 'deals/affiliate_disclaimer.html')
