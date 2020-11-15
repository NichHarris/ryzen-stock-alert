# import json
# with open('sites.json', 'r') as f:
#     sites = json.load(f)

import subprocess
subprocess.run(['scrapy', 'crawl', 'amazon'])
print('here')

