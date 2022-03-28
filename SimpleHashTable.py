class SimpleHashTable:
    def __init__ (self, lenght):
        self._table = [0] * lenght
    def table(self):
        return self._table
    def _HashKey(self, data):
        return ord(data[0]) % len(self._table)
    def get(self, key):
        return self._table[self._HashKey(key)]
    def add(self, string, value):
        index = self._HashKey(string)
        self._table[index] = value
        return True

a = SimpleHashTable(20)

a.add("test", 999)
data = a.get("test")

print(data)