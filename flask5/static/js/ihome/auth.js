function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function () {
    $('#form-auth').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/user/auth/',
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.code.code == 200) {

                    $('#real-name').attr('value', data.user.id_name)
                    $('#id-card').attr('value', data.user.id_card)
                     $('.btn-success').hide()
                    $('.error-msg').hide()
                }
                if (data.code == 1008){
                    $('.error-msg i').html(data.msg)
                    $('.error-msg').show()
                }
                if (data.code == 1005){
                    $('.error-msg').show()
                }
            },
            error: function () {
                alert('987')
            }
        });

    });
    $.get('/user/show_id/', function (data) {
        if (data.code.code == 200){
            if (data.user_id.id_name && data.user_id.id_card){
                $('#real-name').attr('value', data.user_id.id_name)
                $('#id-card').attr('value', data.user_id.id_card)
                $('.btn-success').hide()
            }
        }
    })
})

