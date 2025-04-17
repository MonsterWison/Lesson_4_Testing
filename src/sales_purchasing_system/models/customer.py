from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class CustomerAddress(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    address_type: str  # e.g., "Billing", "Shipping", etc.
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: Optional[str] = None
    postal_code: str
    country: str
    is_default: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: Optional[datetime] = None
    last_modified_by: Optional[str] = None

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: str = Field(unique=True, index=True)
    short_name: str
    long_name: str
    contact_person: str
    contact_title: Optional[str] = None
    contact_department: Optional[str] = None
    telephone: str
    fax: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    payment_terms: str
    memo: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: Optional[datetime] = None
    last_modified_by: Optional[str] = None
    is_active: bool = Field(default=True)
    
    # Relationships
    addresses: List[CustomerAddress] = [] 