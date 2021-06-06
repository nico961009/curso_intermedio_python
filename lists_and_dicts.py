def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Nico", "lastname": "Andrade"}

    super_list = [
        {"firstname": "Nico", "lastname": "Andrade"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Carlota", "lastname": "Andrade"},
        {"firstname": "Miguel", "lastname": "García"},
        {"firstname": "Amanda", "lastname": "Hdez"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1, 4.5, 6.63]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)


if __name__ == '__main__':
    run()