# coding: utf-8
from clio import Clio

if __name__ == "__main__":
    clio = Clio(3, 'blue')
    print(clio.number_doors)
    print(clio.color)
    print(clio.color_number)
    clio.color = 'black'
    print(clio.color)
    print(clio.color_number)
    print(clio.price)
    Clio.update_price(15000)
    print(clio.price)
    clio2 = Clio(5, 'green')
    print(clio2.price)
    clio_Emira = Clio(5, "red")
    print(clio_Emira.price)
    Clio.update_price(30000)
    print(clio_Emira.price)
