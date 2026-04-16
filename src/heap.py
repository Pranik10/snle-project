class MinHeap:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if self.is_empty():
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return None if self.is_empty() else self.data[0]

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index][0] < self.data[parent][0]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.data)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < size and self.data[right][0] < self.data[smallest][0]:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break


class MaxHeap:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)
        self._heapify_up(len(self.data) - 1)

    def dequeue(self):
        if self.is_empty():
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return None if self.is_empty() else self.data[0]

    def _priority_value(self, item):
        return item["priority"]

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._priority_value(self.data[index]) > self._priority_value(self.data[parent]):
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.data)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._priority_value(self.data[left]) > self._priority_value(self.data[largest]):
                largest = left
            if right < size and self._priority_value(self.data[right]) > self._priority_value(self.data[largest]):
                largest = right

            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                index = largest
            else:
                break
