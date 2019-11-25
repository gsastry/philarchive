
import os
import requests

from ratelimit import limits, sleep_and_retry

DIRNAME = os.path.dirname(__file__)
RATELIMIT_PERIOD = 4 # 10 seconds
ERROR_IDS = []
SUCCESS_IDS = []

def download_pdf(url):
    print(f"Downloading: {url}")
    file_name_start_pos = url.rfind("/") + 1
    identifier = url[file_name_start_pos:]
    pdf_filename = os.path.join(DIRNAME, 'pdfs', identifier)

    response = requests.get(url, stream=True)

    if(response.status_code == 200):
        print(response.headers['content-type'])
        SUCCESS_IDS.append(identifier)
        with open(pdf_filename, 'wb') as f:
            f.write(response.content)
        print(f"Succesfully downloaded pdf from {url}")
    else:
        print(f"Got error response status {response.status_code} for url {url}")
        ERROR_IDS.append(identifier)



@sleep_and_retry
@limits(calls=1, period=RATELIMIT_PERIOD)
def process_line(line):
    base_url = 'https://philarchive.org/archive'
    url = f"{base_url}/{line}".strip()

    download_pdf(url)

    return url

if __name__ == "__main__":

    identifiers_file = os.path.join(DIRNAME, 'data/philarchive_shuffled.txt')
    start_line = 5304

    p = 0 
    with open(identifiers_file) as f:
        # Skip to `start_line`
        for i in range(start_line):
            f.readline()
        for line in f:
            process_line(line) 

            # print every 10 lines
            if(p % 10 ==0):
                print(f"Total: {len(SUCCESS_IDS) + len(ERROR_IDS)} Success: {len(SUCCESS_IDS)} Failure: {len(ERROR_IDS)}")
            p +=1
