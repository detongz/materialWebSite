$(document).ready(function(){
    $('#submit').click(function(){
        var flag=0;
        $('.alert-danger').alert('close');
        var id=$('#user_id').val();
        var name=$('#user_name').val();
        var pwd=$('#user_pwd').val();
        var pwdC=$('#user_pwd_confirm').val();
        var email=$('#user_email').val();
        if(id==''||pwd==''||pwd!=pwdC||email==''){
            $("#tab").after(
              '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 10px; padding-top:5px;">'+
                '<button type="button" class="close" ' +
                        'data-dismiss="alert" aria-hidden="true">' +
                    '&times;' +
                '</button>' +
                '请将需要输入的内容补充完整' +
             '</div>');
            flag+=1;
            $('#content').css('height',($('#content').css('height')+55*flag)+'px');
        }
        else{
            $.ajax({
                url:window.location.href,
                type:'post',
                dataType:'json',
                data:{
                    'id':id,
                    'name':name,
                    'email':email,
                    'pwd':pwd,
                },
                success:function(data){
                    if(data.result=='success'){
                        window.location.href='/Material/user/teacher/setting/picture/'+id;
                    }
                    else{
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
            })
        }
    });
});