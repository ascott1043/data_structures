#hash table / hash map / dictionary
# find specific value is O(1)


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        
        for index, element in enumerate(self.arr[h]):
            if len(element = 2) and element[0]==key:
                self.arr[h][index] =(key,val)
        

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None




t = HashTable()

t['nbr'] = 10
del t['nbr']
print(t['nbr'])
