import sys
import os
import importlib

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test loading individual certification files
def test_loading():
    certifications_root = os.path.join(os.path.dirname(__file__), 'seed_data', 'certifications')
    
    # Test Azure category
    category_folder = 'azure'
    category_path = os.path.join(certifications_root, category_folder)
    
    import glob
    cert_files = glob.glob(os.path.join(category_path, '*.py'))
    print(f"Found {len(cert_files)} files in {category_folder}")
    
    for cert_file in cert_files:
        if os.path.basename(cert_file).startswith('__'):
            continue
            
        cert_module_name = os.path.splitext(os.path.basename(cert_file))[0]
        cert_module_path = f'seed_data.certifications.{category_folder}.{cert_module_name}'
        print(f"Trying to import: {cert_module_path}")
        
        try:
            cert_module = importlib.import_module(cert_module_path)
            
            if hasattr(cert_module, 'CERTIFICATION'):
                print(f"  ✅ {cert_module_name}: Found CERTIFICATION")
                print(f"     Name: {cert_module.CERTIFICATION['name']}")
            else:
                print(f"  ❌ {cert_module_name}: No CERTIFICATION attribute")
                
            if hasattr(cert_module, 'QUESTIONS'):
                print(f"  ✅ {cert_module_name}: Found QUESTIONS ({len(cert_module.QUESTIONS)} questions)")
            else:
                print(f"  ❌ {cert_module_name}: No QUESTIONS attribute")
                
        except ImportError as e:
            print(f"  ❌ Failed to import {cert_module_name}: {e}")
        except Exception as e:
            print(f"  ❌ Error with {cert_module_name}: {e}")

if __name__ == "__main__":
    test_loading()
