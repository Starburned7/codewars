def mutually_exclusive(dice, call1, call2):
    dice_dict = { k[0]: k[1] for k in dice}
    if sum(dice_dict.values()) != 1:
            return None
    else:
        first_toss = dice_dict[call1]
        second_toss = dice_dict[call2]
        p = round(first_toss+second_toss,2)
        return "{:.2f}".format(p)
    
        #return str(round(first_toss+second_toss,2))
   
#mutually_exclusive([[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.1]],1,6)
mutually_exclusive([[1,0.1],[2,0.14],[3,0.16],[4,0.2],[5,0.15],[6,0.25]],1,4)
   