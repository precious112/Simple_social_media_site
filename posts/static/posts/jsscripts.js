$(document).on('click', '#buttonOne', function(){
  $.ajax({
   url: 'add-friend/',
   data: {
   'serializedVal': $(this).attr("value")
   },
   type: "GET",
   success: function(response) {
   $("#buttonOne").hide();
   alert("friend request has been sent successfully");
   }
  });
 
 });
 
 
$(document).on('click', '#buttonTwo', function(){
  $.ajax({
   url: '/friends/accept-requests-detail/',
   data: {
   'serializedVall': $(this).attr("value")
   },
   type: "GET",
   success: function(response) {
   $("#buttonTwo").hide();
   alert("friend request has been added successfully");
   }
  });
 
 });