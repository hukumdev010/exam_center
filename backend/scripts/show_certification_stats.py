#!/usr/bin/env python3
"""
Show current certification file statistics without updating.
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple


def find_certification_files(base_path: str) -> List[str]:
    """Find all certification Python files"""
    certification_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                certification_files.append(os.path.join(root, file))

    return certification_files


def get_certification_stats(file_path: str) -> Dict:
    """Get certification stats from file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        stats = {
            "name": "Unknown",
            "questions_count_defined": 0,
            "duration_defined": 0,
            "actual_questions": 0,
            "calculated_duration": 0,
            "level": "Unknown",
            "category": "Unknown",
        }

        # Extract CERTIFICATION dictionary info
        cert_match = re.search(
            r"CERTIFICATION\s*=\s*(\{[^}]*\})",
            content,
            re.DOTALL)
        if cert_match:
            cert_str = cert_match.group(1)

            # Extract individual fields
            name_match = re.search(r'"name":\s*"([^"]*)"', cert_str)
            if name_match:
                stats["name"] = name_match.group(1)

            questions_match = re.search(
                r'"questions_count":\s*(\d+)', cert_str)
            if questions_match:
                stats["questions_count_defined"] = int(
                    questions_match.group(1))

            duration_match = re.search(r'"duration":\s*(\d+)', cert_str)
            if duration_match:
                stats["duration_defined"] = int(duration_match.group(1))

            level_match = re.search(r'"level":\s*"([^"]*)"', cert_str)
            if level_match:
                stats["level"] = level_match.group(1)

            category_match = re.search(
                r'"category_slug":\s*"([^"]*)"', cert_str)
            if category_match:
                stats["category"] = category_match.group(1)

        # Count actual questions
        questions_match = re.search(
            r"QUESTIONS\s*=\s*\[(.*)\]", content, re.DOTALL)
        if questions_match:
            questions_content = questions_match.group(1)
            # Count question objects by looking for the pattern:
            # {
            #     "text": "question text",
            #     "explanation": ...
            # This pattern is more specific than just counting "text" fields
            # which would include answer choices too
            question_pattern = r'{\s*"text":\s*"[^"]*",\s*"explanation":'
            stats["actual_questions"] = len(
                re.findall(question_pattern, questions_content, re.DOTALL)
            )

        stats["calculated_duration"] = stats["actual_questions"] * 3

        return stats

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}


def main():
    """Main function"""
    print("📊 CERTIFICATION FILES STATISTICS")
    print("=" * 100)

    # Find all certification files in all categories
    base_path = Path(__file__).parent / "seed_data" / "certifications"
    certification_files = find_certification_files(str(base_path))

    if not certification_files:
        print("No certification files found!")
        return

    # Header
    print(
        f"{'Certification Name':<45} {'Category':<12} {'Level':<12} {'Q-Def':<5} {'Q-Act':<5} {'D-Def':<5} {'D-Cal':<5} {'Status'}"
    )
    print("-" * 100)

    stats_summary = {
        "total_files": 0,
        "needs_update": 0,
        "total_questions": 0,
        "total_duration": 0,
        "by_category": {},
        "by_level": {},
    }

    # Process each file
    for file_path in sorted(certification_files):
        stats = get_certification_stats(file_path)
        if not stats:
            continue

        stats_summary["total_files"] += 1
        stats_summary["total_questions"] += stats["actual_questions"]
        stats_summary["total_duration"] += stats["calculated_duration"]

        # Track by category
        category = stats["category"]
        if category not in stats_summary["by_category"]:
            stats_summary["by_category"][category] = 0
        stats_summary["by_category"][category] += 1

        # Track by level
        level = stats["level"]
        if level not in stats_summary["by_level"]:
            stats_summary["by_level"][level] = 0
        stats_summary["by_level"][level] += 1

        # Check if update needed
        needs_update = (
            stats["questions_count_defined"] != stats["actual_questions"]
            or stats["duration_defined"] != stats["calculated_duration"]
        )

        if needs_update:
            stats_summary["needs_update"] += 1
            status = "⚠️ NEEDS UPDATE"
        else:
            status = "✓ OK"

        # Format name to fit column
        name = stats["name"][:42] + \
            "..." if len(stats["name"]) > 45 else stats["name"]

        print(
            f"{name:<45} {category:<12} {level:<12} {stats['questions_count_defined']:<5} {stats['actual_questions']:<5} {stats['duration_defined']:<5} {stats['calculated_duration']:<5} {status}"
        )

    # Summary
    print("-" * 100)
    print(f"\n📈 SUMMARY:")
    print(f"   Total certification files: {stats_summary['total_files']}")
    print(f"   Files needing updates: {stats_summary['needs_update']}")
    print(
        f"   Files up to date: {stats_summary['total_files'] - stats_summary['needs_update']}"
    )
    print(f"   Total questions: {stats_summary['total_questions']}")
    print(
        f"   Total calculated duration: {stats_summary['total_duration']} minutes ({stats_summary['total_duration']/60:.1f} hours)"
    )

    if stats_summary["total_files"] > 0:
        print(
            f"   Average questions per certification: {stats_summary['total_questions'] / stats_summary['total_files']:.1f}"
        )
        print(
            f"   Average duration per certification: {stats_summary['total_duration'] / stats_summary['total_files']:.1f} minutes"
        )

    print(f"\n📂 BY CATEGORY:")
    for category, count in sorted(stats_summary["by_category"].items()):
        print(f"   {category}: {count} certifications")

    print(f"\n🎯 BY LEVEL:")
    for level, count in sorted(stats_summary["by_level"].items()):
        print(f"   {level}: {count} certifications")

    print("\n" + "=" * 100)


if __name__ == "__main__":
    main()
