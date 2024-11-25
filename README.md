# 🏢 Employee API Testing Platform

A comprehensive API testing environment designed for QA engineers to learn and practice API testing using a real-world employee management system.

## 📋 Features

- **RESTful API Endpoints**
  - Complete CRUD operations for employee management
  - Department management
  - Analytics endpoints
- **Interactive Testing UI**
  - Built with Streamlit
  - Real-time API testing interface
  - Visual analytics dashboard
- **Comprehensive Documentation**
  - API endpoint documentation
  - Request/Response examples
  - Testing guides
- **Data Persistence**
  - SQLite database integration
  - Sample data population
  - Data validation

## 🛠️ Technology Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Database**: SQLAlchemy with SQLite
- **Testing**: pytest
- **Documentation**: FastAPI Swagger/ReDoc
- **Data Validation**: Pydantic

## 📁 Project Structure

```
employee_api_testing/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── api.py          # FastAPI application
│   └── ui/
│       ├── __init__.py
│       └── app.py       # Streamlit interface
└── tests/
    ├── __init__.py
    ├── test_api.py
    └── test_data.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/employee_api_testing.git
cd employee_api_testing
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

### Running the Application

1. Start the FastAPI backend server:
```bash
uvicorn src.api:app --reload --port 8000
```

2. In a new terminal, start the Streamlit UI:
```bash
streamlit run src/ui/app.py
```

3. Access the applications:
- API Documentation: http://localhost:8000/docs
- Streamlit Interface: http://localhost:8501

## 🔍 Available Endpoints

### Employees
- `GET /employees` - List all employees
- `GET /employees/{id}` - Get specific employee
- `POST /employees` - Create new employee
- `PUT /employees/{id}` - Update employee
- `DELETE /employees/{id}` - Delete employee

### Departments
- `GET /departments` - List all departments
- `POST /departments` - Create new department

### Analytics
- `GET /analytics/department-stats` - Get department statistics

## 🧪 Running Tests

Execute the test suite:
```bash
pytest tests/
```

## 🎓 Learning Resources

### API Testing Concepts Covered
- HTTP Methods (GET, POST, PUT, DELETE)
- Request/Response handling
- Status codes and error handling
- Data validation
- Database interactions
- Analytics and reporting

### Recommended Learning Path
1. Start with simple GET requests
2. Practice data creation with POST
3. Implement data updates with PUT
4. Learn data deletion with DELETE
5. Explore analytics endpoints
6. Write automated tests

## 🛟 Troubleshooting

Common Issues and Solutions:

1. **Import Errors**
   - Ensure you're in the virtual environment
   - Verify package installation with `pip list`

2. **Database Issues**
   - Delete the `employee_test.db` file to reset the database
   - Restart the API server

3. **Port Conflicts**
   - Change ports using `--port` flag with uvicorn
   - Check for running processes on ports 8000 and 8501

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.