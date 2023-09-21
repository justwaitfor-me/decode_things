def domain_name(url):
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

def assert_equals(arg1, arg2):
    if arg1 == arg2:
        print(f"passed! >>{arg1}<< == >>{arg2}<<")
    else:
        print(f"faild! >>{arg1}<< == >>{arg2}<<")

# TODO: check_url und class (domain_name.abc)


assert_equals(domain_name("http://google.com"), "google")
assert_equals(domain_name("http://google.co.jp"), "google")
assert_equals(domain_name("www.xakep.ru"), "xakep")
assert_equals(domain_name("https://youtube.com"), "youtube")
assert_equals(domain_name("http://google.com/support"), "google")
assert_equals(domain_name("xakep.ru"), "xakep")
assert_equals(domain_name("youtube.com/test"), "youtube")
assert_equals(domain_name("www.google.com/support"), "google")
assert_equals(domain_name("http://google.co.jp/test1/test2/test3"), "google")
assert_equals(domain_name("xakep"), "xakep")
