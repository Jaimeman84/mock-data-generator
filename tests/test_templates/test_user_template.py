# tests/test_templates/test_user_template.py
import pytest
from src.data_types.field_types import FieldTypes
from src.templates.user_template import UserTemplate

def test_user_template_structure(user_template):
    """Test user template structure and fields"""
    template_def = user_template.get_template()
    
    # Verify required fields
    assert "id" in template_def
    assert "email" in template_def
    assert "username" in template_def
    
    # Verify field types
    assert template_def["id"].field_type == FieldTypes.INTEGER
    assert template_def["email"].field_type == FieldTypes.EMAIL
    assert template_def["id"].unique

def test_user_template_constraints(user_template):
    """Test user template field constraints"""
    template_def = user_template.get_template()
    
    assert template_def["id"].min_value == 1000
    assert template_def["id"].max_value == 9999
    assert template_def["username"].pattern == "[a-z0-9_]{5,15}"