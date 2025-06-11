from proj.tasks import add,divide


""" calling tasks by apply_async(()) """


result1 = add.apply_async(  (15,15) ,   countdown=15 )
print(result1.get(propagate=False , timeout=5 ))   # get is a sync method

result2 = add.apply_async( (25,25) )
result2.forget()


# result3 = add.apply_async(  (15,15) ,   countdown=15 )
# print(result3.get(propagate=False , timeout=5 ))
# result1.forget()




""" command & Line Prompt to run this app """
# active venv
# python myapp2.py