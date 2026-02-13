#---the discount function main part----#
def apply_discount(price,discount) ->int|float|str:
    if not isinstance(price,(int,float)):
        return "The price should be a number"
    elif not isinstance(discount,(int,float)):
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    elif discount == 0:
        return price
    elif discount == 100:
        return 0
    elif discount<0 or discount > 100  :
        return "The discount should be between 0 and 100"
    final_discount = discount/100
    return price-price*final_discount
#-----the test part for the discount function--#
#-----extra code-----#

def discount_analysis(test_value:tuple[int|float,int|float]) ->bool:
    calling_discount = apply_discount(price=test_value[0],discount=test_value[1])

    if calling_discount== 80 :
        return  True
    elif calling_discount==  100 :
        return True
    elif calling_discount==  50 :
        return  True
    elif calling_discount ==  59.6 :
        return  True
    else:
        return  False

def final_determines(test_value:tuple[float|int,float|int]) ->str:
    if discount_analysis(test_value) :
        return  "pass to the this test"
    else:
        return  "no pass this test"
#-----extra code end--------#
if __name__ =="__main__":
    lad_list = [(100,20),(200,50),(50,0),(74.5,20.0)]
    lad_sentence= [final_determines(i) for i in lad_list]
    #print(''.join([chr(i) for i in range(97,123)] ))
    print(lad_sentence)

