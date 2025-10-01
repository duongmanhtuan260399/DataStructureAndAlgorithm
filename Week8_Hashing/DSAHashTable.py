import numpy as np

class DSAHashEntry:
    STATE_FREE = 0
    STATE_USED = 1
    STATE_PREVIOUSLY_USED = 2  # Tombstone

    def __init__(self, key=None, value=None, state=STATE_FREE):
        self.key = key
        self.value = value
        self.state = state

    def is_free(self):
        return self.state == DSAHashEntry.STATE_FREE

    def is_used(self):
        return self.state == DSAHashEntry.STATE_USED

    def is_previously_used(self):
        return self.state == DSAHashEntry.STATE_PREVIOUSLY_USED

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def get_state(self):
        return self.state


class DSAHashTable:
    DEFAULT_CAPACITY = 11  
    MAX_LOAD_FACTOR = 0.7  # Upper threshold for growing
    MIN_LOAD_FACTOR = 0.2  # Lower threshold for shrinking
    MIN_CAPACITY = 11      # Minimum capacity to prevent excessive shrinking

    def __init__(self, capacity=None, probing_mode="linear"):
        initial_capacity = capacity if capacity is not None else DSAHashTable.DEFAULT_CAPACITY
        self._capacity = self._next_prime(max(self.MIN_CAPACITY, int(initial_capacity)))
        self._count = 0
        self._array = np.empty(self._capacity, dtype=object)
        for i in range(self._capacity):
            self._array[i] = DSAHashEntry()
        if probing_mode not in ("linear", "double"):
            raise ValueError("probing_mode must be 'linear' or 'double'")
        self._probing_mode = probing_mode
        # Debug flag for collision/tombstone tracing
        self._debug = False

    def put(self, key, value):
        self._validate_key(key)
        # Check if we need to grow before inserting
        if (self._count + 1) / self._capacity > self.MAX_LOAD_FACTOR:
            self._resize(self._next_prime(self._capacity * 2))

        index = self._find_slot(key, for_insert=True)
        entry = self._array[index]
        if entry.is_used():
            self._array[index].value = value
        else:
            self._array[index].key = key
            self._array[index].value = value
            self._array[index].state = DSAHashEntry.STATE_USED
            self._count += 1

    def hasKey(self, key):
        self._validate_key(key)
        index = self._find_slot(key, for_insert=False)
        return self._array[index].is_used() and self._array[index].key == key

    def get(self, key):
        self._validate_key(key)
        index = self._find_slot(key, for_insert=False)
        entry = self._array[index]
        if entry.is_used() and entry.key == key:
            return entry.value
        raise KeyError(f"Key not found: {key}")

    def remove(self, key):
        self._validate_key(key)
        index = self._find_slot(key, for_insert=False)
        entry = self._array[index]
        if entry.is_used() and entry.key == key:
            removed_value = entry.value
            entry.key = None
            entry.value = None
            entry.state = DSAHashEntry.STATE_PREVIOUSLY_USED
            self._count -= 1
            
            # Check if we need to shrink after removing
            if (self._capacity > self.MIN_CAPACITY and 
                self._count / self._capacity < self.MIN_LOAD_FACTOR):
                new_capacity = max(self.MIN_CAPACITY, self._prev_prime(self._capacity // 2))
                self._resize(new_capacity)
            
            return removed_value
        raise KeyError(f"Key not found: {key}")

    def __len__(self):
        return self._count

    def __contains__(self, key):
        return self.hasKey(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        for entry in self._array:
            if entry.is_used():
                yield entry.key

    # Helpers / Introspection
    def capacity(self):
        return self._capacity

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def load_factor(self):
        return 0.0 if self._capacity == 0 else self._count / self._capacity

    def keys(self):
        result = np.empty(self._count, dtype=object)
        index = 0
        for entry in self._array:
            if entry.is_used():
                result[index] = entry.key
                index += 1
        return result[:index]

    def values(self):
        result = np.empty(self._count, dtype=object)
        index = 0
        for entry in self._array:
            if entry.is_used():
                result[index] = entry.value
                index += 1
        return result[:index]

    def items(self):
        result = np.empty(self._count, dtype=object)
        index = 0
        for entry in self._array:
            if entry.is_used():
                result[index] = (entry.key, entry.value)
                index += 1
        return result[:index]

    def clear(self):
        self._array = np.empty(self._capacity, dtype=object)
        for i in range(self._capacity):
            self._array[i] = DSAHashEntry()
        self._count = 0

    def set_probing_mode(self, mode):
        if mode not in ("linear", "double"):
            raise ValueError("probing_mode must be 'linear' or 'double'")
        if mode != self._probing_mode:
            self._probing_mode = mode
            # Rehash to normalize probe chains for the new mode
            self._resize(self._capacity)

    def set_debug(self, enabled):
        """Enable or disable debug printing for collisions/tombstones."""
        self._debug = bool(enabled)

    def _validate_key(self, key):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

    def _hash_primary(self, key):
        # A simple, repeatable string hash (djb2 variant)
        h = 5381
        for ch in key:
            h = ((h << 5) + h) + ord(ch)  # h * 33 + ord(ch)
        return h & 0x7FFFFFFF

    def _hash_secondary(self, key):
        # A secondary hash ensuring a non-zero step; typical choice
        # Make it depend on different mixing than primary
        h = 0
        for ch in key:
            h = (h * 131) + ord(ch)
        h &= 0x7FFFFFFF
        step = 1 + (h % (self._capacity - 1))
        return step

    def _probe_step(self, key):
        if self._probing_mode == "linear":
            return 1
        else:
            return self._hash_secondary(key)

    def _find_slot(self, key, for_insert):
        start_index = self._hash_primary(key) % self._capacity
        step = self._probe_step(key)

        first_tombstone_index = -1
        index = start_index
        probes = 0
        while True:
            entry = self._array[index]
            if entry.is_free():
                if for_insert:
                    # Use an earlier tombstone if found; otherwise this slot
                    return first_tombstone_index if first_tombstone_index != -1 else index
                else:
                    # Never used means key cannot be further down the chain
                    return index
            elif entry.is_used():
                if entry.key == key:
                    return index
                else:
                    if self._debug:
                        print(f"Collision: key='{key}' hit index {index} holding key='{entry.key}' (step={step})")
            else:  # Tombstone
                if for_insert and first_tombstone_index == -1:
                    first_tombstone_index = index
                if self._debug:
                    print(f"Tombstone encountered at index {index} while probing for key='{key}'")

            probes += 1
            if probes >= self._capacity:
                # Table appears full (should not happen with resizing); fall back
                return first_tombstone_index if first_tombstone_index != -1 else start_index

            index = (index + step) % self._capacity

    def _resize(self, new_capacity):
        # Ensure new capacity is prime and respects minimum capacity
        new_capacity = self._next_prime(max(self.MIN_CAPACITY, int(new_capacity)))
        
        old_entries = np.empty(self._count, dtype=object)
        index = 0
        for e in self._array:
            if e.is_used():
                old_entries[index] = e
                index += 1
        
        # Create new array with new capacity
        self._capacity = new_capacity
        self._array = np.empty(self._capacity, dtype=object)
        for i in range(self._capacity):
            self._array[i] = DSAHashEntry()
        
        # Reset count and rehash all entries
        self._count = 0
        for i in range(index):
            self.put(old_entries[i].key, old_entries[i].value)

    def _is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def _next_prime(self, n):
        candidate = n if n % 2 == 1 else n + 1
        while not self._is_prime(candidate):
            candidate += 2
        return candidate
    
    def _prev_prime(self, n):
        """Find the largest prime number less than or equal to n."""
        if n <= 2:
            return 2
        candidate = n if n % 2 == 1 else n - 1
        while candidate > 2 and not self._is_prime(candidate):
            candidate -= 2
        return max(2, candidate)


__all__ = ["DSAHashTable", "DSAHashEntry"]


