def domain(url):
    if "https://" in url:
        if "https://www." in url:
            change = url[12:]
        elif not "https://www." in url:
            change = url[8:]
        else:
            change = None
    elif "http://" in url:
        if "http://www." in url:
            change = url[11:]
        elif not "https://www." in url:
            change = url[7:]
        else:
            change = None
    else:
        if "www." in url:
            change = url[4:]
        elif not "www." in url:
            change = url
        else:
            change = None
    
    if change != None:
        if not "/" in change and not "." in change:
            return change
        else:
            end = ""
            for i in change:
                if i != "/" and i != ".":
                    end += i
                else:
                    break
            return end
            
    else:
        return "pleas enter a valid url!"
    
def censor(string):
    # TODO errors vermeiden
    exp = ['a', 'e', 'i', 'o', 'u', 'y']
    res  = ""
    for i in string:
        if not i.lower() in exp:
            res += i    
    return res

