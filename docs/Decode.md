# Modul: Decode

## domain(url)
arg: string (valid url)

return: https://github.com => github

Example:
```python
from decode_things import decode

domain = decode.domain(url)
print(domain)
```

## censor(string)
arg: string

return: arg withoud vowels

Example:
```python
from decode_things import decode

censor = decode.censor(string)
print(censor)
```

## valid_url(url)
arg: string

return: True if url is valid/False

Example:
```python
from decode_things import decode

valid = decode.valid_url(url)
print(valid)
```

## online_url(url)
arg: string (valid url) 

return: True if url is online/False

Example:
```python
from decode_things import decode

online = decode.online_url(url)
print(online)
```

## xml_json(path, arg='output.json')
arg1: string (path to .xml file)

arg2: string (name of output.json file, default=output.json)

return: None (ouput.json file will be created)

Example:
```python
from decode_things import decode

decode.xml_json('path/to/xml/file.xml', 'name.json')
```

