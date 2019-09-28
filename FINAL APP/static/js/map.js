(function() {
  var placesAutocomplete = places({
    appId: "plOQN1VFM7PR",
    apiKey: "365ba44089fa518e43f04b557e701aad",
    container: document.querySelector("#input-map")
  });

  var map = L.map("map-example-container", {
    center: [39.8283, -98.5795],
    zoom: 13,
    scrollWheelZoom: false,
    zoomControl: true
  });

  var x =
    "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}";
  var y = L.tileLayer(x, {
    minZoom: 3,
    maxZoom: 18,
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: "mapbox.streets",
    accessToken:
      "pk.eyJ1IjoicmZ1a2FtYWNoaSIsImEiOiJjazBqNGlycTQwNnduM3BxczFvbmhxc3BzIn0.4YsTym9VpET0D6rq-qRiQw"
  }).addTo(map);

  var markers = [];

  map.setView(new L.LatLng(39.8283, -98.5795), 1);

  placesAutocomplete.on("suggestions", handleOnSuggestions);
  placesAutocomplete.on("cursorchanged", handleOnCursorchanged);
  placesAutocomplete.on("change", handleOnChange);
  placesAutocomplete.on("clear", handleOnClear);

  function handleOnSuggestions(e) {
    markers.forEach(removeMarker);
    markers = [];

    if (e.suggestions.length === 0) {
      map.setView(new L.LatLng(0, 0), 1);
      return;
    }

    e.suggestions.forEach(addMarker);
    findBestZoom();
  }

  function handleOnChange(e) {
    markers.forEach(function(marker, markerIndex) {
      if (markerIndex === e.suggestionIndex) {
        markers = [marker];
        marker.setOpacity(1);
        findBestZoom();
      } else {
        removeMarker(marker);
      }
    });
  }

  function handleOnClear() {
    map.setView(new L.LatLng(0, 0), 1);
    markers.forEach(removeMarker);
  }

  function handleOnCursorchanged(e) {
    markers.forEach(function(marker, markerIndex) {
      if (markerIndex === e.suggestionIndex) {
        marker.setOpacity(1);
        marker.setZIndexOffset(1000);
      } else {
        marker.setZIndexOffset(0);
        marker.setOpacity(0.5);
      }
    });
  }

  function addMarker(suggestion) {
    var marker = L.marker(suggestion.latlng, { opacity: 0.4 });
    marker.addTo(map);
    markers.push(marker);
  }

  function removeMarker(marker) {
    map.removeLayer(marker);
  }

  function findBestZoom() {
    var featureGroup = L.featureGroup(markers);
    map.fitBounds(featureGroup.getBounds().pad(0.5), { animate: false });
  }
})();
