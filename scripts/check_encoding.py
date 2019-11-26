import magic

blob_chunked = open('chunked/00000.jsonl').read()
blob_all = open('philarchive_pdfs_en.jsonl').read()
blob = blob_all
m = magic.Magic(mime_encoding=True)
encoding = m.from_buffer(blob)  # "utf-8" "us-ascii" etc
print(encoding)
