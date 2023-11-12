import json

# Replace 'file_path.jsonl' with the path to your JSONL file
file_path = '/home/ubuntu/AI_Agent/gold_dev.jsonl'

# Function to extract data from each JSON line
def extract_data_from_jsonl(line):
    data = json.loads(line)
    # Extract all the keys and values
    extracted_data = {key: data[key] for key in data}
    return extracted_data
all_data = []
# Read the JSONL file and process each line
with open(file_path, 'r') as file:
    for line in file:
        extracted_data = extract_data_from_jsonl(line)
        all_data.append(extracted_data)
        # Print or process the extracted data
        # print(extracted_data)
