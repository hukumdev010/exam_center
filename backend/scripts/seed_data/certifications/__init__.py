"""Certification Data Package"""

from . import information_technology


CERTIFICATIONS = []
ALL_QUESTIONS = {}

if hasattr(information_technology, 'CERTIFICATIONS'):
    CERTIFICATIONS.extend(information_technology.CERTIFICATIONS)


if hasattr(information_technology, 'ALL_QUESTIONS'):
    ALL_QUESTIONS.update(information_technology.ALL_QUESTIONS)