$(document).ready(function(){
    $('#submit').click(function(){
        var flag = 0;
        var uri = window.location.pathname.split('/');
        var stuid = uri[2].split('_')[0];
        var period = uri[2].split('_')[1];
        var content = $('.commenting').val();
        if(content==""){
           $(".commenting").after(
          '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 10px; padding-top:5px;">'+
            '<button type="button" class="close" ' +
                    'data-dismiss="alert" aria-hidden="true">' +
                '&times;' +
            '</button>' +
            '请输入评价内容' +
         '</div>');
            flag+=1;
        }
        if(!flag){
            $.ajax({
                url:window.location.pathname,
                type:'POST',
                dataType:'json',
                data:{
                  stuid:stuid,
                  period:period,
                  content:content,
                },
                success:function(data){
                    if(data.result=="success"){
                        window.location.href='/student/'+stuid;
                    }
                    else{
                      $('#content-wrap').replaceWith(
                        '<div style="text-align: center; font-size:20px; margnnin-top:50px;">'+
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
                }
            });
        }
        else{
          $('#content').css('height',  ($('#content').css('height')+55*flag)+'px');
        }
    });
});