FROM tomcat:9-jre8
MAINTAINER GeoNode Development Team

#
# Set GeoServer version and data directory
#
ENV GEOSERVER_VERSION=2.10.x
ENV GEOSERVER_DATA_DIR="/geoserver_data/data"

RUN mkdir -p $GEOSERVER_DATA_DIR
# ADD compiled_geoserver_data /geoserver_data/data

ADD resources /tmp/resources

#
# Download and install GeoServer
#
RUN if [ ! -f /tmp/resources/geoserver.war ]; then \
    wget --progress=bar:force:noscroll http://build.geonode.org/geoserver/latest/geoserver-${GEOSERVER_VERSION}.war \
      -O /tmp/resources/geoserver.war; \
    fi; \

    unzip /tmp/resources/geoserver.war -d $CATALINA_HOME/webapps/geoserver \
    && rm -rf $CATALINA_HOME/webapps/geoserver/data \
    && rm -rf /tmp/geoserver

# Custom settings for envronment variables
ENV GEOSERVER_OPTS "-Xms2G -Xmx4G -XX:+UseG1GC"

#-XX:+UseConcMarkSweepGC use this rather than parallel GC?
ENV JAVA_OPTS "$JAVA_OPTS $GEOSERVER_OPTS "


# copy the script and perform the run of scripts from entrypoint.sh
RUN mkdir -p /usr/local/tomcat/tmp
WORKDIR /usr/local/tomcat/tmp

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y python python-pip python-dev \
    && pip install --upgrade pip

COPY entrypoint.sh /usr/local/tomcat/tmp

RUN chmod +x /usr/local/tomcat/tmp/entrypoint.sh

# Install any plugin zip files in resources/plugins
RUN if ls /tmp/resources/plugins/*.zip > /dev/null 2>&1; then \
      for p in /tmp/resources/plugins/*.zip; do \
        unzip $p -d /tmp/gs_plugin \
        && mv /tmp/gs_plugin/*.jar $CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ \
        && rm -rf /tmp/gs_plugin; \
      done; \
    fi

COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml


CMD ["/usr/local/tomcat/tmp/entrypoint.sh"]
