# src/generators/xml_generator.py
from typing import Dict, Any, List
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import date, datetime
from .base_generator import DataGenerator
from .json_generator import JSONGenerator
from ..data_types.field_types import FieldDefinition
import faker

class XMLGenerator(DataGenerator):
    def __init__(self):
        self.fake = faker.Faker()
        self.json_generator = JSONGenerator()
        
    def _format_value(self, value: Any) -> str:
        """
        Format value to proper string representation for XML.
        """
        if value is None:
            return ""
        elif isinstance(value, (date, datetime)):
            return value.isoformat()
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, (int, float)):
            return str(value)
        else:
            # Escape special XML characters
            return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')
    
    def generate(self, template: Dict[str, FieldDefinition], count: int) -> List[Dict[str, Any]]:
        """Generate data using JSON generator for consistency"""
        return self.json_generator.generate(template, count)
    
    def export(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """Export data to XML format"""
        root = ET.Element("records")
        
        for record in data:
            record_elem = ET.SubElement(root, "record")
            for key, value in record.items():
                field_elem = ET.SubElement(record_elem, key)
                field_elem.text = self._format_value(value)
        
        # Convert to string with pretty printing
        rough_string = ET.tostring(root, encoding='unicode', method='xml')
        reparsed = minidom.parseString(rough_string)
        
        # Write to file with explicit encoding
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(reparsed.toprettyxml(indent="  "))