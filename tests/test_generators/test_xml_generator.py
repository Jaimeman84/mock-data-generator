# tests/test_generators/test_xml_generator.py
import pytest
import tempfile
import os
import xml.etree.ElementTree as ET

def test_generate_and_export_xml(xml_generator, basic_template):
    """Test generating and exporting XML data"""
    data = xml_generator.generate(basic_template, count=3)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xml') as tmp:
        xml_generator.export(data, tmp.name)
        
        # Parse and verify XML structure
        tree = ET.parse(tmp.name)
        root = tree.getroot()
        
        assert root.tag == "records"
        assert len(root) == 3
        
        for record in root:
            assert record.tag == "record"
            assert "name" in [child.tag for child in record]
            assert "age" in [child.tag for child in record]
            
            age = int(record.find("age").text)
            assert 18 <= age <= 100
            
    os.unlink(tmp.name)