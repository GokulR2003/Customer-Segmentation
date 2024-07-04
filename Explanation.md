## GUI Setup:
We use Tkinter to create a simple GUI with a button to load the customer data CSV file.
## File Loading and Validation:
The user can select a CSV file containing customer data. The code checks if the necessary columns ('Gender', 'Age', 'Annual Income (₹)', 'Spending Score (1-100)') are present.
## Data Processing and Clustering:
- The 'Gender' column is converted to numerical values.
- The Elbow Method is used to determine the optimal number of clusters.
- K-Means clustering is applied, and the results are visualized using a scatter plot.
## Visualization:
The clustering results are displayed using seaborn and matplotlib.
## User Feedback:
The application provides feedback to the user about the success or failure of the clustering process through message boxes
