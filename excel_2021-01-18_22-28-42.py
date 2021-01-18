# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))

cf.key_write_enter('otepad',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_press('enter')
time.sleep(2)
cf.key_write_enter('hi',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_press('ctrl+A')
cf.key_press('ctrl+Z')
cf.key_press('ctrl+X')
cf.key_press('ctrl+C')
cf.key_press('ctrl+V')

time.sleep(0)
cf.key_press('space')
time.sleep(0)
cf.key_write_enter('how',key='')
time.sleep(0)
cf.key_press('space')
time.sleep(1)
cf.key_write_enter('ru',key='')
time.sleep(1)
cf.key_press('space')
time.sleep(2)
cf.key_press('alt')
time.sleep(2)


time.sleep(1)
cf.key_press('f4')
time.sleep(0)
cf.key_press('alt')
time.sleep(1)
cf.key_write_enter('n',key='')
time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Sushil\AppData\Local\Temp\cf_log_638_yp0q_generator\Images\Snips\1-ProgramManager-785_430.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(785,430,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Program Manager')