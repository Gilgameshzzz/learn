function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}



$(document).ready(function () {
    $('#form-avatar').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url:'/user/profile/',
            dataType:'json',
            type:'PATCH',
            success:function (data) {
                if (data.code.code == 200) {
                    $('#user-avatar').attr('src', '/static/media/'+data.img)
                }

            },
            error:function (data) {
                alert('请求失败')
            }
        })
    });
    $('#form-name').submit(function (e) {
        /*"阻止默认行为 不写会提交两次请求 一次get,一次patch"*/
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/user/change_name/',
            type:'POST',
            dataType: 'json',
            success:function (data) {
            if (data.code == 200){
                $('#user-name').html(data.name)
                $('.menu-title h3').html('用户名：'+data.name)
            }
            if (data.code == 1007){
                $('.error-msg').show()
            }
        },
            error:function (data) {
                alert('请求失败')
        }

        })
    });
     $.post("/user/my/", function(data){
        $('.menu-title h3').html('用户名：'+data.user_info.name)
        $('#user-avatar').attr('src','/static/media/'+data.user_info.avatar)
    })
})