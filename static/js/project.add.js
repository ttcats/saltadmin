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

function submitForm(formId) {
	var xmlHttp = createXmlHttp();
	if(!xmlHttp) {
		alert("您的浏览器不支持AJAX！");
		return 0;
	}
	// 定义端口匹配规则
	var portExp = /^[1-9]*[1-9][0-9]*$/
	var bw_list = []
        var F = document.getElementById(formId)
        var lang = document.getElementById("lang")
        var lang = lang.options[lang.selectedIndex]
        var type = document.getElementById("type")
        var type = type.options[type.selectedIndex]
        var status = document.getElementById("status")
        var status = status.options[status.selectedIndex]
        var pro = document.getElementById("pro")
        var pro = pro.options[pro.selectedIndex]
        var bw = document.getElementsByName("bw")
        //var isPublic = document.getElementById("isPublic")
        //var isPublic = isPublic.options[isPublic.selectedIndex]
        var name = F.name
        //var cname = F.cname
        //var domain = F.domain
        //var port = F.port
        var cdate = F.cdate
        //var man = F.man
        var developer = F.developer
        //var directory = F.directory
        //var relation = F.relation
        var comment = F.comment
        
        if(name.value=='')
           {
               alert('请输入项目名称！');
               name.focus();
               return false;
           }
        if(comment.value=='')
           {
               alert('请输入项目标识！');
               comment.focus();
               return false;
           }
        if(lang.value=='0')
           {
               alert('请选择开发框架！');
               document.getElementById("lang").focus();
               return false;
           }
        if(developer.value=='')
           {
               alert('请输入开发者！');
               developer.focus();
               return false;
           }
        if(type.value=='0')
           {
               alert('请选择应用类型！');
               type.focus();
               return false;
           }
        if(status.value=='0')
           {
               alert('请选择应用状态！');
               status.focus();
               return false;
           }
        if(pro.value=='0')
           {
               alert('请选择所属项目！');
               pro.focus();
               return false;
           }
	for(var i=0; i<bw.length;i++){
		var s="bw_"+i;
		if(bw[i].value!=''){
			bw_list.push(bw[i].value);
			//alert(bw[i].id);
               		//return false;
		}else{
			alert("请输入应用所在ip和端口");
               		return false;
		};
	};

	var e = document.getElementById(formId);
	var url = e.action;
	var inputs = e.elements;
	var postData = "name="+name.value+"&type="+type.value+"&lang="+lang.value+"&status="+status.value+"&cdate="+cdate.value+"&comment="+comment.value+"&developer="+developer.value+"&pro="+pro.value+"&bw="+bw_list;
	xmlHttp.open("POST", url, true);
	xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlHttp.send(postData);
	xmlHttp.onreadystatechange = function() {
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			//tip.innerHTML = xmlHttp.responseText;
			var PostAnswer=xmlHttp.responseText;
			            var rt = eval(PostAnswer);
                        if(rt[0]=="true")   //跳转到该项目配置界面
                            {
                            alert("添加成功！");
                            //var purl = "/project/config?pid=" + rt[2]; 
                            var purl = "/project"; 
                            window.location.href=purl;
                            //window.location.href="/project";
                            }
                        else if(rt[0]=="repeat") {
	                        alert("啊噢，域名和端口重复！\n项目：" + rt[1] + "\n域名：" + rt[2]);
	                        document.getElementById("domain").focus();
                        }
                        else {
                            alert("...::>_<::...\n错误：可能数据库挂了");
                            //document.userForm.reset();
                            document.getElementById("name").focus();
                            }
		    }
	        }
}

function resetForm() {
	document.getElementById("projectForm").reset();
	document.getElementById("name").focus();
}

function Add_IP(formId) {
	var xmlHttp = createXmlHttp();
	if(!xmlHttp) {
		alert("您的浏览器不支持AJAX！");
		return 0;
	}
	// 定义端口匹配规则
	var portExp = /^[1-9]*[1-9][0-9]*$/
        var F = document.getElementById(formId)
        var name = F.bw
	alert(name);

}
