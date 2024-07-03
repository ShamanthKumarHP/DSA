p = 1
try:
    print(1/0)
except:
    print("found error")
    raise Exception("error")
finally:
    print("Done")