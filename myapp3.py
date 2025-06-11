from proj.tasks import add,divide,zarb
from celery import group ,chain,chord


""" Signatures """

res_sig= add.signature((2,2))
result =res_sig.delay()
print(result.get())


res_sig2= zarb.s(3,5)
result2 =res_sig2.delay()
print(result2.get())


"""partial  Signatures """


res_sig3= zarb.s(4)
result3 =res_sig3.delay(4)
print(result3.get())





""" primitives with signature """
    
"""     tip = sig and primitive both togheder dont need calling func like delay     """


#group 
# returns a list 

result_group = group(add.s(i, i) for i in range(10))().get()
print(result_group)

rg2 = group(add.s(i) for i in range(10))
print(rg2(10).get())






# chain 
#used for linking functions in patial mode and dosnt return list 

result_chain = chain(add.s(10, 10) | zarb.s(10))().get()
print(result_chain)





# chord makes a list that chain acts in each item 
result_chord = chord((add.s(i, i) for i in range(3)), zarb.s(1))().get()
print(result_chord)






# mix chord (group | chain)
ch = (group(add.s(i,i) for i in range(2)) | zarb.s(10) )
print(ch().get())




""" command & Line Prompt to run this app """
# active venv
# python myapp.py