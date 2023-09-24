# Modul: Decode

## domain(arg)
arg: string (valid url)
return: https://github.com => github

Example:
```python
from decode_things import decode

domain = decode.domain(url)
print(domain)
```

## censor(arg)
arg: string
return: arg withoud vowels

Example:
```python
from decode_things import decode

censor = decode.censor(string)
print(censor)
```