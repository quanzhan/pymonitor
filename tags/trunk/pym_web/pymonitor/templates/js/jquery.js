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
 * *作者： @窄文颖
 * *---------------------------------------------------------------------------------*/ 

 

  $(document).ready(function(){
      var title=$("ul>li.L_meanu");
      var con=$("div.hpcleft3b");
      title.first().css("color","#095881").siblings().css("color","#333333");       
      con.first().show().nextAll().hide();
      title.each(function( index ){
      $(this).click(function(){
      $(this).css("color","#095881").siblings().css("color","#333333");
      $(this).css('height','34px').siblings().css('height','32px' );
      $(this).css({'backgroundImage':'url(../images/a1.jpg)'}).siblings().css({'backgroundImage':'url(../images/04.png)'} );
      con.eq(index).show().siblings().hide();    
      });
   });

   var a=window.location.href;
   a=a.split('/')[3];
   if(a!=''){
       if(a=='localstatus'){$('.hpcleft3b:eq(0)').show();$('.hpcleft3b:eq(1)').hide();$('(.hpcleft3b:eq(2)').hide();$('.L_meanu:eq(0)').css({'backgroundImage':'url(../images/a1.jpg)'});$('.L_meanu:eq(0)').css({"color":"#095881"});$('.L_meanu:eq(2)').css({'backgroundImage':'url(../images/04.png)'});$('.L_meanu:eq(2)').css({"color":"#333333"});$('.L_meanu:eq(1)').css({'backgroundImage':'url(../images/04.png)'});$('.L_meanu:eq(1)').css({"color":"#333333"});}
       if(a=='localoperate'){$('.hpcleft3b:eq(1)').show();$('.hpcleft3b:eq(0)').hide();$('(.hpcleft3b:eq(2)').hide();$('.L_meanu:eq(1)').css({'backgroundImage':'url(../images/a1.jpg)'});$('.L_meanu:eq(1)').css({"color":"#095881"});$('.L_meanu:eq(0)').css({'backgroundImage':'url(../images/04.png)'});$('.L_meanu:eq(0)').css({"color":"#333333"});$('.L_meanu:eq(2)').css({'backgroundImage':'url(../images/04.png)'});$('.L_meanu:eq(2)').css({"color":"#333333"});}
       if(a=='adminsystem'){$('(.hpcleft3b:eq(2)').show();$('.hpcleft3b:eq(0)').hide();$('(.hpcleft3b:eq(1)').hide();$('.L_meanu:eq(2)').css({'backgroundImage':'url(../images/a1.jpg)'});$('.L_meanu:eq(2)').css({"color":"#095881"});$('.L_meanu:eq(0)').css({'backgroundImage':'url(../images/04.png)'});$('.L_meanu:eq(0)').css({"color":"#333333"});$('.L_meanu:eq(1)').css({'backgroundImage':'url(../images/04.png)'});$('.L_meanu:eq(1)').css({"color":"#333333"});}
   }

    	 var ts=$("div.hpcleft3b2ab");
         var domainUrl=['/localoperate/logging/logstatus/','/localoperate/selfstatus/teststatus/']
    	 ts.each(function( i ){
         if (window.location.href.toLowerCase().indexOf(domainUrl[i]) > 0) {
    	 $(this).css({'backgroundImage':'url(../images/diaj1.jpg)'}).siblings().css({'backgroundImage':'url(../images/diaj2.jpg)'});   
     }               
  });
    	 var titles=$("div.hpcleft3b2aa");
         var domainUrl=['/localstatus/overview/overview/','/localstatus/cluster/cluster/','/localstatus/taskstatus/taskstatus/','/localstatus/nodestatus/nodestatus/']
    	 titles.each(function( i ){
         if (window.location.href.toLowerCase().indexOf(domainUrl[i]) > 0) {
    	 $(this).css({'backgroundImage':'url(../images/diaj1.jpg)'}).siblings().css({'backgroundImage':'url(../images/diaj2.jpg)'});   
     }               
  });

     var ti=$("div.hpcleft3b2ad");
         var domainUrl=['/localstatus/cluster/cluster/','/localstatus/taskstatus/taskstatus/','/localstatus/nodestatus/nodestatus/']
         ti.each(function( i ){
         if (window.location.href.toLowerCase().indexOf(domainUrl[i]) > 0) {
         $(this).css({'backgroundImage':'url(../images/diaj1.jpg)'}).siblings().css({'backgroundImage':'url(../images/diaj2.jpg)'});
     }
  });


     var titless=$("div.hpcleft3b2ab");
     var domainUrl=['/localoperate/projects/projectstatus/','/localoperate/taskadd/taskadd/']     
     titless.each(function( i ){
     if (window.location.href.toLowerCase().indexOf(domainUrl[i]) > 0) {
     $(this).css({'backgroundImage':'url(../images/diaj1.jpg)'}).siblings().css({'backgroundImage':'url(../images/diaj2.jpg)'});      
      } 
    });
               
     var tits=$("div.hpcleft3b2ac");
     var domainUrl=['/adminsystem/localadmin/modpassword/','/adminsystem/adminservices/services/','/adminsystem/adminusers/account/users/']
     tits.each(function( i ){
     if (window.location.href.toLowerCase().indexOf(domainUrl[i]) > 0) {
     $(this).css({'backgroundImage':'url(../images/diaj1.jpg)'}).siblings().css({'backgroundImage':'url(../images/diaj2.jpg)'});      
  }
   });
});
