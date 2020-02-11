# Python 基础

![python](./logo/Python.png)

```python
"""
代码越少越好，越简单越好
python less, work more!
"""
```

***

## 变量和语法

- 常量
  - 通常用全部大写的变量名表示

- 变量
  - None 特殊空值，可用于未访问的Excel单元格数据

- 字符编码
  - ```ASCII -> Unicode -> UTF-8```
  - 注释申明编码 ```# -*- coding: utf-8 -*-```
  - 文本编辑器编码 ```utf-8```

- 格式化
  - ```%``` 占位符格式化
  - ```"".format()```方法格式化

- 容器
  - 数组```list = []```，字典```dict = {}```，元组```tuple = (,)```，集合```set = set()```

- ```if ... elif ... else```
  - 执行第一真值
  - 借用if语句生成代码块（定义常量等）
  - ```if True: block```

- ```for ... break ... continue ... else ...```
  - for循环，只要作用于一个可迭代对象，就可运行

    ```python
    from collections import Iterable
    ```

- ```while ...```

***

## 函数

- 函数调用
  - 接口定义（参数的名字和位置确定之后，函数的接口定义即完成，对于内部的复杂实现完成了封装，调用者只需要知道如何传递正确的参数，以及返回什么样的值就够了）

    ```python
    # python code
    def demo():
        print("hello world !")
    ```

  - 函数参数（顺序:必选参数->默认参数->可变参数->命名关键字参数->关键字参数）

    ```python
    # 参数示例
    def func(a, b, c: int=0, *args, **kw):
        pass

    def func(a, b, c: int=0, *, d, **kw):
        pass
    ```

    - 必选参数在前，默认参数在后
    - python传参时，按顺序赋值，默认参数在前的话，若参数不足，则分配到必选参数的时候已经没有数值可用，将会报错
    - 多个参数，变化大的放在前面，变化小的可以放在后面作为默认参数
    - python函数在定义的时候，默认参数的值就被计算出来了，如果默认参数是一个变量，每次调用函数，如果改变了默参的内容，那下次调用的时候，默参的内容就变了

        ```python
        # python arg
        def add_end(L = []):
            L.append('END')
            return(L)

        # change to
        def add_end(L = None):
            if L is None:
                L = []
            L.append('END')
            return(L)
        ```

    - 可变参数和关键字参数

        ```python
        # 可变参数
        def func(*args):
            pass

        # 关键字参数
        def func(**args):
            pass
        ```

- 生成器
  - 生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用```yield```返回函数值，每次调用```yield```会暂停，而可以用```next()```函数和```send()```函数恢复生成器

    ```python
    (f(x) for x in range())
    ```

  - 一般通过for循环来迭代，不需要关心StopInteration的错误，函数定义的生成器调用需要先生成

    ```python
    def fib():
        pass
    FIB = fib()
    ```

***

## 模块(module)和包(package)

- 一个 .py 文件称为一个模块
- 为了避免模块名冲突，引入来按目录来组织模块的方法，称为包
- 为了简洁或避免冲突，可以引入的时候赋予别名，```import ... as ...```
- 作用域
  - 动态语言，函数签名一致接口就一样
  - 通过 _ 前缀来实现
    - 正常的函数和变量名是公开的(public)
    - \_\_xxx\_\_ 特殊变量，可以被直接引用，但是有特殊用途(\_\_doc\_\_ 访问文档注释(module 的第一个字符串))
    - \_xxx， \_\_xxx 非公开的(private)，不应该被直接引用
