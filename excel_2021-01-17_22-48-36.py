# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))

cf.key_press('cmd')
time.sleep(1)
cf.key_write_enter('notepad',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(1)
cf.key_write_enter('hi',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('ushiil',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('\x18\x03\x16',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_press('ctrl+Z')
time.sleep(1)
cf.key_press('space')
time.sleep(3)


time.sleep(1)
cf.key_press('ctrl+A')
time.sleep(1)
cf.key_press('ctrl+S')
time.sleep(3)


time.sleep(1)


time.sleep(2)
cf.key_press('esc')
time.sleep(1)
cf.key_press('f4')
time.sleep(0)
cf.key_press('alt')
time.sleep(1)
cf.key_write_enter('n',key='')
time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_3loprauk_generator\Images\Snips\1--179_254.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(179,254,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('nan')