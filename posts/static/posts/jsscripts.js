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
   context: this,
   url: '/friends/accept-requests-detail/',
   data: {
   'serializedVall': $(this).attr("value")
   },
   type: "GET",
   success: function(response) {
   $(this).hide();
   alert("friend request has been added successfully");
   }
  });
 
 });
 
 $(document).on('click', '#liked', function(e){
  e.preventDefault();
  $.ajax({
   context: this,
   url: '/posts/like/',
   data: {
   'serializedVall': $(this).attr("value")
   },
   type: "GET",
   success: function (json) {
  $('.far').removeClass('far').addClass('fas');
  $('.fa-heart').css('color','red')
  $('#NumLike').css('color','red')
  $('#NumLike').html(json['result']);
  console.log(json);
    
   }
  });
 
 });



 $(document).on('click', '.posts', function(e){
  e.preventDefault();
  
  $.ajax({
   context: this,
   url: '/posts/like/',
   data: {
   'serializedVall': $(this).attr("value")
   },
   type: "GET",
   success: function (json) {

  $(this).removeClass(json['odd']).addClass(json['lat'])
  $(this).css('color',json['col'])
  $(this).html(json['result'])



  
  console.log(json);
   }
  });
 
 });

 