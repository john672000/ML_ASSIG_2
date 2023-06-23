import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the glass dataset
glass_data = pd.read_csv('glass.csv')

# Visualization 1: Correlation Matrix
corr_matrix = glass_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Visualization 2: Pairwise Scatter Plot
sns.pairplot(glass_data, hue='Type')
plt.title('Pairwise Scatter Plot')
plt.show()

# Visualization 3: Matplot Scatter Plot
plt.scatter(glass_data['RI'], glass_data['Ca'])
plt.xlabel('Refractive Index (RI)')
plt.ylabel('Calcium Content (Ca)')
plt.title('Scatter Plot: RI vs Ca')
plt.show()

