�ͻ���ÿ�������˷��͵����� 
    1. CPU ���أ� /usr/bin/uptime  
    2. ��Ŀ¼��С�� /bin/df -h | grep '/$'
    3. �ڴ棺 free -m | grep Mem
    4. IO���أ� iostat -d -x ���������ף� ������Ҫ���Ƕ��Ӳ�̵������ע������

����ʹ�õ��ǣ�while sleep 1; do cat /proc/diskstats | grep -v ram | grep -v loop; echo ===========================; done
�ο����ĵ��ǣ�http://users.sosdg.org/~qiyong/lxr/diff/Documentation/iostats.txt?a=arm;diffval=um;diffvar=a

    5. ��������� ������������Ŀ��ܣ���������,�ֿ����ͣ�  /sbin/ifcongig eth0 | grep bytes

    ÿ���ڵ㽫�Լ��������ݱ��浽���ص�/optĿ¼����ʱ�ģ�һ���ػ�����û���ˣ���Ҫ��ʱ��ȥ������???��

    ���нڵ�����ݣ�����ƽ���Ȳ����󱣴浽����ڵ��/optĿ¼

    ˵����ÿ���ڵ�����ݱ��浽 /opt/hpcserver/logs/
        1. CPU���ر��浽 /opt/hpcserver/logs/uptime.dat
            ��ʽ�� 
172.16.0.1 2:31$$7$$0.02$$0.20$$0.43 current_date
        2. ��Ŀ¼��С���浽 /opt/hpcserver/logs/hostdir.dat
            ��ʽ��
172.16.0.1 /dev/sda1$$29G$$16G$$2G$$58% current_date
        3. �ڴ��С���浽  /opt/hpcserver/logs/free.dat
172.16.0.1 3855$$2180$$1674$$0$$61$$1385
        4. IO���ر��浽 /opt/hpcserver/logs/iostat.dat
172.16.0.1 4.34$$21.68$$6.29$$3.03$$426.67$$197.27$$66.92$$0.41$$44.03$$5.63$$5.25
        5. ���縺��
    
����ڵ�����û��������
    
    
