# src/data_types/field_types.py
from dataclasses import dataclass
from typing import Any, Optional, List
from datetime import datetime

@dataclass
class FieldDefinition:
    """
    Defines the structure and constraints for a field in the mock data.
    """
    name: str
    field_type: str
    min_value: Optional[Any] = None
    max_value: Optional[Any] = None
    choices: Optional[List[Any]] = None
    pattern: Optional[str] = None
    nullable: bool = False
    unique: bool = False

class FieldTypes:
    """
    Supported field types for mock data generation.
    """
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    EMAIL = "email"
    PHONE = "phone"
    ADDRESS = "address"
    NAME = "name"