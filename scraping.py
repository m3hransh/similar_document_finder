import requests
from bs4 import BeautifulSoup
from googlesearch import search
from docs_sim import Docs_Sim
import re
from urllib.error import HTTPError

def geeks_lcs(url, t1):
    '''
    url: geeksforgeeks url
    t1: document string
    return: docs_sim object of t1 and most similar code section in the URL
    '''

    r = requests.get(url, headers = {'User-agent': 'your robot 0.1'})

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
    try:
        for j in search(query, tld='co.in', num=num, stop=num, pause=5,user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'):
            docs= geeks_lcs(j, t1)
            if docs > max_docs:
                max_docs = docs
                url = j
        
    except HTTPError as err:
        raise err


    return url, max_docs

def google_list_files(query,file_contents, num=5):
    '''
    query: search on google
    t1: document to compare against
    num: number of search on the google
    return: (url that had the most similar code sec, 
                docs_sim object of t1 and most similar code section in the url)
    '''
    result_list = []
    try:
        searches = list(search(query, tld='co.in', num=num, stop=num,
                         pause=5,user_agent='robot 0.1'))
        print('search results:')
        for i, s in enumerate(searches):
            print(f'{i+1}- {s}')
    except:
        print('error occured')
        raise
    
    for file_name, content in file_contents:
    
        max_docs = Docs_Sim(content)
        url = ''
        for j in searches:
            docs= geeks_lcs(j, content)
            if docs > max_docs:
                max_docs = docs
                url = j
        result_list.append((file_name, url, max_docs))
        


    return result_list