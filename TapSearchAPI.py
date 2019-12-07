import sys
from collections import defaultdict


    
class TapSearch:
    
    def __init__(self, text):
        
        self.text = text.lower()
        self.inverted_index = defaultdict(set)
        
    
    def index(self):
        
        # splitting input into paragraph
        self.text = self.text.replace('\r','')
        # print(list(self.text))
        
        raw_list = self.text.split('\n\n')
        print(raw_list)
        
        
        raw_list = [x for x in raw_list if x is not '']
    

        
        paragraph_list = []
        
        for i in range(len(raw_list)):
            y = raw_list[i].replace('\n', ' ')
            paragraph_list.append(y)
            
        
        document_index = dict(enumerate(paragraph_list,1))
        
        return document_index
        
        
    
    def create_inverted_index(self):
        
        document = self.index()
        
        for i in document.keys():
            
            paragraph = document[i].strip().split(' ')
        
            for x in paragraph:
                x = x.strip()
                self.inverted_index[x].add(i)
                
        return self.inverted_index
    
    
    def search(self, word):
        inverted_index = self.create_inverted_index()
        paragraph = self.index()
        
        if word in inverted_index.keys():
            
            if len(inverted_index[word]) < 9:

                return list(inverted_index[word])
            
            else:
                return list(inverted_index[word])[:10]
        
        else:
            return []

    
    def clear(self):
        
        self.inverted_index = defaultdict(set)
            
        
        


if __name__ == "__main__":  
  
    text = sys.stdin.read() 
    n = TapSearch(text)
    print(n.index())
    print(n.create_inverted_index())
    print(n.search('jain'))
        
    
    
    
    
    
    
    
    
    
    