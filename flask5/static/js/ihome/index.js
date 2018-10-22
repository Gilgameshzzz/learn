//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function setStartDate() {
    var startDate = $("#start-date-input").val();
    if (startDate) {
        $(".search-btn").attr("start-date", startDate);
        $("#start-date-btn").html(startDate);
        $("#end-date").datepicker("destroy");
        $("#end-date-btn").html("离开日期");
        $("#end-date-input").val("");
        $(".search-btn").attr("end-date", "");
        $("#end-date").datepicker({
            language: "zh-CN",
            keyboardNavigation: false,
            startDate: startDate,
            format: "yyyy-mm-dd"
        });
        $("#end-date").on("changeDate", function() {
            $("#end-date-input").val(
                $(this).datepicker("getFormattedDate")
            );
        });
        $(".end-date").show();
    }
    $("#start-date-modal").modal("hide");
}

function setEndDate() {
    var endDate = $("#end-date-input").val();
    if (endDate) {
        $(".search-btn").attr("end-date", endDate);
        $("#end-date-btn").html(endDate);
    }
    $("#end-date-modal").modal("hide");
}

function goToSearchPage(th) {
    var url = "/house/search/?";
    url += ("aid=" + $(th).attr("area-id"));
    url += "&";
    var areaName = $(th).attr("area-name");
    if (undefined == areaName) areaName="";
    url += ("aname=" + areaName);
    url += "&";
    url += ("sd=" + $(th).attr("start-date"));
    url += "&";
    url += ("ed=" + $(th).attr("end-date"));
    url += ("&sk=new")
    location.href = url;
}

$(document).ready(function(){
    $(".top-bar>.register-login").show();

    $(".area-list a").click(function(e){
        $("#area-btn").html($(this).html());
        $(".search-btn").attr("area-id", $(this).attr("area-id"));
        $(".search-btn").attr("area-name", $(this).html());
        $("#area-modal").modal("hide");
    });
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);               //当窗口大小变化的时候
    $("#start-date").datepicker({
        language: "zh-CN",
        keyboardNavigation: false,
        startDate: "today",
        format: "yyyy-mm-dd"
    });
    $("#start-date").on("changeDate", function() {
        var date = $(this).datepicker("getFormattedDate");
        $("#start-date-input").val(date);
    });
    $.get('/house/new/', function (data) {
        if (data.code == 200) {
            for (var i = 1; i <= data.house_area.length; i++) {
                var a = '<a href="#" area-id="'+i+'">'+data.house_area[i - 1]+'</a>';
                $('.area-list').append(a);
            }
            $(".area-list a").click(function(e){
                $("#area-btn").html($(this).html());
                $(".search-btn").attr("area-id", $(this).attr("area-id"));
                $(".search-btn").attr("area-name", $(this).html());
                $("#area-modal").modal("hide");
            });
        }
    });
    $.post('/house/index/', function (data) {
        if (data.code == 200){
            if (data.user){
                $('.user-info a').html(data.user.name)
                $('.user-info').show()
                $('.register-login').hide()

            };
              for (var i=0; i < 3; i++){
                var a = parseInt(data.house.length)
                var num = Math.floor(Math.random() * a );
                var info = '<div class="swiper-slide">\n' +
                '  <a href="/house/detail/?house_id='+data.house[num]['id'] +'"><img src="/static/media/'+data.house[num]['image'] +'"></a>\n' +
                '  <div class="slide-title">房屋标题:'+data.house[num]['title']+'</div>\n' +
                '   </div>'
                $('.swiper-wrapper').append(info)
            }
            var mySwiper = new Swiper ('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationClickable: true
            });
        }
    });
})
