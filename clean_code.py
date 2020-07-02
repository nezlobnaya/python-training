import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()


#You want to replace the spaces in the column labels with underscores 
# to be able to reference columns with dot notation. Here's one way you could've done it.
# Bad
new_df = df.rename(columns={'fixed acidity': 'fixed_acidity',
                             'volatile acidity': 'volatile_acidity',
                             'citric acid': 'citric_acid',
                             'residual sugar': 'residual_sugar',
                             'free sulfur dioxide': 'free_sulfur_dioxide',
                             'total sulfur dioxide': 'total_sulfur_dioxide'
                            })
new_df.head()

#Better
labels = list(df.columns)
labels[0] = labels[0].replace(' ', '_')
labels[1] = labels[1].replace(' ', '_')
labels[2] = labels[2].replace(' ', '_')
labels[3] = labels[3].replace(' ', '_')
labels[5] = labels[5].replace(' ', '_')
labels[6] = labels[6].replace(' ', '_')

#Best solution:
df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

median_alcohol = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= median_alcohol:
        df.loc[i, 'alcohol'] = 'high'
    else:
        df.loc[i, 'alcohol'] = 'low'
df.groupby('alcohol').quality.mean()

median_pH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= median_pH:
        df.loc[i, 'pH'] = 'high'
    else:
        df.loc[i, 'pH'] = 'low'
df.groupby('pH').quality.mean()

median_sugar = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= median_sugar:
        df.loc[i, 'residual_sugar'] = 'high'
    else:
        df.loc[i, 'residual_sugar'] = 'low'
df.groupby('residual_sugar').quality.mean()

median_citric_acid = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= median_citric_acid:
        df.loc[i, 'citric_acid'] = 'high'
    else:
        df.loc[i, 'citric_acid'] = 'low'
df.groupby('citric_acid').quality.mean()

#Best
def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low' 

for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')


