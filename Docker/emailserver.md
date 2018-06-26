[Thomas VIAL Docker Image](https://github.com/tomav)

A pre-configured Docker image gives you a head start. Docker Hub has a couple of e-mail-related images available. Some are bare bones and others are full-blown ones with the support for database and webmail. If a minimal cloud server instance is used and you have just 1-2 domains, it is your best bet to use the one that needs minimal configuration, has time-tested tools available, is based on a filesystem and has all the necessary security and anti-spam features.

[Thomas Vial](https://tvi.al/page/2/)’s  [docker-mailserver](https://github.com/tomav/docker-mailserver)  seemed like the best option:

-   it has the standard tools available for the sending and inbox: postfix, dovecot, courier-imap
-   there are security features both for incoming and outgoing e-mail: clamav, opendkim, opendmarc, spamassassin, SSL via LetsEncrypt
-   uses filesystem to save e-mails. It will be easy to backup the data.  
    

Here is how to have fully functional e-mail system ready in less than 20 steps:

1.  It is assumed that an Ubuntu-based Linux distribution is used. See [prerequisites and packages for Ubuntu 16 Xenial](https://docs.docker.com/engine/installation/linux/ubuntulinux/). All the commands are meant to be executed as root, but that should not be the usual habit. An alternative non-root user should be added into the system and  _sudo_ used only when needed.  
    
2.  Add some swap space (see the [recommendations of amount](https://www.cyberciti.biz/tips/linux-swap-space.html) and change the value of "count" if needed)  
      
    dd if=/dev/zero of=/swapfile bs=1M count=2048  
    dd if=/dev/zero of=/swapfile bs=1M count=2048  
    mkswap /swapfile  
    chmod 600 /swapfile  
    mkswap /swapfile  
    swapon /swapfile  
    echo 'echo "/swapfile none swap defaults 0 0" >> /etc/fstab' | sh  
    free -m  
    
3.  Install and start Docker  
      
    `apt-get update  
    apt-get install docker-engine` git  
    `service docker start`  
    
4.  Set up  [Docker Compose](https://docs.docker.com/compose/overview/)  
      
    apt-get install python-pip  
    pip install --upgrade pip  
    pip install docker-compose  
    
5.  Install the [Docker image](https://github.com/tomav/docker-mailserver/wiki)  
      
    docker pull tvial/docker-mailserver:latest  
    
6.  DNS part 1: Determine the (sub)domain you are planning to use to receive and send your e-mails and add the needed A and MX name server records to your DNS provider.  
      
    Open the control panel of your DNS provider and generate a subdomain, something like mail.yourdomain.com, with its A record pointing to your server's IP address. You will also need to make sure that the root domain yourdomain.com also points to the IP address of your new server, this is needed for LetsEncrypt. It will be used later on in the Docker configuration and in e-mail client software. Then open the records for your main domain, yourdomain.com and add a new record of type MX. Set its priority to 10 and then set the value to match the previously added subdomain mail.yourdomain.com.  
    
7.  Install ufw, open ports  
      
    apt-get install ufw  
    ufw status verbose  
    ufw allow 80/tcp  
    ufw allow 443/tcp  
    ufw allow 22/tcp  
    ufw allow 25/tcp  
    ufw allow 143/tcp  
    ufw allow 587/tcp  
    ufw allow 993/tcp  
    ufw allow 4190/tcp  
    ufw enable  
    
8.  Add the support for  [LetsEncrypt](https://letsencrypt.org/)  
      
    cd /root  
    mkdir ~/src  
    cd src  
    git clone https://github.com/letsencrypt/letsencrypt  
    cd letsencrypt  
    chmod g+x letsencrypt-auto  
    cd ../..  
    mv src/letsencrypt .  
    cd letsencrypt  
    `./letsencrypt-auto`  
    ./letsencrypt-auto certonly --standalone --email info@yourdomain.com --agree-tos -d subdomain-for-sending-receiving.yourdomain.com  
    IMPORTANT NOTES:  
    - Congratulations! Your certificate and chain have been saved at  
    /etc/letsencrypt/live/subdomain-for-sending-receiving.yourdomain.com/fullchain.pem.  
    crontab -e  
    0 5 * * 1 /root/letsencrypt/letsencrypt-auto renew  
    
9.  Set up the Docker image and an email account  
      
    cd /root  
    mkdir -p {config,spamassassin}  
    docker run --rm \  
    -e MAIL_USER=yourname@yourdomain.com \  
    -e MAIL_PASS=password324wf \  
    -ti tvial/docker-mailserver:latest \  
    /bin/sh -c 'echo "$MAIL_USER|$(doveadm pw -s SHA512-CRYPT -u $MAIL_USER -p $MAIL_PASS)"' >> config/postfix-accounts.cf  
    
10.  DNS part 2  
      
    Open the control panel of your DNS provider
    1.  **DKIM**: It is important to generate DKIM in order to ensure that your emails are going to Inbox folder on GMail or Outlook online. This is one of the measures that validates the sender. Here is how to generate the DKIM key for the domain yourdomain.com: docker run --rm -v "$(pwd)/config":/tmp/docker-mailserver -ti tvial/docker-mailserver:latest generate-dkim-config .Now the keys have been generated. Add a new TXT record to your yourdomain.com zone, named mail._domainkey.yourdomain.com. View the generated content: cat config/opendkim/keys/yourdomain.com/mail.txt The value for the TXT record should look like this: v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQE...IDAQAB  
        
    2.  **DMARC**: Add the following TXT record to your DNS zone: _dmarc.yourdomain.com with the following content: v=DMARC1; p=none  
        
    3.  **SPF**: Visit a generator like [http://spfwizard.com](http://spfwizard.com/) and fill in the information. Add a new TXT record to your DNS zone under  yourdomain.com. Its value will need to be something like this: v=spf1 a -all **or** v=spf1 mx -all (if MX handles email for the domain) or something like this, if you are planning to use MailGun to send some of your emails: v=spf1 mx a mx:mailgun.org include:mailgun.org -all  
        
    4.  **Reverse DNS and PTR records**  
        When for example DigitalOcean is used as the cloud server provider, just rename your droplet to yourdomain.com and the required records will be automatically set. Please contact your cloud service provider for details on how to generate these records. See [more information](http://www.itworld.com/article/2833006/networking/how-to-setup-reverse-dns-and-ptr-records.html).  
        
11.  Add the configuration file for the Docker image  
      
    nano /root/docker-compose.yml
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    
    version: '2'
    services:
      mail:
        image: tvial/docker-mailserver:latest
        hostname: mail
        domainname: yourdomain.com
        container_name: mail
        ports:
        - "25:25"
        - "143:143"
        - "587:587"
        - "993:993"
        volumes:
        - /var/mail/:/var/mail
        - ./spamassassin:/tmp/spamassassin/
        - ./postfix:/tmp/postfix/
        - /etc/letsencrypt:/etc/letsencrypt
        - ./config/:/tmp/docker-mailserver/
        environment:
        - ENABLE_MANAGESIEVE=1
        - ENABLE_FAIL2BAN=1
        - SA_TAG=2.0
        - SA_TAG2=6.31
        - SA_KILL=3
        - SSL_TYPE=letsencrypt
        cap_add:
        - NET_ADMIN
    
      
    
12.  Compose the container  
      
    docker-compose up -d mail  
    
13.  Set up  [greylisting](http://www.greylisting.org/)  
      
    Greylisting is a method of protecting e-mail users against spam. Mail transfer agent will temporarily reject any e-mail from a sender it does not recognize. Spammers are usually in a hurry to send out their e-mails, so their sending software has not been set up to retry.  
      
    docker exec -it mail apt-get update  
    docker exec -it mail apt-get install postgrey  
    docker exec -it mail /etc/init.d/postgrey start  
    docker exec -it mail vi /etc/postfix/main.cf  
      
    Add  check_policy_service inet:127.0.0.1:10023  after  reject_unauth_destination  
      
    smtpd_recipient_restrictions =  
    permit_mynetworks  
    permit_sasl_authenticated  
    reject_unauth_destination  
    check_policy_service inet:127.0.0.1:10023  
      
    docker exec -it mail vi /etc/default/postgrey  
      
    Add the opts:  
    POSTGREY_OPTS="--inet=10023"  
      
    docker exec -it mail service postgrey restart  
    docker exec -it mail service postfix reload  
      
    Ensure that greylisting works:  
      
    docker exec -it mail tail -f /var/log/syslog
    1.  Greylisting  
        Dec 11 11:09:45 mail postgrey[2527]: action=greylist, reason=new, client_name=unknown, client_address=178.62.70.39, sender=sven@infohaiku.com, recipient=youruser@yourdomain.com  
        Dec 11 11:09:45 mail postfix/smtpd[2573]: NOQUEUE: reject: RCPT from unknown[178.62.70.39]: 450 4.2.0 : Recipient address rejected: Greylisted, see http://postgrey.schweikert.ch/help/yourdomain.ee.html; from= to= proto=ESMTP helo=
    2.  Finally allowing  
        Sep 11 11:18:02 mail postgrey[2527]: action=pass, reason=triplet found, delay=497, client_name=unknown, client_address=178.62.70.39, sender=sven@infohaiku.com, recipient=youruser@yourdomain.com
    3.  Allowing right away because of whitelisting:  
        Sep 11 11:13:43 mail postgrey[2527]: action=pass, reason=client whitelist, client_name=mail-lf0-f42.google.com, client_address=209.85.215.42, sender=sven.kauber@gmail.com, recipient=youruser@yourdomain.com  
          
        You might need to start the greylisting daemon each time you restart your server:  
        docker exec -it mail postgrey --inet=127.0.0.1:10023 This can be daemonized and added to the start sequence. See step 13 for some tips on how to do that.  
        
14.  Configure the client software  
      
    INCOMING  
    Account type: IMAP  
    Incoming Mail Server: mail.yourdomain.com  
    User Name: yourname@yourdomain.com  
    Password: password32444  
      
    OUTGOING  
    Outgoing Mail Server: mail.yourdomain.com  
    Authentication: the same as before  
    
15.  Set up  [auto-restart for the Docker image](https://docs.docker.com/engine/admin/host_integration/)  
      
    nano /etc/systemd/system/docker-mail.service
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    
    [Unit]
    Description=E-Mail Server
    Requires=docker.service
    After=docker.service
    
    [Service]
    Restart=always
    ExecStart=/usr/bin/docker start -a mail
    ExecStop=/usr/bin/docker stop -t 2 mail
    
    [Install]
    WantedBy=default.target
    
      
    systemctl daemon-reload  
    systemctl stop docker-mail.service  
    systemctl start docker-mail.service  
    systemctl enable docker-mail.service  
    
16.  Set up learning and backups for SpamAssassin  
      
    Run the following command whenever you have non-spam messages in your inbox:  
      
    docker exec -it mail sa-learn --no-sync --ham /var/mail/yourdomain.com/yourname/{cur,new}  
      
    Set up crons:  
      
    crontab -e  
    5 * * * * docker exec -it mail sa-learn --no-sync --spam /var/mail/yourdomain.com/yourname/.INBOX.Junk  
    0 0 */2 * * docker exec -it mail sa-learn --sync && docker exec -it mail sa-learn --backup > /root/spamassassin/spamassassin-backup.txt  
    
17.  Testing this all  
      
    Use  [https://www.mail-tester.com](https://www.mail-tester.com/)  to ensure that you have everything set up correctly. Send an email from your email client software to the temporary email address set up by Mail Tester.  
      
    **Your result should be:  
      
    ![](http://www.svenkauber.com/files/blog/51/score.jpg)**

  
**Some Docker one-liners**  
  
docker ps  
docker stats  
docker exec -it the_container_id_from_docker_ps somecommand  
docker exec -it mail somecommand  
docker exec -it mail tail -f /var/log/mail/mail.log  
docker exec -it mail bash #"log in"  
docker images  
  
  
**IMPORTANT! Saving the state of a Docker image. This is needed when for example something has been changed inside the running Docker container.**  
  
docker ps -a  
docker commit -m "Set up youruser@yourdomain.com, some other change" -a "FirstName LastName" a0d1e7d37917 root/docker-mailserver:v2

Modifying the configuration:  
  
nano /root/docker-compose.yml  
image: root/docker-mailserver:v2  
  
docker-compose rm mail #removing the older version of the image  
docker stop a0d1e7d37917 #stopping the container  
docker rm a0d1e7d37917 #removing the container  
docker images #to check the available images, ensuring that the previous one was removed  
docker-compose up -d mail #regenerating the image
