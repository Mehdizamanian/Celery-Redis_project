from tasks import add , divide


# calling tasks 
# add.delay(52,1)
# divide.apply_async([12,4])



# restoring result in backend needed to be added a backend(redis) and u use get or forget method

result1 = add.delay(5,5)
print(result1.get())


result2 = add.delay(3,2)
result2.forget()


result3 = add.delay(3,5)
print(result3.get(propagate=False))   #other features => timeout , ... 
print("proparger used for error handeling and print all ting after caliing a function thou ")





""" command to run this app """
# active venv
# python myapp.py