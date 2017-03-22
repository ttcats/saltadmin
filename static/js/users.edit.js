function createXmlHttp() {
	var xmlHttp = null;
	try {
		//Firefox, Opera 8.0+, Safari
		xmlHttp = new XMLHttpRequest();
	} catch (e) {
		//IE
		try {
			xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
		}
	}
	return xmlHttp;
}

// 获取单选框的值
function GetRadioValue(RadioName){
    var obj = document.getElementsByName(RadioName);
    if(obj!=null){
        var i;
        for(i=0;i<obj.length;i++){
            if(obj[i].checked){
                return obj[i].value;            
            }
        }
    }
    return null;
}

function submitForm(formId) {
	var xmlHttp = createXmlHttp();
	if(!xmlHttp) {
		alert("您的浏览器不支持AJAX！");
		return 0;
    }
        var F = document.getElementById(formId);
        var myuid = F.myuid;
        var oldpassword = F.oldpassword;
        var password = F.password;
        var password2 = F.password2;
        if (oldpassword)
        {
	        if(oldpassword.value=='')
               {
               alert('请输入原始密码！');
               oldpassword.focus();
               return false;
               }  
        }
        if(password.value=='')
           {
               alert('请输入新密码！');
               password.focus();
               return false;
           }
        if(password2.value=='')
           {
               alert('请再次输入新密码！');
               password2.focus();
               return false;
           }
        if(password.value!==password2.value)
           {
               alert('新密码输入不一致！');
               password.focus();
               return false;
           }

	var e = document.getElementById(formId);
	var url = e.action;
	var inputs = e.elements;
	if (oldpassword)
	    var postData = "myuid="+myuid.value+"&oldpassword="+oldpassword.value+"&password="+password.value;
	else
	    var postData = "myuid="+myuid.value+"&password="+password.value;
	xmlHttp.open("POST", url, true);
	xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlHttp.send(postData);
	xmlHttp.onreadystatechange = function() {
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			var PostAnswer=xmlHttp.responseText;
                        if(PostAnswer=="my.true") {
                            alert("修改成功！");
                            location.reload();
                            }
                        else if(PostAnswer=="true") {
                            alert("修改成功！");
                            window.location.href="/users";
                            }
                        else if (PostAnswer=="oldpass.false") {
                            alert("原始密码错误！");
                            $("a[name='reset']").click();
                            oldpassword.focus();
                            }
                        else if (PostAnswer=="error") {
                            alert("数据库可能挂了！");
                            }
                        else {
                            alert("不知道哪出错了噢！");
                            }
		    }
	    }
}

// 重设表单
function resetForm(formID,focusID) {
	document.getElementById(formID).reset();
	//document.formID.reset();
	document.getElementById(focusID).focus();
}

// 切换“用户信息”和“密码修改”模式
function changeMode(ShowID,HideID) {
	  document.getElementById(HideID).style.display = "none"; 
    document.getElementById(ShowID).style.display = "block";
}

function submituserForm(formId) {
	var xmlHttp = createXmlHttp();
	if(!xmlHttp) {
		alert("您的浏览器不支持AJAX！");
		return 0;
    }
        var F = document.getElementById(formId);
        var myuid = F.myuid;
        var nickname = F.nickname;
        var mobile = F.mobile;
        var email = F.email;
        var comment = F.comment;
        var level = F.level;
        var status = F.status;

        if(nickname.value=='')
           {
               alert('请输入姓名！');
               nickname.focus();
               return false;
           }

	var e = document.getElementById(formId);
	var url = e.action;
	var inputs = e.elements;
	var postData = "myuid="+myuid.value+"&nickname="+nickname.value+"&mobile="+mobile.value+"&email="+email.value+"&comment="+comment.value+"&level="+level.value+"&status="+status.value;
	xmlHttp.open("POST", url, true);
	xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlHttp.send(postData);
	xmlHttp.onreadystatechange = function() {
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			var PostAnswer=xmlHttp.responseText;
                        if(PostAnswer=="true") {
                            alert("修改成功！");
                            window.location.href="/users";
                            }
                        else if (PostAnswer=="error") {
                            alert("数据库可能挂了！");
                            }
                        else {
                            alert("不知道哪出错了噢！");
                            }
		    }
	    }
}


