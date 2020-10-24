'''
Created on 2020/10/24

@author: conan
'''
__all__ = ['SearchFile', ]

import os.path

from logging import getLogger
logger = getLogger(__name__)


def SearchFile(FileName, BasePath):
    """
    BasePathより上位フォルダに遡りながら最初に見つかったFileNameのパスを返す。
    """
    Path = os.path.join(BasePath, FileName)
    if os.path.exists(Path):
        return Path
    Path = os.path.dirname(BasePath)
    if Path == BasePath:
        return None
    return SearchFile(FileName, Path)


if __name__ == '__main__':
    pass
