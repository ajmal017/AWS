def cancelOrder(order_id):
    i=0
    while i < 10:
        try:
            kite.cancel_order(variety = kite.VARIETY_REGULAR,order_id=order_id)
            break
        except Exception as e:
                print(i,":",e)
        i+=1
    
    if i==10:
        print("Order failed after {} tries".format(i))
