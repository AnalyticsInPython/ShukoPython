import os
from pathlib import Path
from datetime import datetime, timedelta
import random

def create_test_data(count=500, output_dir="/Users/apple/Fall2026/test_data"):
    """
    Generate test data files with random company names and dates.
    
    Args:
        count: Number of test files to create
        output_dir: Directory to store test files
    """
    
    # Clean up existing files
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # List of company names
    companies = [
        "Apple", "Google", "Microsoft", "Amazon", "Tesla", 
        "Meta", "Netflix", "Adobe", "Intel", "Nvidia",
        "Oracle", "Salesforce", "IBM", "Cisco", "Qualcomm",
        "AMD", "Broadcom", "Zoom", "Shopify", "Spotify"
    ]
    
    # File extensions
    extensions = ["csv", "xlsx", "xls", "json", "txt"]
    
    # Base date
    base_date = datetime(2020, 1, 1)
    
    created_count = 0
    
    print(f"Creating {count} test files in {output_path}...")
    print("-" * 60)
    
    for i in range(count):
        # Random company
        company = random.choice(companies)
        
        # Random date between 2020-2026
        days_offset = random.randint(0, 2500)
        random_date = base_date + timedelta(days=days_offset)
        date_str = random_date.strftime("%Y%m%d")
        
        # Random extension
        extension = random.choice(extensions)
        
        # File name
        filename = f"{company}_{date_str}.{extension}"
        filepath = output_path / filename
        
        # Create empty file
        filepath.touch()
        created_count += 1
        
        if (i + 1) % 100 == 0:
            print(f"Created {i + 1}/{count} files...")
    
    print("-" * 60)
    print(f"Successfully created {created_count} test files!")

if __name__ == "__main__":
    create_test_data(500)
