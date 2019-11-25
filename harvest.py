from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

import os

def harvest(url):
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)

    client = Client(url, registry)
    client.ignoreBadCharacters(true_or_false=True)

    identifiers = []
    for header in client.listIdentifiers(metadataPrefix='oai_dc'):
        # if (not(header.isDeleted())):
        print(f"Found identifier {header.identifier()}")
        identifiers.append(header.identifier())
        # else:
        #     print(f"Skipping (DELETED) identifier {header.identifier()}")
    
    print(f"Total number of identifiers: {len(identifiers)}")

    # Only get the identifier string at the end of the url
    identifiers = [ x.split('/')[-1] for x in identifiers ]

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'philarchive-2.txt')

    with open(filename, 'w') as f:
        print(f"Writing to {filename}")
        f.writelines('\n'.join(identifiers))

if __name__ == "__main__":
    url = 'https://philarchive.org/oai.pl'
    harvest(url)