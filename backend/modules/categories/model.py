from typing import List, Optional
from pydantic import BaseModel


class Answer(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int

    class Config:
        from_attributes = True


class Question(BaseModel):
    id: int
    text: str
    explanation: Optional[str]
    reference: Optional[str]
    certification_id: int
    answers: List[Answer]

    class Config:
        from_attributes = True


class SimpleCertification(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str]
    level: Optional[str]
    duration: Optional[int]
    questions_count: Optional[int]
    is_active: bool
    category_id: int

    class Config:
        from_attributes = True


class Category(BaseModel):
    id: int
    name: str
    description: Optional[str]
    slug: str
    icon: Optional[str]
    color: Optional[str]
    certifications: List[SimpleCertification] = []

    class Config:
        from_attributes = True


class SimpleCategory(BaseModel):
    id: int
    name: str
    description: Optional[str]
    slug: str
    icon: Optional[str]
    color: Optional[str]

    class Config:
        from_attributes = True


class CategoryGroup(BaseModel):
    """A top-level category with its subcategories"""
    parent: SimpleCategory
    children: List[SimpleCategory]

    class Config:
        from_attributes = True


class GroupedCategories(BaseModel):
    """Categories grouped by top-level parent categories"""
    groups: List[CategoryGroup]

    class Config:
        from_attributes = True


class PaginatedCertifications(BaseModel):
    certifications: List[SimpleCertification]
    total: int
    page: int
    per_page: int
    has_next: bool
    has_prev: bool

    class Config:
        from_attributes = True