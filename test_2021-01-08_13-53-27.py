# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))


try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log_5lu5eyba_generator\Images\Snips\1--326_1065.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(326,1065,left_or_right='left', single_double_triple = 'single')

time.sleep(1)
cf.key_write_enter('chrome',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(3)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log_5lu5eyba_generator\Images\Snips\2-NewTabGoogleChrome-1011_40.png',conf=0.7, wait=13),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1011,40,left_or_right='left', single_double_triple = 'single')

time.sleep(3)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log_5lu5eyba_generator\Images\Snips\3--1267_985.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1267,985,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('nan')