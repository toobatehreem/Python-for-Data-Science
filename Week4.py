#files

with open("Week4.txt", "w") as W:
    a = "hello world\nThis is Tooba Tehreem Sheikh\nI am an extreme programmar"
    W.write(a)      #writes a file

with open ("Week4.txt", "r") as W:
    reads = W.read()
    print(reads)            #reads the context of the file
    #W.close()
print(W.closed)

with open ("Week4.txt", "r") as W:
    reads = W.readline()        #reads one line at a time
    print(reads)

with open ("Week4.txt", "r") as W:
    reads = W.readlines(1)       #reads all lines
    print(reads)

with open ("Week4.txt", "a") as W:
    #appends into the file instead of overwriting
    W.write("\nthis is appeneded")

with open ("Week4.txt", "r") as W:
    reads = W.read()
    print(reads)            #reads the context of the file

#pandas

import pandas as pd

csv_path ='C:\\Users\\Tooba Tehreem Sheikh\\Documents\\Csv1.csv' #or 'Csv1.csv
df = pd.read_csv(csv_path)

print(df.head())        #prints only a number of rows


