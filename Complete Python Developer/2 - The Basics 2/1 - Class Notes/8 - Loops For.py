# 1 - O que você quer repetir?
# 2 - O que você quer mudar a cada repetição?
# 3 - Quantas vezes deseja repetir?

#for every item in " "

for item in [
    1, # [1a, 1b, 1c]
    2, # [2a, 2b, 2c]
    3, # [3a, 3b ,3c]
    ]:
    for x in [
        "a", #a1 , a2 , a3 
        "b", #b1 , b2 , b3
        "c"  #c1 , c2 , c3
        ]:
        print(item, x)
        for i in x:
            print(i, item)


