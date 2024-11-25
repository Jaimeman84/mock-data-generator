# src/generators/base_generator.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from ..data_types.field_types import FieldDefinition

class DataGenerator(ABC):
    """
    Abstract base class for all data generators following the Interface Segregation Principle.
    Each generator type (JSON, XML, CSV) will implement this interface.
    """
    
    @abstractmethod
    def generate(self, template: Dict[str, FieldDefinition], count: int) -> List[Dict[str, Any]]:
        """
        Generate mock data based on the provided template.
        
        Args:
            template: Dictionary defining the data structure and constraints
            count: Number of records to generate
            
        Returns:
            List of generated data records
        """
        pass
    
    @abstractmethod
    def export(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """
        Export generated data to a file.
        
        Args:
            data: List of generated data records
            filepath: Path to save the exported file
        """
        pass