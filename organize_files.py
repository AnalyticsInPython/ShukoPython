import os
import re
import shutil
from pathlib import Path
from datetime import datetime

def organize_files(source_dir, output_dir="processed"):
    """
    Organize files from CompanyName_yyyymmdd.extension format
    into processed/yyyy/mm/dd/ folder structure.
    
    Args:
        source_dir: Source directory containing files
        output_dir: Root output directory name
    """
    
    source_path = Path(source_dir)
    output_root = source_path.parent / output_dir
    
    # File name pattern: CompanyName_yyyymmdd.extension
    pattern = r'^(.+?)_(\d{8})\.(.+?)$'
    
    moved_count = 0
    error_count = 0
    
    print(f"Source directory: {source_path}")
    print(f"Output directory: {output_root}")
    print("-" * 60)
    
    for file in source_path.iterdir():
        if file.is_file():
            match = re.match(pattern, file.name)
            
            if match:
                company_name = match.group(1)
                date_str = match.group(2)
                extension = match.group(3)
                
                # Parse date
                try:
                    date_obj = datetime.strptime(date_str, "%Y%m%d")
                    year = date_obj.strftime("%Y")
                    month = date_obj.strftime("%m")
                    day = date_obj.strftime("%d")
                    
                    # Create output folder
                    output_folder = output_root / year / month / day
                    output_folder.mkdir(parents=True, exist_ok=True)
                    
                    # Move file
                    output_file = output_folder / file.name
                    shutil.move(str(file), str(output_file))
                    
                    print(f"✓ Moved: {file.name}")
                    print(f"  → {year}/{month}/{day}/")
                    moved_count += 1
                    
                except ValueError as e:
                    print(f"✗ Error processing {file.name}: Invalid date format")
                    error_count += 1
            else:
                print(f"✗ Skipped: {file.name} (doesn't match pattern)")
                error_count += 1
    
    print("-" * 60)
    print(f"Moved: {moved_count}, Errors: {error_count}")

if __name__ == "__main__":
    # Organize files in test_data folder
    organize_files("/Users/apple/Fall2026/test_data")
