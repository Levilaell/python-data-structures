class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, _ in bucket:
            if k == key:
                return True
        return False

    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value))
        self.size += 1


    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
            
        return None

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
            
        return None


    def keys(self):
        all_keys = []

        for bucket in self.buckets:
            for k, _ in bucket:
                all_keys.append(k)
        
        return all_keys

    def values(self):
        all_values = []

        for bucket in self.buckets:
            for _, v in bucket:
                all_values.append(v)

        return all_values

    def items(self):
        all_items = []

        for bucket in self.buckets:
            for k, v in bucket:
                all_items.append((k, v))

        return all_items

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity