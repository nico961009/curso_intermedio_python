# my_list = [1,2,3,4,5]

# for i in my_list:
#     (i**2)


def run():
    squares= [i**2 for i in range(1,5)]

    print(squares)

if __name__ == '__main__':
    run()