import pandas as pd
from sklearn.cluster import KMeans
import statsmodels.api as sm
import statsmodels.formula.api as smf

QWE = pd.read_csv('QWE-data.csv')

linear_mod = smf.glm(formula='Churn~Age*CHI+Views+Last_Login', data=QWE, family=sm.families.Binomial())
linear_result = linear_mod.fit()

print linear_result.summary()
print

QWE_data = QWE.drop(['Churn','id'], axis=1)
QWE_array = QWE_data.values

print '>>>>> Input Array <<<<<<'
print
print QWE_array
print

km = KMeans(n_clusters=6)
km.fit(QWE_array)

print '>>>>> Cluster Means Raw Output <<<<<<'
print
print km.cluster_centers_
print

print '>>>>> Cluster Means Final DataFrame <<<<<<'
print
clus_mean = pd.DataFrame(km.cluster_centers_, columns=QWE_data.columns.values)
clus_mean['cluster'] = clus_mean.index + 1
print clus_mean


