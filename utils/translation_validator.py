"""
Translation Key Validator
Ensures all locales have consistent translation keys
"""
import json
import os
from pathlib import Path
from typing import Dict, List, Set

def load_translation(filepath: Path) -> Dict:
    """Load translation JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def flatten_keys(data: Dict, parent_key: str = '', sep: str = '.') -> Set[str]:
    """Flatten nested dictionary keys"""
    keys = set()
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            keys.update(flatten_keys(v, new_key, sep=sep))
        else:
            keys.add(new_key)
    return keys

def validate_translation_keys(base_locale: str = 'en-US') -> List[str]:
    """
    Validate all locales have same keys as base locale
    Returns list of errors
    """
    locales_dir = Path('locales')
    base_file = locales_dir / base_locale / 'common.json'
    
    if not base_file.exists():
        return [f"Base locale file not found: {base_file}"]
    
    base_data = load_translation(base_file)
    base_keys = flatten_keys(base_data)
    
    errors = []
    
    for locale_dir in locales_dir.iterdir():
        if not locale_dir.is_dir() or locale_dir.name == base_locale:
            continue
        
        locale_file = locale_dir / 'common.json'
        if not locale_file.exists():
            errors.append(f"Missing translation file: {locale_file}")
            continue
        
        locale_data = load_translation(locale_file)
        locale_keys = flatten_keys(locale_data)
        
        # Find missing and extra keys
        missing = base_keys - locale_keys
        extra = locale_keys - base_keys
        
        if missing:
            errors.append(f"{locale_dir.name} missing keys: {sorted(missing)}")
        
        if extra:
            errors.append(f"{locale_dir.name} extra keys: {sorted(extra)}")
    
    return errors

if __name__ == '__main__':
    errors = validate_translation_keys()
    if errors:
        print("❌ Translation validation failed:")
        for error in errors:
            print(f"  - {error}")
        exit(1)
    else:
        print("✅ All translations are valid!")
        exit(0)
