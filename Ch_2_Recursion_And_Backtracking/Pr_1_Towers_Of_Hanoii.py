def towers_of_hanoii(num, start, end, aux):
    if num>0:
        towers_of_hanoii(num-1,start, aux, end)
        print('Move from', start, 'to', end)
        towers_of_hanoii(num-1, aux, end, start)

towers_of_hanoii(3,'A','B','C')