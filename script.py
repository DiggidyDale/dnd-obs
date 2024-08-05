import os
import json
import shutil

def update_file_paths(json_file_path, new_directory):
    # Load the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Create the new directory if it does not exist
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    # Function to update file paths in the sources
    def update_sources(sources):
        for source in sources:
            if "name" in source and "settings" in source and "file" in source["settings"]:
                old_path = source["settings"]["file"]
                new_file_name = os.path.basename(old_path)
                
                # Check if the file name starts with "DALL"
                if new_file_name.startswith("DALL"):
                    new_file_name = f"{source['name']}{os.path.splitext(old_path)[1]}"
                
                new_path = os.path.join(new_directory, new_file_name)
                
                # Copy the file to the new directory
                shutil.copy(old_path, new_path)
                
                # Update the path in the JSON data
                source["settings"]["file"] = new_path

    # Check if the data has 'sources' and update them
    if "sources" in data:
        update_sources(data["sources"])

    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
json_file_path = 'test.json'
new_directory = 'images'
update_file_paths(json_file_path, new_directory)
