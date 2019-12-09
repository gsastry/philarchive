# philarchive
This repo contains instructions to download ~30k philosophy papers via https://philarchive.org/help/oai.html.

# Installation

1. Install https://github.com/gsastry/pyoai
2. Run `python harvest.py` to download identifier strings, which are strings of 5 letters identifying a document.
3. Shuffle your identifiers, e.g. `sort -R philarchive.txt > philarchive_shuffled.txt`
4. Run `python download.py` to download the raw files based on the identifiers. (this shuffling can happen after the raw files are downloaded as file)
5. Run `python textify.py` to convert the pdfs and docs to text. (you will probably have to lightly edit this to work correctly)
6. Run `python scripts/fix_text.py` to remove mojibake from the text and compress whitespace.

# More details

- IMPORTANT: http://philpapers.org will go down if you exceed a rate limit of 2 requests a second!
- The downloader doesn't currently grab the filetype at download time
- `scripts/tagfiles.py` is a script to append a filetype to the downloaded files (you will likely have to lightly edit this to work correctly).
- `scripts/check.py` is a script that checks the encoding of the data after shuffling (you probably won't ever have to use this, but I had a bug after shuffling. Also checks that it's valid JSON.

