$(document).ready(function(){
    var year=$('.year').text();
    for(var i=year;i<(parseInt(year)+6);i++){
        $(".year_menu").append('<li class="year_opt"><a>'+i+'</a></li>');
    }
    $(".year_opt").click(function(){
        $(".year").text($(this).text());
    });
    $(".term-opt").click(function(){
        $(".term").text($(this).text());
    });

    $('#submit').click(function(event){
        event.preventDefault();
        var flag=0;
        $('.alert').alert('close');
        var week=$('#week-num').val();
        if(week==''){
            $('#week-num').after(
              '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 20px; padding-top:2px;">'+
                '<button type="button" class="close" ' +
                        'data-dismiss="alert" aria-hidden="true">' +
                    '&times;' +
                '</button>' +
                '请输入课程开始周数' +
             '</div>');
            flag+=1;
        }
        var num=$('#course-num').val();
        if(num==""){
            flag+=1;
            $('#course-num').after(
              '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 20px; padding-top:2px;">'+
                '<button type="button" class="close" ' +
                        'data-dismiss="alert" aria-hidden="true">' +
                    '&times;' +
                '</button>' +
                '请输入课序号' +
             '</div>'
            );
        }
        var max=$('#max').val();
        if(max==""){
            flag+=1;
            $('#max').after(
              '<div class="alert alert-danger alert-dismissable"  style="margin-bottom: 20px; padding-top:2px;">'+
                '<button type="button" class="close" ' +
                        'data-dismiss="alert" aria-hidden="true">' +
                    '&times;' +
                '</button>' +
                '请输入课程提交作业总数' +
             '</div>'
            );
        }
        var term=$('.term').text();
        if(term=="秋季学期")
          term="autumn";
        else if(term=='春季学期')
          term="spring";
        else
          term="summer";
        var year=$('.year').text();
        if(!flag){
            $.ajax({
                url:'/createCourse',
                type:'POST',
                dataType:'json',
                data:{
                    'year':year,
                    'term':term,
                    'course_num':num,
                    'start_week':week,
                    'max':max,
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
                },
            });
        }
        else{
            $('#content').css('height',  ($('#content').css('height')+40*flag)+'px');
        }
    });
});