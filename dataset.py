import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

plt.scatter(df["sepal_length"], df["sepal_width"])

plt.title("Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Save graph as image
plt.savefig("iris_graph.png")

plt.show()
