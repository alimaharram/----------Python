def massive_func():
    arr = [1,2,3,4,5,6,7,8,9,10]
    multiples = [x for x in arr if not x%3]
    print(multiples)

massive_func()
