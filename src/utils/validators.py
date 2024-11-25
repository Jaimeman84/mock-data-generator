# src/utils/validators.py
import re
from typing import Any, Optional
from ..data_types.field_types import FieldDefinition

class FieldValidator:
    """Validator for field values"""
    
    @staticmethod
    def validate_string(value: str, field_def: FieldDefinition) -> bool:
        """Validate string fields"""
        if field_def.pattern:
            return bool(re.match(field_def.pattern, value))
        return True
    
    @staticmethod
    def validate_numeric(value: float, field_def: FieldDefinition) -> bool:
        """Validate numeric fields"""
        if field_def.min_value is not None and value < field_def.min_value:
            return False
        if field_def.max_value is not None and value > field_def.max_value:
            return False
        return True
    
    @staticmethod
    def validate_email(value: str) -> bool:
        """Validate email format"""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, value))
    
    @staticmethod
    def validate_field(value: Any, field_def: FieldDefinition) -> bool:
        """Validate a field value against its definition"""
        if value is None:
            return field_def.nullable
            
        if field_def.choices and value not in field_def.choices:
            return False
            
        if field_def.field_type == FieldTypes.STRING:
            return FieldValidator.validate_string(value, field_def)
        elif field_def.field_type in [FieldTypes.INTEGER, FieldTypes.FLOAT]:
            return FieldValidator.validate_numeric(float(value), field_def)
        elif field_def.field_type == FieldTypes.EMAIL:
            return FieldValidator.validate_email(value)
            
        return True