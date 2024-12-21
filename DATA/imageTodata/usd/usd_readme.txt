1. unvailabe time
     saturday 6:00 ~ monday 6:00
     holiday 6:00 ~ next day 6:00
  should not use these time in usd.json.
  else the program will be very difficult (in function count_days and count_hours).

2. program to get data from chat
python C:\LOC\develop\GITHUB\predict_tools\chartToCordinate\chart_2_data.py C:\LOC\develop\GITHUB\predict_tools\DATA\imageTodata\usd\03.png C:\LOC\develop\GITHUB\predict_tools\DATA\imageTodata\usd\usd.json

3. program to predict
python C:\LOC\develop\GITHUB\predict_tools\predict\predict_main.py C:\LOC\develop\GITHUB\predict_tools\DATA\imageTodata\usd\usd.csv

4. automatically get last number and last time from data file

5. ***MANUALY*** should add ",yyyy-mm-dd hh:mi" to the last row of data file every time.
