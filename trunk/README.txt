客户端每秒向服务端发送的数据 
    1. CPU 负载： /usr/bin/uptime  
    2. 根目录大小： /bin/df -h | grep '/$'
    3. 内存： free -m | grep Mem
    4. IO负载： iostat -d -x 这个命令不靠谱， 此外需要考虑多个硬盘的情况，注意整合

现在使用的是：while sleep 1; do cat /proc/diskstats | grep -v ram | grep -v loop; echo ===========================; done
参考的文档是：http://users.sosdg.org/~qiyong/lxr/diff/Documentation/iostats.txt?a=arm;diffval=um;diffvar=a

    5. 网络浏览： 考虑两套网络的可能（至少两套,分开发送）  /sbin/ifcongig eth0 | grep bytes

    每个节点将自己以上数据保存到本地的/opt目录（临时的，一旦关机，就没有了，需要定时的去清理缓存???）

    所有节点的数据，经过平均等操作后保存到管理节点的/opt目录

    说明：每个节点的数据保存到 /opt/hpcserver/logs/
        1. CPU负载保存到 /opt/hpcserver/logs/uptime.dat
            格式： 
172.16.0.1 2:31$$7$$0.02$$0.20$$0.43 current_date
        2. 根目录大小保存到 /opt/hpcserver/logs/hostdir.dat
            格式：
172.16.0.1 /dev/sda1$$29G$$16G$$2G$$58% current_date
        3. 内存大小保存到  /opt/hpcserver/logs/free.dat
172.16.0.1 3855$$2180$$1674$$0$$61$$1385
        4. IO负载保存到 /opt/hpcserver/logs/iostat.dat
172.16.0.1 4.34$$21.68$$6.29$$3.03$$426.67$$197.27$$66.92$$0.41$$44.03$$5.63$$5.25
        5. 网络负载
    
管理节点接收用户输入命令：
    
    
