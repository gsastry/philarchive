import ftfy
import json
import os

from tqdm import tqdm

# This script runs `ftfy` to remove mojibake from converted `philarchive` text

def load_jsonl(input_path) -> list:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data

def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path))

def fix_text(filepath, output_path):
    """
        Given a `jsonl` file, just runs ftfy on it.
    """
    raw_data = load_jsonl(filepath)
    fixed_data = []

    for js_obj in tqdm(raw_data):
        raw_text = js_obj['text']
        # 1. Split by line break
        # 2. Remove extra whitespace within each line
        # 3. Join all lines into one line, separated by \n
        fixed_text = '\n'.join([ ' '.join(s.split()) for s in raw_text.splitlines() ])
        # 4. Remove mujibake
        fixed_text = ftfy.fix_text(fixed_text)
        fixed_data.append({ 'metadata': js_obj['metadata'], 'text': fixed_text })
    dump_jsonl(fixed_data, output_path)

if __name__ == "__main__":
    input_path = os.path.expanduser('~/data/philarchive/philarchive_pdfs_docs.jsonl')
    output_path = os.path.expanduser('~/data/philarchive/philarchive_pdfs_docs_fixed_v4.jsonl')
    fix_text(input_path, output_path)