## Jenkins Installation Steps

- Steps to install Jenkins
```
sudo yum -y install git java-1.8.0-openjdk
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum -y install jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

- You can check the Jenkins log like so:

```
sudo tail -f /var/log/jenkins/jenkins.log

```

- Once you install Jenkins, you will need the temporary admin password to complete setup in the browser. You can get the temporary admin password with this command:

```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```


- Check for services running on 8080 before starting the Jenkins service.
```
netstat -tulpn | grep 8080
```
