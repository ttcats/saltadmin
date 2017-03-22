
// 是否删除
function isDel()
{
    return confirm('确定删除该条配置？');
}


function createXmlHttp() {
	var xmlHttp = null;
	try {
		xmlHttp = new XMLHttpRequest();
	} catch (e) {
		try {
			xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
		}
	}
	return xmlHttp;
}

function submitF(formId) {
	var xmlHttp = createXmlHttp();
	if(!xmlHttp) {
		alert("您的浏览器不支持AJAX！");
		return 0;
	}
        var F = document.getElementById(formId);
        var num = document.getElementById("num")
        var num = num.options[num.selectedIndex].value
        var content = F.content.value
        var seed = F.seed.value

	var postData = "num="+num+"&content="+content+"&seed="+seed;
	xmlHttp.open("POST", "/encryption", true);
	xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlHttp.send(postData);
	xmlHttp.onreadystatechange = function() {
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			var PostAnswer=xmlHttp.responseText;
			document.getElementById("encryption").innerHTML=PostAnswer;
		    }
	        }
}

