# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))

cf.key_write_enter('otepad',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(1)
cf.key_write_enter('hi',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('sushil',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('how',key='')
time.sleep(0)
cf.key_press('ctrl+A')

time.sleep(0)
cf.key_write_enter('r',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('\x03',key='')
time.sleep(3)
cf.key_write_enter('\x1a',key='')
time.sleep(3)


time.sleep(2)


time.sleep(1)
cf.key_press('alt+f4')
time.sleep(0)


time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_xjmiz0q2_generator\Images\Snips\1-ProgramManager-739_190.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'double')
except:
    cf.mouse_click(739,190,left_or_right='left', single_double_triple = 'double')

time.sleep(0)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_xjmiz0q2_generator\Images\Snips\2-ProgramManager-825_371.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(825,371,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Program Manager')