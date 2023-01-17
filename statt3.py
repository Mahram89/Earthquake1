##Author: Mahram 
##Date: January.2023
import datetime, json, requests, pandas as pd, numpy as np, folium, os
from IPython.display import HTML, display
from folium.plugins import MarkerCluster
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from dateutil import relativedelta
from requests_futures.sessions import FuturesSession
from concurrent.futures import wait
from datetime import datetime,timedelta
from pandas.io.json import json_normalize
from pandas.plotting import scatter_matrix

#count 1
{type:"FeatureCollection",
 metadata:{
     generated:1673967514000,
     url:"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson",
     title:"USGS Magnitude 1.0+ Earthquakes, Past Hour",
     status:200,
     api:"1.10.3",
     count:5
     },
 bbox: [
   -155.4006652832,
   18.763666666667,
    1.3500000238419,
   -65.111166666667,
   38.8346672,
   32.619998931885
 ],
 features:[
     {
      type:"Feature",
      properties:{
          mag:1.08,
          place:"8km WSW of Idyllwild, CA",
          time:1673967386870,
          updated:1673967512649,
          tz:null,
          url:"https://earthquake.usgs.gov/earthquakes/eventpage/ci40403320",
          detail:"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40403320.geojson",
          felt:null,
          cdi:null,
          mmi:null,
          alert:null,
          status:"automatic",
          tsunami:0,
          sig:18,
          net:"ci",
          code:"40403320",
          ids:",ci40403320,",
          sources:",ci,",
          types:",nearby-cities,origin,phase-data,scitech-link,",
          nst:17,
          dmin:0.07561,
          rms:0.11,
          gap:111,
          magType:"ml",
          type:"earthquake",
          title:"M 1.1 - 8km WSW of Idyllwild, CA"
          },
      geometry:{
          type:"Point",
          coordinates:[
              -116.8021698,
              33.706665,
              16.78
              ]
          },
      id:"ci40403320"},
     
     # count 2 takes the features
{
 type:"Feature",
 properties:{
     mag:1.33,
     place:"8km W of Cobb, CA",
     time:1673967064220,
     updated:1673967159333,
     tz:null,
     url:"https://earthquake.usgs.gov/earthquakes/eventpage/nc73833196",
     detail:"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73833196.geojson",
     felt:null,
     cdi:null,
     mmi:null,
     alert:null,
     status:"automatic",
     tsunami:0,
     sig:27,
     net:"nc",
     code:"73833196",
     ids:",nc73833196,",
     sources:",nc,",
     types:",nearby-cities,origin,phase-data,",
     nst:28,
     dmin:null,
     rms:0.02,
     gap:51,
     magType:"md",
     type:"earthquake",
     title:"M 1.3 - 8km W of Cobb, CA"
     },
 geometry:{
     type:"Point",
     coordinates:[-122.809166,
                  38.8346672,
                  2.09
                  ]
     },
 id:"nc73833196"
 },

# count 3 takes the features and geometry. 
{
 type:"Feature",
 properties:{
     mag:1.8,
     place:"14 km SSE of Volcano, Hawaii",
     time:1673966702870,
     updated:1673967355241,
     tz:null,
     url:"https://earthquake.usgs.gov/earthquakes/eventpage/hv73305897",
     detail:"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv73305897.geojson",
     felt:1,
     cdi:2,
     mmi:null,
     alert:null,
     status:"automatic",
     tsunami:0,
     sig:50,
     net:"hv",
     code:"73305897",
     ids:",hv73305897,",
     sources:",hv,",
     types:",dyfi,origin,phase-data,",
     nst:40,
     dmin:null,
     rms:0.200000003,
     gap:92,
     magType:"ml",
     type:"earthquake",
     title:"M 1.8 - 14 km SSE of Volcano, Hawaii"
     },
 geometry:{
     type:"Point",
     coordinates:[-155.167999267578,
                  19.3271675109863,
                  1.35000002384186
                  ]
     },
 id:"hv73305897"
 },

# count 4 takes the features and geometry.
{
 type:"Feature",
 properties:{
     mag:2.67,
     place:"Virgin Islands region",
     time:1673964753380,
     updated:1673966696040,
     tz:null,
     url:"https://earthquake.usgs.gov/earthquakes/eventpage/pr71393058",
     detail:"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr71393058.geojson",
     felt:null,
     cdi:null,
     mmi:null,
     alert:null,
     status:"reviewed",
     tsunami:0,
     sig:110,
     net:"pr",
     code:"71393058",
     ids:",pr71393058,",
     sources:",pr,",
     types:",origin,phase-data,",
     nst:5,
     dmin:0.4346,
     rms:0.25,
     gap:274,
     magType:"md",
     type:"earthquake",
     title:"M 2.7 - Virgin Islands region"
     },
 geometry:{
     type:"Point",
     coordinates:[-65.1111666666667,
                  18.7636666666667,
                  17.16
                  ]
     },
 id:"pr71393058"
 },

# count 5 takes the features and geometry 
{
 type:"Feature",
 properties:{
     mag:2.1400001,
     place:"10 km NE of Pāhala, Hawaii",
     time:1673964726310,
     updated:1673967176249,
     tz:null,
     url:"https://earthquake.usgs.gov/earthquakes/eventpage/hv73305877",
     detail:"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv73305877.geojson",
     felt:1,
     cdi:2,
     mmi:null,
     alert:null,
     status:"automatic",
     tsunami:0,
     sig:71,
     net:"hv",
     code:"73305877",
     ids:",hv73305877,",
     sources:",hv,",
     types:",dyfi,origin,phase-data,",
     nst:37,
     dmin:null,
     rms:0.140000001,
     gap:125,
     magType:"md",
     type:"earthquake",
     title:"M 2.1 - 10 km NE of Pāhala, Hawaii"
     },
 geometry:{
     type:"Point",
     coordinates:[-155.400665283203,
                  19.2646675109863,
                  32.6199989318848
                  ]
     },
 id:"hv73305877"
 }
],
#bbox:[-155.4006652832,18.763666666667,1.3500000238419,-65.111166666667,38.8346672,32.619998931885]}
