data = {
    "Names" : ["Kuda", "Tindo", "Kufrashe", "Pete"],
    "Ages" : [17, 23, 17, 25],
    "Height" : [1.6, 1.55, 1.5, 1.8]
}

def learn(x, y, z):
    learn_rate = 0.4
    learn_bias = 0.35
    print("Supplied input :{}, \n Supplied Expected Output: {}, \n Supplied z value: {}".format(x, y, z))
    process_data = x * learn_bias * y
    print("Process_data Value: {}".format(process_data))
    if process_data > y:
        learn_rate  = process_data - y
        print("Learn Rate is now : {}".format(learn_rate))
        z = process_data - learn_rate
    elif process_data < y:
        learn_rate = y - process_data
        print("Learn Rate is now : {}".format(learn_rate))
        z = process_data + learn_rate   
    else:
        print(process_data)
    print("The Computed Output is : {}".format(z))

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            learn(i, j, k)