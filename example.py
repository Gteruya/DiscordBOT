#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Discord Bot プログラム：Discord Botとして動作します。
"""

__author__ = ''
__version__ = '0.0.0'
__date__ = '2023/02/22 (Created: 2023/02/22)'

import sys

from config import CONFIG

def main():
    """
    Discord Botとして動作するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """

    # print(CONFIG["ACCESS_TOKEN"])

    return 0

if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    sys.exit(main())
