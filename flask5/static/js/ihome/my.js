function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.post("/user/my/", function(data){
        $('#user-name').html(data.user_info.name)
        $('#user-mobile').html(data.user_info.phone)
        $('#user-avatar').attr('src','/static/media/'+data.user_info.avatar)
    })

})