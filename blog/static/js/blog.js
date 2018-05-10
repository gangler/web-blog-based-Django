
$(function(){
    $("#button-save").hide();
    $("#button-reply").hide();
});

function delete_click(){

    if(confirm('确定删除？') == true){
        document.getElementById('a-delete').href = "delete/";
    }
}

function title_filter(){
    title = $("#id_title").val();
    str = special_filter(title);
    str = script_filter(str);
    str = image_filter(str);
    str = other_filter(str);
    str = keyword_filter(str);
    return str
}

function text_filter(){
    text = $("#id_text").val();
    str = special_filter(text);
    str = script_filter(str);
    str = image_filter(str);
    str = other_filter(str);
    str = keyword_filter(str);
    return str
}

function cclick(){
    var str = title_filter();
    $("#id_title").val(str);
    var str2 = text_filter();
    $("#id_text").val(str2);
    $("#button-check").hide();
    $("#button-save").show();
}

function dclick(){
    var str = text_filter();
    $("#id_text").val(str);
    $("#button-check").hide();
    $("#button-reply").show();
}

function special_filter(s){
    // 去掉转义字符
    //\'\"\\\/\b\f\n\r\t
    // 去掉特殊字符
    //\@\#\$\%\^\&\*\{\}\:\L\<\>\?
    var str = s.replace(/\\'|\\"|\\b|\\f|\\n|\\r|\\t|\\@|\\#|\\$|\\%|\\&|\\*|\\:|\\L|\\?/g, '');
    return str
}

function script_filter(s){
    //去掉<script>标签
    var str = s.toLowerCase().replace(/<script/g, '');
    return str
}

function image_filter(s){
    //去掉贴图代码
    var str = s.replace(/<img/g, '');
    return str
}

function other_filter(s){
    //去掉其他代码
    //<embed ，<input ，<iframe ，<object ，<applet ，<meta
    var str = s.replace(/<embed|<input|<object|<applet|<meta/g, '');
    return str
}

function keyword_filter(s){
    //去掉关键字词
    var dict = ["过滤","字词"]
    for(var i=0;i<dict.length;i++){
        s = s.replace(dict[i].substr(0), '');
    }
    return s
}