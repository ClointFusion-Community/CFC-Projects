# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))


try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hrlg2bmo_generator\Images\Snips\1--324_31.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(324,31,left_or_right='left', single_double_triple = 'single')

time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hrlg2bmo_generator\Images\Snips\2--324_31.png',conf=0.7, wait=11),left_or_right='left', single_double_triple = 'double')
except:
    cf.mouse_click(324,31,left_or_right='left', single_double_triple = 'double')

time.sleep(1)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hrlg2bmo_generator\Images\Snips\3-NewTabGoogleChrome-383_81.png',conf=0.7, wait=12),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(383,81,left_or_right='left', single_double_triple = 'single')

time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_hrlg2bmo_generator\Images\Snips\4-NewTabGoogleChrome-1916_70.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1916,70,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('New Tab - Google Chrome')