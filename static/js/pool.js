

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

function modeviews(ip,nodeview)
{
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
	var postData = "&ip="+ip+"&nodeview="+nodeview;
	xmlhttp.open("POST", "/nginx/pool_node", true);
	xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlhttp.send(postData);
	xmlhttp.onreadystatechange = function() {
		if(xmlhttp.readyState==4 && xmlhttp.status==200) {
			var PostAnswer=xmlhttp.responseText;
                        document.getElementById("pool_model").innerHTML=PostAnswer;
		    };
	};
}


function update_index(ip,nodeview)
{
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
	var postData = "&ip="+ip+"&nodeview="+nodeview;
	xmlhttp.open("POST", "/nginx/pool", true);
	xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlhttp.send(postData);
	xmlhttp.onreadystatechange = function() {
		if(xmlhttp.readyState==4 && xmlhttp.status==200) {
			var PostAnswer=xmlhttp.responseText;
                        document.getElementById(nodeview).innerHTML=PostAnswer;
		    };
	};
}


function action_pool(ip,nodeview,pool_ip,pool_port,pool_status) 
{
var xmlhttp;
var Img_status_id = "#Img_status" + nodeview + pool_ip.replace(/\./g,"_") + pool_port;
var pool_status_id = "#pool_status" + nodeview + pool_ip.replace(/\./g,"_") + pool_port;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
	var postData = "&ip="+ip+"&nodeview="+nodeview+"&pool_ip="+pool_ip+"&pool_port="+pool_port+"&pool_status="+pool_status;
	xmlhttp.open("POST", "/nginx/action", true);
	xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlhttp.send(postData);
	xmlhttp.onreadystatechange = function() {
		if(xmlhttp.readyState==4 && xmlhttp.status==200) {
			var PostAnswer=xmlhttp.responseText;
			//function update_index(){
				//$.post("/nginx/pool",{ip:ip,nodeview:nodeview},function(data){
				//document.getElementById(nodeview).innerHTML=data;
				//var s = data;
				//$(sta_id).html("123");
				//alert(data)
				//});
			//};
			//update_index(ip,nodeview);
			if(PostAnswer=="down_true"){
			$(pool_status_id).attr('src',"/static/images/status2.gif");
			$(Img_status_id).attr('src',"/static/images/switch1.png");
			alert(PostAnswer);
			}else if(PostAnswer=="up_true"){
			$(pool_status_id).attr('src',"/static/images/status1.gif");
			$(Img_status_id).attr('src',"/static/images/switch2.png");
			alert(PostAnswer);
			}else if(PostAnswer=="one_pool"){
			alert("NO Action Nodes!")};
			window.location.reload();
			//top.location.reload();
		    };
	};
}


function modeviws(ip,nodeview){
	//$.ajax({url:"/nginx/pool_node",async:true,data:{ip:ip,nodeview:nodeview},type:"post"});
        //$("#pool_model").html(htmlobj);

        
	console.log('success');
	$.post("/nginx/pool_node",
	{
		ip:ip,
		nodeview:nodeview
	},
	function(test){
		console.log("callback");
		var s = test;
		document.getElementById("pool_model").innerHTML=test;
		//$("#pool_model").html(msg);
	},
	"text/html");

}
