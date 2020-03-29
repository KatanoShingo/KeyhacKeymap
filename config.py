import sys
import os
import datetime
import pyauto
from keyhac import *
def configure(keymap):
 #どのウインドウにフォーカスがあっても効くキーマップ
    if 1:
        keymap_global = keymap.defineWindowKeymap()
#アプリ切り替え
        keymap_global[ "RS-Z" ] = "Win-1"
        keymap_global[ "RS-X" ] = "Win-2"
        keymap_global[ "RS-C" ] = "Win-3"
        keymap_global[ "RS-V" ] = "Win-4"
        keymap_global[ "RS-B" ] = "Win-5"
#ウィンドウの移動の配置変更
        keymap_global[ "LC-LW-Left" ] = "LW-LS-Left"
        keymap_global[ "LC-LW-Right" ] = "LW-LS-Right"
#仮想ウデスクトップ追加
        keymap_global[ "LC-LW-LA-N" ] = "LC-LW-D"
#仮想ウデスクトップ削除
        keymap_global[ "LC-LW-LA-Delete" ] = "LC-LW-F4"
#仮想ウデスクトップ移動
        keymap_global[ "LC-LW-LA-Left" ] = "LC-LW-Right"
        keymap_global[ "LC-LW-LA-Right" ] = "LC-LW-Left"
#クローム用タブ切り替え
        keymap_global[ "RS-LS-Z" ] = "C-1"
        keymap_global[ "RS-LS-X" ] = "C-2"
        keymap_global[ "RS-LS-C" ] = "C-3"
        keymap_global[ "RS-LS-V" ] = "C-4"
        keymap_global[ "RS-LS-B" ] = "C-5"
# アンダースコア入れ替え
        keymap_global[ "Underscore" ] = "S-Underscore"
        keymap_global[ "S-Underscore" ] = "Underscore"
#無変換をWinキーに置き換え
        keymap.replaceKey( 29, "LWin" )