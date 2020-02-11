# Python 编程技巧

## 程序可执行设定

- 直接运行 ```*.py``` 文件
  - windows
    - 直接设置 ```pylaunch``` 为默认执行程序
  - Mac
    - ```#!/usr/bin/evn python3``` 指明解释器位置
    - ```$ chmod a+x *.py```  赋予执行权限

## 如何解决自定义库的搜索路径问题

- 编写初始化脚本

  ```python
  import os
  import sys

  # python 安装目录
  pth = sys.exec_prefix
  # 在 python 根目录添加.pth路径文件
  pkg = os.path.join(pth, 'pkg.pth')

  ''' 读写区分
  if not os.path.exists(pkg):
      with open(pkg, 'w', encoding='utf-8') as pkh:
          pkh.write(os.getcwd())
  else:
      with open(pkg, 'r+', encoding='utf-8') as pkh:
          pkh.write(os.getcwd())
  '''

  # 作为临时工作目录修改
  with open(pkg, 'w', encoding='utf-8') as pkh:
      # 将当前工作目录，即顶层目录写入路径文件
      pkh.write(os.getcwd())
      print("path: \"{0}\" is added to \"{1}\"".format(os.getcwd(), pkg))
  ```

## 代码维护

### 通过配置文件来间接保存数据库密码等信息

- 参考<https://blog.csdn.net/u013344884/article/details/81224213>

## openpyxl

### read and write

- sheet.rows produce a generator, the same as sheet.columns
- list(sheet.rows) change the generator to a list
- 参考<https://www.cnblogs.com/sun-haiyu/p/7096423.html>
