1. 

2. program to get data from chat
python C:\predict_tools\chartToCordinate\chart_2_data.py C:\predict_tools\DATA\imageTodata\aud_daily\01.png C:\predict_tools\DATA\imageTodata\aud_daily\aud_daily.json

3. program to predict
python C:\predict_tools\predict\predict_main.py C:\predict_tools\DATA\imageTodata\aud_daily\aud_daily.csv
m_b=20, p_b=1
next_y=91.80665084409138, delta=-0.008567485484974244

4. automatically get last number and last time from data file

5. ***MANUALY*** should add ",yyyy-mm-dd hh:mi" to the last row of data file every time.

6. ********** daily is failing... bug. can't get last day value
   finally, i did it....
    # right edge, it will not be so accurate, so give it a range
    if abs(px - img_width) < 2:
        # to avoid a px out of bound
        px = img_width - 1
    if px - img_width > 2:
        break
        # to end the loop

7. the image, should have red point at edge.