# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))

cf.key_write_enter('ote',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(2)
cf.key_write_enter('hi',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('ushsil',key='')
time.sleep(0)
cf.key_write_enter('\x01\x18\x03',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(1)
cf.key_write_enter('how',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('ru',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(1)
cf.key_write_enter('\x03',key='')
time.sleep(0)
cf.key_write_enter('\x1a',key='')
time.sleep(1)


time.sleep(3)


time.sleep(1)
cf.key_press('alt+f4')
time.sleep(0)


time.sleep(1)
cf.key_write_enter('n',key='')
time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_tz583slx_generator\Images\Snips\1-ProgramManager-744_138.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(744,138,left_or_right='left', single_double_triple = 'single')

time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_tz583slx_generator\Images\Snips\2-ProgramManager-773_306.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(773,306,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Program Manager')