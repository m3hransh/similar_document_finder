import requests
from bs4 import BeautifulSoup
from googlesearch import search
from docs_sim import Docs_Sim
import re

def geeks_lcs(url, t1):
    '''
    url: geeksforgeeks url
    t1: document string
    return: docs_sim object of t1 and most similar code section in the URL
    '''

    r = requests.get(url)

    # parse the html
    soup = BeautifulSoup(r.content, 'html5lib')

    # parse tree of codes sections 
    code_sections = soup.findAll('div', attrs={'class': 'container'})

    max_score= 0
    max_docs = Docs_Sim(t1) 
    # get each sectoin parse tree
    for code_sec in code_sections:
        code = []
        # add words of each line of the code sectoin
        for line in code_sec.findAll('code'):
            if line['class'][0] !='comments':
                code += re.findall(r'(\w+)', line.text)
        docs = Docs_Sim(t1)
        docs.text2 = code
        # find lcs between t1 and the code
        docs.LCS()
        score = docs.sim_score()
        # check if the section is more similar to t1 or not
        if score > max_score:
            max_score = score
            max_docs = docs
    
    return max_docs


def google_lcs(query,t1, num=5):
    '''
    query: search on google
    t1: document to compare against
    num: number of search on the google
    return: (url that had the most similar code sec, 
                docs_sim object of t1 and most similar code section in the url)
    '''
    max_docs = Docs_Sim(t1)
    url = ''
    for j in search(query, tld='co.in', num=num, stop=num, pause=2):
        docs= geeks_lcs(j, t1)
        if docs > max_docs:
            max_docs = docs
            url = j

    return url, max_docs