import sys

def main():
  data = sys.stdin.buffer.read().split()
  n = int(data[0])
  ages = sorted(map(int, data[1:n + 1]))

  answer = min(b - a for a, b in zip(ages, ages[1:]))
  print(answer)

main()
