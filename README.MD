** Introduction **
       The iParking product aims at providing new age parking experience for the end user and provides a integrated
       platform for parking Avenues. The parking avenue dashboard provides a real time parking management platform 
       via which each parking slot can be dynamically priced based on demand, attributes of the car. 

 **Config**
       The web app contains a python REST client which populates the BMW Car Simulator with mock up car data.
       It populates Vehicles with all the necessary  information like static data of the car, geo points of the car, its
       billing history. A mock up parking slots are also added via the python rest client with all necessary data points 
       like availability of the parking slots, billing price, its history. 

       This web app feeds real time events into keen io data streaming which processes the events in time series fashion. 
       Keen IO facilitates time series view of the events with stats like parking business, hourly occupany of the parking 
       avenue and related activities.
    
**Codebase**   
       * Web App
           simulator.py
       *  Keen IO stereaming
            keen_cl.py

**Future**
       All these real time stat is planned to be fed into other arenas like parking bidding system, retailers parking avenue 
       for easier parking management meanwhile providing seemless parking for end user.
