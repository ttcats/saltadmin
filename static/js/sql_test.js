
function showCustomer(str)
{
var xmlhttp;
if (str=="")
  {
  document.getElementById("txtHi").innerHTML="";
  return;
  }
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("txtHi").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","/db/choose?dbs="+str,true);
xmlhttp.send();
}


function sql_1(tag,name){
	$.get("/db/sqltest",{sql:tag,dbs:name},function(test){
		if(test != ''){
			document.getElementById(name).innerHTML=test;
			//alert(test);
			var nameid = "div" + name ;
			var inputid = "input" + name;
			var ds = document.getElementById(nameid);
			if(ds.style.display == "none"){
				document.getElementById(inputid).value = "-";
				ds.style.display = "block";
			}else{
				document.getElementById(inputid).value = "+";
				ds.style.display = "none";
			};
		}else{
			alert("d");
		};
	},
	"text"
	);
};


function ergodic(){
	var sql_text = $("#tet").val();
	$("div.dbs span.schema.current").each(function(){
		// table = $(this).text();
		table_name = $(this).attr("name")
		// alert(table)
	});
	var table_name;
	// var g
	if(sql_text == ""){
		alert("please input sql")
	}else if(table_name == undefined){
		alert("choice the db")
	}else{
		$.get("/db/sql_onput",{table:table_name,sql:sql_text},function(test){
			document.getElementById("onse_onput").innerHTML=test;	
		},
		"text"
		);
		// alert(table + sql_text)
	}
	// var s = sql_text + table
	// alert(s)
	// alert(table)

	// alert($("#tet").val());
	// $("#onse span.schema.current").each(function(){
	// 	alert($(this).text())

	// });
}
