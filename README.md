# Mock Test Data Generator

A Python-based mock data generator with a Streamlit interface for creating test data in various formats.

## Features

### Data Generation
- Generate mock data in multiple formats (JSON, CSV, XML)
- Specify custom number of records (1-1000)
- Preview generated data before download
- Export data in different formats with proper encoding

### Field Types Support
- String
- Integer
- Float
- Email
- Date
- Boolean
- Name
- Phone
- Address

### Templates
- Custom template creation
- Pre-built templates:
  - User Data Template (user profiles)
  - Financial Data Template (transaction records)

### Field Configuration
- Define custom fields with:
  - Name
  - Data type
  - Min/Max values for numeric fields
  - Nullable option
  - Unique value constraints
  - Pattern matching
  - Predefined choices

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mock-data-generator.git
cd mock-data-generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the web interface (typically http://localhost:8501)

3. Configure your data generation:
   - Select export format (JSON, CSV, XML)
   - Choose number of records to generate
   - Select a template or create custom fields
   - Configure field properties

4. Click "Generate Data" to:
   - Preview the generated data
   - See total records generated
   - Download the complete dataset

## Project Structure
```
mock_data_generator/
│
├── src/
│   ├── __init__.py
│   ├── generators/
│   │   ├── __init__.py
│   │   ├── base_generator.py     # Abstract base class for generators
│   │   ├── json_generator.py     # JSON format generator
│   │   ├── xml_generator.py      # XML format generator
│   │   └── csv_generator.py      # CSV format generator
│   │
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── base_template.py      # Template interface
│   │   ├── user_template.py      # User data template
│   │   └── financial_template.py # Financial data template
│   │
│   ├── data_types/
│   │   ├── __init__.py
│   │   ├── field_types.py        # Field definitions and types
│   │   └── constraints.py        # Field constraints
│   │
│   └── utils/
│       ├── __init__.py
│       └── validators.py         # Data validation utilities
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures and configuration
│   ├── test_generators/         # Generator tests
│   │   ├── test_json_generator.py
│   │   ├── test_xml_generator.py
│   │   └── test_csv_generator.py
│   │
│   └── test_templates/          # Template tests
│       ├── test_user_template.py
│       └── test_financial_template.py
│
├── app.py                       # Streamlit application
├── requirements.txt             # Project dependencies
└── README.md                    # This file
```

## Development

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/test_generators/test_json_generator.py

# Run tests with specific marker
pytest -k "json"
```

### SOLID Principles Implementation
- **Single Responsibility**: Each generator handles one format
- **Open/Closed**: Easy to add new generators and templates
- **Liskov Substitution**: All generators follow the base interface
- **Interface Segregation**: Clean interfaces for generators and templates
- **Dependency Inversion**: High-level modules depend on abstractions

### Adding New Features

1. Adding a New Field Type:
   - Add type to `FieldTypes` class in `src/data_types/field_types.py`
   - Implement generation logic in generators

2. Adding a New Template:
   - Create new template class in `src/templates/`
   - Implement `get_template()` and `get_name()`
   - Add corresponding tests

3. Adding a New Export Format:
   - Create new generator class in `src/generators/`
   - Implement `generate()` and `export()`
   - Add corresponding tests

## Requirements

- Python 3.8+
- streamlit>=1.32.0
- faker>=24.0.0
- pytest>=8.0.0
- pytest-cov>=4.1.0
- Additional requirements listed in requirements.txt

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.