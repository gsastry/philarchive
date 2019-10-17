from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

def harvest(url):
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)

    client = Client(url, registry)
    client.ignoreBadCharacters(true_or_false=True)

    n = 0

    identifiers = []
    for header in client.listIdentifiers(metadataPrefix='oai_dc'):
        identifiers.append(header.identifier())
    
    with open('philarchive.txt', 'w') as f:
        f.writelines('\n'.join(identifiers))

if __name__ == "__main__":
    url = 'https://philarchive.org/oai.pl'
    harvest(url)