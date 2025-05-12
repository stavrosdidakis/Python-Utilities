import json

# Load the JSON content from the file
with open('fx.txt', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract all 'utf8' segments across all events into one list
words = []
for event in data.get('events', []):
    if 'segs' in event:
        for seg in event['segs']:
            if 'utf8' in seg:
                token = seg['utf8'].strip()
                if token:  # skip empty strings or newline characters
                    words.append(token)

# Join all words with a single space into one continuous paragraph
full_text = ' '.join(words)

# Optional: fix spacing around punctuation
import re
full_text = re.sub(r'\s+([.,!?;:])', r'\1', full_text)

# Save the final output to a file
with open('extracted_text.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(full_text)
