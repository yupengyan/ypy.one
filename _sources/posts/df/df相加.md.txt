# 
## 空值填充
填充：

填充空值主要使用下面这个语句：

df.fillna( )

#Signature: df.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)



value可以是一个值（标量），比如我们用一列的均值来填充该列的所有空值：

df['column_name'].fillna(value = df['column_name'].mean()]
value 也可以是 dict, Series, 甚至 DataFrame，比如我们可以用字典来实现对不同的列填充不同的值：

df.fillna({'column_name_A': 0,'column_name_B': 100})

 

## Add
两个series相加，根据常识我们可以知道index不同的地方会变成空值，如下图

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
s1 + s2
a     NaN
b     NaN
c    13.0
d    24.0
e     NaN
f     NaN
如果我们希望空值的地方被原series中的值填充，即得到以下效果：

a     1
b     2
c    13
d    24
e    30
f    40
可以使用add而不是加号来进行：

s1.add(s2, fill_value = 0)