function hrefBack() {
    history.go(-1);
}

function decodeQuery() {
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function (result, item) {
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function () {
    var house_id = location.search.split('=')[1]
    $.get('/house/detail/' + house_id + '/', function (data) {
        var booking_temp = template('booking_temp_script', {ohouse: data.house_detail});
        $('.detail-con').html(booking_temp);
        var img_temp = template('img_temp_script', {oimg: data.house_detail});
        $('#swiper-container').append(img_temp);
        $('.book-house').attr('href', '/order/booking/?house_id=' + house_id)
        var mySwiper = new Swiper('.swiper-container', {
            loop: true,
            autoplay: 2000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            paginationType: 'fraction'
        });
        $(".book-house").show();
        if (data.flag) {
            $('.book-house').hide()
        }
        ;
    })
})