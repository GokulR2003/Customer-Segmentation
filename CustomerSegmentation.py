import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox

def load_and_cluster():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            df = pd.read_csv(file_path)
            if not all(col in df.columns for col in ['Gender', 'Age', 'Annual Income (₹)', 'Spending Score (1-100)']):
                messagebox.showerror("Error", "Dataset must contain 'Gender', 'Age', 'Annual Income (₹)', and 'Spending Score (1-100)' columns.")
                return
            df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
            X = df[['Gender', 'Age', 'Annual Income (₹)', 'Spending Score (1-100)']]
            wcss = []
            for i in range(1, 11):
                kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
                kmeans.fit(X)
                wcss.append(kmeans.inertia_)
            plt.figure(figsize=(10, 5))
            plt.plot(range(1, 11), wcss, marker='o')
            plt.title('The Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            plt.show()
            optimal_clusters = 3
            kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
            df['Cluster'] = kmeans.fit_predict(X)
            plt.figure(figsize=(10, 5))
            sns.scatterplot(data=df, x='Annual Income (₹)', y='Spending Score (1-100)', hue='Cluster', palette='viridis', s=100)
            plt.title('Customer Segmentation')
            plt.xlabel('Annual Income (₹)')
            plt.ylabel('Spending Score (1-100)')
            plt.legend()
            plt.show()
            messagebox.showinfo("Success", "Customer segmentation completed and visualized successfully.")
        else:
            messagebox.showwarning("Warning", "No file selected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
root = tk.Tk()
root.title("Customer Segmentation")
btn_load = tk.Button(root, text="Load Data and Cluster", command=load_and_cluster)
btn_load.pack(pady=20)
root.mainloop()
