/**------------------------------------------------------------------
 *
 * *2012-07-1 Info.Inc
 *
 * *------------------------------------------------------------------
 *
 * *HPC ENV - Info High Proformace Computing Environment
 *
 * *“迎福高性能计算环境”
 *
 * *HPC ENV是一个使用很多处理器（作为单个机器的一部分）或者某一集群中组织的几台计算机（作为单个计算资源操作）的计算系统和环境。
 *
 * *HPC ENV统一每个节点的操作系统配置，有效的监控和管理集群的日常操作。
 *
 * *HPC ENV具有集中的集群管理、快速响应、易于支持、易于设置及可扩展等优点。
 *
 * *HPC ENV的产生我们希望对您所遇到的问题是有帮助的，希望您用的满意。
 *
 * *如您还不明白，可以询问本公司相关人员。公司网址：www.infu.com.cn
 *
 * *版权归属: 北京迎福时代数码科技有限公司
 *
 * *开发： 迎福研发部
 *
 * *作者： @李佳龙
 * *---------------------------------------------------------------------------------*/



$(document).ready(function(){
	$('#alertdialog').append('<div style="margin:0px;padding:0px;position:fixed;top:0;left:0;width:100%;height:100%;filter:alpha(opacity=30);opacity:0.4;background-color:gray;"></div><div id="alertposition" style="position:fixed;top:100px;left:582px;"><img onclick="javascript:$(\'#alertdialog\').css(\'display\',\'none\');location.reload();"style="float:right;cursor:pointer;"src="images/guanb.gif"/><div style="padding:12px;"><div style="padding:14px;border:1px solid #70adc6;background-color:#f8fbfd;"><div id="ajaxalertdialog" style="border:1px solid #cedde9;padding:14px; background-color:#ffffff;"><img src="images/loading.gif"/></div></div></div></div>')
	$('#alertdialog').css('display','none');
});
function alertreload(urlspage,x,y,datas){
	$('#alertdialog').css('display','block');
	$('#alertposition').css('left',y);
	$('#alertposition').css('top',x);
	$('#ajaxalertdialog').html('');
	var dates= new Object();
	datas=datas.split('$$');
	var i=0;
	while (i<datas.length){
		var aa=datas[i].split('_');
		var aaa=aa[0];
		dates[aaa]=aa[1];
		i++
	}
	
	$.ajax({
		url:urlspage,
		type:'post',
		data:dates,
	    success:function(data,textStatus){
	    	$('#ajaxalertdialog').html(data);
	    },
	    error:function(){
	    	$('#ajaxalertdialog').html('<font color="red">对不起，信息加载失败。</font>');
	    },
	});
}
