import visionapi
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

for (i,data) in enumerate(all_data):
    # Initialize the Inference Engine
    inference = visionapi.Inference()

    # Provide an image URL or a local path
    image = data['image_url']

    # Set your descriptive prompt
    prompt = " must guess the contry of the picture in a format of 'The country is: ', and must guess the tiem of the picture in a format of 'The time is: ' "

    # Get the AI's perspective
    response = inference.image(image, prompt)
    print('response')
    # Revel in the AI-generated description
    print(response.message.content)

    ## print gold location 
    print('gold location')
    print(data['gold_location'])
    ## print gold time
    print('gold time')
    print(data['gold_time'])
    if i>3:
        break
