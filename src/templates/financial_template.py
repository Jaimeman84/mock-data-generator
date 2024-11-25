# src/templates/financial_template.py
from typing import Dict
from .base_template import BaseTemplate
from ..data_types.field_types import FieldDefinition, FieldTypes

class FinancialTemplate(BaseTemplate):
    def get_name(self) -> str:
        return "Financial Data"
    
    def get_template(self) -> Dict[str, FieldDefinition]:
        return {
            "transaction_id": FieldDefinition(
                name="transaction_id",
                field_type=FieldTypes.STRING,
                pattern="TRX[0-9]{10}"
            ),
            "amount": FieldDefinition(
                name="amount",
                field_type=FieldTypes.FLOAT,
                min_value=0.01,
                max_value=10000.00
            ),
            "currency": FieldDefinition(
                name="currency",
                field_type=FieldTypes.STRING,
                choices=["USD", "EUR", "GBP", "JPY"]
            ),
            "transaction_date": FieldDefinition(
                name="transaction_date",
                field_type=FieldTypes.DATE
            ),
            "status": FieldDefinition(
                name="status",
                field_type=FieldTypes.STRING,
                choices=["completed", "pending", "failed"]
            ),
            "account_number": FieldDefinition(
                name="account_number",
                field_type=FieldTypes.STRING,
                pattern="[A-Z]{2}[0-9]{20}"
            )
        }