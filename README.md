
# eCommerce Django Project

## Overview
This is a basic eCommerce web application built with Django. It features product listings with categories, a shopping cart, user registration and profile, order history, and order placement functionality.

## Features
- Product management with categories
- User registration and authentication
- Shopping cart with add/remove functionality
- Order creation and history view
- Admin interface for managing products and categories

## Technologies Used
- Python 3.x
- Django 4.x
- SQLite (default Django database)

## Setup Instructions

### Prerequisites
- Python 3.6 or higher installed
- pip package manager installed

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   # On Windows
   .\env\Scripts\activate
   # On Linux/macOS
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage
- Admin can add categories and products via Django admin panel.
- Users can browse products by category, add items to cart, and place orders.
- Users can view their order history in their profile.

## Project Structure
```
ecommerce/
├── store/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├───README.md
└──requirements.txt
```

## Known Issues
- Product image handling is URL-based; file uploads are not implemented.
- Search and filtering features are basic and can be improved.

## Future Enhancements
- Add file upload for product images.
- Implement advanced search and filter options.
- Add payment gateway integration.
- Improve UI and UX with frontend frameworks.

