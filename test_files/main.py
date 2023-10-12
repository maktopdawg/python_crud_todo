import csv
# import pandas as pd

filename = './test_files/todos.csv'
file = open('./test_files/todos.csv')
reader = csv.reader(file)
# for line in reader:
#     print(line[-1])


with open('./test_files/todos.csv', 'a') as f:
    f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    f_writer.writerow([23453, 'Learn CSV', False])
    f_writer.writerow([23453, 'Learn Frontend', True])
    # print(len(f))

with open(filename) as f:
    reader = csv.reader(f)
    for x in reader:
        del reader[1]