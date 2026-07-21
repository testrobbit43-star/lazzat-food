from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

User = get_user_model()

# ============================================================================
# RESTAURANT MODELS
# ============================================================================

class Restaurant(models.Model):
    """
    Restaurant model - represents a restaurant/cafe.
    Owner field creates relationship with Restaurant Owner user.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='restaurants',
        limit_choices_to={'role': 'OWNER'},
        verbose_name=_('Restoran Egasi')
    )
    
    name = models.CharField(
        max_length=100,
        verbose_name=_('Restoran Nomi')
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name=_('URL Slug')
    )
    description_uz = models.TextField(
        verbose_name=_('Tavsif (Uzbek)')
    )
    description_ru = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Tavsif (Russian)')
    )
    description_en = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Tavsif (English)')
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_('Manzil')
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_('Telefon')
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_('Email')
    )
    image = models.ImageField(
        upload_to='restaurants/images/',
        blank=True,
        null=True,
        verbose_name=_('Rasm')
    )
    banner = models.ImageField(
        upload_to='restaurants/banners/',
        blank=True,
        null=True,
        verbose_name=_('Banner')
    )
    telegram_chat_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Telegram Chat ID'),
        help_text=_('Buyurtmalar uchun Telegram guruh/kanal ID-si')
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        verbose_name=_('Latitude')
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        verbose_name=_('Longitude')
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name=_('Reyting')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Faol')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Yangilandi')
    )

    class Meta:
        db_table = 'restaurant_restaurant'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['owner']),
            models.Index(fields=['is_active']),
        ]
        verbose_name = _('Restoran')
        verbose_name_plural = _('Restoranlar')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuCategory(models.Model):
    """
    Menu category for organizing menu items.
    Each restaurant has its own categories.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name=_('Restoran')
    )
    name_uz = models.CharField(
        max_length=100,
        verbose_name=_('Toifaning Nomi (Uzbek)')
    )
    name_ru = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Toifaning Nomi (Russian)')
    )
    name_en = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Toifaning Nomi (English)')
    )
    slug = models.SlugField(
        verbose_name=_('URL Slug')
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('Emoji yoki icon nomi (masalan: 🍕 yoki pizza)'),
        verbose_name=_('Icon')
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Tartibi')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )

    class Meta:
        db_table = 'restaurant_menucategory'
        ordering = ['order', '-created_at']
        unique_together = ('restaurant', 'slug')
        indexes = [
            models.Index(fields=['restaurant', 'order']),
        ]
        verbose_name = _('Menu Toifasi')
        verbose_name_plural = _('Menu Toifalari')

    def __str__(self):
        return f"{self.name_uz} ({self.restaurant.name})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """
    Menu item model - represents a dish/product.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name=_('Restoran')
    )
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name=_('Toifa')
    )
    name_uz = models.CharField(
        max_length=100,
        verbose_name=_('Taom Nomi (Uzbek)')
    )
    name_ru = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Taom Nomi (Russian)')
    )
    name_en = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Taom Nomi (English)')
    )
    slug = models.SlugField(
        verbose_name=_('URL Slug')
    )
    description_uz = models.TextField(
        verbose_name=_('Taom Tavsifi (Uzbek)')
    )
    description_ru = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Taom Tavsifi (Russian)')
    )
    description_en = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Taom Tavsifi (English)')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Narxi')
    )
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Chegirmalangan Narxi')
    )
    image = models.ImageField(
        upload_to='menu_items/',
        verbose_name=_('Taom Rasmi')
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name=_('Mavjud')
    )
    is_vegetarian = models.BooleanField(
        default=False,
        verbose_name=_('Vegetarian')
    )
    is_spicy = models.BooleanField(
        default=False,
        verbose_name=_('Achchiq')
    )
    preparation_time = models.PositiveIntegerField(
        default=15,
        help_text=_('Daqiqalar cinsidan'),
        verbose_name=_('Tayyorlash Vaqti')
    )
    calories = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Kalorijalar')
    )
    allergies = models.CharField(
        max_length=255,
        blank=True,
        help_text=_('Vergul bilan ajratilgan allergen ro'yxati'),
        verbose_name=_('Allergenlar')
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Tartibi')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Yangilandi')
    )

    class Meta:
        db_table = 'restaurant_menuitem'
        ordering = ['category', 'order', '-created_at']
        unique_together = ('restaurant', 'slug')
        indexes = [
            models.Index(fields=['restaurant', 'is_available']),
            models.Index(fields=['category']),
        ]
        verbose_name = _('Menyu Taomi')
        verbose_name_plural = _('Menyu Taomlari')

    def __str__(self):
        return f"{self.name_uz} - {self.restaurant.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)

    @property
    def current_price(self):
        """Return discount price if available, otherwise regular price."""
        return self.discount_price if self.discount_price else self.price


class Order(models.Model):
    """
    Order model - represents a customer order.
    """
    class Status(models.TextChoices):
        PENDING = "PENDING", _('Yangi')
        ACCEPTED = "ACCEPTED", _('Qabul qilindi')
        PREPARING = "PREPARING", _('Tayyorlanmoqda')
        DELIVERING = "DELIVERING", _('Yo\'lda')
        COMPLETED = "COMPLETED", _('Yetkazildi')
        CANCELLED = "CANCELLED", _('Bekor qilindi')

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name=_('Restoran')
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='orders',
        verbose_name=_('Mijoz')
    )
    customer_name = models.CharField(
        max_length=100,
        verbose_name=_('Mijoz Ismi')
    )
    customer_phone = models.CharField(
        max_length=20,
        verbose_name=_('Telefon')
    )
    address = models.CharField(
        max_length=255,
        default="Olib ketish",
        verbose_name=_('Manzil')
    )
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_('Jami Summa')
    )
    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name=_('Chegirma')
    )
    delivery_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name=_('Yetkazish To\'lovi')
    )
    payment_method = models.CharField(
        max_length=50,
        default="Naqd",
        choices=[
            ("Naqd", _('Naqd To\'lov')),
            ("Payme", "Payme"),
            ("Click", "Click"),
            ("Uzcard", "Uzcard"),
        ],
        verbose_name=_('To\'lov Usuli')
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_('Holati')
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_('Izohlar')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Yangilandi')
    )

    class Meta:
        db_table = 'restaurant_order'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['restaurant', '-created_at']),
            models.Index(fields=['status']),
        ]
        verbose_name = _('Buyurtma')
        verbose_name_plural = _('Buyurtmalar')

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.customer_name}"


class OrderItem(models.Model):
    """
    Individual items in an order.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('Buyurtma')
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.PROTECT,
        verbose_name=_('Menyu Taomi')
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name=_('Miqdori')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Narxi')
    )
    notes = models.TextField(
        blank=True,
        help_text=_('Masalan: achchiq bo\'lmasin, sabzavotlar bermasin'),
        verbose_name=_('Izohlar')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )

    class Meta:
        db_table = 'restaurant_orderitem'
        ordering = ['created_at']
        verbose_name = _('Buyurtma Taomi')
        verbose_name_plural = _('Buyurtma Taomlari')

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name_uz}"

    @property
    def subtotal(self):
        return self.quantity * self.price


class Reservation(models.Model):
    """
    Table reservation model.
    """
    class Status(models.TextChoices):
        PENDING = "PENDING", _("Kutilmoqda")
        CONFIRMED = "CONFIRMED", _("Tasdiqlandi")
        COMPLETED = "COMPLETED", _("Yakunlandi")
        CANCELLED = "CANCELLED", _("Bekor qilindi")

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name=_('Restoran')
    )
    customer_name = models.CharField(
        max_length=100,
        verbose_name=_('Mijoz Ismi')
    )
    customer_phone = models.CharField(
        max_length=20,
        verbose_name=_('Telefon')
    )
    customer_email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_('Email')
    )
    date = models.DateField(
        verbose_name=_('Sana')
    )
    time = models.TimeField(
        verbose_name=_('Vaqt')
    )
    guests_count = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name=_('Mehmonlar Soni')
    )
    table_number = models.CharField(
        max_length=10,
        blank=True,
        verbose_name=_('Stol Raqami')
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_('Izohlar')
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_('Holati')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Yangilandi')
    )

    class Meta:
        db_table = 'restaurant_reservation'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['restaurant', 'date', 'time']),
            models.Index(fields=['status']),
        ]
        verbose_name = _('Stol Band Qilish')
        verbose_name_plural = _('Stol Band Qilishlar')

    def __str__(self):
        return f"Band #{self.id} - {self.customer_name} ({self.date})"


class Review(models.Model):
    """
    Customer review/rating model.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Restoran')
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Mijoz')
    )
    order = models.OneToOneField(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='review',
        verbose_name=_('Buyurtma')
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_('Reyting')
    )
    comment = models.TextField(
        blank=True,
        verbose_name=_('Fikri')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Yaratildi')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Yangilandi')
    )

    class Meta:
        db_table = 'restaurant_review'
        ordering = ['-created_at']
        unique_together = ('restaurant', 'customer', 'order')
        verbose_name = _('Sharh')
        verbose_name_plural = _('Sharhlar')

    def __str__(self):
        return f"⭐ {self.rating} - {self.restaurant.name}"
