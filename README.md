# Sales & Purchasing System

A comprehensive sales and purchasing system with inventory and accounting capabilities, built with Flask and SQLModel.

## Features

- Multi-language support (English, Traditional Chinese, Simplified Chinese)
- User authentication and authorization
- Customer management
- Supplier management
- Item management
- Sales system (Quotations, Sales Orders, Invoices)
- Purchasing system
- Inventory management
- Accounting system (AR, AP, General Ledger)
- Administrative functions
- Report generation

## Requirements

- Python 3.8+
- SQLite (for development)
- PostgreSQL (for production)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sales-purchasing-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Create an admin user:
```bash
flask create-admin
```

6. Run the development server:
```bash
flask run
```

## Configuration

The system can be configured using environment variables or a configuration file. The following environment variables are available:

- `FLASK_APP`: The application instance (default: `src.sales_purchasing_system`)
- `FLASK_ENV`: The environment (default: `development`)
- `FLASK_DEBUG`: Debug mode (default: `True` in development)
- `SECRET_KEY`: Secret key for session management
- `DATABASE_URL`: Database connection URL
- `BABEL_DEFAULT_LOCALE`: Default language (default: `en`)
- `BABEL_SUPPORTED_LOCALES`: Supported languages (default: `en,zh_Hant,zh_Hans`)

## Usage

1. Access the system at `http://localhost:5000`
2. Log in with your admin credentials
3. Navigate through the modules using the sidebar menu
4. Use the language selector to switch between languages

## Development

### Project Structure

```
sales-purchasing-system/
├── src/
│   └── sales_purchasing_system/
│       ├── __init__.py
│       ├── models/
│       ├── templates/
│       ├── static/
│       ├── auth/
│       ├── basic_info/
│       ├── sales/
│       ├── purchases/
│       ├── inventory/
│       ├── accounting/
│       ├── admin/
│       └── reports/
├── tests/
├── migrations/
├── translations/
├── config/
├── requirements.txt
└── README.md
```

### Adding New Features

1. Create a new module in the appropriate directory
2. Add models in `models/`
3. Add views in the module directory
4. Add templates in `templates/`
5. Add translations for new strings
6. Write tests for new functionality

### Running Tests

```bash
pytest
```

### Code Style

The project follows PEP 8 guidelines and uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting

Run code style checks:
```bash
black .
isort .
flake8
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 