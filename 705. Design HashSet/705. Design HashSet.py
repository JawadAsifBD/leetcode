NUM_BUCKETS = 2003  # A prime number


class MyHashSet:

    def __init__(self):
        # Make the hash buckets.
        self.buckets = [[] for _ in range(NUM_BUCKETS)]

    def add(self, key: int) -> None:
        mod = key % NUM_BUCKETS
        if not key in self.buckets[mod]:
            self.buckets[mod].append(key)

    def remove(self, key: int) -> None:
        mod = key % NUM_BUCKETS
        # Remove if it's present
        try:
            self.buckets[mod].remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        mod = key % NUM_BUCKETS
        return key in self.buckets[mod]
