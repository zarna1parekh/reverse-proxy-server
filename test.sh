#!/bin/bash

curl "http://localhost:8080/stats"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeList&a=sf-muni"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=N"
sleep 2
curl "http://localhost:8080/stats?responseTime>0.2"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeList&a=sf-muni"
sleep 2
curl "http://localhost:8080/stats?responseTime>0.7"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=predictionsForMultiStops&a=sf-muni&stops=N|6997&stops=N|3909"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=schedule&a=sf-muni&r=N"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&r=N&t=1144953500233"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=predictions&a=sf-muni&r=N&s=5205&useShortTitles=true"
sleep 2
curl "http://localhost:8080/stats"
sleep 2


curl "http://localhost:8080/stats"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeList&a=sf-muni"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=N"
sleep 2
curl "http://localhost:8080/stats?responseTime>0.2"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeList&a=sf-muni"
sleep 2
curl "http://localhost:8080/stats?responseTime>0.7"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=predictionsForMultiStops&a=sf-muni&stops=N|6997&stops=N|3909"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=schedule&a=sf-muni&r=N"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&r=N&t=1144953500233"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=predictions&a=sf-muni&r=N&s=5205&useShortTitles=true"
sleep 2
curl "http://localhost:8080/stats"
sleep 2



curl "http://localhost:8080/stats"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeList&a=sf-muni"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=N"
sleep 2
curl "http://localhost:8080/stats?responseTime>0.2"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=routeList&a=sf-muni"
sleep 2
curl "http://localhost:8080/stats?responseTime>0.7"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=agencyList"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=predictionsForMultiStops&a=sf-muni&stops=N|6997&stops=N|3909"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=schedule&a=sf-muni&r=N"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&r=N&t=1144953500233"
sleep 2
curl "http://localhost:8080/service/publicXMLFeed?command=predictions&a=sf-muni&r=N&s=5205&useShortTitles=true"
sleep 2
curl "http://localhost:8080/stats"
sleep 2

