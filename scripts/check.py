import json
import magic
import os


def check_encoding(filepath):
    # blob_chunked = open('chunked/00014.jsonl').read()
    blob_all = open(filepath).read()
    blob = blob_all
    m = magic.Magic(mime_encoding=True)
    encoding = m.from_buffer(blob)  # "utf-8" "us-ascii" etc
    print(encoding)
    return encoding

def check_json(filepath):
    print('Checking JSON...')
    with open(filepath) as f:
        for line in f:
            json.loads(line)
    print('JSON OK')
    return True

if __name__ == "__main__":
    filepath = os.path.expanduser('~/data/philarchive/philarchive_pdfs_docs_fixed_v3.jsonl')
    # check_encoding(filepath)
    check_json(filepath)


