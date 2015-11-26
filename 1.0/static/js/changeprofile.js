$(document).ready(function(){
     $("#submit").click(function(){
        var flag = 0;
        $('.alert').alert('close');
        var id=$('#user_id').text();
        var name=$('#user_name').val();
        if(name==""){
          flag+=1;
          $("#user_name").after(
        '<div class="alert alert-danger alert-dismissable" style="margin-bottom: 10px; padding-top:5px;">'+
            '<button type="button" class="close" ' +
                    'data-dismiss="alert" aria-hidden="true">' +
                '&times;' +
            '</button>' +
            '请输入姓名' +
         '</div>');
        }

        var class_num=$("#user_class_num").val();
        var course_num=$('#Num0').text();
         if(course_num=="选择课序号"){
             course_num=''
         }
        var email=$("#user_email").val();
        var pwd_user=$('#user_pwd').val();
        var pwd_confirm=$('#user_pwd_confirm').val();
        if(pwd_user==""){
          flag+=1;
          $("#user_pwd").after(
        '<div class="alert alert-danger alert-dismissable" style="margin-bottom: 10px; padding-top:5px;">'+
            '<button type="button" class="close" ' +
                    'data-dismiss="alert" aria-hidden="true">' +
                '&times;' +
            '</button>' +
            '请输入密码' +
         '</div>');
        }
        else if(pwd_confirm==""){
          flag+=1;
          $("#user_pwd_confirm").after(
        '<div class="alert alert-danger alert-dismissable" style="margin-bottom: 10px; padding-top:5px;">'+
            '<button type="button" class="close" ' +
                    'data-dismiss="alert" aria-hidden="true">' +
                '&times;' +
            '</button>' +
            '请确认密码' +
         '</div>');
        }
        else if(pwd_user!=pwd_confirm){
            alert(pwd_user);
            alert(pwd_confirm);
            flag+=1;
            $("#user_pwd_confirm").after(
          '<div class="alert alert-danger alert-dismissable" style="margin-bottom: 10px; padding-top:5px;">'+
              '<button type="button" class="close" ' +
                      'data-dismiss="alert" aria-hidden="true">' +
                  '&times;' +
              '</button>' +
              '两次输入密码不同' +
           '</div>');
        }

        var term=$('#fun2').text();
        if(term=="秋季学期")
          term="1";
        else if(term=='春季学期')
          term="2";
        else
          term="3";

        if(!flag){
            $.ajax({
                url:window.location.link,
                type:'POST',
                dataType:'json',
                data:{
                    'id':id,
                    'email':email,
                    'name':name,
                    'class':class_num,
                    'course':course_num,
                    'pwd':pwd_user,
                    'time':term,
                },
                success:function(data){
                  if(data.result=='success'){
                    window.location.href="/user";
                  }
                  else {
                    $('#content-wrap').replaceWith(
                      '<div style="text-align: center; font-size:20px; margin-top:50px;">'+
                      '<i class="fa fa-exclamation-circle" style="font-size:40px;"></i>'+
                      '<p style="margin-top:20px;">'+
                      data.result+
                      '</p>'+
                      '</div>'
                    )
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
