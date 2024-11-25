# app.py
import streamlit as st
import json
import tempfile
import os
from src.generators.json_generator import JSONGenerator
from src.generators.xml_generator import XMLGenerator
from src.generators.csv_generator import CSVGenerator
from src.data_types.field_types import FieldDefinition, FieldTypes
from src.templates.user_template import UserTemplate
from src.templates.financial_template import FinancialTemplate
import base64
from contextlib import contextmanager

@contextmanager
def temp_file_handler(suffix: str):
    """Context manager for handling temporary files"""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    try:
        yield temp_file.name
    finally:
        temp_file.close()
        try:
            os.unlink(temp_file.name)
        except Exception:
            pass

def get_file_content_as_string(filepath: str) -> str:
    """Read file content as string"""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def get_file_download_link(file_content: str, filename: str, text: str) -> str:
    """Generate a download link for file content"""
    b64 = base64.b64encode(file_content.encode()).decode()
    mime_types = {
        'json': 'application/json',
        'xml': 'application/xml',
        'csv': 'text/csv'
    }
    extension = filename.split('.')[-1]
    mime_type = mime_types.get(extension, 'text/plain')
    href = f'<a href="data:{mime_type};base64,{b64}" download="{filename}">{text}</a>'
    return href

def main():
    st.title("Mock Test Data Generator")
    
    st.sidebar.header("Configuration")
    export_format = st.sidebar.selectbox(
        "Export Format",
        ["JSON", "CSV", "XML"]
    )
    
    record_count = st.sidebar.number_input(
        "Number of Records",
        min_value=1,
        max_value=1000,
        value=10
    )
    
    preview_count = min(5, record_count)  # Show at most 5 records in preview
    
    st.header("Define Fields")
    
    # Template selection
    template_type = st.selectbox(
        "Select Template",
        ["Custom", "User Data", "Financial Data"]
    )
    
    fields = []  # Initialize fields list
    
    if template_type == "Custom":
        num_fields = st.number_input("Number of Fields", min_value=1, max_value=10, value=3)
        
        for i in range(num_fields):
            st.subheader(f"Field {i+1}")
            col1, col2 = st.columns(2)
            
            with col1:
                field_name = st.text_input(f"Field Name", key=f"name_{i}")
                field_type = st.selectbox(
                    "Field Type",
                    [FieldTypes.STRING, FieldTypes.INTEGER, FieldTypes.FLOAT,
                     FieldTypes.EMAIL, FieldTypes.DATE, FieldTypes.BOOLEAN,
                     FieldTypes.NAME, FieldTypes.PHONE, FieldTypes.ADDRESS],
                    key=f"type_{i}"
                )
                
            with col2:
                nullable = st.checkbox("Nullable", key=f"null_{i}")
                if field_type in [FieldTypes.INTEGER, FieldTypes.FLOAT]:
                    min_value = st.number_input("Min Value", key=f"min_{i}", value=0)
                    max_value = st.number_input("Max Value", key=f"max_{i}", value=100)
                else:
                    min_value = None
                    max_value = None
                    
            if field_name:  # Only add field if name is provided
                fields.append(FieldDefinition(
                    name=field_name,
                    field_type=field_type,
                    min_value=min_value,
                    max_value=max_value,
                    nullable=nullable
                ))
    elif template_type == "User Data":
        user_template = UserTemplate()
        fields = list(user_template.get_template().values())
    elif template_type == "Financial Data":
        financial_template = FinancialTemplate()
        fields = list(financial_template.get_template().values())
    
    if st.button("Generate Data"):
        if not fields:
            st.error("Please define at least one field")
            return
            
        template = {field.name: field for field in fields if field.name}
        
        try:
            # Create appropriate generator
            if export_format == "JSON":
                generator = JSONGenerator()
            elif export_format == "XML":
                generator = XMLGenerator()
            else:  # CSV
                generator = CSVGenerator()
            
            # Generate data with specified record count
            generated_data = generator.generate(template, record_count)
            
            # Show preview
            st.subheader(f"Preview (showing {preview_count} of {record_count} records)")
            st.json(generated_data[:preview_count])
            
            # Show total records generated
            st.info(f"Total records generated: {len(generated_data)}")
            
            st.markdown("### Download Data")
            
            file_extension = export_format.lower()
            output_filename = f"mock_data.{file_extension}"
            
            # Use context manager for temporary file handling
            with temp_file_handler(f".{file_extension}") as temp_filepath:
                # Export data to temporary file
                generator.export(generated_data, temp_filepath)
                
                # Read content immediately after writing
                file_content = get_file_content_as_string(temp_filepath)
                
                # Create download link
                st.markdown(
                    get_file_download_link(
                        file_content,
                        output_filename,
                        f"Download {export_format}"
                    ),
                    unsafe_allow_html=True
                )
                
        except Exception as e:
            st.error(f"Error generating data: {str(e)}")
            st.exception(e)  # This will show the full traceback in development

if __name__ == "__main__":
    main()