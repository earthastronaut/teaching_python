# ###### Variables ####### #
#
# A variable in any programming language is a named piece of computer memory, containing some information inside.
#
# Variables have a type which define their logical representation and size 
#

bool_variable = True
int_variable = 1
float_variable = 3.1419
string_variable = "hello"


# ###### Built-in Data Structures ####### #
#
# Four built in python data structures: list, tuple, dictionary, set
#
# check out -- https://python.swaroopch.com/data_structures.html 

# ###### List ####### #
# 
# A list is a ordered collection of variables
# 

list_variable = [1, 2, 3]

a = [1, "hello", True]

# accessing lists

a[0]
a[:3]
a[1:-1]

# mutation

a[0] = "change_variable"

# looping
for variable in a:
    print(variable)

# methods

a.append(2.2)
a.pop(0)


# ###### Tuple ####### #
# 
# A tuple is a immutable ordered collection of variables
#

tuple_variable = (1, 2, 3)

b = (1, "hello", True)

# accessing lists

b[0]
b[:3]
b[1:-1]

# looping

for variable in b:
    print(variable)


# ###### Dict ####### #
# 
# A dictionary is a mutable, random access, key-value structure
#

dict_variable = {
    'key1': 'variable',
    'key2': 1.23,
    'value_is_list': [1, 2.34],
    5: 'five',
}

c = dict_variable

# accessing

c['key1']
c[5]
c['value_is_list']

# mutations

c['key2'] = 'changed variable'
c['new_key'] = 'added_a_key_value_pair'

# looping

for i in range(2, 10):
    print(i)
    # add the key `i` with value 'hello'
    c[i] = 'hello'

for key in c:
    print(key, ' is set to ', c[key])

for key, value in c.items():
    print(key, 'is set to ', value)

# methods

c.pop('key1')
c.get('not_a_key', 'default')


# ###### Set ####### #
# 
# A set is a mutable, unordered unique collection of objects
#

set_variable = {1, 1, 3, 3, 'hello'}

d = {2, 4, 6}
e = {1, 2, 3}

# methods

d.add(7)
d.remove(7)

# set operations
# 
# http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1526998740/15_union_intersection_difference_symmetric.png
#
d.union(e)                # = {1, 2, 3, 4, 6} union or full outer join
d.intersection(e)         # = {2} intersection or inner join
d.difference(e)           # = {4, 6} difference between d and e
d.symmetric_difference(e) # = {1, 3, 4, 6} union minus the intersection



# ###### Data Science Data Structures ####### #
#
# There are several key data structures not built into python but widely used
#


# ###### Array ####### #
# 
# An array is an ordered collection of variables of a single type. 
#

import numpy as np 

array_variable = np.array([1, 2, 3])

# constructing

np.linspace(1, 100, 10) # min, max, number of steps
f = np.arange(1, 10, 0.5) # min, max, step size

# accessing

f[0]
f[:2]
f[2:-1]

# accessing: masks
#
# a mask is an array of same length with True/False values 
#

mask = (f > 5)
f[mask]


# methods

f.sum()
f.mean()


# matrix

g = np.array([
    [1, 2, 3],
    [4, 5, 6],
]) # 2 x 3 matrix

# accessing matrix

g[0, :2]
g[:-1, 1:2]

# mutations

g[0, :2] = -1

# methods

g.shape 
g.sum()
g.mean()
g.ravel()
g.T # transpose

# linear algebra

g.dot([1, 2, 3])
np.linalg


# ###### Data Frame ####### #
# 
# A data frame, is a collection of arrays very similar to a table. 
#

import pandas as pd 

dataframe_variable = pd.DataFrame({
    'column1': [1.1, 2.1, 3.1],
    'column2': ['a', 'b', 'c'],
})

h = dataframe_variable

h['col3'] = np.random.rand(3)


# index and columns

h.index 
h.columns

h.set_index('column1', inplace=True)

# accessing

h['col3']
h['col3'][2.1]
h['col3'][:2]

h[['column2', 'col3']]

# accessing: loc
#
# loc and iloc are the two primary access methods for data frames
# loc uses the names within the index
# 

h.loc[:, 'col3']
mask = (h['column2'] == 'a')
h.loc[mask, 'column2']

# accessing: iloc
#
# loc and iloc are the two primary access methods for data frames
# iloc uses the index as though it was a 2d matrix
# 

h.iloc[:2, 0]
h.iloc[:2, :-1]

# looping

for column in h:
    print(column, h[column])

# Input output (IO)

h.to_csv('untracked_example.csv')
h_other = pd.read_csv('untracked_example.csv')

iris = pd.read_csv('data/iris.csv')


# Group by operations

"""
SELECT COUNT(*) 
FROM iris
GROUP BY species
"""
iris.groupby('species').size()


"""
SELECT
    COUNT(*) AS number
    , AVG(pedal_length) AS avg_pedal_length
    , AVG(pedal_width) AS avg_pedal_width
    , AVG(pedal_length - pedal_width) AS avg_pedal_length_to_width
FROM iris
GROUP BY species
WHERE
    petal_length > 1.2
"""
gb = iris.query('petal_length > 1.2').groupby('species')
df = pd.DataFrame()
df['number'] = gb.size()
df['avg_petal_length'] = gb['petal_length'].mean()
df['avg_petal_width'] = gb['petal_width'].mean()


def difference_length_and_width(group):
    average_diff = (group['petal_length'] - group['petal_width']).mean()
    return average_diff
df['avg_petal_length_to_width'] = gb.apply(difference_length_and_width)


# joins (aka merge)

rows = [
    ('setosa', 'Arctic Sea'),
    ('setosa', 'Russia'),
    ('setosa', 'North Eastern Asia'),
    ('setosa', 'Japan'),
    ('virginica', 'Eastern North America'),
    ('versicolor', 'Eastern North America'),
    ('versicolor', 'Eastern Canada'),
]
region_info = pd.DataFrame(rows, columns=['species', 'region'])


"""
SELECT *
FROM 
    iris i
    JOIN region_info ri ON i.species = ri.species
"""
iris.merge(region_info, on='species', how='inner')

