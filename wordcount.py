# put your code here.
test = "test.txt"
twain = "twain.txt"

def word_counting(log_file):
    """Counts each time a word appears in the txt"""

    log_file = open(test)
    # empty dictionary
    word_bank = {}

    #for every word in the txt file
    for word in log_file: #for each line in the txt file
        word = word.rstrip() #remove all white spaces to the right...
        sentence = word.split() #put each word individually in the sentence list

        #we want to put the word in the word_bank
        # print(word)
        
        for item in sentence: #for each item in the sentence list...
            
            #add the item into the word_bank
            #if new item then default value to 0 and +1
            #if not new then item/value + 1
            word_bank[item] = word_bank.get(item, 0) + 1 
        
    
    return word_bank