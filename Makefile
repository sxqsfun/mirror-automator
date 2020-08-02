test-all: test-java-maven-example

test-quick: test-java-maven-quick

test-java-maven-example:
	cd tests/java/maven/example; timeout 10 mvn compile


MAVEN_EXAMPLE_JAR := org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.jar
MAVEN_APACHE_ORG_JAR_URL := https://repo.maven.apache.org/maven2/$(MAVEN_EXAMPLE_JAR)
MAVEN_ALIYUN_COM_JAR_URL := https://maven.aliyun.com/repository/public/$(MAVEN_EXAMPLE_JAR)

test-java-maven-quick:
	timeout 3 wget $(MAVEN_ALIYUN_COM_JAR_URL)