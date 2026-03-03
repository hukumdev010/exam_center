#!/usr/bin/env python3
"""
Robust certification files updater with better pattern matching.
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

MINUTES_PER_QUESTION = 3


def find_certification_files(base_path: str) -> List[str]:
    """Find all certification Python files"""
    certification_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                certification_files.append(os.path.join(root, file))
    return certification_files


def count_questions_in_file(file_path: str) -> int:
    """Count questions in a certification file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Count questions in QUESTIONS list
        questions_match = re.search(
            r"QUESTIONS\s*=\s*\[(.*)\]", content, re.DOTALL)
        if not questions_match:
            return 0

        questions_content = questions_match.group(1)

        # Count question objects by looking for the pattern:
        # {
        #     "text": "question text",
        #     "explanation": ...
        # This pattern is more specific than just counting "text" fields
        # which would include answer choices too
        question_pattern = r'{\s*"text":\s*"[^"]*",\s*"explanation":'
        question_count = len(
            re.findall(
                question_pattern,
                questions_content,
                re.DOTALL))

        return question_count

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0


def update_certification_values(file_path: str, question_count: int) -> bool:
    """Update duration and questions_count in the certification file"""
    if question_count == 0:
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_duration = question_count * MINUTES_PER_QUESTION
        original_content = content

        # Update duration - use raw string and proper escaping
        content = re.sub(
            r'("duration":\s*)\d+',
            r"\g<1>" +
            str(new_duration),
            content)

        # Update questions_count - use raw string and proper escaping
        content = re.sub(
            r'("questions_count":\s*)\d+',
            r"\g<1>" +
            str(question_count),
            content)

        # If content changed, write it back
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def main():
    """Main function to update all certification files"""
    print("🔧 ROBUST CERTIFICATION FILES UPDATER")
    print("=" * 60)
    print(
        f"Duration calculation: {MINUTES_PER_QUESTION} minutes per question\n")

    # Find all certification files in all categories
    base_path = Path(__file__).parent / "seed_data" / "certifications"
    certification_files = find_certification_files(str(base_path))

    if not certification_files:
        print("No certification files found!")
        return

    print(
        f"Found {len(certification_files)} certification files in all categories\n")

    updated_count = 0

    # Process each file
    for file_path in sorted(certification_files):
        relative_path = os.path.relpath(file_path, base_path.parent.parent)
        cert_name = (
            os.path.basename(file_path).replace(
                ".py", "").replace(
                "_", " ").title())

        question_count = count_questions_in_file(file_path)

        if question_count > 0:
            updated = update_certification_values(file_path, question_count)

            if updated:
                updated_count += 1
                new_duration = question_count * MINUTES_PER_QUESTION
                print(f"✅ UPDATED: {cert_name}")
                print(
                    f"   Questions: {question_count}, Duration: {new_duration} minutes"
                )
                print(f"   File: {relative_path}")
                print()
            else:
                print(
                    f"✓ Already correct: {cert_name} ({question_count} questions)")
        else:
            print(f"⚠️  No questions: {cert_name}")

    print("=" * 60)
    print(f"📊 SUMMARY: Updated {updated_count} certification files")
    print("=" * 60)


if __name__ == "__main__":
    main()
