from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Store(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to='stores/', blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True, help_text="URL of store logo image")
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def active_deals_count(self):
        return self.deals.filter(is_active=True, expiry_date__gte=timezone.now().date()).count()


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('shoes', 'Shoes'),
        ('mobiles', 'Mobiles'),
        ('home_appliances', 'Home Appliances'),
        ('beauty', 'Beauty & Personal Care'),
        ('sports', 'Sports & Fitness'),
        ('books', 'Books'),
        ('grocery', 'Grocery'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ]

    ICON_CHOICES = [
        ('bi-laptop', '💻 Electronics'),
        ('bi-bag', '👗 Fashion'),
        ('bi-boot', '👟 Shoes'),
        ('bi-phone', '📱 Mobiles'),
        ('bi-house', '🏠 Home Appliances'),
        ('bi-stars', '✨ Beauty'),
        ('bi-trophy', '🏆 Sports'),
        ('bi-book', '📚 Books'),
        ('bi-cart', '🛒 Grocery'),
        ('bi-airplane', '✈️ Travel'),
        ('bi-grid', '📦 Other'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='bi-grid')
    color = models.CharField(max_length=20, default='#6366f1', help_text="Hex color code e.g. #6366f1")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def active_deals_count(self):
        return self.deals.filter(is_active=True, expiry_date__gte=timezone.now().date()).count()


class Deal(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='deals/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="External image URL")
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.IntegerField(help_text="Discount percentage (auto-calculated if left 0)", default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='deals')
    affiliate_link = models.URLField(help_text="Affiliate URL to redirect user")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='deals')
    expiry_date = models.DateField(help_text="Deal expiry date")
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    is_popular = models.BooleanField(default=False, help_text="Show in popular section")
    click_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            counter = 1
            while Deal.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        # Auto-calculate discount
        if self.old_price and self.new_price and self.old_price > 0:
            self.discount_percent = int(((self.old_price - self.new_price) / self.old_price) * 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_expired(self):
        return self.expiry_date < timezone.now().date()

    def savings(self):
        return self.old_price - self.new_price

    def get_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return '/static/img/placeholder.png'


class DealClick(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='clicks')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    clicked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Click on {self.deal.title} at {self.clicked_at}"


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
