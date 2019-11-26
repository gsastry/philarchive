# philarchive
philarchive data

# Installation

1. Install https://github.com/gsastry/pyoai
2. Run `python harvest.py` to download identifier strings, which are strings of 5 letters identifying a document.
3. Run `python download.py` to download the raw files based on the identifiers.
4. Shuffle your downloaded file, e.g. `sort -R philarchive.txt > philarchive_shuffled.txt`

# More details

The downloader doesn't currently grab the filetype at download time, and `scripts` contains one-off scripts to append a filetype to the downloaded files (you will likely have to lightly edit this to work correctly).
