import docx
import json
import glob
import os
import pdftotext
import pprint
from collections import defaultdict

from langdetect import detect
from tika import language, parser
from tqdm import tqdm

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter

DIRNAME = os.path.dirname(__file__)
DATA_DIR = os.path.expanduser('~/data/philarchive/raw')

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

def get_languages(data_path):
    languages_dict = defaultdict(int)

    i = 0
    for filepath in tqdm(glob.iglob(f"{data_path}/*.pdf")):
        if i == 3000:
            break
        with open(filepath, "rb") as f:
            try:
                text = '\n\n'.join(pdftotext.PDF(f))
            except Exception as e:
                print(e)
            try:
                lang = detect(text)
                languages_dict[lang] += 1
            except Exception as e:
                print(e)
        i += 1
    languages_dict = { k : v/total * 100 for total in (sum(languages_dict.values()),) for k,v in languages_dict.items()}
    pprint.pprint(languages_dict) 

def doc2text(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def textify(data_path): 
    documents = []
    for filepath in tqdm(glob.iglob(f"{data_path}/*.pdf")): 
        with open(filepath, "rb") as f:
            try:
                text = '\n\n'.join(pdftotext.PDF(f))
                try:
                    # lang = detect(text)
                    # if lang == 'en':
                    identifier = os.path.basename(filepath)
                    documents.append({ 
                        'metadata': {
                            'id': identifier
                        },
                        'text': text 
                    })
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

    for filepath in tqdm(glob.iglob(f"{data_path}/*.doc*")): 
        with open(filepath, "rb") as f:
            try:
                text = doc2text(filepath)
                try:
                    # lang = detect(text)
                    # if lang == 'en':
                    identifier = os.path.basename(filepath)
                    documents.append({ 
                        'metadata': {
                            'id': identifier
                        },
                        'text': text 
                    })
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    return documents
        
if __name__ == "__main__":
    documents = textify(data_path=DATA_DIR)
    dump_jsonl(documents, os.path.expanduser('~/data/philarchive/philarchive_pdfs_docs.jsonl'))
