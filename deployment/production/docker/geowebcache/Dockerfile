FROM tomcat:9-jre8

MAINTAINER Dimas Ciputra (dimas@kartoza.com)

COPY ./software/ /usr/local/tomcat/webapps/

COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
