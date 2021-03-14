from pprint import pprint

dictonary = {}

def writting_function(result_file_link, file_name_link, rows_count):
    with open(result_file_link, 'w', encoding='utf-8') as f:
        pass

def auxiliary_function(link_list, result_link):
    rows_count = 0
    for link in link_list:
        with open(link, 'r', encoding='utf-8') as f:
            rows_count = len(f.readlines())
            dictonary[link] = rows_count
    sorted_dict = {}
    sorted_keys = sorted(dictonary, key = dictonary.get)
    for iter, file_name in enumerate(sorted_keys):
        # длина файла = dictonary[file_name]
        # название файла  = file_name
        if iter == 0:
            with open(result_link, 'w', encoding='utf-8') as s:
                s.write(str(file_name)+'\n')
                s.write(str(dictonary[file_name])+'\n')
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                s.write(' '.join(content) + '\n')
        else:
            with open(result_link, 'a', encoding='utf-8') as s:
                s.write(str(file_name)+'\n')
                s.write(str(dictonary[file_name])+'\n')
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                s.write(' '.join(content) + '\n')

list = ['1.txt','2.txt','3.txt']
auxiliary_function(list, 'Result file.txt')





