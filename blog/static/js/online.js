$(document).ready(function(){

$("#id_username").blur(function(){
    var username = $("#id_username").val();
    var reg = /^[\w]{4,16}$/;
    var flag = reg.test(username);
    if(username != "" && flag == false){
        alert("用户名格式错误，必须为4-16位的英文字母或数字");
        return;
    }
});

$("#id_password").blur(function(){
    var password = $("#id_password").val();
    var reg = /^[\w]{3,12}$/;
    var flag = reg.test(password);
    if(password != "" && flag == false){
        alert("密码格式错误，必须为4-12位的英文字母或数字");
        return;
    }
});




});

