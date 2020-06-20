import psycopg2
import numpy as np
from matplotlib import pyplot as plt
from keras.layers import Dense, Activation
from keras.models import Sequential
import statsmodels.api as sm


try:
    connection = psycopg2.connect(
        user="viewer",
        password="viewing",
        host="192.168.1.229",
        port="5432",
        database="linevu"
    )
    cursor = connection.cursor()
    
    cursor.execute("""SELECT \"Temperature\" from public.\"NG001\" where 
    timestamp between '2019-12-18 00:00:00+00' and '2019-12-20 00:00:00+00';""")
    temp = np.array(cursor.fetchall())
    
    cursor.execute("""SELECT \"Pressure\" from public.\"NG001\" where 
    timestamp between '2019-12-18 00:00:00+00' and '2019-12-20 00:00:00+00';""")
    pressure = np.array(cursor.fetchall())
    pressure_min = np.amin(pressure)
    pressure_max = np.amax(pressure)

    temp_min = np.amin(temp)
    temp_max = np.amax(temp)
    for row in pressure:
        row[0] = (row[0]-pressure_min)/(pressure_max-pressure_min)

    for row in temp:
        row[0] = (row[0]-temp_min)/(temp_max-temp_min)

    #model = Sequential()
    #model.add(Dense(4,input_dim=1,activation='relu'))
    #model.add(Dense(4,activation='relu'))
    #model.add(Dense(1,activation='sigmoid'))
    #model.compile(loss='mean_squared_error',optimizer='SGD',metrics=['mean_squared_error'])
    
   # history=model.fit(temp,pressure,epochs=10,verbose=1)


    #scores = model.evaluate(temp,pressure)
    #print("Baseline Error: %.2f%%" % (100-scores[1]*100))
    #predictions = model.predict(temp)
    #plt.plot(predictions,'r')
    #plt.plot(history.history['loss'])
    

    mod = sm.RecursiveLS(temp, pressure)
    res = mod.fit()
    print(res.summary())
    
    plt.plot(temp,'b')
    plt.plot(pressure,'g')
    plt.legend(['Prediction','Temp','Pressure'])
    plt.show()
except (Exception, psycopg2.Error) as error:
    print ("Error ", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("Postgresql connection is closed")