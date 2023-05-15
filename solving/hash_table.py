from typing import Any


class HashTableException(BaseException):
    ...


class Cell:
    def __init__(self, key: int, value: Any) -> None:
        self.key = key
        self.value = value


class HashTable:
    MIN: Any = None
    MAX: int = 0
    TOTAL: int = 0

    def __init__(self, number_of_cells: int = 1) -> None:
        if isinstance(number_of_cells, int) or number_of_cells < 0:
            raise HashTableException("Invalid value for hash table value")
        self.num_cells: int = number_of_cells
        self.cells = [None for _ in range(self.num_cells)]

    def __str__(self) -> str:
        string = '{'
        for element in self.cells:
            if element:
                for entry in element:
                    if isinstance(entry.key, str):
                        string += ("'%s': " % entry.key)
                    else:
                        string += ("%s: " % entry.key)
                    if isinstance(entry.value, str):
                        string += ("'%s', " % entry.value)
                    else:
                        string += ("%s, " % entry.value)
        return string.rstrip(', ') + "}"

    def hash(self, key) -> int:
        power: int = 0
        hashing: int = 0
        for element in key:
            hashing += (ord(element) - 32) * pow(95, power)
            power += 1
        index = hashing % self.num_cells
        return index

    def add(self, key, value):
        index = self.hash(str(key))
        if index < 0 or index > self.num_cells:
            return False
        if not self.cells[index]:
            self.cells[index] = [Cell(key, value)]
            return True
        else:
            for entry in self.cells[index]:
                if entry.key == key:
                    entry.value = value
                    return True
            self.cells[index].append(Cell(key, value))
            return True

    def update_value(self, key, value):
        index = self.hash(str(key))
        if not index:
            return False
        if not self.cells[index]:
            return False
        else:
            for entry in self.cells[index]:
                if entry.key == key:
                    entry.value = value
                    return True
            return False

    def delete(self, key):
        index = self.hash(str(key))
        if not index:
            return False
        if not self.cells[index]:
            return False
        else:
            for entry in self.cells[index]:
                if entry.key == key:
                    self.cells[index].remove(entry)
                    return True
            return False

    def look_up(self, key):
        index = self.hash(str(key))
        if not self.cells[index]:
            return False
        else:
            for entry in self.cells[index]:
                if entry.key == key:
                    return entry.value
            return False

    def print_distribution(self):
        value: str = ''
        bucket_num = 0
        for bucket in self.cells:
            if bucket:
                count = 0
                for _ in bucket:
                    count += 1
                self.TOTAL += count
                if count > self.MAX:
                    self.MAX = count
                if not self.MIN or count < self.MIN:
                    self.MIN = count
            else:
                pass
            bucket_num += 1
        value += ("Largest Bucket has %d entries\n"
                  "Smallest Bucket has %d entries\nTotal entries: %d\n"
                  "Avg bucket size is %f" % (self.MAX, self.MIN, self.TOTAL, (self.TOTAL / self.num_cells)))
        return value
