# DealsHub - Affiliate Discount Website

DealsHub is a premium, responsive affiliate deal aggregator built with **Django 6.0**, **Bootstrap 5**, and **Vanilla CSS**. It features a modern design, full admin control, and affiliate tracking.

## 🚀 Quick Start

### 1. Installation
The project is already set up. If you need to install dependencies on a new machine:
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python manage.py runserver
```
Access the site at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3. Admin Panel
Manage deals, stores, and categories here:
- **URL:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- **Username:** `admin`
- **Password:** `admin123`

---

## ✨ Key Features

### 🏢 Store & Category Management
- **Dynamic Stores:** Add stores like Amazon, Flipkart, or Myntra with logos and affiliate links.
- **Smart Categories:** Organize deals into Electronics, Fashion, Mobiles, etc.
- **Auto-Calculations:** Discount percentages are automatically calculated based on Old and New prices.

### 🛍️ Premium Deal Cards
- **Discount Badges:** Visual indicators for "Hot" (50%+), "Warm" (30%+), and "Cool" deals.
- **Expiry Tracking:** Deals automatically hide from the frontend once they expire.
- **Mobile First:** The UI is fully responsive and looks stunning on all devices.

### 📈 Affiliate Tools
- **Click Tracking:** Every "Get Deal" click is logged with IP and User Agent for analytics.
- **Affiliate Disclosures:** Built-in compliance banners and dedicated disclaimer pages.
- **SEO Optimized:** Semantic HTML, meta descriptions, and clean URL structures.

### 📧 Marketing & Legal
- **Newsletter:** Functional signup form for deal alerts.
- **Contact Form:** Integrated contact system for user queries.
- **Legal Pages:** Pre-written Privacy Policy, Terms & Conditions, and About Us pages.

---

## 🛠️ Project Structure

- `deals/`: Core application logic (models, views, templates).
- `dealshub/`: Project configuration (settings, main URLs).
- `static/`:
  - `css/style.css`: Premium custom design system.
  - `js/main.js`: Scroll animations and cookie consent.
- `templates/`:
  - `base.html`: Main layout wrapper.
  - `deals/`: Page-specific templates.
- `seed_data.py`: Script to populate the site with sample deals.

---

## 🔧 Database Configuration
The project uses **SQLite** by default for easy portability. To switch to **MySQL** or **PostgreSQL**:
1. Open `dealshub/settings.py`.
2. Locate the `DATABASES` section.
3. Uncomment the MySQL configuration and update your credentials.
4. Run `python manage.py migrate`.

---

## 📦 Deliverables Summary
- [x] Full Frontend UI (Bootstrap 5 + Custom CSS)
- [x] Django Backend with Admin Panel
- [x] Click Tracking & Analytics
- [x] Affiliate Disclosure & Legal Pages
- [x] Sample Dummy Deals (Seeded)
- [x] Mobile Responsive Design
