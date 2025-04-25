# GreenHaven - Interior Design Platform

GreenHaven is a comprehensive web platform for interior design services built with Django. The platform connects users with designers, shops, and delivery services for interior design projects.

## Features

### User Roles
- **Admin**: System management and user verification
- **Users**: Browse designs, submit complaints/feedback, manage profile
- **Designers**: Showcase portfolio, handle client projects
- **Shops**: List interior design products
- **Delivery Boys**: Handle product deliveries

### Key Functionalities
- User authentication and profile management
- Project showcase and portfolio management
- Complaint and feedback system
- Shop product management
- Delivery tracking
- Responsive design for all devices

## Technical Stack

- **Backend**: Django 5.1.3
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: Django ORM
- **Additional Libraries**: 
  - mathfilters
  - django.contrib modules

## Installation

1. Clone the repository
```bash
git clone [repository-url]
```

2. Create and activate virtual environment
```bash
python -m venv MainEnv
source MainEnv/bin/activate  # On Windows: MainEnv\Scripts\activate
```

3. Install dependencies
```bash
pip install django mathfilters
```

4. Configure database
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run development server
```bash
python manage.py runserver
```

## Project Structure

```
MainProject/
├── Admin/
├── Designer/
├── DeliveryBoy/
├── Guest/
├── Shop/
├── User/
└── MainProject/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## URLs

- Admin Dashboard: `/Admin/`
- User Interface: `/User/`
- Designer Portal: `/Designer/`
- Shop Management: `/shop/`
- Delivery Interface: `/DeliveryBoy/`
- Guest/Public Pages: `/`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project uses templates from:
- Colorlib (Main template)
- BootstrapMade (iPortfolio template)

Please refer to their respective licenses for usage terms.

## Contact

For any queries or support, please submit an issue through the project's issue tracker.