#! /home/mehran/.virtualenvs/lcs/bin/python3
import click
import os
import sys
import re
from scraping import google_lcs
from docs_sim import Docs_Sim

@click.group()
def cli():
    '''
    Simple CLI for finding similarity between codes
    '''
    pass

@cli.command()
@click.option('--file','-f', help='File path',type=click.Path(exists=True))
@click.option('--dir','-d', help='Directory of code files')
@click.option('--num', '-n', default=3, help='Number websites will check on Google')
@click.option('--keywords', '-k', help='Keywords for searching on google' )
@click.option('--website', '-w', default='site:www.geeksforgeeks.org ', help='Website to search on google, default value: www.geeksforgeeks.org')
@click.option('--plot/--no-plot', default=False, help='Darw plot of the lcs occurance distribution of two top documents')
def query(file, dir, num, keywords, website, plot):
    '''
        Search files on the google.
    '''
    if file:
        if keywords != None:
            with open(file, 'r') as f:
                t1 = f.read()
            
            # geeksforgeeks query
            query = website
            query += keywords
            url,docs = google_lcs(query, t1, num)
            print('url: {} \nSimilarity Score: {:.2%}\n'
                'dependency Score: ({:.2%}, {:.2%})\n LCS:\n {}'.format(url,
                     docs.sim_score(),*docs.depend_score(),' '.join(docs.lcs)))
            if plot:
                docs.draw_dist()
        else:
            click.echo("--keywords option is not given!")
    elif dir:
        if keywords != None:
            files = os.listdir(dir) 

            docs_list = []
            for f in files:
                with open(os.path.join(dir,f), 'r') as file:
                    t1 = file.read()

                query = website
                query += keywords
                url, docs_sim = google_lcs(query, t1, 5)
                docs_list.append((f, url, docs_sim))
        
            docs_list.sort(key = lambda x : x[2],reverse=True)
            for d in docs_list:
                print('file:{}\nurl: {} \nSimilarity Score: {:.2%}\n'
                    'dependency Score: ({:.2%}, {:.2%})\n'.format(d[0], d[1],
                        d[2].sim_score(),*d[2].depend_score()))
    
            if plot:
                docs_list[0][2].draw_dist()
        else:
            click.echo("--keywords option is not given!")

@cli.command()
@click.argument('filename1', type=click.Path(exists=True))
@click.argument('filename2', type=click.Path(exists=True))
@click.option('--plot/--no-plot', default=False, help='Draw plot of the lcs occurance distribution')
def check_files(filename1, filename2, plot):
    '''Check the similarity of two code files.'''
    with open(filename1, 'r') as f1:
        t1 = f1.read()
    
    with open(filename2, 'r') as f2:
        t2 = f2.read()
    
    docs = Docs_Sim(t1,t2)
    docs.LCS()
    sim = docs.sim_score()
    dep1,dep2 = docs.depend_score()

    print("Similarity Score: {:.2%}  \n"
            "Dependency Score of text1 on text2: {:.2%}  \n"
            "Dependency Score of text2 on text1: {:.2%}  \n"
            "\nLCS Words: \n{}".format(sim, dep1, dep2, ' '.join(docs.lcs)))
    if plot: 
        docs.draw_dist()


@cli.command()
@click.argument('dir', type=click.Path(exists=True))
@click.option('--plot/--no-plot', default=False, help='Draw plot of the lcs occurance distribution')
def check_dir(dir, plot):
    '''Find most similar pairs for each file in the directory.'''
    files = os.listdir(dir) 

    docs_list = []
    for f1 in files:
        with open(os.path.join(dir,f1), 'r') as f:
            t1 = f.read()

        max_docs_sim = Docs_Sim(t1)
        f2_max = ''
        for f2 in files:
            if f1 != f2:
                with open(os.path.join(dir, f2), 'r') as f:
                    t2 = f.read()
                
                docs_sim = Docs_Sim(t1, t2)
                if docs_sim > max_docs_sim:
                    max_docs_sim = docs_sim
                    f2_max = f2 
        
        docs_list.append((f1, f2_max, max_docs_sim))

    docs_list.sort(key = lambda x : x[2],reverse=True)
    for d in docs_list:
        print('file1: {}\nfile2: {} \nSimilarity Score: {:.2%}\n'
                    'dependency Score: ({:.2%}, {:.2%})\n'.format(d[0], d[1],
                        d[2].sim_score(),*d[2].depend_score()))
        
    if plot:
        docs_list[0][2].draw_dist()


def remove_commment(string, file_ex='py'):
    if file_ex == 'py':
        string = re.sub(r'#.*?\n', '',string)
    elif file_ex == 'cpp' or file_ex == 'c':
        # remove all occurrences streamed comments (/*COMMENT */) from string
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) 
        # remove all occurrence single-line comments (//COMMENT\n ) from string
        string = re.sub(r"//.*?\n"  ,"" ,string) 

    return string


@cli.command()
@click.argument('dir', type=click.Path(exists=True))
def clean_comments(dir):
    '''Remove C-style and python-style comments of files in directory.'''
    file_list = os.listdir(dir)

    for file in file_list:
        with open(os.path.join(dir, file), 'r') as f:
            code = f.read()

        file_extention = re.search(r'\.(.*)$', file).group(1)
        code = remove_commment(code, file_extention)

        with open(os.path.join(dir , file), 'w') as f:
            f.write(code)
        

if __name__ == "__main__":
    cli()
    
    

