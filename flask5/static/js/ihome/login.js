function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        $.ajax({
            url: '/user/login/',
            type: 'POST',
            dataType: 'json',
            data: {'mobile':mobile, 'password':passwd},
            success:function(data){
                if (data.code == 200){
                    window.location.href='/house/index/'
                }
                if (data.code == 1000) {
                    $("#mobile-err span").html(data.msg);
                    $("#mobile-err").show();
                    return;
                }
                if (data.code ==1005) {
                    $("#password-err span").html(data.msg);
                    $("#password-err").show();
                    return;
                }
                if (data.code ==1004) {
                    $("#password-err span").html(data.msg);
                    $("#password-err").show();
                    return;
                }
                if (data.code == 1006) {
                    $("#mobile-err span").html(data.msg);
                    $("#mobile-err").show();
                    return;
                }
            },
            error:function (data) {
            }
        })
    });
})