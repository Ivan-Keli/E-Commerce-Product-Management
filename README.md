# 🛒 E-Commerce Product Management System

A comprehensive Django-based web application designed for efficient product catalog management with category organization, image uploads, and an intuitive admin interface.

## 🚀 Project Overview

This application provides a complete solution for managing an e-commerce product database. Built with Django 5.2.8, it offers seamless product creation, categorization, and display functionality with support for image uploads and detailed product descriptions.

## ⚡ Key Features

### Product Management
- **Dynamic Product Creation**: Form-based interface for adding new products
- **Category Organization**: Products linked to categories via foreign key relationships
- **Image Support**: Upload and display product images with Pillow integration
- **Detailed Information**: Store names, prices, descriptions, and timestamps
- **Product Detail Views**: Individual pages for comprehensive product information

### Administration
- **Django Admin Integration**: Full backend access for managing products and categories
- **User Authentication**: Secure superuser access for administrative tasks
- **Database Management**: Built on SQLite with easy migration support

## 📋 Technical Specifications

### Product Model Structure
| Field | Type | Constraints |
|-------|------|-------------|
| name | CharField | Required, max 255 chars |
| category | ForeignKey | CASCADE delete, related_name="products" |
| price | DecimalField | 10 digits max, 2 decimal places |
| description | TextField | Optional |
| image | ImageField | Optional, stored in `products/` directory |
| created_at | DateTimeField | Auto-generated timestamp |

### Category Model Structure
| Field | Type | Constraints |
|-------|------|-------------|
| name | CharField | Max 255 chars |

## 🔧 Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Process

**1. Clone the repository**
```bash
git clone https://github.com/Ivan-Keli/E-Commerce-Product-Management.git
cd E-Commerce-Product-Management
```

**2. Set up a virtual environment**
```bash
python -m venv venv
```

**3. Activate the virtual environment**

*Windows:*
```bash
venv\Scripts\activate
```

*macOS/Linux:*
```bash
source venv/bin/activate
```

**4. Install required packages**
```bash
pip install -r requirements.txt
```

**5. Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Create an admin account**
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

**7. Launch the development server**
```bash
python manage.py runserver
```

## 🌐 Application URLs

Once the server is running, access the application through:

| Page | URL | Description |
|------|-----|-------------|
| Product Catalog | `http://127.0.0.1:8000/` | View all products |
| Add New Product | `http://127.0.0.1:8000/products/add/` | Create product entries |
| Product Details | `http://127.0.0.1:8000/products/<id>/` | View individual product |
| Admin Dashboard | `http://127.0.0.1:8000/admin/` | Backend management |

## 📂 Project Architecture

```
E-Commerce-Product-Management/
│
├── ecommerce/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Main configuration
│   ├── urls.py               # Root URL routing
│   └── wsgi.py
│
├── products/
│   ├── migrations/           # Database schema versions
│   ├── Templates/
│   │   └── products/
│   │       ├── add_product.html
│   │       ├── list_product.html
│   │       └── product_detail.html
│   ├── __init__.py
│   ├── admin.py              # Admin panel configuration
│   ├── apps.py
│   ├── models.py             # Data models
│   ├── urls.py               # App-level routing
│   └── views.py              # Request handlers
│
├── media/                    # User-uploaded files
│   └── products/
│
├── .gitignore
├── db.sqlite3                # SQLite database
├── manage.py                 # Django CLI tool
├── README.md
└── requirements.txt          # Python dependencies
```

## 💻 Usage Examples

### Adding a Product
1. Navigate to the "Add Product" page
2. Fill in the product name and select a category
3. Enter the price (supports decimal values)
4. Optionally add a description and upload an image
5. Click "Submit" to save

### Viewing Products
- The homepage displays all products with names, prices, categories, and thumbnails
- Click "View Details" on any product to see full information including creation date

### Managing via Admin
- Log in to the admin panel with your superuser credentials
- Create, edit, or delete products and categories
- View all database records in a structured interface

## 🛠️ Technology Stack

- **Framework**: Django 5.2.8
- **Database**: SQLite3
- **Image Processing**: Pillow 12.0.0
- **Template Engine**: Django Templates
- **Backend Language**: Python 3.x

## 📝 Implementation Notes

- All product models include `__str__` methods for readable object representation
- Image uploads are handled through Django's `ImageField` with automatic file management
- The application uses Django's built-in ORM for database operations
- CSRF protection is enabled on all forms
- Media files are served during development through Django's static file handler

## 🔐 Security Considerations

- The `SECRET_KEY` in `settings.py` should be changed for production use
- `DEBUG` mode should be set to `False` in production environments
- Ensure proper file upload validation before deploying publicly
- Use environment variables for sensitive configuration data

## 🤝 Contributing

This project was created as part of a Django class activity. Feel free to fork and customize for your own learning purposes.

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**Ivan Keli**
- GitHub: [@Ivan-Keli](https://github.com/Ivan-Keli)

---

*Built with Django - The web framework for perfectionists with deadlines*
