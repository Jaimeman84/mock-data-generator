# src/data_types/constraints.py
from dataclasses import dataclass
from typing import Optional, Any, List

@dataclass
class Constraint:
    """Base class for field constraints"""
    message: str

@dataclass
class RangeConstraint(Constraint):
    min_value: Optional[Any] = None
    max_value: Optional[Any] = None

@dataclass
class PatternConstraint(Constraint):
    pattern: str

@dataclass
class ChoiceConstraint(Constraint):
    choices: List[Any]

@dataclass
class UniqueConstraint(Constraint):
    pass

def validate_constraints(value: Any, constraints: List[Constraint]) -> Optional[str]:
    """
    Validate a value against a list of constraints
    Returns error message if validation fails, None otherwise
    """
    for constraint in constraints:
        if isinstance(constraint, RangeConstraint):
            if constraint.min_value is not None and value < constraint.min_value:
                return constraint.message
            if constraint.max_value is not None and value > constraint.max_value:
                return constraint.message
        elif isinstance(constraint, PatternConstraint):
            if not re.match(constraint.pattern, str(value)):
                return constraint.message
        elif isinstance(constraint, ChoiceConstraint):
            if value not in constraint.choices:
                return constraint.message
                
    return None