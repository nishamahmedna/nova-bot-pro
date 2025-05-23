import os
import json

def find_broken_metadata_files(base_path):
    broken_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == "metadata.json":
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r") as f:
                        json.load(f)
                except json.JSONDecodeError as e:
                    broken_files.append((full_path, str(e)))
                except Exception as e:
                    broken_files.append((full_path, f"Other error: {str(e)}"))

    return broken_files

if __name__ == "__main__":
    pages_path = "pages"  # adjust if your path is different
    broken = find_broken_metadata_files(pages_path)

    if not broken:
        print("All metadata.json files are valid.")
    else:
        print("\n[!] Broken metadata.json files found:")
        for path, error in broken:
            print(f" - {path} --> {error}")
