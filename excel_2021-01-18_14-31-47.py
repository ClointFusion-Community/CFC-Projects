# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))

cf.key_write_enter('ote',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(1)
cf.key_write_enter('hi',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(1)
cf.key_write_enter('sshil',key='')
time.sleep(0)
cf.key_press('backspace')
time.sleep(0)
cf.key_press('backspace')
time.sleep(0)
cf.key_press('backspace')
time.sleep(0)
cf.key_press('ctrl+A')
cf.key_press('ctrl+X')
cf.key_press('ctrl+C')
cf.key_press('ctrl+V')
cf.key_press('ctrl+Z')

time.sleep(0)
cf.key_write_enter('ushil',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('how',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(1)
cf.key_write_enter('r',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('u',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(1)


time.sleep(1)
cf.key_press('f4')
time.sleep(0)
cf.key_press('alt')
time.sleep(1)
cf.key_write_enter('n',key='')
time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_p5mk6zd0_generator\Images\Snips\1-ProgramManager-914_133.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'double')
except:
    cf.mouse_click(914,133,left_or_right='left', single_double_triple = 'double')

time.sleep(0)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_p5mk6zd0_generator\Images\Snips\2-ProgramManager-914_133.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(914,133,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Program Manager')