class HashTable:
    def __init__(self, size=100) -> None:
        """
        Initialize the hash table with a given size.
        The table is represented as a list of empty lists to handle collisions using chaining.
        :param size: The size of the hash table (default: 100).
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        """
        Compute the hash value for the given key.
        The hash value is calculated as the sum of ASCII values of characters in the key,
        modulo the size of the hash table.
        :param key: The key for which to compute the hash value.
        :return: The computed hash value.
        """
        return sum(ord(char) for char in key) % self.size

    def __setitem__(self, key, value):
        """
        Add or update a key-value pair in the hash table.
        If the key already exists, its value is updated. Otherwise, a new key-value pair is added.
        :param key: The key to add or update.
        :param value: The value to associate with the key.
        """
        hash_key = self._get_hash(key)
        # Check if the key exists in the chain at this hash index
        for pair in self.table[hash_key]:
            if pair[0] == key:  # Key found, update value
                pair[1] = value
                return
        # Key not found, append as a new entry
        self.table[hash_key].append([key, value])

    def __getitem__(self, key):
        """
        Retrieve the value associated with a given key.
        :param key: The key to look up.
        :return: The value associated with the key.
        :raises KeyError: If the key is not found.
        """
        hash_key = self._get_hash(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def __delitem__(self, key):
        """
        Remove a key-value pair from the hash table.
        :param key: The key to remove.
        :raises KeyError: If the key is not found.
        """
        hash_key = self._get_hash(key)
        for idx, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                del self.table[hash_key][idx]
                return
        raise KeyError(f"Key '{key}' not found")


# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht["march 7"] = "smz"
    ht["march 7"] = "sabbir"
    ht["march 17"] = "Mahmud"
    del ht["march 17"]

    try:
        print(ht["march 7"])  # Output: sabbir
        print(ht["march 17"])  # Raises KeyError
    except KeyError as e:
        print(e)
