def konversi():
    print("== PROGRAM KONVERSI TIPE DATA == \n")

    list_awal = ["apel", "jeruk", "mangga", "apel"] 
    set_dari_list = set(list_awal)
    print("List menjadi Set (Duplikat akan otomatis hilang):")
    print(f"Sebelum: {list_awal} (Tipe: {type(list_awal).__name__})")
    print(f"Sesudah: {set_dari_list} (Tipe: {type(set_dari_list).__name__})\n")

    set_awal = {"kucing", "anjing", "kelinci"}
    list_dari_set = list(set_awal)
    print("Set menjadi List:")
    print(f"Sebelum: {set_awal} (Tipe: {type(set_awal).__name__})")
    print(f"Sesudah: {list_dari_set} (Tipe: {type(list_dari_set).__name__})\n")

    tuple_awal = (10, 20, 30, 20, 10)
    set_dari_tuple = set(tuple_awal)
    print("Tuple menjadi Set:")
    print(f"Sebelum: {tuple_awal} (Tipe: {type(tuple_awal).__name__})")
    print(f"Sesudah: {set_dari_tuple} (Tipe: {type(set_dari_tuple).__name__})\n")

    set_awal_2 = {True, False, "Python"}
    tuple_dari_set = tuple(set_awal_2)
    print("Set menjadi Tuple:")
    print(f"Sebelum: {set_awal_2} (Tipe: {type(set_awal_2).__name__})")
    print(f"Sesudah: {tuple_dari_set} (Tipe: {type(tuple_dari_set).__name__})\n")

konversi()
