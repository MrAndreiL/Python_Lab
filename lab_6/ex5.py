import re 

def xml_task(xml_path, attrs):
    result = []
    try:
        fd = open(xml_path)
        list1 = re.findall("<\w+.*?>", fd.read())
        for tag in list1:
            matched = 0
            for item in attrs.items():
                if re.search(item[0]+"\s*=\s*"+item[1], tag):
                    matched += 1
            if matched > 0:
                result.append(tag)
    except Exception as e:
        print(e)
    return result

print(xml_task("test.xml", {"class": "url", "name": "url-form", "data-id": "item"} ))