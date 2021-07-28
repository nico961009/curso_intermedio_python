def run():
    # vocales= []
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        # for i in f:
        #     if i[2] == "a":
        #         vocales.append(i)
        vocales= [i for i in f if i[0] == "e"]

    print (vocales)
    



if __name__ == '__main__':
    run()
