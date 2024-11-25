# src/generators/json_generator.py
import json
import random
from typing import Dict, Any, List
from datetime import datetime, timedelta
from ..data_types.field_types import FieldDefinition, FieldTypes
from .base_generator import DataGenerator
import faker

class JSONGenerator(DataGenerator):
    """
    Concrete implementation of DataGenerator for JSON format.
    """
    
    def __init__(self):
        self.fake = faker.Faker()
        
    def _generate_field_value(self, field_def: FieldDefinition) -> Any:
        """
        Generate a single field value based on its definition.
        """
        if field_def.nullable and random.random() < 0.1:  # 10% chance of null
            return None
            
        if field_def.field_type == FieldTypes.STRING:
            if field_def.choices:
                return random.choice(field_def.choices)
            elif field_def.pattern:
                # You might want to add a pattern-based generator here
                return self.fake.pystr()
            return self.fake.text(max_nb_chars=50)
            
        elif field_def.field_type == FieldTypes.INTEGER:
            min_val = field_def.min_value if field_def.min_value is not None else 0
            max_val = field_def.max_value if field_def.max_value is not None else 1000
            return random.randint(min_val, max_val)
            
        elif field_def.field_type == FieldTypes.FLOAT:
            min_val = float(field_def.min_value if field_def.min_value is not None else 0)
            max_val = float(field_def.max_value if field_def.max_value is not None else 1000)
            return round(random.uniform(min_val, max_val), 2)
            
        elif field_def.field_type == FieldTypes.EMAIL:
            return self.fake.email()
            
        elif field_def.field_type == FieldTypes.DATE:
            start_date = datetime.now() - timedelta(days=365)
            end_date = datetime.now()
            return self.fake.date_between(start_date=start_date, end_date=end_date)
            
        elif field_def.field_type == FieldTypes.NAME:
            return self.fake.name()
            
        elif field_def.field_type == FieldTypes.BOOLEAN:
            return random.choice([True, False])
            
        elif field_def.field_type == FieldTypes.PHONE:
            return self.fake.phone_number()
            
        elif field_def.field_type == FieldTypes.ADDRESS:
            return self.fake.address()
            
        return None
        
    def generate(self, template: Dict[str, FieldDefinition], count: int) -> List[Dict[str, Any]]:
        """
        Generate mock data based on the provided template.
        
        Args:
            template: Dictionary defining the data structure and constraints
            count: Number of records to generate
            
        Returns:
            List of generated data records
        """
        result = []
        unique_values = {field_name: set() for field_name, field_def in template.items() 
                        if field_def.unique}
        
        for _ in range(count):
            record = {}
            for field_name, field_def in template.items():
                value = self._generate_field_value(field_def)
                
                # Handle unique constraint
                if field_def.unique:
                    max_attempts = 100  # Prevent infinite loop
                    attempts = 0
                    while str(value) in unique_values[field_name] and attempts < max_attempts:
                        value = self._generate_field_value(field_def)
                        attempts += 1
                    unique_values[field_name].add(str(value))
                
                record[field_name] = value
            result.append(record)
        
        return result
        
    def export(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """
        Export generated data to a JSON file.
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)