$(document).ready(function(){
  $('#next_homework').click(function(){
    var uri=window.location.pathname.split('/');
    var courseid=uri[3];
    $.ajax({
      url:'/user/updateCourse/',
      type:'POST',
      dataType:'json',
      data:{
        'signal':1,
        'idcourse':courseid,
      },
      success:function(data){
        if(data.result=="success"){
          if(data.setform==1){
              window.location.href="/setForm/"+courseid;
          }
          else{
              window.location.href="/user";
          }
        }
        else{
          $('#content-wrap').replaceWith(
            '<div style="text-align: center; font-size:20px; margin-top:50px;">'+
            '<i class="fa fa-exclamation-circle" style="font-size:40px;"></i>'+
            '<p style="margin-top:20px;">'+
            data.result+
            '</p>'+
            '</div>'
          );
          var docHeight = $(window).height();
          var footerHeight = $('#footer').height();
          var footerTop = $('#footer').position().top;

          if (footerTop < docHeight) {
           $('#content').css('height',  (docHeight - footerHeight - 40) + 'px');
          }
        }
      },
    })
  });
  $('#start_next').click(function(){
    var uri=window.location.pathname.split('/');
    var courseid=uri[3];
    $.ajax({
      url:'/user/updateCourse/',
      type:'POST',
      dataType:'json',
      data:{
        'signal':0,
        'idcourse':courseid,
      },
      success:function(data){
        if(data.result=="success"){
          if(data.setform==1){
              window.location.href="/setForm/"+courseid;
          }
          else{
              window.location.href="/user";
          }
        }
        else{
          $('#content-wrap').replaceWith(
            '<div style="text-align: center; font-size:20px; margin-top:50px;">'+
            '<i class="fa fa-exclamation-circle" style="font-size:40px;"></i>'+
            '<p style="margin-top:20px;">'+
            data.result+
            '</p>'+
            '</div>'
          );
          var docHeight = $(window).height();
          var footerHeight = $('#footer').height();
          var footerTop = $('#footer').position().top;

          if (footerTop < docHeight) {
           $('#content').css('height',  (docHeight - footerHeight - 40) + 'px');
          }
        }
      },
    })
  });
});
