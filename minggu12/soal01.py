dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(f"{'key':<8} {'value':<8} {'item':<8}")
for kunci, nilai in dictionary.items():
    print(f"{kunci:<8} {nilai:<8} {kunci:<8}")
