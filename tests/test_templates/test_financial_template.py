# tests/test_templates/test_financial_template.py
import pytest
from src.data_types.field_types import FieldTypes
from src.templates.financial_template import FinancialTemplate

def test_financial_template_structure(financial_template):
    """Test financial template structure and fields"""
    template_def = financial_template.get_template()
    
    # Verify required fields
    assert "transaction_id" in template_def
    assert "amount" in template_def
    assert "currency" in template_def
    
    # Verify field types and constraints
    assert template_def["amount"].field_type == FieldTypes.FLOAT
    assert template_def["amount"].min_value > 0
    assert "USD" in template_def["currency"].choices

def test_financial_template_currency_choices(financial_template):
    """Test currency choices in financial template"""
    template_def = financial_template.get_template()
    expected_currencies = ["USD", "EUR", "GBP", "JPY"]
    
    assert all(currency in template_def["currency"].choices 
              for currency in expected_currencies)

@pytest.mark.parametrize("field_name,expected_type", [
    ("transaction_id", FieldTypes.STRING),
    ("amount", FieldTypes.FLOAT),
    ("currency", FieldTypes.STRING),
    ("transaction_date", FieldTypes.DATE),
    ("status", FieldTypes.STRING),
    ("account_number", FieldTypes.STRING)
])
def test_financial_template_field_types(financial_template, field_name, expected_type):
    """Test field types of financial template"""
    template_def = financial_template.get_template()
    assert template_def[field_name].field_type == expected_type

@pytest.mark.parametrize("field_name,expected_choices", [
    ("currency", ["USD", "EUR", "GBP", "JPY"]),
    ("status", ["completed", "pending", "failed"])
])
def test_financial_template_field_choices(financial_template, field_name, expected_choices):
    """Test choice fields in financial template"""
    template_def = financial_template.get_template()
    assert all(choice in template_def[field_name].choices 
              for choice in expected_choices)