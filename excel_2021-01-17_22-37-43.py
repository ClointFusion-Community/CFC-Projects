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
time.sleep(2)
cf.key_write_enter('hi',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('sushil',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('how',key='')
time.sleep(1)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('r',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('u',key='')
time.sleep(1)
cf.key_press('space')
time.sleep(1)
cf.key_press('alt')
time.sleep(0)
cf.key_press('f4')
time.sleep(1)
cf.key_write_enter('n',key='')
time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_c3h8hfy__generator\Images\Snips\1--182_329.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(182,329,left_or_right='left', single_double_triple = 'single')

time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_c3h8hfy__generator\Images\Snips\2--189_465.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(189,465,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('nan')