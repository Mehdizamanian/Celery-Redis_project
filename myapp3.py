from proj.tasks import add,divide,zarb


""" Signature & primitives  """

res_sig= add.signature((2,2))
result =res_sig.delay()
print(result.get())


res_sig2= zarb.s(3,5)
result2 =res_sig2.delay()
print(result2.get())




""" command & Line Prompt to run this app """
# active venv
# python myapp.py