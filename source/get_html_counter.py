from collections import Counter

import requests

result = requests.get('https://python.org')
print(Counter(result.text.strip()))  # Можно через Selenium получить фулл DOM со всеми JS и их тоже включить :)
