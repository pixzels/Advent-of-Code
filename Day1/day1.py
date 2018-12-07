data = [int(f) for f in open("input.txt")]

# PART 1
print(sum(data))

# PART 2
def _():
    freq = 0
    history = {0,}
    while True:
        for step in data:
            freq += step
            if freq in history: return freq
            else: history.add(freq)

print(_())