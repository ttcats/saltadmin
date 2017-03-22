// 是否禁用
function isDisable()
{
    return confirm('确定禁用该条配置？');
}

// 是否启用
function isEnable()
{
    return confirm('确定启用该条配置？');
}

// 是否删除
function isDel()
{
    return confirm('确定删除该条配置？');
    //var a=confirm('确定删除该条配置？');
    //if (a == true)
    //{document.write("恭喜你答对了！")}
}

// 新增
function AddOps() {
	//document.getElementById("AddTr").style.display = "none"; 
    document.getElementById("AddTr").style.display = "table-row";
}

// 取消新增
function CancellNullOps() {
	document.getElementById("AddTr").style.display = "none"; 
    //document.getElementById("AddTr").style.display = "inline";
}

// 重置表单
function ResetForm(FormID) {
	document.getElementById(FormID).reset();
	document.getElementById('AddType').focus();
	
}

// 提交新增
function SubmitOps() {
	//document.getElementById("AddForm").submit();
	document.AddForm.submit();
}

// 编辑模式与取消编辑模式
function EditOps(ShowID,HideID) {
	document.getElementById(HideID).style.display = "none"; 
    document.getElementById(ShowID).style.display = "table-row";
}

// 保存编辑后的结果
function SaveOps(FormID) {
    document.getElementById(FormID).submit();
}

// 删除表单
function DelOps(FormID) {
    var a=confirm('确定删除该条配置？');
    if (a == true)
    {removeObj.parentNode.removeChild(FormID);}
}


function Delops(FormID) {
    var a=confirm('确定删除该条配置？');
    if (a == true)
    {var xmlhttp;
    xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET",FormID,true);
    xmlhttp.send();
    window.location.reload();
    }
}

// hosts页面按照条件刷选显示
function onSearch(selectID,row){//js函数开始
	setTimeout(function(){//因为是即时查询，需要用setTimeout进行延迟，让select选定时，再读取
		var storeId = document.getElementById('datalist');//获取table的id标识
		var rowsLength = storeId.rows.length - 1;//表格总共有多少行，这里减1表示去除最后一行footer标题
		//var key = obj.value;//获取输入框的值
        var select = document.getElementById(selectID)
        var key = select.options[select.selectedIndex].value;     //获取select的值
		var searchCol = row;//要搜索的哪一列，这里用变量row

		for(var i=1;i<rowsLength;i++){//按表的行数进行循环，第一行是标题不计算在内，所以i=1，从第二行开始筛选（从0数起）
			var searchText = storeId.rows[i].cells[searchCol].innerHTML;//取得table行，列的值

			if(searchText.match(key)){//用match函数进行筛选，如果input的值，即变量 key的值为空，返回的是true，
				storeId.rows[i].style.display='';//显示行操作，
			}else{
				storeId.rows[i].style.display='none';//隐藏行操作
			}
		}
	},100);//100为延时时间，这里是100毫秒
}

// hosts页面按照条件刷选显示
function onSearchs(selectID,row){//js函数开始
	var xmlHttp = createXmlHttp();
	setTimeout(function(){//因为是即时查询，需要用setTimeout进行延迟，让select选定时，再读取
		var storeId = document.getElementById('datalist');//获取table的id标识
		var rowsLength = storeId.rows.length - 1;//表格总共有多少行，这里减1表示去除最后一行footer标题
		//var key = obj.value;//获取输入框的值
        var select = document.getElementById(selectID)
        var key = select.options[select.selectedIndex].value;     //获取select的值
	var postData = "&key="+key;
	xmlHttp.open("GET", "/options", true);
	xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); 
	xmlHttp.send(postData);
	xmlHttp.onreadystatechange = function() {
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			//tip.innerHTML = xmlHttp.responseText;
			var PostAnswer=xmlHttp.responseText;
                        if(PostAnswer=="Add.True")   //跳转到主机管理界面
                            {
                            alert("添加成功！");
                            window.location.href="/hosts";
                            };
			};
		};
		var searchCol = row;//要搜索的哪一列，这里用变量row

		for(var i=1;i<rowsLength;i++){//按表的行数进行循环，第一行是标题不计算在内，所以i=1，从第二行开始筛选（从0数起）
			var searchText = storeId.rows[i].cells[searchCol].innerHTML;//取得table行，列的值

			if(searchText.match(key)){//用match函数进行筛选，如果input的值，即变量 key的值为空，返回的是true，
				storeId.rows[i].style.display='';//显示行操作，
			}else{
				storeId.rows[i].style.display='none';//隐藏行操作
			}
		}
	},100);//100为延时时间，这里是100毫秒
}


function onSearches(selectID,row){
	$.ajax({
	type:"get",
	url:"/options",
        async:true,
        data:{selid:$("#show4type").val()},
        sucess:function(msg){
	alert("true");},
});
}
