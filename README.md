# Django E-Commerce Product Management

A Django application for managing products with categories, images, and full CRUD functionality.

## Features

✅ **Product Model** with all required fields:
- name (CharField, required)
- category (ForeignKey to Category with CASCADE delete)
- price (DecimalField with 2 decimal places)
- description (TextField, optional)
- image (ImageField, optional, uploads to `products/`)
- created_at (DateTimeField, auto-generated)

✅ **Views**:
- Add Product (form-based)
- List All Products
- Product Detail Page (optional task completed)

✅ **Admin Panel**:
- Product and Category models registered
- Full admin interface access

✅ **Templates**:
- Add Product form
- Product listing with name, price, image, and category
- Product detail page with full information

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

## Usage

### Access the Application
- **Home/Product List**: http://127.0.0.1:8000/
- **Add Product**: http://127.0.0.1:8000/products/add/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### Adding Products
1. Go to http://127.0.0.1:8000/products/add/
2. Fill in the product details
3. Upload an image (optional)
4. Submit the form

### Viewing Products
- All products are listed on the homepage
- Click "View Details" on any product to see full information

### Admin Panel
- Access at http://127.0.0.1:8000/admin/
- Login with your superuser credentials
- Manage products and categories

## Project Structure
```
ecommerce/
├── ecommerce/          # Project settings
├── products/           # Products app
│   ├── migrations/     # Database migrations
│   ├── Templates/      # HTML templates
│   │   └── products/
│   │       ├── add_product.html
│   │       ├── list_product.html
│   │       └── product_detail.html
│   ├── models.py       # Product & Category models
│   ├── views.py        # View functions
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configuration
├── media/              # Uploaded images
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Models

### Category
- `name`: CharField (max 255 characters)

### Product
- `name`: CharField (max 255 characters, required)
- `category`: ForeignKey to Category (CASCADE, related_name="products")
- `price`: DecimalField (max 10 digits, 2 decimal places)
- `description`: TextField (optional)
- `image`: ImageField (upload to "products/", optional)
- `created_at`: DateTimeField (auto-generated)

## Notes
- Pillow is required for image handling
- Media files are stored in the `media/products/` directory
- The project uses SQLite database by default
