import os
import sys
import django
from datetime import date, timedelta

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealshub.settings')
django.setup()

from deals.models import Store, Category, Deal

print("Seeding database...")

# ── STORES ──
stores_data = [
    {"name": "Amazon", "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/320px-Amazon_logo.svg.png", "website": "https://www.amazon.in", "description": "India's largest online marketplace with millions of products."},
    {"name": "Flipkart", "logo_url": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Flipkart_Logo.svg/320px-Flipkart_Logo.svg.png", "website": "https://www.flipkart.com", "description": "One of India's leading e-commerce platforms."},
    {"name": "Myntra", "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Myntra_logo.svg/320px-Myntra_logo.svg.png", "website": "https://www.myntra.com", "description": "India's leading fashion e-commerce platform."},
    {"name": "Ajio", "logo_url": "https://logos-world.net/wp-content/uploads/2023/01/Ajio-Logo.png", "website": "https://www.ajio.com", "description": "Premium fashion and lifestyle brand by Reliance."},
    {"name": "Meesho", "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Meesho_Logo.svg/320px-Meesho_Logo.svg.png", "website": "https://www.meesho.com", "description": "Affordable fashion and products for every Indian home."},
    {"name": "Nykaa", "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Nykaa-logo.svg/320px-Nykaa-logo.svg.png", "website": "https://www.nykaa.com", "description": "India's #1 beauty and wellness destination."},
]

stores = {}
for s in stores_data:
    obj, _ = Store.objects.get_or_create(name=s["name"], defaults=s)
    stores[s["name"]] = obj
    print(f"  Store: {s['name']}")

# ── CATEGORIES ──
cats_data = [
    {"name": "Electronics", "icon": "bi-laptop", "color": "#3b82f6"},
    {"name": "Fashion", "icon": "bi-bag", "color": "#ec4899"},
    {"name": "Shoes", "icon": "bi-boot", "color": "#8b5cf6"},
    {"name": "Mobiles", "icon": "bi-phone", "color": "#f59e0b"},
    {"name": "Home Appliances", "icon": "bi-house", "color": "#10b981"},
    {"name": "Beauty", "icon": "bi-stars", "color": "#f43f5e"},
    {"name": "Sports", "icon": "bi-trophy", "color": "#06b6d4"},
    {"name": "Books", "icon": "bi-book", "color": "#84cc16"},
]

cats = {}
for c in cats_data:
    obj, _ = Category.objects.get_or_create(name=c["name"], defaults=c)
    cats[c["name"]] = obj
    print(f"  Category: {c['name']}")

# ── DEALS ──
future = date.today() + timedelta(days=30)
deals_data = [
    {
        "title": "Apple iPhone 15 (128GB) – Black",
        "description": "The iPhone 15 features a new 48MP camera, A16 Bionic chip, and a beautiful OLED Super Retina XDR display.",
        "image_url": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-finish-select-202309-6-1inch-black?wid=400&fmt=webp",
        "old_price": 79900, "new_price": 69900,
        "store": "Amazon", "category": "Mobiles", "affiliate_link": "https://www.amazon.in",
        "is_featured": True, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Samsung Galaxy S24 Ultra (256GB)",
        "description": "Stunning 200MP camera, built-in S Pen, and Snapdragon 8 Gen 3 chipset.",
        "image_url": "https://images.samsung.com/is/image/samsung/p6pim/in/2401/gallery/in-galaxy-s24-ultra-s928-sm-s928bztdins-thumb-539573052?$400_400_PNG$",
        "old_price": 129999, "new_price": 99999,
        "store": "Flipkart", "category": "Mobiles", "affiliate_link": "https://www.flipkart.com",
        "is_featured": True, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Dell Inspiron 15 Laptop (Intel i5, 16GB RAM, 512GB SSD)",
        "description": "Powerful performance for work and entertainment with a 15.6-inch FHD display.",
        "image_url": "https://m.media-amazon.com/images/I/71c5W9NxN5L._SX679_.jpg",
        "old_price": 65000, "new_price": 45000,
        "store": "Amazon", "category": "Electronics", "affiliate_link": "https://www.amazon.in",
        "is_featured": True, "is_popular": False, "expiry_date": future,
    },
    {
        "title": "boAt Airdopes 141 TWS Earbuds",
        "description": "42H total playback, IPX4 water resistance, and ENx Technology for clear calls.",
        "image_url": "https://m.media-amazon.com/images/I/61KNJav3S9L._SX679_.jpg",
        "old_price": 2999, "new_price": 1199,
        "store": "Amazon", "category": "Electronics", "affiliate_link": "https://www.amazon.in",
        "is_featured": False, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Nike Air Max 270 Running Shoes",
        "description": "Max Air unit in the heel for all-day comfort. Engineered mesh upper for breathability.",
        "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/1ee62aca-c4e9-4e50-a92e-360e6e902b78/air-max-270-mens-shoes-KkLcGR.png",
        "old_price": 12995, "new_price": 7999,
        "store": "Myntra", "category": "Shoes", "affiliate_link": "https://www.myntra.com",
        "is_featured": True, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Levi's Men's Slim Fit Jeans",
        "description": "Classic slim fit jeans in stretch denim for all-day comfort and style.",
        "image_url": "https://m.media-amazon.com/images/I/616xchp1ECL._SY879_.jpg",
        "old_price": 3499, "new_price": 1799,
        "store": "Myntra", "category": "Fashion", "affiliate_link": "https://www.myntra.com",
        "is_featured": False, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Samsung 55-inch 4K Ultra HD Smart TV",
        "description": "Crystal 4K processor, HDR, built-in Alexa, and slim bezels for cinematic viewing.",
        "image_url": "https://m.media-amazon.com/images/I/81TjRLHaz1L._SX679_.jpg",
        "old_price": 65990, "new_price": 44990,
        "store": "Flipkart", "category": "Home Appliances", "affiliate_link": "https://www.flipkart.com",
        "is_featured": True, "is_popular": False, "expiry_date": future,
    },
    {
        "title": "Lakme Absolute Matte Melt Mini Liquid Lip Color",
        "description": "Long-lasting matte finish with a lightweight, melt-on formula. 100% vegan.",
        "image_url": "https://m.media-amazon.com/images/I/51r+J6dO8QL._SY879_.jpg",
        "old_price": 699, "new_price": 349,
        "store": "Nykaa", "category": "Beauty", "affiliate_link": "https://www.nykaa.com",
        "is_featured": False, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Sony WH-1000XM5 Wireless Headphones",
        "description": "Industry-leading noise cancellation, 30-hour battery, and Hi-Res Audio support.",
        "image_url": "https://m.media-amazon.com/images/I/51aXvjzcukL._SX679_.jpg",
        "old_price": 29990, "new_price": 21990,
        "store": "Amazon", "category": "Electronics", "affiliate_link": "https://www.amazon.in",
        "is_featured": True, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "H&M Women's Floral Dress",
        "description": "Elegant floral print midi dress, perfect for summer outings and casual events.",
        "image_url": "https://m.media-amazon.com/images/I/61KxT3Y-JAL._SY879_.jpg",
        "old_price": 2999, "new_price": 1299,
        "store": "Ajio", "category": "Fashion", "affiliate_link": "https://www.ajio.com",
        "is_featured": False, "is_popular": True, "expiry_date": future,
    },
    {
        "title": "Adidas Ultraboost 22 Running Shoes",
        "description": "Boost midsole for incredible energy return. Primeknit+ upper for adaptive fit.",
        "image_url": "https://m.media-amazon.com/images/I/71D9ImsvEtL._SY695_.jpg",
        "old_price": 16999, "new_price": 9999,
        "store": "Myntra", "category": "Shoes", "affiliate_link": "https://www.myntra.com",
        "is_featured": True, "is_popular": False, "expiry_date": future,
    },
    {
        "title": "Atomic Habits by James Clear (Paperback)",
        "description": "The #1 New York Times bestseller. Tiny changes, remarkable results.",
        "image_url": "https://m.media-amazon.com/images/I/81bGKUa1e0L._SY466_.jpg",
        "old_price": 799, "new_price": 399,
        "store": "Amazon", "category": "Books", "affiliate_link": "https://www.amazon.in",
        "is_featured": False, "is_popular": True, "expiry_date": future,
    },
]

for d in deals_data:
    store = stores[d.pop("store")]
    cat = cats[d.pop("category")]
    title = d.pop("title")
    Deal.objects.update_or_create(title=title, defaults={"store": store, "category": cat, **d})
    print(f"  Deal: {title[:50]}")

try:
    print("\n✅ Database seeded successfully!")
except UnicodeEncodeError:
    print("\n[SUCCESS] Database seeded successfully!")
print("  Stores:", Store.objects.count())
print("  Categories:", Category.objects.count())
print("  Deals:", Deal.objects.count())
