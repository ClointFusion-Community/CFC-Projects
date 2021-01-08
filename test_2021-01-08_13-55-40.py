# This code is generated automatically by ClointFusion BOT Builder Tool.
import ClointFusion as cf 
import time 

cf.window_show_desktop() 
cf.mouse_click(int(cf.pg.size()[0]/2),int(cf.pg.size()[1]/2))


try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r'C:\Users\Karth\AppData\Local\Temp\cf_log_4c8f77fw_generator\Images\Snips\1--1275_973.png',conf=0.7, wait=10),left_or_right='left', single_double_triple = 'single')
except:
    cf.mouse_click(1275,973,left_or_right='left', single_double_triple = 'single')

time.sleep(0)
cf.window_close_windows('nan')