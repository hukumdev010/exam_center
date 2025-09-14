#!/usr/bin/env python3
"""Count total certifications in the organized seed data structure"""

import glob
import importlib
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def count_organized_certifications():
    """Count and display certification statistics from organized structure"""
    print("🔢 ORGANIZED CERTIFICATION STATISTICS")
    print("=" * 60)

    certifications_root = os.path.join(
        os.path.dirname(__file__), "seed_data", "certifications"
    )

    total_certifications = 0
    total_questions = 0
    category_stats = {}

    # Get all category folders
    category_folders = [
        f
        for f in os.listdir(certifications_root)
        if os.path.isdir(os.path.join(certifications_root, f))
        and not f.startswith("__")
    ]

    for category_folder in category_folders:
        try:
            # Try to load organized structure first
            module_path = f"seed_data.certifications.{category_folder}"
            category_module = importlib.import_module(module_path)

            if hasattr(category_module, "CERTIFICATIONS"):
                cert_count = len(category_module.CERTIFICATIONS)
                question_count = 0

                if hasattr(category_module, "ALL_QUESTIONS"):
                    for cert_slug, questions in category_module.ALL_QUESTIONS.items():
                        question_count += len(questions)

                category_stats[category_folder] = {
                    "certifications": cert_count,
                    "questions": question_count,
                    "type": "organized",
                }

        except ImportError:
            # Fallback: try individual files
            category_path = os.path.join(certifications_root, category_folder)
            cert_files = glob.glob(os.path.join(category_path, "*.py"))

            cert_count = 0
            question_count = 0

            for cert_file in cert_files:
                if os.path.basename(cert_file).startswith("__"):
                    continue

                try:
                    cert_module_name = os.path.splitext(os.path.basename(cert_file))[0]
                    cert_module_path = (
                        f"seed_data.certifications.{category_folder}.{cert_module_name}"
                    )
                    cert_module = importlib.import_module(cert_module_path)

                    if hasattr(cert_module, "CERTIFICATION"):
                        cert_count += 1

                        if hasattr(cert_module, "QUESTIONS") and cert_module.QUESTIONS:
                            question_count += len(cert_module.QUESTIONS)

                except ImportError:
                    continue

            if cert_count > 0:
                category_stats[category_folder] = {
                    "certifications": cert_count,
                    "questions": question_count,
                    "type": "individual",
                }

    # Display results
    for category, stats in sorted(category_stats.items()):
        cert_count = stats["certifications"]
        question_count = stats["questions"]
        cert_type = stats["type"]

        total_certifications += cert_count
        total_questions += question_count

        category_name = category.replace("_", " ").title()
        type_indicator = "📁" if cert_type == "organized" else "📄"

        print(
            f"{type_indicator} {category_name}: {cert_count} certifications, {question_count} sample questions"
        )

    print("=" * 60)
    print(
        f"🎯 TOTAL: {total_certifications} certifications with {total_questions} sample questions"
    )
    print("=" * 60)

    # Check if we have enough certifications
    if total_certifications >= 30:
        print(
            f"✅ SUCCESS: We have {total_certifications} certifications (30+ requirement met!)"
        )
    else:
        print(f"❌ Need more: Only {total_certifications} certifications (need 30+)")

    # Show new categories
    new_categories = [
        cat for cat in category_stats.keys() if cat in ["linux", "system_design"]
    ]
    if new_categories:
        print(f"\n🆕 NEW CATEGORIES ADDED:")
        for cat in new_categories:
            stats = category_stats[cat]
            cat_name = cat.replace("_", " ").title()
            print(f"   • {cat_name}: {stats['certifications']} certifications")


if __name__ == "__main__":
    count_organized_certifications()
