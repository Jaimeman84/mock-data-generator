# tests/conftest.py
import pytest
from typing import Dict
from src.generators.json_generator import JSONGenerator
from src.generators.xml_generator import XMLGenerator
from src.generators.csv_generator import CSVGenerator
from src.templates.user_template import UserTemplate
from src.templates.financial_template import FinancialTemplate
from src.data_types.field_types import FieldDefinition, FieldTypes

@pytest.fixture
def basic_template() -> Dict[str, FieldDefinition]:
    """Fixture providing a basic template for testing"""
    return {
        "name": FieldDefinition(
            name="name",
            field_type=FieldTypes.STRING
        ),
        "age": FieldDefinition(
            name="age",
            field_type=FieldTypes.INTEGER,
            min_value=18,
            max_value=100
        ),
        "email": FieldDefinition(
            name="email",
            field_type=FieldTypes.EMAIL
        )
    }

@pytest.fixture
def json_generator() -> JSONGenerator:
    """Fixture providing a JSON generator instance"""
    return JSONGenerator()

@pytest.fixture
def xml_generator() -> XMLGenerator:
    """Fixture providing an XML generator instance"""
    return XMLGenerator()

@pytest.fixture
def csv_generator() -> CSVGenerator:
    """Fixture providing a CSV generator instance"""
    return CSVGenerator()

@pytest.fixture
def user_template() -> UserTemplate:
    """Fixture providing a user template instance"""
    return UserTemplate()

@pytest.fixture
def financial_template() -> FinancialTemplate:
    """Fixture providing a financial template instance"""
    return FinancialTemplate()