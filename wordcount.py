import string

def wordcount(filename):
    """Counts occurrences of words in a text file.  By Erica and Roo."""  
    
    poem_count = {}
    count = 0
    log_file = open(filename)
    
    #make a list of each line of the poem and clean 'em up
    for line in log_file:
        line = line.strip()
        words = line.split(' ')
        for word in words:
            word = word.strip('.,?')
            word = word.lower()

    #create dictionary and add each word to it
            if poem_count.get(word) == None:
                count = 1
                poem_count[word] = count
            else:
                count = poem_count[word]
                new_count = count + 1
                poem_count[word] = new_count

        for word, count in poem_count.iteritems():
                print "%s %d" % (word, count)





wordcount("test.txt")