import sys
import os
import datetime
import pyauto
from keyhac import *

class MAP:
    def __init__(self, keymap):
        self.ime = False
#ユーザー設定    
        MultiDisplay = True
#どのウインドウにフォーカスがあっても効くキーマップ
        keymap_global = keymap.defineWindowKeymap()
#アプリ切り替え
        keymap_global[ "RS-Z" ] = "Win-1"
        keymap_global[ "RS-X" ] = "Win-2"
        keymap_global[ "RS-C" ] = "Win-3"
        keymap_global[ "RS-V" ] = "Win-4"
        keymap_global[ "RS-B" ] = "Win-5"

        if MultiDisplay:
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
# アンダースコア入れ替え
        keymap_global[ "Underscore" ] = "S-Underscore"
        keymap_global[ "S-Underscore" ] = "Underscore"
        
#左十字キー
        keymap_global[ "RA-W" ] = "Up"
        keymap_global[ "RA-A" ] = "Left"
        keymap_global[ "RA-D" ] = "Right"
        keymap_global[ "RA-S" ] = "Down"

        def key_A():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "A" )()
        keymap_global[ "A" ] = key_A

        def key_B():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "B" )()
        keymap_global[ "B" ] = key_B 
        
        def key_C():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "C" )()
        keymap_global[ "C" ] = key_C 

        def key_D():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "D" )()
        keymap_global[ "D" ] = key_D

        def key_E():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "E" )()
        keymap_global[ "E" ] = key_E
        
        def key_F():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "F" )()
        keymap_global[ "F" ] = key_F

        def key_G():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "G" )()
        keymap_global[ "G" ] = key_G

        def key_H():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "H" )()
        keymap_global[ "H" ] = key_H 
        
        def key_I():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "I" )()
        keymap_global[ "I" ] = key_I

        def key_J():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "J" )()
        keymap_global[ "J" ] = key_J

        def key_L():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "L" )()
        keymap_global[ "L" ] = key_L 
        
        def key_N():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "N" )()
        keymap_global[ "N" ] = key_N

        def key_M():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "M" )()
        keymap_global[ "M" ] = key_M

        def key_O():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "O" )()
        keymap_global[ "O" ] = key_O 
        
        def key_P():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "P" )()
        keymap_global[ "P" ] = key_P

        def key_Q():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "Q" )()
        keymap_global[ "Q" ] = key_Q

        def key_R():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "R" )()
        keymap_global[ "R" ] = key_R
        
        def key_S():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "S" )()
        keymap_global[ "S" ] = key_S

        def key_T():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "T" )()
        keymap_global[ "T" ] = key_T

        def key_U():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "U" )()
        keymap_global[ "U" ] = key_U
        
        def key_V():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "V" )()
        keymap_global[ "V" ] = key_V

        def key_W():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "W" )()
        keymap_global[ "W" ] = key_W

        def key_X():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "X" )()
        keymap_global[ "X" ] = key_X
        
        def key_Y():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "Y" )()
        keymap_global[ "Y" ] = key_Y
        
        def key_Z():
            if ( self.ime ):
                keymap.getWindow().setImeStatus(1)
            else:
                keymap.getWindow().setImeStatus(0)        
            return keymap.InputKeyCommand( "Z" )()
        keymap_global[ "Z" ] = key_Z

#CapsLock
        def key_240():
            self.ime = not self.ime       
            keymap.InputKeyCommand( "(240)" )()
        keymap_global[ "(240)" ] = key_240 

#半角全角        
        def key_243():
            self.ime = not self.ime       
            keymap.InputKeyCommand( "(243)" )()
        keymap_global[ "(243)" ] = key_243 

        def key_244():
            self.ime = not self.ime       
            keymap.InputKeyCommand( "(244)" )()
        keymap_global[ "(244)" ] = key_244 

#数字対応
        def num_1():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "1" )()
        keymap_global[ "1" ] = num_1

        def num_2():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "2" )()
        keymap_global[ "2" ] = num_2

        def num_3():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "3" )()
        keymap_global[ "3" ] = num_3

        def num_4():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "4" )()
        keymap_global[ "4" ] = num_4

        def num_5():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "5" )()
        keymap_global[ "5" ] = num_5

        def num_6():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "6" )()
        keymap_global[ "6" ] = num_6

        def num_7():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "7" )()
        keymap_global[ "7" ] = num_7

        def num_8():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "8" )()
        keymap_global[ "8" ] = num_8

        def num_9():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "9" )()
        keymap_global[ "9" ] = num_9

        def num_0():
            if ( keymap.wnd.getImeStatus() ):
                keymap.getWindow().setImeStatus(0)
            keymap.InputKeyCommand( "0" )()
        keymap_global[ "0" ] = num_0

#Insertをbackspaceに置き換え
        keymap.replaceKey( 45, 8 )

#無変換、変換を未定義の仮想キーに置き換え
        keymap.replaceKey( 28, 58 )
        keymap.replaceKey( 29, 59 )
#IMEオン
        def ime_on():
            keymap.getWindow().setImeStatus(1)
            self.ime =  True
        keymap_global[ "(58)" ] =  ime_on
#IMEオフ
        def ime_off():
            keymap.getWindow().setImeStatus(0)
            self.ime = False  
        keymap_global[ "(59)" ] = ime_off


        keymap_chrome = keymap.defineWindowKeymap( exe_name="chrome.exe" )
#クローム用タブ切り替え
        keymap_chrome[ "RS-LS-Z" ] = "C-1"
        keymap_chrome[ "RS-LS-X" ] = "C-2"
        keymap_chrome[ "RS-LS-C" ] = "C-3"
        keymap_chrome[ "RS-LS-V" ] = "C-4"
        keymap_chrome[ "RS-LS-B" ] = "C-5"
#クローム用タブ削除
        keymap_chrome[ "LC-Delete" ] = "LC-W"

def configure(keymap):
    if 1:
        MAP(keymap)    