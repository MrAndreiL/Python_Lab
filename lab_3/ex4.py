def build_xml_element(tag, content, href, clas, idi):
    return  "<" + tag + " href=\"" + href + "\" _class=\"" + clas + "\" id=\"" + idi + "\">" + content + "</" + tag + ">"

def main():
    print(build_xml_element("a", "Hello there", href="http://python.org", clas="my-link", idi="someid"))

if __name__ == "__main__":
    main()