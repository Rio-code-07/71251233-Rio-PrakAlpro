lista = ['red', 'green', 'blue']
listb = ['#FF0000', '#008000', '#0000FF']
x = dict(zip(lista, listb))
sorting_kunci= sorted(x.keys(), key=len, reverse=True)
hasil = {k: x[k] for k in sorting_kunci}
print(hasil)
