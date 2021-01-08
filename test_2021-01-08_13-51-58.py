# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))


try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log_ix7fhvxl_generator\Images\Snips\1--205_1076.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(205,1076,left_or_right='left', single_double_triple = 'single')

time.sleep(1)
cf.key_write_enter('chrome',key='')
time.sleep(1)
cf.key_press('enter')
time.sleep(1)
cf.key_write_enter('google',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(0)


time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log_ix7fhvxl_generator\Images\Snips\2-GoogleGoogleChrome-1011_27.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1011,27,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('Google - Google Chrome')