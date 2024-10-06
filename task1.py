import os
import json
import csv
import pickle
def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size
def traverse_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)
            result.append({
                'name': name,
                'path': path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
                })
    return result
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'path', 'type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)
def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
def main(directory):
    data = traverse_directory(directory)
    save_to_json(data, 'directory_info.json')
    save_to_csv(data, 'directory_info.csv')
    save_to_pickle(data, 'directory_info.pkl')
if __name__ == "__main__":
    main('your_directory')
