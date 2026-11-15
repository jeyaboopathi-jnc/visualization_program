import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")

# Create scatter plot
plt.scatter(df["sepal_length"], df["sepal_width"])

# Add title and labels
plt.title("Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Display graph
plt.show()
