# tests/test_generators/test_json_generator.py
import pytest
import tempfile
import os
import json
from datetime import datetime

def test_generate_basic_types(json_generator, basic_template):
    """Test generating basic data types"""
    data = json_generator.generate(basic_template, count=5)
    
    assert len(data) == 5
    for record in data:
        assert isinstance(record["name"], str)
        assert isinstance(record["age"], int)
        assert 18 <= record["age"] <= 100
        assert isinstance(record["email"], str)
        assert "@" in record["email"]

def test_export_json(json_generator, basic_template):
    """Test exporting data to JSON file"""
    data = json_generator.generate(basic_template, count=3)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        json_generator.export(data, tmp.name)
        
        with open(tmp.name, 'r') as f:
            loaded_data = json.load(f)
            
        assert len(loaded_data) == 3
        for record in loaded_data:
            assert all(key in record for key in basic_template.keys())
    
    os.unlink(tmp.name)

@pytest.mark.parametrize("record_count", [1, 5, 10])
def test_generate_multiple_records(json_generator, basic_template, record_count):
    """Test generating different numbers of records"""
    data = json_generator.generate(basic_template, count=record_count)
    assert len(data) == record_count