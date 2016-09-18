from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

def similar_gemeentes(df, gemeente_id, columns, n=5):

    normalizer = StandardScaler()
    nn = NearestNeighbors()

    values = df[columns].values

    values = normalizer.fit_transform(values)
    nn.fit(values)

    value = df.loc[gemeente_id][columns].values.reshape(1, -1)
    value = normalizer.transform(value)

    near = nn.kneighbors(value, n_neighbors=n)[1][0]

    return df.ix[df.index[near]]
