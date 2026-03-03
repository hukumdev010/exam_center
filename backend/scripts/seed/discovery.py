"""
Module for discovering categories and certifications from folder structure.
Handles recursive directory traversal and dynamic module loading.
"""
import glob
import importlib
import os


def discover_recursive(
    path,
    certifications_root,
    discovered_data,
    parent_slug=None,
    level=0,
):
    """
    Recursively discover categories and certifications.
    
    Args:
        path: Current directory path to scan
        certifications_root: Root directory for certifications
        discovered_data: Dictionary to accumulate discovered data
        parent_slug: Parent category slug for hierarchy
        level: Current nesting level
    """
    if not os.path.isdir(path):
        return
        
    folder_name = os.path.basename(path)
    if folder_name.startswith("__"):
        return
        
    # Check if this folder has a certifications.py file
    cert_file = os.path.join(path, "certifications.py")
    has_certifications = os.path.exists(cert_file)
    
    if has_certifications:
        # This is a category with certifications
        slug = folder_name.replace("_", "-")
        
        # Create category metadata
        category_data = {
            "name": folder_name.replace("_", " ").title(),
            "slug": slug,
            "description": (
                f"{folder_name.replace('_', ' ').title()} certifications"
            ),
            "parent_slug": parent_slug,
            "level": level
        }
        
        discovered_data["categories"][slug] = category_data
        
        # Load certifications from this folder
        try:
            relative_path = os.path.relpath(path, certifications_root)
            module_path = (
                f"scripts.seed_data.certifications."
                f"{relative_path.replace(os.sep, '.')}.certifications"
            )
            cert_module = importlib.import_module(module_path)
            
            if hasattr(cert_module, "CERTIFICATIONS"):
                # Update category slugs in certifications to match
                # discovered category
                for cert in cert_module.CERTIFICATIONS:
                    cert_copy = cert.copy()
                    cert_copy["category_slug"] = slug
                    
                    # Ensure all required fields have defaults
                    cert_copy.setdefault("is_active", True)
                    cert_copy.setdefault("level", "Beginner")
                    cert_copy.setdefault("duration", 60)
                    cert_copy.setdefault("questions_count", 10)
                    
                    discovered_data["certifications"].append(cert_copy)
                
                cert_count = len(cert_module.CERTIFICATIONS)
                print(f"  📋 {folder_name}: {cert_count} certifications")
                
                # Load questions if available
                if hasattr(cert_module, "ALL_QUESTIONS"):
                    discovered_data["questions"].update(
                        cert_module.ALL_QUESTIONS
                    )
                
                # Try to load individual certification files for questions
                for cert in cert_module.CERTIFICATIONS:
                    cert_slug = cert["slug"]
                    # Try to find individual certification file with questions
                    cert_files = glob.glob(os.path.join(path, "*.py"))
                    for cert_file_path in cert_files:
                        if (os.path.basename(cert_file_path) ==
                                "certifications.py"):
                            continue
                        if os.path.basename(cert_file_path).startswith("__"):
                            continue
                            
                        try:
                            cert_module_name = os.path.splitext(
                                os.path.basename(cert_file_path)
                            )[0]
                            cert_module_path = (
                                f"scripts.seed_data.certifications."
                                f"{relative_path.replace(os.sep, '.')}."
                                f"{cert_module_name}"
                            )
                            individual_cert_module = (
                                importlib.import_module(cert_module_path)
                            )
                            
                            has_cert = hasattr(
                                individual_cert_module, "CERTIFICATION"
                            )
                            has_qs = hasattr(
                                individual_cert_module, "QUESTIONS"
                            )
                            if has_cert and has_qs:
                                cert_check = (
                                    individual_cert_module.CERTIFICATION
                                    .get("slug") == cert_slug
                                )
                                if cert_check:
                                    discovered_data["questions"][
                                        cert_slug
                                    ] = individual_cert_module.QUESTIONS
                                    break
                        except ImportError:
                            continue
                            
        except ImportError as e:
            print(f"    ❌ Failed to load {folder_name}: {e}")
    
    # Recursively check subdirectories
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path) and not item.startswith("__"):
                if has_certifications:
                    current_slug = folder_name.replace("_", "-")
                else:
                    current_slug = parent_slug
                discover_recursive(
                    item_path, certifications_root, discovered_data,
                    current_slug, level + 1
                )
    except PermissionError:
        pass


def auto_discover_categories_and_certifications():
    """
    Auto-discover categories and certifications from folder structure.
    Each folder with certifications.py becomes a category.
    
    Returns:
        dict: Discovered data with categories, certifications, and questions
    """
    certifications_root = os.path.join(
        os.path.dirname(__file__), "..", "seed_data", "certifications"
    )
    
    discovered_data = {
        "categories": {},
        "certifications": [],
        "questions": {}
    }
    
    print(
        "📂 Auto-discovering categories and certifications from "
        "folder structure..."
    )
    discover_recursive(
        certifications_root, certifications_root, discovered_data
    )
    
    return discovered_data
