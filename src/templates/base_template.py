# src/templates/base_template.py
from abc import ABC, abstractmethod
from typing import Dict
from ..data_types.field_types import FieldDefinition

class BaseTemplate(ABC):
    """Base class for all data templates"""
    
    @abstractmethod
    def get_template(self) -> Dict[str, FieldDefinition]:
        """Return the template definition"""
        pass
        
    @abstractmethod
    def get_name(self) -> str:
        """Return template name"""
        pass