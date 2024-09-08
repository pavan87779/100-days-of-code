def love_calculator(name1,name2):
    combine=name1+name2
    low_combine=combine.lower()
    t=low_combine.count("t")
    r=low_combine.count("r")
    u=low_combine.count("u")
    e=low_combine.count("e")

    first_digi=t+r+u+e

    l=low_combine.count("l")
    o=low_combine.count("o")
    v=low_combine.count("v")
    e=low_combine.count("e")

    second_digi=l+o+v+e
    score=int(str(first_digi)+str(second_digi))
    print(score)

love_calculator("roemo","juliet")