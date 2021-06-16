$(document).ready(function () {


    var crd;

var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

console.log(csrftoken);



function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});




$.ajax({
    type : "PUT",
    url : "/users/userlocation/userlocation/",
    csrfmiddlewaretoken: csrftoken,
    data : '{"ul_location_lat": 22.22, "user_location_lng": 33.33 }',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
      },
    success: function(){
        console.log("Saved! It worked.");
      },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      console.log("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
      }
    });

// $.ajax({
//     url: '/users/userlocation/userlocation/',
//     type: 'POST',
//     csrfmiddlewaretoken: "{{ csrf_token }}",
//     data: "ul_location_lat=22.22&user_location_lng=33.33",
//     success: function(data) {
//       alert('Load was performed.');
//     }
//   });

function success(pos) {
    crd = pos.coords;
  
 
    console.log(crd);

    


}

function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }
  
  navigator.geolocation.getCurrentPosition(success, error, options);
  




});

