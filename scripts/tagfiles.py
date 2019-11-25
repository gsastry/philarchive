import os
import pprint
from collections import defaultdict

import filetype
import magic

DIRNAME = os.path.dirname(__file__)
DATA_DIR = os.path.join(DIRNAME, os.path.abspath('..'), "data")
UNTAGGED_DIR = os.path.join(DATA_DIR, "untagged")
TAGGED_DIR = os.path.join(DATA_DIR, "tagged")

def tag(): 
    kind_to_counts = defaultdict(int)

    for fname in os.listdir(UNTAGGED_DIR):
        fpath = os.path.join(UNTAGGED_DIR, fname)
        try: 
            kind = magic.from_file(fpath, mime=True)
        except UnicodeDecodeError:
            kind = "probably docx"

        if('Microsoft' in kind or 'Windows' in kind):
            kind = 'probably docx'
        elif 'msword' in kind:
            # fpath_new = os.path.join(f"{TAGGED_DIR}", f"{fname}.doc")
            # print(fpath_new)
            # os.rename(fpath, fpath_new)
        elif 'PDF document' or 'pdf' in kind:
            # fpath_new = os.path.join(f"{TAGGED_DIR}", f"{fname}.pdf")
            # print(fpath_new)
            # os.rename(fpath, fpath_new)
        kind_to_counts[kind] += 1
    pprint.pprint(kind_to_counts)

if __name__ == "__main__":
    tag()
