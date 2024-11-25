# Mock Test Data Generator

A Python-based mock data generator with a Streamlit interface for creating test data in various formats.

## Features

- Generate mock data in multiple formats (JSON, CSV, XML)
- Define custom fields with various data types and constraints
- Pre-built templates for common data structures
- Export generated data for testing environments
- User-friendly web interface built with Streamlit

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

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Configure your data generation:
   - Select the export format (JSON, CSV, XML)
   - Choose a template or create custom fields
   - Set the number of records to generate
   - Define field types and constraints

4. Click "Generate Data" to create and preview the mock data

5. Download the generated data using the provided download link

## Development

### Project Structure

The project follows SOLID principles and is organized as follows:

- `src/`: Source code
  - `generators/`: Data generation implementations
  - `templates/`: Predefined data templates
  - `data_types/`: Field type definitions
  - `utils/`: Utility functions
- `tests/`: Unit tests
- `app.py`: Streamlit application
- `requirements.txt`: Project dependencies

### Running Tests

```bash
python -m unittest discover tests
```

### Adding New Features

1. To add a new field type:
   - Add the type to `src/data_types/field_types.py`
   - Implement generation logic in the appropriate generator class

2. To add a new template:
   - Create a new template class in `src/templates/`
   - Add corresponding unit tests

3. To add a new export format:
   - Create a new generator class implementing the `DataGenerator` interface
   - Add corresponding unit tests

## Requirements

- Python 3.8+
- Streamlit
- Faker
- Additional requirements listed in requirements.txt

## License

This project is licensed under the MIT License - see the LICENSE file for details.