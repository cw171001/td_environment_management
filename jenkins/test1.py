# this will test python and jenkins
import teradata
fh = open("C:/Users/CW171001.TD/PycharmProjects/td_environment_management/jenkins/junk.txt","w")
print("hello",file=fh)
fh.close()
udaexec = teradata.UdaExec(appName="test1",version=1)
exit(0)