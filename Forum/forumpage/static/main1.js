  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function makeGrid(n) {
    for (var x=0; x<n; x++) {
        tr = $('<tr></tr>');
        for (var y=0; y<n; y++) {
            tr.append('<td><div class="canvas"></div></td>');
        }
        $('#TABLE_ID').append(tr)
    }
}

$(document).ready(function() {
  $("#Post").click(function(){
    // console.log("in ajax")
      $.ajax({
        url: "/db/",
        type: "post",
        data: {'text': $("#PostContent").val(), 'RoomID' : window.roomID, csrfmiddlewaretoken: getCookie('csrftoken')},
        success: function(result){
            postText = $("#PostContent").val()
            postelement = "<p class='postlist' align='center'>" + postText + "</p>"
            $("#posthere").append(postelement);
          }
      });
    });

  $("body").on("click","#newroombutton",function() {
    $.ajax({
        url: createRoomURL,
        type: "post",
        success: function(result) {
            var atags = '';
            for (var i = 0; i < result["roomIDs"].length; i++) {
                id = result["roomIDs"][i];
                atags = atags + "<a href=\"" + homepageRedirectURL + id + "/\"> Room" +  id + "</a>";
            }
            atags = atags + '<a id="newroombutton"> New Room</a>';
            $("#dropdownmenu").html(atags);
        }
    })


  });
})


// function redirectTo(){
//      var link = $order.paymentBefore; // some thing like this you can set value for 1st Param.
//     window.location.href="http://google.com/"+link+"/";

// }


