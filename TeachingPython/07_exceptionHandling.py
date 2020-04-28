try:
    a,b = 20,0
    print(a/b)
except ZeroDivisionError:
    print('Divide by zero occurred')
finally:
    print("Finalizing...")
