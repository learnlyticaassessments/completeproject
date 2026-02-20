"""
Test Helper Functions
Common utilities for testing
"""
import os
import json
from pathlib import Path
from typing import Dict, Optional

def load_locale_data(locale: str, file: str = 'common.json') -> Dict:
    """Load translation data for a specific locale"""
    filepath = Path(f'locales/{locale}/{file}')
    if not filepath.exists():
        raise FileNotFoundError(f"Translation file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_translation(locale: str, key: str) -> Optional[str]:
    """Get translation for a specific key"""
    data = load_locale_data(locale)
    keys = key.split('.')
    
    for k in keys:
        if isinstance(data, dict):
            data = data.get(k)
        else:
            return None
    
    return data

def get_env(key: str, default: str = '') -> str:
    """Get environment variable"""
    return os.getenv(key, default)

def is_rtl_locale(locale: str) -> bool:
    """Check if locale uses RTL text direction"""
    rtl_locales = ['ar-SA', 'he-IL', 'fa-IR', 'ur-PK']
    return locale in rtl_locales

def get_expected_date_format(locale: str) -> str:
    """Get expected date format for locale"""
    formats = {
        'en-US': 'MM/DD/YYYY',
        'es-ES': 'DD/MM/YYYY',
        'fr-FR': 'DD/MM/YYYY',
        'de-DE': 'DD.MM.YYYY',
        'ja-JP': 'YYYY/MM/DD',
        'ar-SA': 'DD/MM/YYYY'
    }
    return formats.get(locale, 'MM/DD/YYYY')

def get_expected_currency_symbol(locale: str) -> str:
    """Get expected currency symbol for locale"""
    symbols = {
        'en-US': '$',
        'es-ES': '€',
        'fr-FR': '€',
        'de-DE': '€',
        'ja-JP': '¥',
        'ar-SA': 'ر.س'
    }
    return symbols.get(locale, '$')
