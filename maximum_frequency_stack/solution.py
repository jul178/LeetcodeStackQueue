from collections import deque, defaultdict
class FreqStack:

    def __init__(self):
        self.stack = deque()
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] += 1


    def pop(self) -> int:
        max_f = max(self.freq.values())
        temp_stack = deque()
        val_to_return = None

        while self.stack:
            current_val = self.stack.pop()

            if self.freq[current_val] == max_f:
                val_to_return = current_val
                self.freq[val_to_return] -= 1
                break
            else:
                temp_stack.append(current_val)

        while temp_stack:
            self.stack.append(temp_stack.pop())
        return val_to_return
