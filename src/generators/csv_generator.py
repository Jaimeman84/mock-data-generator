# src/generators/csv_generator.py
from typing import Dict, Any, List
import csv
from .base_generator import DataGenerator
from .json_generator import JSONGenerator  # Added this import
from ..data_types.field_types import FieldDefinition

class CSVGenerator(DataGenerator):
    def __init__(self):
        self.json_generator = JSONGenerator()  # Reuse JSON generator for field generation
        
    def generate(self, template: Dict[str, FieldDefinition], count: int) -> List[Dict[str, Any]]:
        """Generate data using JSON generator for consistency"""
        return self.json_generator.generate(template, count)
    
    def export(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """Export data to CSV format"""
        if not data:
            return
            
        fieldnames = data[0].keys()
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)