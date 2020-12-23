from sklearn.cluster import KMeans
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import tkinter as tk

def getKMeans():
    style.use("ggplot")

    col1 = str(entry2.get())
    col2 = str(entry3.get())

    iris = pd.read_csv("iris.csv",sep=",", usecols=[col1, col2])

    iris_x = iris.iloc[:, 0:2]

    # mengubah variabel data frame menjadi array
    x_array = np.array(iris_x)

    # menampilkan data iris pada console/terminal/cmd
    # print("===== Iris =====")
    # print(iris)

    n = int(entry1.get())

    # Cek parameter dari input
    if n > 1:
        nCluster = n
    else:
        nCluster = 1

    kmeans = KMeans(n_clusters=nCluster)
    kmeans.fit(x_array)
    iris["kluster"] = kmeans.labels_

    # visualisasi
    # memberikan plot plot poin untuk visualisasi data
    output = plt.scatter(x_array[:, 0], x_array[:, 1], s=100, c=iris.kluster, marker="o", alpha=1, )
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c="red", s=200, alpha=1, marker="o")
    plt.title("Hasil Klustering Iris dengan K-Means")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.colorbar(output)
    plt.show()
    
    quit()

def getPower():
    x1 = entry1.get()

    label4 = tk.Label(root, text= float(x1)**2,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='K-Means')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Masukkan jumlah centroid:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

label3 = tk.Label(root, text='pilih 1 kolom (tidak boleh sama)\nsepal_length, sepal_width, petal_length, petal_width')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 180, window=label3)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 260, window=entry3)

button1 = tk.Button(text='Visualisasi K-Means', command=getKMeans, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 300, window=button1)

root.mainloop()