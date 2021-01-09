# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))

cf.key_press('cmd')
time.sleep(3)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hcx12b0q_generator\Images\Snips\1--27_1060.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(27,1060,left_or_right='left', single_double_triple = 'single')

time.sleep(1)
cf.key_write_enter('notepad',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(1)
cf.key_press('shift')
time.sleep(0)
cf.key_write_enter('hello',key='')
time.sleep(0)
cf.key_press('f4')
time.sleep(0)
cf.key_press('alt')
time.sleep(3)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hcx12b0q_generator\Images\Snips\2-Notepad-945_242.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(945,242,left_or_right='left', single_double_triple = 'single')

time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hcx12b0q_generator\Images\Snips\3-Notepad-987_359.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(987,359,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Notepad')