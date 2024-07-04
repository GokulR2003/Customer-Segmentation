# Customer Segmentation with K-Means Clustering

This project demonstrates customer segmentation using the K-Means clustering algorithm, enhanced with a simple graphical user interface (GUI) built with Tkinter. The GUI allows users to load a dataset, perform clustering, and visualize the results.

## Features

- Load customer data from a CSV file
- Perform K-Means clustering
- Visualize the optimal number of clusters using the Elbow Method
- Visualize the clusters using a scatter plot

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/GokulR2003/Customer-Segmentation.git
    cd customer-segmentation
    ```

2. Install the required libraries:

    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```

## Usage

1. Run the main script:

    ```bash
    python CustomerSegmentation.py
    ```

2. Click the "Load Data and Cluster" button to load your customer data CSV file.

3. The script expects the CSV file to contain the following columns:
    - `Gender`: Male or Female
    - `Age`: Customer's age
    - `Annual Income (₹)`: Customer's annual income in Indian Rupees
    - `Spending Score (1-100)`: Customer's spending score

4. After loading the data, the script will display the Elbow Method graph to help determine the optimal number of clusters.

5. The script will then perform K-Means clustering and visualize the clusters in a scatter plot.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

