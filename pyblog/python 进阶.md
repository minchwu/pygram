# 流畅的 Python

## Python 的面向对象

> 通过mro表查看类的继承关系
> class.mro() = class.\_\_mro\_\_
> python 独有多继承特性，可以同时继承多个类
> 经典类查找深度优先；新式类查找广度优先
> python 没有真正的私有化变量，是借由重命名实现的外部不可直接访问
> 在python中没有真正意义的隐藏，只能从语法级别去实现这件事

```python
# 经典类
class A:
    pass
# 新式类
class B(object):
    pass
```

## Python 的函数式编程
