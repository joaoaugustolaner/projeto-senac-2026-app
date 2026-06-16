def contar_quebra_linha(filename:str):
    with open(filename) as archive:
        count = 0
        for line in archive.readlines():
            if line.endswith('\n') or line.startswith('\n'):
                count+=1