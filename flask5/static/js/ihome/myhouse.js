$(document).ready(function(){
    $(".auth-warn").show();
    $("#houses-list").hide();
    $.get('/house/myhouse_info/',function (data) {
        if (data.code == 200){
            if (data.id_name){
                $(".auth-warn").hide()
                $("#houses-list").show()

            };
            for (var i=0; i < data.house_info.length; i++){
                var info = "<li>\n" +
                    ' <a href="/house/detail/?house_id='+data.house_info[i]['id']+'">\n' +
                    "  <div class=\"house-title\">\n" +
                    "     <h3>房屋ID:"+data.house_info[i]['id']+ " ——"+ data.house_info[i]['title']+"</h3>\n" +
                    "  </div>\n" +
                    "    <div class=\"house-content\">\n" +
                    "   <img src=\"/static/media/"+data.house_info[i]['image']+"\">\n" +
                    "    <div class=\"house-text\">\n" +
                    "     <ul>\n" +
                    "      <li>位于："+data.house_info[i]['area']+"</li>\n" +
                    "     <li>价格：￥"+data.house_info[i]['price']+"/晚</li>\n" +
                    "    <li>发布时间："+data.house_info[i]['create_time']+"</li>\n" +
                    "      </ul>\n" +
                    "   </div> \n" +
                    "   </div>\n" +
                    "  </a>\n" +
                    " </li>";
                $("#houses-list").append(info)
            }
        }
    })
})