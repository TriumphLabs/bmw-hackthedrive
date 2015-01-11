var client = new Keen({
  projectId: "54b1af4a2fd4b13c34583e3c",
  readKey: "e82a057e6db0420eae3f8731c8b3e6ab2495d4896820d94d916c513a1ef3bcc082bd2840c2b1155ef172676519c6b4b2b663eae703c89ace55ccd1b8af35fd4a75908e323e52a7fe9a5bb57983386d8d870e2bf71ac9062c2dc8fb3ba0b063479d7c64399d0168d893148a5fc8cedb5f"
});

var geoProject = new Keen({
  projectId: "54b1af4a2fd4b13c34583e3c",
  readKey: "e82a057e6db0420eae3f8731c8b3e6ab2495d4896820d94d916c513a1ef3bcc082bd2840c2b1155ef172676519c6b4b2b663eae703c89ace55ccd1b8af35fd4a75908e323e52a7fe9a5bb57983386d8d870e2bf71ac9062c2dc8fb3ba0b063479d7c64399d0168d893148a5fc8cedb5f"
});

Keen.ready(function(){

  // ----------------------------------------
  // Mapbox Demo
  // ----------------------------------------
  var DEFAULTS = {
    coordinates: {
      lat: 37.77350,
      lng: -122.41104
    },
    zoom: 15
  };

  var map,
      markerStart = DEFAULTS.coordinates,
      activeMapData;


    L.mapbox.accessToken = "pk.eyJ1Ijoia2Vlbi1pbyIsImEiOiIza0xnNXBZIn0.PgzKlxBmYkOq6jBGErpqOg";
    map = L.mapbox.map("map", "keen-io.kae20cg0", {
      attributionControl: true,
      center: [markerStart.lat, markerStart.lng],
      zoom: DEFAULTS.zoom
    });
    var center = map.getCenter();
    var zoom = map.getZoom();

    z = zoom-1;
    if (zoom = 0){
      radius = false;
    }
    else {
      radius = 10000/Math.pow(2,z);
    }

    activeMapData = L.layerGroup().addTo(map);

    map.attributionControl.addAttribution('<a href="https://keen.io/">Custom Analytics by Keen IO</a>');

    var scoped_events = new Keen.Query("select_unique", {
      eventCollection: "parking_v4",
      targetProperty: "keen.location.coordinates",
      groupBy: "occupied",
      latest: 25,
    });
    geoProject.run(scoped_events, function(res){

      Keen.utils.each(res.result[0].result, function(coord, index){
        var em = L.marker(new L.LatLng(coord[1], coord[0]), {
          icon: L.mapbox.marker.icon({
              "marker-color": Keen.Visualization.defaults.colors[1]
            })
        }).addTo(activeMapData);
      });

      Keen.utils.each(res.result[1].result, function(coord, index){
        var em = L.marker(new L.LatLng(coord[1], coord[0]), {
          icon: L.mapbox.marker.icon({
              "marker-color": Keen.Visualization.defaults.colors[0]
            })
        }).addTo(activeMapData);
      });

    });

    map.on('zoomend', function(e) {
      resize();
    });
    map.on('dragend', function(e) {;
      resize();
    });



  var resize = function(){
    activeMapData.clearLayers();

    center = map.getCenter(),
    zoom = map.getZoom();

    z = zoom-1;
    if (zoom = 0){
      radius = false;
    }
    else {
      radius = 10000/Math.pow(2,z);
    }

    var scoped_events = new Keen.Query("select_unique", {
      eventCollection: "parking_v4",
      targetProperty: "keen.location.coordinates",
      groupBy: "occupied",
      latest: 25,
    });
    geoProject.run(scoped_events, function(res){

      Keen.utils.each(res.result[0].result, function(coord, index){
        var em = L.marker(new L.LatLng(coord[1], coord[0]), {
          icon: L.mapbox.marker.icon({
              "marker-color": Keen.Visualization.defaults.colors[1]
            })
        }).addTo(activeMapData);
      });

      Keen.utils.each(res.result[1].result, function(coord, index){
        var em = L.marker(new L.LatLng(coord[1], coord[0]), {
          icon: L.mapbox.marker.icon({
              "marker-color": Keen.Visualization.defaults.colors[0]
            })
        }).addTo(activeMapData);
      });

    });
    
  };



  // ----------------------------------------
  // Violations line chart
  // ----------------------------------------
  var pageviews_timeline = new Keen.Query("count", {
    eventCollection: "parking_v4",
    groupBy: "occupied",
    latest: 25
    // timeframe: {
    //   start: "2015-01-11T10:00:00.000Z",
    //   end: "2015-01-12T05:00:00.000Z"
    // }
  });
  client.draw(pageviews_timeline, document.getElementById("chart-01"), {
    chartType: "piechart",
    title: null,
    height: 175,
    width: "auto",
    colors: null,
    chartOptions: {
      chartArea: {
        left: "5%",
        top: "5%",
        height: "85%",
        width: "95%"
      },
      pieHole: .4
    }
  });


  // ----------------------------------------
  // Violations
  // ----------------------------------------
  var impressions_timeline = new Keen.Query("count", {
    eventCollection: "parking_v4",
    groupBy: "occupied",
    interval: "every_10_minutes",
    timeframe: {
      start: "2015-01-11T10:00:00.000Z",
      end: "2015-01-12T05:00:00.000Z"
    }
  });
  client.draw(impressions_timeline, document.getElementById("chart-03"), {
    chartType: "columnchart",
    title: false,
    height: 175,
    width: "auto",
    chartOptions: {
      chartArea: {
        left: "5%",
        top: "5%",
        height: "85%",
        width: "93%"
      },
      bar: {
        groupWidth: "85%"
      },
      isStacked: true
    }
  });

  // ----------------------------------------
  // Violations by Officer
  // ----------------------------------------
  var impressions_timeline_by_country = new Keen.Query("sum", {
    eventCollection: "parking_v4",
    interval: "every_30_minutes",
    targetProperty: "bill_amt",
    timeframe: {
      start: "2015-01-11T10:00:00.000Z",
      end: "2015-01-12T05:00:00.000Z"
    }
  });
  client.draw(impressions_timeline_by_country, document.getElementById("chart-05"), {
    chartType: "columnchart",
    title: false,
    height: 175,
    width: "auto",
    chartOptions: {
      chartArea: {
        left: "5%",
        top: "5%",
        height: "85%",
        width: "93%"
      },
      bar: {
        groupWidth: "85%"
      },
      isStacked: true
    }
  });
});
