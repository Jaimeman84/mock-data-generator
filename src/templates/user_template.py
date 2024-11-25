# src/templates/user_template.py
from typing import Dict
from .base_template import BaseTemplate
from ..data_types.field_types import FieldDefinition, FieldTypes

class UserTemplate(BaseTemplate):
    def get_name(self) -> str:
        return "User Data"
    
    def get_template(self) -> Dict[str, FieldDefinition]:
        return {
            "id": FieldDefinition(
                name="id",
                field_type=FieldTypes.INTEGER,
                min_value=1000,
                max_value=9999,
                unique=True
            ),
            "username": FieldDefinition(
                name="username",
                field_type=FieldTypes.STRING,
                pattern="[a-z0-9_]{5,15}"
            ),
            "email": FieldDefinition(
                name="email",
                field_type=FieldTypes.EMAIL
            ),
            "first_name": FieldDefinition(
                name="first_name",
                field_type=FieldTypes.NAME
            ),
            "last_name": FieldDefinition(
                name="last_name",
                field_type=FieldTypes.NAME
            ),
            "date_joined": FieldDefinition(
                name="date_joined",
                field_type=FieldTypes.DATE
            ),
            "is_active": FieldDefinition(
                name="is_active",
                field_type=FieldTypes.BOOLEAN
            )
        }