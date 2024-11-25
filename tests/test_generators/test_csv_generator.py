# tests/test_generators/test_csv_generator.py
import pytest
import tempfile
import os
import csv

def test_generate_and_export_csv(csv_generator, basic_template):
    """Test generating and exporting CSV data"""
    data = csv_generator.generate(basic_template, count=3)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
        csv_generator.export(data, tmp.name)
        
        with open(tmp.name, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            assert len(rows) == 3
            for row in rows:
                assert "name" in row
                assert "age" in row
                
                age = int(row["age"])
                assert 18 <= age <= 100
                
    os.unlink(tmp.name)