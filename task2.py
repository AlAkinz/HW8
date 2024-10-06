import json
import glob
def merge_json_files(input_files, output_file):
    merged_data = []
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                merged_data.extend(data)
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON файла: {file}")
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4) 
if __name__ == "__main__":
    json_files = glob.glob('employees*.json')
    merge_json_files(json_files, 'all_employees.json')