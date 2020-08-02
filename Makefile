test-all: test-java-maven-example

test-java-maven-example:
	cd tests/java/maven/example; timeout 10 mvn compile