# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))


try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_6hg4_u_z_generator\Images\Snips\1--330_36.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(330,36,left_or_right='left', single_double_triple = 'single')

time.sleep(0)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_6hg4_u_z_generator\Images\Snips\2--330_36.png',conf=0.7, wait=12),left_or_right='left', single_double_triple = 'double')
except:
    cf.mouse_click(330,36,left_or_right='left', single_double_triple = 'double')

time.sleep(2)
cf.key_write_enter('modi',key='')
time.sleep(0)
cf.key_press('enter')
time.sleep(2)

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\mrmay\AppData\Local\Temp\cf_log_6hg4_u_z_generator\Images\Snips\3-modiGoogleSearchGoogleChrome-1919_69.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1919,69,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('modi - Google Search - Google Chrome')