$(document).ready(function(){
    $('#submit').click(function(event){
        event.preventDefault();
        $('.alert-danger').alert('close');
        var flag=0;
        var score= -1;
        var comment=$('.commenting').val();
        if($('#checker').is(':checked')){
            $('.alert-danger').alert('close');
        }
        else{
            $('.alert-danger').alert('close');
            score=$('.score').val();
             if(score==''){
                flag+=1;
                $('.score').after(
                  '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 20px; padding-top:2px;">'+
                    '<button type="button" class="close" ' +
                            'data-dismiss="alert" aria-hidden="true">' +
                        '&times;' +
                    '</button>' +
                    '请输入课程评分' +
                 '</div>');
            }
        }
        if(comment==''){
            flag+=1;
            $('.commenting').after(
              '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 20px; padding-top:2px;">'+
                '<button type="button" class="close" ' +
                        'data-dismiss="alert" aria-hidden="true">' +
                    '&times;' +
                '</button>' +
                '请输入课程评价' +
             '</div>');
        }
        if(!flag){
            $.ajax({
                url:window.location.pathname,
                type:'POST',
                dataType:'json',
                data:{
                    mark:score,
                    comment:comment,
                    sduId:window.location.pathname.split('/')[2],
                },
                success:function(data){
                    if(data.result=="success"){
                        window.location.href="/user";
                    }
                    else{
                        $('#content-wrap').replaceWith(
                          '<div style="font-size:20px; margin-top:50px;">'+
                          '<i class="fa fa-exclamation-circle" style="font-size:20px;float:left;margin:3px 15px 0 0;"></i>'+
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
            $('#content').css('height',  ($('#content').css('height')+40*flag)+'px');
        }
    });
});