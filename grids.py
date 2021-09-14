import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# print(sns.get_dataset_names())
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')
# print(iris.head())

# sns.pairplot(iris)

# g = sns.PairGrid(iris)
# g.map(plt.scatter)
# g.map_diag(sns.distplot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot)

# Facet Grid
g = sns.FacetGrid(data=tips, col='time', row='smoker')
# g.map(sns.distplot, 'total_bill')
g.map(sns.scatterplot, 'total_bill', 'tip')

plt.show()