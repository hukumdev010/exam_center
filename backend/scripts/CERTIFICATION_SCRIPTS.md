# Certification Management Scripts

This directory contains several scripts to manage certification question counts and durations in the exam center application.

## Scripts Overview

### 1. `show_certification_stats.py`
Shows current statistics for all certification files without making any changes.

**Usage:**
```bash
python scripts/show_certification_stats.py
```

**Features:**
- Displays question counts (defined vs actual)
- Shows duration calculations (3 minutes per question)
- Groups statistics by category and level
- Indicates which files need updates

### 2. `update_certification_files.py`
Updates certification files with accurate question counts and calculated durations.

**Usage:**
```bash
python scripts/update_certification_files.py
```

**Features:**
- Scans all certification files for questions
- Updates `questions_count` and `duration` fields
- Uses 3 minutes per question for duration calculation
- Shows detailed progress and summary

### 3. `update_certification_files_robust.py`
A more robust version of the updater with better pattern matching.

**Usage:**
```bash
python scripts/update_certification_files_robust.py
```

**Features:**
- Improved regex patterns for various file formats
- Better error handling
- Handles edge cases in file formatting

### 4. `update_stats_simple.py`
A simple database updater (updates database records instead of files).

**Usage:**
```bash
python scripts/update_stats_simple.py
```

**Features:**
- Updates certification records in the database
- Runs automatically without user prompts
- Useful for production deployments

## Configuration

### Duration Calculation
All scripts use **3 minutes per question** as the standard duration calculation:
```python
MINUTES_PER_QUESTION = 3
```

To change this, modify the constant at the top of each script.

### File Structure
Scripts expect certification files to follow this structure:
```python
CERTIFICATION = {
    "name": "Certification Name",
    "description": "Description",
    "slug": "certification-slug",
    "level": "Professional",
    "duration": 180,           # Will be updated
    "questions_count": 60,     # Will be updated
    "category_slug": "category",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Question text...",
        "answers": [...]
    },
    # More questions...
]
```

## Workflow

1. **Check current status:**
   ```bash
   python scripts/show_certification_stats.py
   ```

2. **Update files if needed:**
   ```bash
   python scripts/update_certification_files.py
   ```

3. **Verify updates:**
   ```bash
   python scripts/show_certification_stats.py
   ```

4. **Seed database with updated data:**
   ```bash
   python scripts/seed.py
   ```

## Output Examples

### Stats Display
```
📊 CERTIFICATION FILES STATISTICS
Certification Name                            Category     Level        Q-Def Q-Act D-Def D-Cal Status
AWS Certified Solutions Architect - Professional aws      Professional 290   290   870   870   ✓ OK
Azure Fundamentals                            azure        Foundational 15    15    45    45    ✓ OK
CompTIA Security+                            cybersecurity Entry        10    10    30    30    ✓ OK
```

### Update Summary
```
📊 SUMMARY:
   Total files processed: 116
   Files updated: 80
   Total questions found: 5415
   Average questions per certification: 46.7
```

## Notes

- Scripts automatically skip files without questions (shows "⚠️ No questions found")
- Files already up-to-date are marked as "✓ Already correct"
- Duration is always calculated as `questions_count * 3` minutes
- The scripts preserve all other certification metadata unchanged

## Troubleshooting

If a file isn't updating properly:
1. Check the file format matches the expected structure
2. Ensure the CERTIFICATION dictionary uses double quotes
3. Try the robust updater for better pattern matching
4. Manually verify the QUESTIONS array format

## Dependencies

- Python 3.6+
- Standard library only (no external dependencies)
- Access to the certification files directory structure
