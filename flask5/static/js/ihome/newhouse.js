function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
    var area_id = document.getElementById("area-id");
    $.get('/house/new/', function (data) {
        if (data.code == 200){
            for (var i = 1; i <= data.house_area.length; i++){
                var opt = document.createElement("option");
                opt.value = i;
                opt.innerText = data.house_area[i-1];
                area_id.appendChild(opt);
            };
            for (var j = 1; j <= data.facility.length; j++){
                var str2 = '<li><div class="checkbox"><label><input type="checkbox" name="facility" value="' + j + '">' + data.facility[j-1] + '</label></div></li>'
                $('.clearfix').append(str2)
            };

        }
    });
    $("#form-house-info").submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url:'/house/newhouse/',
            type:'POST',
            dataType:'json',
            success:function (data) {
                if (data.code == 200){
                    alert('添加成功')
                    $("#form-house-info").hide()
                    $("#form-house-image").show()

                    $("#house-id").attr('value',data.house_id)
                }
            },
            error:function () {
                alert('失败')
            }
        })

    });
    $("#form-house-image").submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url:'/house/image/',
            type:'PATCH',
            dataType: 'json',
            success:function (data) {
                if (data.code == 200){
                    for (var i=0;i < data.imgs.length;i++){
                        var img = ' <img src="'+'/static/media/'+data.imgs[i]+'" >'
                        $('#show-photo').append(img)
                    }

                }

            },
            error:function () {
                alert(893)
            }
        })
    })
})