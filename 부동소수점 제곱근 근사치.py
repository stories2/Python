def square_root(x, epsilon):
        low =  0
        high = x

        middle = (low + high) / 2.0

        count = 0

        while abs(middle ** 2 - x) > epsilon and count < 100:
            if middle ** 2 < x:
                low = middle
            else:
                high = middle

            middle = (low + high)/2.0
            count += 1
            print( "count #"+str(count)+" low "+str(low)+" middle "+str(middle)+" high "+str(high))
        return middle
