class HashTable:
    def __init__(self):
        self.max = 10
        self.array = [None for i in range(self.max)]

    def hash_function(self,key):
        total = 0
        for char in key:
            total += ord(char)
        return total % 10

    def __grow__(self):
        """doubles array length, called in the event that
        the existing array's space in memory is filled"""
        self.max *= 2
        new = [None for i in range(self.max)]
        for index in range(len(self.array)):
            new[index] = self.array[index]
        self.array = new
        
    def __setitem__(self, key, value):
        h = self.hash_function(key)
        while True:
            for nbr in range(self.max):
                if not self.array[h]:
                    self.array[h] = (key,value)
                    return
                else:
                    if self.array[h][0] == key:
                        self.array[h] = (key,value)
                        return
                    if h == self.max:
                        h = 0
                    else:
                        h += 1
            self.__grow__()

    def __getitem__(self, key):
        h = self.hash_function(key)

        
        for i in range(self.max):
            if not self.array[h]:
                return("No value found for key " + key)

            if self.array[h][0] == key:
                return self.array[h][1]

            if h == self.max:
                h = 0
            else:
                h += 1
        return("No value found for key " + key)

    def __delitem__(self, key):
        h = self.hash_function(key)

        for i in range(self.max):
            if self.array[h][0] == key:
                self.array[h] = None
                return
            if h == self.max:
                h = 0
            else:
                h+= 1
            




if __name__ == '__main__':
    t = HashTable()
    c = ''
    l = []
    for i in range(1):
        c += '2'
        l.append(c)
    for entry in l:
        t[entry] = 1

    t['one'] = 1
    t['22'] = 2
    t['222'] = 3
    t['2E'] = 'e'
    t['22U'] = '5'
    t['22K'] = 'K'
    del t['222']

    print(t.array)
