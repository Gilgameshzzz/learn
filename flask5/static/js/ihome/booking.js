function hrefBack() {
    history.go(-1);
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

function showErrorMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function() {
    var house_id = location.search.split('=')[1]
    $.get('/order/booking/' + house_id + '/', function (data) {
        var booking = template('booking_script', {ohouse: data.house_info});
        $('.house-info').html(booking);
    });
    $(".input-daterange").datepicker({
        format: "yyyy-mm-dd",
        startDate: "today",
        language: "zh-CN",
        autoclose: true
    });
    $(".input-daterange").on("changeDate", function () {
        var startDate = $("#start-date").val();
        var endDate = $("#end-date").val();

        if (startDate && endDate && startDate > endDate) {
            showErrorMsg();
        } else {
            var sd = new Date(startDate);
            var ed = new Date(endDate);
            days = (ed - sd) / (1000 * 3600 * 24) + 1;
            var price = $(".house-text>p>span").html();
            var amount = days * parseFloat(price);
            $(".order-amount>span").html(amount.toFixed(2) + "(共" + days + "晚)");
        }
    });
    $('.submit-btn').click(function () {
            var start_date = $('#start-date').val()
            var end_date = $('#end-date').val()
            if (start_date && end_date){
                /*向后台传输数据*/
                $.ajax({
                    url:'/order/order/',
                    data:{'start_date':start_date, 'end_date':end_date, 'house_id':house_id},
                    dataType:'json',
                    type:'POST',
                    success:function (data) {
                        if (data.code == 200){
                            window.location.href='/order/order/'
                        }
                    },
                    error:function () {
                        alert('提交失败')
                    }
                })
            }
    })
})
