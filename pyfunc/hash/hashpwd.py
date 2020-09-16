# -*- coding: utf-8 -*-
# author: Wu Mingchun
"""hashpwd.

哈希函数加密数据库密码
"""

import hashlib

PWD = "Wu12260917"

hm = hashlib.md5()
hm.update("WATCHDOG!@#SPACE".encode('utf-8'))
hm.update(PWD.encode('utf-8'))

print(hm.hexdigest())
