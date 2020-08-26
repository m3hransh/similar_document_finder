import numpy as np
import matplotlib.pyplot as plt
import re


class Docs_Sim:
    '''
    takes two list of strings.
    finds similarity between them by scoring them.
    '''

    def __init__(self, text1='', text2=''):
        '''
        text1, text2: list of string words
        '''
        
        self.text1 = re.findall(r'(\w+)', text1)
        self.text2 = re.findall(r'(\w+)', text2)
        self.lcs = self.LCS()

    def LCS(self):
        '''
        Implementing longest common sequence using Dynamic programming.
        Take two file as an input and will find longest common sequence of
        words in that.
        text1, text2 : two string or list of strings.
        return: list of similar characters of strings.
        '''
        n = len(self.text1)
        m = len(self.text2)

        # create (n+1)*(m+1) table
        table = [[[]]*(m+1) for i in range(n+1)]

        # map index of texts to table
        indx = lambda i: i+1 
        
        for i in range(n):
            for j in range(m):
                if self.text1[i] == self.text2[j]:
                    # LCS(i,j) = LCS(i-1, j-1) + 1
                    table[indx(i)][indx(j)] = table[indx(i-1)][indx(j-1)] + [self.text1[i]]
                else:
                    # LCS(i, j) = max(LCS(i, j-1), LCS(i-1, j))
                    table[indx(i)][indx(j)] = max(table[indx(i)][indx(j-1)], table[indx(i-1)][indx(j)], key= lambda x:len(x))

        self.lcs = table[n][m] 
        return self.lcs


    def dist_finder(self):
        ''' Returns: (dist_list1, dist_list2) list occurance distributaoin 
        of lcs in the text1 and text2
        '''
        counter = 0
        dist_list1 = []

        for i, word in enumerate(self.text1):
            if len(self.lcs) == counter:
                break
            if self.lcs[counter] == word:
                dist_list1.append(i)
                counter += 1
        
        counter = 0
        dist_list2 = []

        for i, word in enumerate(self.text2):
            if len(self.lcs) == counter:
                break
            if self.lcs[counter] == word:
                dist_list2.append(i)
                counter += 1

        return dist_list1, dist_list2

    def sim_score(self):
        '''
        return: similarity rate'''

        rate = 0
        if self.lcs !=[]:
            try:
                rate = len(self.lcs)/(len(self.text1)+len(self.text2)-len(self.lcs))
            except ZeroDivisionError :
                print(f'lcs: {self.lcs}')
                print(f"text1: {self.text1}")
                print(f'text2: {self.text2}')

        return rate


    def depend_score(self):
        '''
        return: (dependency score of t1 on t2, dependency score of t2 on t1)'''
        if len(self.text1) != 0 and len(self.text2):
            try: 
                dep_t1 = len(self.lcs)/len(self.text1)
            except ZeroDivisionError as err:
                dep_t1 = 0
            try:
                dep_t2 = len(self.lcs)/len(self.text2)
            except ZeroDivisionError as err:
                dep_t2 = 0

            return (dep_t1, dep_t2) 
        else:
            return (0, 0)


    def draw_dist(self):
        '''Ploting lcs occurance distribution of each text'''
        fig, (ax1, ax2) = plt.subplots(2)
        dist1,dist2 = self.dist_finder()

        ax1.set_title("Text1 LCS occurance")
        ax1.plot(dist1, np.zeros_like(dist1) + 0, 'x',color='green')
        ax1.set_yticklabels([])

        ax2.set_title("Text2 LCS occurance")
        ax2.plot(dist2, np.zeros_like(dist2) + 0, 'x',color='green')
        ax2.set_yticklabels([])

        plt.show()
    
    def __it__(self, other):
        return self.sim_score() < other.sim_score()
    
    def __gt__(self, other):
        return self.sim_score() > other.sim_score()