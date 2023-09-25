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

## valid_url(arg)
arg: string
return: True if url is valid/False

Example:
```python
from decode_things import decode

valid = decode.valid_url(url)
print(valid)
```

## online_url(arg)
arg: string (valid url) 
return: True if url is online/False

Example:
```python
from decode_things import decode

online = decode.online_url(url)
print(online)
```