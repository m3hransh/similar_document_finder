#! /usr/bin/python3
import sys
from docs_sim import Docs_Sim


if __name__ == "__main__":
    # getting file names from Terminal args
    if len(sys.argv) >= 3:
        f_name1 = sys.argv[1]
        f_name2 = sys.argv[2]
    else:
        # default values of filenames
        f_name1 = 'text1.txt'
        f_name2 = 'text2.txt'
    
    #opening files
    with open(f_name1, 'r') as f1:
        with open(f_name2, 'r') as f2:
            # Read and split text to words
            t1 = f1.read()
            t2 = f2.read()
            docs = Docs_Sim(t1,t2)
            docs.LCS()
            sim = docs.sim_score()
            dep1,dep2 = docs.depend_score()

            print("Similarity Score: {:.2%}  \n"
                    "Dependency Score of text1 on text2: {:.2%}  \n"
                    "Dependency Score of text2 on text1: {:.2%}  \n"
                    "\nLCS Words: \n{}".format(sim, dep1, dep2, ' '.join(docs.lcs)))
            
            docs.draw_dist()