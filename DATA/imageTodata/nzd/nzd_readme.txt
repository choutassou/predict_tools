1. unvailabe time
     saturday 6:00 ~ monday 6:00
     holiday 6:00 ~ next day 6:00
  should not use these time in nzd.json.
  else the program will be very difficult (in function count_days and count_hours).

2. program to get data from chat
python C:\predict_tools\chartToCordinate\chart_2_data.py ^
 C:\predict_tools\DATA\imageTodata\nzd\01.png ^
 C:\predict_tools\DATA\imageTodata\nzd\nzd.json

3. program to predict
python C:\predict_tools\predict\predict_main.py C:\predict_tools\DATA\imageTodata\nzd\nzd.csv

4. automatically get last number and last time from data file

5. ***MANUALY*** should add ",yyyy-mm-dd hh:mi" to the last row of data file every time.
