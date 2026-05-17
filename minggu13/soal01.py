def cek_semua_sama(tpl):
    return len(set(tpl)) == 1
tA = (90, 90, 90, 90)
print(cek_semua_sama(tA))

