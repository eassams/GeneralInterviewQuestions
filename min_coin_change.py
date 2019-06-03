def get_min_coin_change(arr , target):

    min_coin = target

    if target in arr:
        return 1
    else:

        for coin in [ _ for _ in arr if _ < target ]:

            res = 1 + get_min_coin_change( arr , target - coin)

            if res < min_coin:
                min_coin  = res
    return res


print get_min_coin_change( [1,2,3,4,10] , 5 )

print get_min_coin_change( [ 1,2,3,4,6,5,10] , 5 )



