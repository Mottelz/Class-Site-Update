#! /usr/local/bin/python3
from grabber import simple_get
from bs4 import BeautifulSoup
import hashlib
import json


# This gets the body of a given page
def get_string_of_page(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    raw_text = ''
    for element in html.find_all('body'):
        raw_text += element.text
    return raw_text


# This gets the md5 for a given string
def get_the_token(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


# Returns a dict
def get_json(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(json.loads(line))
    return data[0]


# These are the pages that I am checking. Change these to the ones you're checking
homepage = get_the_token(get_string_of_page('https://users.encs.concordia.ca/~gregb/home/comp354-w2019.html'))
projectpage = get_the_token(get_string_of_page('https://users.encs.concordia.ca/~gregb/home/comp354-w2019-project-info.html'))
studypage = get_the_token(get_string_of_page('https://users.encs.concordia.ca/~gregb/home/comp354_w2018_study_questions.html'))
# This is where I stored the data,json file. Change this filepath as needed
old_tokens = get_json('~/PycharmProjects/conup/data.json')
update_message = ''

# Verify the md5s (Make sure these if statements reflect the page names above and in the data.json file)
if homepage != old_tokens['homepage']:
    old_tokens['homepage'] = homepage
    update_message += "Homepage was updated\n"

if projectpage != old_tokens['projectpage']:
    old_tokens['projectpage'] = projectpage
    update_message += "Project page was updated\n"

if studypage != old_tokens['studypage']:
    old_tokens['studypage'] = studypage
    update_message += "Study page was updated\n"

# Change the JSON filepath here as well. Also set the place you want the textfile to be placed.
if update_message.__len__() > 0:
    with open('~/PycharmProjects/conup/data.json', 'w') as file:
        json.dump(old_tokens, file)
    with open('~/Desktop/CHECK IT OUT.txt', 'w') as notice:
        notice.write(update_message)
