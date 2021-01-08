# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))


try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log__z3uxdh7_generator\Images\Snips\1--234_1079.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(234,1079,left_or_right='left', single_double_triple = 'single')

time.sleep(1)
cf.key_write_enter('chrome',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log__z3uxdh7_generator\Images\Snips\2-NewTabGoogleChrome-584_40.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(584,40,left_or_right='left', single_double_triple = 'single')

time.sleep(0)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log__z3uxdh7_generator\Images\Snips\3-NewTabGoogleChrome-584_40.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'double')
except:
    cf.mouse_click(584,40,left_or_right='left', single_double_triple = 'double')

time.sleep(0)
cf.key_write_enter('google',key='')
time.sleep(1)
cf.key_press('enter')
time.sleep(0)


time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log__z3uxdh7_generator\Images\Snips\4-GoogleGoogleChrome-1919_0.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1919,0,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Google - Google Chrome')