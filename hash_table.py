#hash table / hash map / dictionary
# find specific value is O(1)


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        
        # Code for if we decide to store key/value pairs in list
        # pair = [key,val]
        # if not self.arr[h]:
        #     self.arr[h].append(pair)
        #     return

        # for value in self.arr[h]:
        #     if value[0]==key:
        #         value[1]=val
        #         return    
        # self.arr[h].append(pair)
        # return

        #Otherwise, key/value pairs will be a tuple dtype:
        pair = (key,val)
        if self.arr[h]:
            for nbr,value in enumerate(self.arr[h]):
                if value[0] == key:
                    self.arr[h][nbr] = pair
                    return
        self.arr[h].append(pair)

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h]:
            for pair in self.arr[h]:
                if pair[0] == key:
                    self.arr[h].remove(pair)
                    return
        print(f'**WARNING** No value found for key {key}\n')

    def import_csv(self, file):
        """Function to open a csv file with two columns and automtically import
        each row as a key/value pair in our hash table.

        parameter file should be a string with the file
         path to your csv file, ex. '.\\directory\\file.csv'
        """

        with open(file, 'r') as csv:
            #iterate over each row and create a list of key/value pairs
            data = []
            for row in csv:
                row = row.replace('\n','')
                pair = tuple(row.split(','))
                data.append(pair)
            #remove title
            del data[0]
            for kv in data:
                self.__setitem__(kv[0],kv[1])

    def all_values(self):
        """returns array of all values in hash table"""
        all_values = []
        for entry in self.arr:
            for pair in entry:
                all_values.append(pair)
        return all_values       


if __name__ == '__main__':   

    t = HashTable()
    t.import_csv('C:\\users\\ascott\\desktop\\pstest\\data_structures\\misc\\nyc_weather.csv')
    
#Calculate average temperature for first 7 days:
    count = 0
    temp = 0
    for pair in t.all_values():
        if int(pair[0].split(' ')[1]) < 8:
            count += 1
            temp += int(pair[1])
    print(f'Average temp for {count} days is {round((temp / count),2)}')

#find max temp for first 10 days:
    max = 0
    for pair in t.all_values():
        if int(pair[1]) > max:
            max = int(pair[1])
    print('Max for 10 days is ' + str(max))


#Count up all words within a poem saved as a txt file
    with open('C:\\users\\ascott\\desktop\\pstest\\data_structures\\misc\\road_less_traveled.txt','r') as txt:
        word_list = []
        for line in txt:
            #remove punctuation characters
            for char in [';',',','\n','—','!','.']:
                line = line.replace(char, '')
            #add words from each line to a global word list
            for word in line.split(' '):
                if word.lower():
                    word_list.append(word.lower())

    #iterate through list of words adding to hash table, 
    #key is the word and value is count of how many times
    #the word appears
    word_table = HashTable()
    for word in word_list:
        if word_table[word]:
            word_table[word] += 1
        else:
            word_table[word] = 1
    counts = word_table.all_values()
    # sort counts in descending order
    sorted_counts = []
    while counts:
        current_max = (0,0)
        for tup in counts:
            if tup[1] > current_max[1]:
                current_max = tup
        sorted_counts.append(current_max)
        counts.remove(current_max)
    print(sorted_counts)