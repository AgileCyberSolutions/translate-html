import json
import re
from bs4 import BeautifulSoup, NavigableString, Tag
import html as htmllib
from googletrans import Translator

def html_to_text(html):
    html = html.strip()
    soup = BeautifulSoup(html, 'html.parser')
    # Ignore anything in head
    body, text = soup.body, []
    heading_re = re.compile('^h\d+$')
    for element in body.descendants:
        if type(element) == NavigableString:
            parent_tags = (t for t in element.parents if type(t) == Tag)
            hidden = False
            for parent_tag in parent_tags:
                # Ignore any text inside a non-displayed tag
                # We also behave is if scripting is enabled (noscript is ignored)
                # The list of non-displayed tags and attributes from the W3C specs:
                if (parent_tag.name in ('area', 'base', 'basefont', 'datalist', 'head', 'link',
                                        'meta', 'noembed', 'noframes', 'param', 'rp', 'script',
                                        'source', 'style', 'template', 'track', 'title', 'noscript') or
                        parent_tag.has_attr('hidden') or
                        (parent_tag.name == 'input' and parent_tag.get('type') == 'hidden')):
                    hidden = True
                    break
            if hidden:
                continue

            # remove any multiple and leading/trailing whitespace
            string = ' '.join(element.string.split()).strip()
            if string:
                text.append(str(string))
    #sort - or smaller text will get replaced in larger texts
    text.sort(key = len, reverse=True)
    #form a key value pair strings from the given html
    doc = dict()       
    for value in text:
        key = value.replace('  ','')
        doc[key] = value
    return doc

def text_to_translate(content):
    """translate the values from the given key value pair and 
     form a dict
    """
    language_locale = "ca" #here you can change the language
    translator = Translator()
    a_dict = dict()
    for i, element in content.items():
        translation = translator.translate(element, dest=language_locale) 
        a_dict[element] = translation.text
    return a_dict

if __name__ == '__main__':
    fp = open("test.html", "r")
    html = fp.read()
    fp.close()
    #parsing html file
    soup = BeautifulSoup(html, 'html.parser')
    html = str(soup.prettify())
    #replace leading and trailing spaces
    html = ' '.join(html.split()).strip()
    while '  ' in html:
        html = html.replace('  ', ' ')
    content = html_to_text(html)
    fields =  text_to_translate(content)
    #replace the translated strings in the original content
    for f_key, f_value in fields.items():
        if f_key != f_value:
            html = html.replace(str(f_key), f_value)
            html = html.replace(htmllib.escape(str(f_key)), f_value)
    #writes the translated content in another file
    f1 = open('output.html', 'w')
    f1.write(html)
    f1.close()
    print('check output html')