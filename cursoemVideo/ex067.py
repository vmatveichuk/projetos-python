n = 0
while True:
    n = int(input("Digite qual valor da tabuada: "))
    if n < 0:
        break
    print(f"------ \33[1;31mTABUADA DO {n}\33[m ------")
    for c in range(1, 11):
        print(f"{n} X {c} = {n * c}")
    print("-------------------------")
print("FIM")
