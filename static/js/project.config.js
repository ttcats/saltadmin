var i = 2;
function addRow(tableID,sm)
{
    //var newRow = document.all(tableID).insertRow();
    a = "<tr><td class='textLeft'>主机IP</td>";
    b = "<td class='inputRight' >";
    //b += "id='bw_" + i + "' >";
    b += "<input type='text' name='bw' class='maininput' ";
    b += "id='bw_" + i +"'" + "/><a href='javascript:void(0)' onclick='removeRow(this)'>删除</a></td>"
    c = "<td class='textLeft'>端口</td>"
    d = "<td class='inputRight'><input type='text' class='maininput'  name='bwconf' /> <a href='javascript:void(0)' onclick='removeRow(this)'>删除</a></td></tr>"
    t = a + b  ;
    $('#'+tableID).append(t);
    document.getElementById("bw_" + i).focus();
    i += 1;
    }

function removeRow(src)
   {
    var oRow = src.parentElement.parentElement;  //获取当前事件的父节点
    document.all("WebConfig").deleteRow(oRow.rowIndex);  //删除当前列
   }

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

function ubmitForm(formId,Appid) {
	var xmlHttp = createXmlHttp();
	if(!xmlHttp) {
		alert("您的浏览器不支持AJAX！");
		return 0;
	};
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
	//var name = document.getElementsByName("developer")
	//var comment = document.getElementsByName("comment")
        //var cdate = F.cdate
        //var developer = F.developer
        
        //if(comment.value=='')
        //   {
        //       alert('请输入项目标识！');
        //       comment.focus();
        //       return false;
        //   }
        if(lang.value=='0')
           {
               alert('请选择开发框架！');
               document.getElementById("lang").focus();
               return false;
           }
        //if(developer.value=='')
        //   {
        //       alert('请输入开发者！');
        //       developer.focus();
        //       return false;
        //   }
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
			alert('请添加IP !');
               		return false;
		};
	};

	//var e = document.getElementById(formId);
	//var url = e.action;
	//var inputs = e.elements;
	var postData = "&type="+type.value+"&lang="+lang.value+"&status="+status.value+"&comment="+comment.value+"&developer="+developer.value+"&pro="+pro.value+"&bw="+bw_list+"&id="+Appid;
	xmlHttp.open("POST", "/project/config", true);
	xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlHttp.send(postData);
	xmlHttp.onreadystatechange = function() {
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			//tip.innerHTML = xmlHttp.responseText;
			var PostAnswer=xmlHttp.responseText;
			if(PostAnswer=="Update_True"){
				alert("修改成功！");
				window.location.href="/project";
			}
		    }
	        }
}

