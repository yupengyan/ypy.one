# Mongo 

## Change User Password

```shell
db.changeUserPassword('username','new_password')
```

## 清空数据
db.collectName.drop() 效率会高些，单索引也没有了，可以用下面这个：
```shell
db.collectName.deleteMany({})
```