


def number_pattern(n:int) ->str:
    if isinstance(n,bool) :
        raise ValueError("Argument data type cannot is boolean.")
    elif not isinstance(n,int) :
        return "Argument must be an integer value."
    elif n < 1 :
        return "Argument must be an integer greater than 0."
    num_list = []
    for digit in range(1,n+1) :
        num_list.append(str(digit))
    return ' '.join(num_list)

if __name__=="__main__":
    print(number_pattern(n=5))
