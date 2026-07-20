# 🍽️ Lazzat Ovqat — Restoran va Kafeler uchun SaaS Platforma

**Lazzat Ovqat** — O'zbekistondagi restoran va kafelerni boshqarish uchun zamonaviy SaaS platforma.

Telegram bot: [@LazzatFoodBot](https://t.me/8896986265:AAHfmDiIrXTnjqa0sxSAh3fA-4iUI2bjb3k)

## 🚀 Tez Boshlash

### Talablar
- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose

### O'rnatish

#### 1. Repositoriyani klonlash
```bash
git clone https://github.com/testrobbit43-star/lazzat-food.git
cd lazzat-food
```

#### 2. Virtual muhit yaratish
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

#### 3. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

#### 4. .env faylini nusxalash
```bash
cp .env.example .env
```

#### 5. Docker orqali ishga tushirish
```bash
docker-compose up -d
```

Ilova manzili: `http://localhost:8000`

---

## 🤖 Telegram Bot

Bot to'liq integrlashtirilgan va quyidagilarni qo'llab-quvvatlaydi:
- 📋 Menyuni ko'rish
- 📦 Buyurtma berish
- 📅 Stol bronirash
- 📱 Buyurtma statusini kuzatish
- 🔔 Real vaqt bildirishnomalar

**Token:** `8896986265:AAHfmDiIrXTnjqa0sxSAh3fA-4iUI2bjb3k`
**Admin Chat ID:** `8191123267`

---

## 📁 Loyiha Tuzilishi

```
lazzat_food/
├── config/                 # Django sozlamalari
├── apps/
│   ├── accounts/          # Foydalanuvchi boshqaruvi
│   ├── restaurants/       # Restoran profillari
│   ├── menu/             # Menyu boshqaruvi
│   ├── orders/           # Buyurtmalar
│   ├── reservations/     # Bronirash
│   ├── telegram_bot/     # Telegram Bot ✅
│   ├── cms/              # Wagtail CMS
│   └── core/             # Umumiy vositalari
├── templates/            # HTML shablonlar
├── docker/              # Docker konfiguratsiyasi
├── manage.py
├── requirements.txt
└── docker-compose.yml
```

---

## 🔧 Texnologiya Staketi

- **Backend**: Django 5.1 + Django REST Framework
- **Ma'lumotlar bazasi**: PostgreSQL 15+
- **Cache**: Redis
- **Frontend**: Tailwind CSS + Alpine.js + HTMX
- **CMS**: Wagtail
- **Bot**: python-telegram-bot ✅
- **Navbat**: Celery + Redis
- **Autentifikatsiya**: JWT + Django-allauth
- **Konteynerizatsiya**: Docker & Docker Compose

---

## 📱 Asosiy Funktsiyalar

### Mijozlar Uchun
- ✅ Restoran menyu ko'rish
- ✅ Buyurtma berish
- ✅ Buyurtmani real vaqtda kuzatish
- ✅ Stol bronirash
- ✅ Telegram Boti qo'llash

### Restoran Egalari Uchun
- ✅ Restoran boshqaruvi dashboardi
- ✅ Menyu boshqaruvi (Wagtail CMS)
- ✅ Buyurtmalarni boshqarish
- ✅ Tahlillar va hisobotlar

### Adminlar Uchun
- ✅ Barcha restoranlarniboshqaruvi
- ✅ Foydalanuvchilarni boshqarish

---

## 🌍 Qo'llab-Quvvatlanadigan Tillar

- 🇺🇿 O'zbek (O'zbekcha)
- 🇷🇺 Ruscha
- 🇬🇧 Inglizcha

---

## 📞 Bog'lanish

- 🤖 Telegram Bot: [@LazzatFoodBot](https://t.me/8896986265:AAHfmDiIrXTnjqa0sxSAh3fA-4iUI2bjb3k)
- 📧 Email: support@lazzatfood.uz

---

**O'zbekistonda ❤️ bilan yaratilgan**
