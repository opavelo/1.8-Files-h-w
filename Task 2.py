from pprint import pprint

class cook:
    def __init__(self, link):
        self.link = link

    def getcookbook(self):
        self.cookbook = {}
        with open(self.link, 'r', encoding='utf-8') as f:
            while True:
                dish_name = f.readline().strip()
                if dish_name == '':
                    break
                ingridients_quant = int(f.readline())
                ingridients_list = []
                for i in range(ingridients_quant):
                    ingr = f.readline().strip().split('|')
                    ignr_dict = {}
                    ignr_dict = {'ingredient_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2]}
                    ingridients_list.append(ignr_dict)
                self.cookbook[dish_name] = ingridients_list
                f.readline()
        pprint(self.cookbook)

    def get_shop_list_by_dishes(self, dishes, person_count):
        ingridients_list_temp = {}
        k = 0
        for j in dishes:
            if j in self.cookbook.keys():
                for i in self.cookbook[j]:
                    if i['ingredient_name'] not in ingridients_list_temp.keys():
                        ingridients_list_temp[i['ingredient_name']] = {'quantity': i['quantity'] * person_count, 'measure' : i['measure']}
                    else:
                        k = ingridients_list_temp.get(i['ingredient_name']).get('quantity') #кол-во ингрид., кот. уже в словаре с учетом множетеля
                        ingridients_list_temp[i['ingredient_name']] = {'quantity': (i['quantity'] * person_count + k), 'measure' : i['measure']}
        pprint(ingridients_list_temp)


example = cook('recipes.txt')
#example.getcookbook()
example.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5)
