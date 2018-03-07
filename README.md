`Amazon AWS` 

> [MD File Editor](https://stackedit.io)

> [AWS FAQ & Interview Preparation](https://docs.google.com/spreadsheets/d/1IXxlZ674sxfCdDvV8iAj2DBQV_ow1QIEpvYn8yJC4J4/edit?ts=5a9f3458#gid=800669335)

> [GitHub Link for AWS notes](https://github.com/agasthik/aws-csa-2017#aws-csa-2017-study-guide)


## AWS Certification Notes

## Course Video Durations

### Can help you plan your study based on your time availability.


|Module|# Lectures|Duration|
|------------- |:-------------:| -----:|
|[Identity Access Management (IAM)](https://github.com/Girish400/AWS/blob/master/README.md#iam---identity-and-access-management) | 
|Additional Exam Tips |9 | 53:39|


# AWS 10000 Feet Overview


=================================================================================
|Module|
|------------- |
| 
|[IAM](## IAM - Identity and Access Management)|
|VPC|
|SNS|
|SQS|
|Kinesis|
|CloudWatch|
|CloudTrail|
|API - Gateway|
|Lambda|
|CloudFromtaion|
|EC2|
|S3|
|Glacier|
|EFS|
|RDS|
|Route53|
|AWS Config|
|DynoamoDB|
|CloudFront|





## IAM - Identity and Access Management
=================================================================================
`IAM : Identity and Access Management
-	IAM is used to control who is authenticated (signed in) and authorized (has permissions) to use AWS resources.
-	IAM allows you to manage users and thier level of access to the AWS console using groups and policies

- Critical Terms
	 -  IAM consists of the following
	 -  Users    :  End users / people.
	 -  Groups   :  Collection of users. Users having one set of permissions.
	 -  Roles    :  An AWS identity with permission policies that determine what the identity can and cannot do in AWS.
				    However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it
	 --  Policies :  Document (JSON format) that defines one or more permissions – assign to user or groups

- What are IAM roles?
	- IAM roles are a secure way to grant permissions to entities that you trust. Examples of entities include the following:
		1. IAM user in another account
	    2. Application code running on an EC2 instance that needs to perform actions on AWS resources
	    3. An AWS service that needs: For example Lambda needs persmission to access AWS resources and run the code
	    4. Users from a corporate directory who use identity federation with SAML
	    5. IAM roles issue keys that are valid for short durations, making them a more secure way to grant access	
	
- IAM Features
	- Shared access to your AWS Account: To grant other people access without sharing your username and password
	- Granular permissions for users / services
	- Secure access to AWS resources for applications that run on Amazon EC2
	- Multi-factor authentication : Extra Security with code from specially configured device
	- Identity Federation – You can allow users who already have passwords elsewhere—for example, in your corporate network or with an internet identity provider—to get temporary access to your AWS account.Facebook, LinkedIn and Active Directory- You can login to AWS with your corporate credentials.
	- Integration with other AWS services.EC2, ELB, AutoScaling
	- AWS recommends very limited usage of root account
	- Supports PCI-DSS compliance
	
- IAM Best Pratices
	- Lock Away Your AWS Account Root User Access Keys
	- Create Individual IAM Users
	- Use AWS Defined Policies to Assign Permissions Whenever Possible
	- Use Groups to Assign Permissions to IAM Users
	- Grant Least Privilege
	- Use Access Levels to Review IAM Permissions
	- Configure a Strong Password Policy 
	- Enable MFA for Privileged Users
	- Use Roles for Applications That Run on Amazon EC2 Instances
	- Delegate by Using Roles Instead of by Sharing Credentials
	- Rotate Credentials Regularly
	- Remove Unnecessary Credentials
	- Use Policy Conditions for Extra Security : For example, you can write conditions to specify a range of allowable IP addresses that a request must come from. You can also specify that a request is allowed only within a specified date range or time range.
	- Monitor Activity in Your AWS Account  : You can use logging features in AWS to determine the actions users have taken in your account and the resources that were used. The log files show the time and date of actions, the source IP for an action, which actions failed due to inadequate permissions, and more.

- Manage AWS resources via
	1. Management console – Using username and password
	2. Rest APIs – Using Access Key ID and Secret Access Key
	3. AWS CLI - Using Access Key ID and Secret Access Key
	4. AWS SDK – various programming languages supported.
	
	 
- IAM Notes
	 -  IAM is a global service. It is not region specific
	 -  Root account :  Accessed by signing in with the email address and password that you used to create the account	 
	 -  You can attach permissions to individual users and groups.
	 -  Secret access key can be retrieved only once during user creation. In case you lose it then you can re-generate it.
	 -  IAM Password policy can be set to access the admin console.
	 -  New users have no permissions when first created. Everything has to be explicitly added.
	 -  Power User Access allows Access to all AWS services except the management of groups and users within IAM.
	 -  Using Access Key ID and Secret Access Key – can be used only via accessing programmatically. 
     -  If a single policy includes a denied action, IAMdenies the entire request and stops evaluating policies
	 -  Configure who uses AWS and their level of access to the AWS Console.
	 -  Centralized control over AWS Account
	 -  Setup password rotation policy and Configure a Strong Password Policy for Your Users
	 -  Use Roles for Applications That Run on Amazon EC2 Instances`
 

   
=================================================================================
  

  
VPC (Virtual Private Cloud)
	-  VPC is a virtual network in the AWS cloud
	-  Amazon VPC lets you provision a logically isolated section of the Amazon Web Services (AWS) cloud where you can launch AWS resources in a virtual network that you define.
	-  Virtual data center in the cloud. You can have multiple VPC's per region. VPC's can also be connected to each other via VPC peering
 
Benefits of Using a VPC
	- Assign static private IPv4 addresses to your instances that persist across starts and stops
	- Assign multiple IPv4 addresses to your instances
	- Define network interfaces, and attach one or more network interfaces to your instances
	- Change security group membership for your instances while they're running
	- Control the outbound traffic from your instances (egress filtering) in addition to controlling the inbound traffic to them (ingress filtering)
	- Add an additional layer of access control to your instances in the form of network access control lists (ACL)
	- Run your instances on single-tenant hardware

You can connect to VPC using 
	~ The Internet (via an Internet gateway)
	~ Your corporate data center using a Hardware VPN connection (via the virtual private gateway)
	~ Both the Internet and your corporate data center (utilizing both an Internet gateway and a virtual private gateway)
	~ Other AWS services (via Internet gateway, NAT, virtual private gateway, or VPC endpoints)
	~ Other VPCs (via VPC peering connections)
	
Elastic Network Interfaces
	-  You can attach or detach one or more network interfaces to an EC2 instance while it’s running
	-  The total number of network interfaces that can be attached to an EC2 instance depends on the instance type.
	-  Network interfaces can only be attached to instances residing in the same Availability Zone
	-  Network interfaces can only be attached to instances in the same VPC as the interface.
	-  You can attach and detach secondary interfaces (eth1-ethn) on an EC2 instance, but you can’t detach the eth0 interface

VPC Flow log :  
	- VPC flow logs is a feature that enables you to capture information about the IP traffic going to and from network interfacs in your VPC		
	- Flow log data is stored using Amazon cloudwatch logs.
	- After you have created a flow log, you can view and retrieve its data in Amazon CloudWatch logs		 
	- Flow logs can be created in three different level
		1. VPC
		2. Subnet
		3. Network Interface Level
	- You cannot enable flow logs for VPCs that are peered with your VPC unless the peer VPC is in your account
	- You cannot tag a flow logging
	- After a flow log is created, you cannot change its confgiuration
	- Not all traffic is monitored 

VPC Peering
	-  VPC Peering - Allows you to connect one VPC with another via a direct network route using private IP addresses
	
	
 -  You have complete contol over your virtual networking environment, including selection of your own IP address range, creation of subnets, and confgiuration of route tables and network gateways
 -  One Subnet = one availability zone
 -  One Internet gateway = One VPC
 -  VPC can span multiple Availability Zones
 -  Internet gateway enables Amazon EC2 instances in the VPC to directly access the Internet
 -  Instances without public IP addresses can access the Internet in one of two ways:
     1. NAT Instance or NAT Gateway
	 2. VPN connecion or Direct Connect Connection
 -  Instances in a VPC can access the Internet using Public IP address
 -  DescribeInstances() will return all running Amazon EC2 instances
 -  You may use a third-party software VPN to create a site to site or remote access VPN connection with your VPC via the Internet gateway
 -  IPsec is a protocol suite for securing Internet Protocol (IP) communications by authenticating and encrypting each IP packet of a data stream
 -  Establishing a hardware VPN connection between your existing network and Amazon VPC allows you to interact with Amazon EC2 instances within a VPC as if they were within your existing network
 
 -  CIDR - Classless Inter-Domain Routing is a method for allocating IP addresses and IP routing
 -  Default VPCs are assigned a CIDR range of 172.31.0.0/16
 -  The minimum size of a subnet is a /28 (or 14 IP addresses.) for IPv4
 -  You can assign one or more secondary private IP addresses to an Elastic Network Interface or an EC2 instance in Amazon VPC.
 -  Elastic IP (EIP) addresses will only be reachable from the Internet (not over the VPN connection)
 -  Router :An Amazon VPC router enables Amazon EC2 instances within subnets to communicate with Amazon EC2 instances in other subnets within the same VPC. The VPC router also enables subnets, Internet gateways, and virtual private gateways to communicate with each other.
 -  Ping (ICMP Echo Request and Echo Reply) requests to the router in your VPC is not supported
 -  Launch instance into a subnets of your chosing



 -  Assign custom IP address ranges in each subnets
 -  Configure route tables between subnets
 -  Much better security control over your AWS resources. Subnets to block specific IP/s. Move to private subnets. 

 -  No Transitive peering
 -  When you create a new VPC, by default Router, Route Table, Network ACL and security group is created
 -  When creating NAT instance, Disable Source/Destination check on the Instance
 -  NAT instannce must be in a public sunet
 -  Comparision between NAT instance and NAT gateway 
		
 -  CIDR.xyz
 -  Security Groups are Stateful (Inbound rules need to be defined not the outbound rules); Network Access Control Lists are Stateless
 -  https://github.com/agasthik/aws-csa-2017#network-acls--security-groups
 -  5 IP address can not be used
 -  When you create new VPC, Auto Assign public IP address is set to No
 -  https://github.com/agasthik/aws-csa-2017#nat-instance--nat-gateway
 -  NAT instance- Disable source/ Destination checks: Eatch EC2 instance performs source/destination checks by default. This means that the instance must be the source or destination of any traffice it sends or receives.
    However NAT instance must be able to send and receive traffic when the source or destination is not itself. Therefor, you must disable source/destination  checks on NAT instance
 -  When you create a NACL, inbound and outbound rules are deny. 
    NACL 
	     Rules are evaluated based on the numerical order, starting with the lowest numbered rule. If Rule # 100 is allow HTTP and Rule # 101 is deny HTTP the NACL will allow because it found rule 100 first as allow
	     Block IP address, Specific IP address ranges
         NACL have seperate inbound and outbound rules and each rule can either allow or deny traffic
-   While creating Application load balancer you need two public subnets
Nat vs Bastion
		NAT instance is used to provide internet connectivity to private subnets.  
		Bastions are used for secure administrative tasks only. Bastions are placed in Public subnets and connect to private subnets via private IP
		You cannot use NAT instance to SSH / RDP into private subnet. For that Bastion (Jump Box) is required.
		For Bastion HA, have multiple Bastions in different AZs – at least 2 public subnets. Auto scaling in multiple AZ, route 53 doing health checks.
		
-   Regions : Grouping of AWS resources in specific geographic location, desined to service AWS customers that are located closest to a region
    Availability  Zones : Within a Region seperate, physical AWS data centers are located. Multiple AZ's in one region provide redundancy/
    Internet Gateway : Connect VPC with the internet
    Route tables : Set of rules, called routes, that are used to determine where network traffic is directed
    NACL - NACL is optional layer of security for you VPC that acts as a firewall for controlling traffic in and out of one or more subnets
	       A subnet can only be associated with one NACL at a time
    Subnet : Subnet is a sub section of a network. Subnets must be associated with route table. Public subnet has a route to internet. Private subnet does not have route to internet.A subnet is located in one specific Availability zone
	High Availability : Creating your architecture in such a way that your system is always available. You can place EC2/RDS in multiple availability zone to create redundancy in your architecture
	Fault Tolerant : The ability of your system to withstand failures in one (or more) of its components and still remain available. If something fails it will repair itself. If my webserver fails my backup server it will automatically failover to backup
	
	Network Control Access list vs Security groups
	https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html		

	-  Advantages of using AWS security groups	
		- Can define public and private subnets 
		- Security Groups
		- NACL
		- Hardware Virtual Private Network and leverage the AWS cloud as an extension of your corporate datacenter
	
	
=======================================================================================================================================================================================================================================		

SQS - Simple Queue Service

Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages waiting to be processed
Use case - One common use case is a distributed, decoupled application whose multiple components and modules need to communicate with each other, but can’t do the same amount of work simultaneously. 
           In this case, Amazon SQS message queues carry messages to be processed by the application running on Amazon EC2 instances.    
		   1. Users submit videos to be transcoded to the website
		   2. The videos are stored in Amazon S3, and a request message is placed in an incoming Amazon SQS queue with a pointer to the video and to the target video format within the message.
		   3. Amazon EC2 instances reads the request message from the incoming queue, retrieves the video from Amazon S3 using the pointer, and transcodes the video into the target format
		   4. The converted video is put back into Amazon S3 and another response message is placed in another outgoing Amazon SQS queue with a pointer to the converted video.   
SQS is a pulled based system
Visibility timeout  - The visibility timeout is a period of time during which Amazon SQS prevents other consuming components from receiving and processing a message.
			          The maximum visibility timeout for an Amazon SQS message is 12 hours.Default Visibility is 30 seconds. ChangeMessageVisibility timeout
SQS polling - Amazon SQS long polling is a way to retrieve messages from your Amazon SQS queues. Maximum long polling is 20 seconds.
              While the regular short polling returns immediately, even if the message queue being polled is empty, long polling doesn’t return a response until a message arrives in the message queue, or the long poll times out.  
Amazon SQS message queues to receive notifications from Amazon SNS topics
Amazon SNS is designed such that each message is delivered at least once to Amazon SQS standard queues.
You can delete all messages in an Amazon SQS message queue using the PurgeQueue action.
Standard Queues -  Standard queues support a nearly unlimited number of transactions per second per API.A message is delivered at least once, but occasionally more than one copy of a message is delivered.
			       Occasionally, messages might be delivered in an order different from which they were sent.
FIFO Queues     -  By default, FIFO queues support up to 300 messages per second. FIFO queues can support up to 3,000 messages per second.A message is delivered once and remains available until a consumer processes and deletes it. Duplicates aren't introduced into the queue.
				   The order in which messages are sent and received is strictly preserved (i.e. First-In-First-Out).
				   FIFO queues are designed to never introduce duplicate messages
Cannot convert existing standard queue to a FIFO queue  
Amazon SQS message retention period to a value from 1 minute to 14 days. The default is 4 days. Once the message retention limit is reached, your messages are automatically deleted.
Set this message size limit to a value between 1,024 bytes (1 KB), and 262,144 bytes (256 KB)
Amazon SQS messages can contain up to 256 KB of text data, including XML, JSON and unformatted text
Queue names are limited to 80 characters
You can create any number of message queues.
No. Each Amazon SQS message queue is independent within each region
Amazon SQS VS  Amazon Kinesis Streams : Kinesis Allows multiple applications to consume the same stream concurrently
The cost of Amazon SQS is calculated per request, plus data transfer charges for data transferred out of Amazon SQS 
SQS are billed in 64KB chunks
SQS Fanning out- Create SNS topic and subscribe multiple queue. When a message is sent to SNS topic, the message will be fanned out to the SQS queues


=======================================================================================================================================================================================================================================

SNS – Simple Notification Service
	Amazon Simple Notification Service (Amazon SNS) is a web service that makes it easy to set up, operate, and send notifications from the cloud. 
	The Amazon SNS service can support a wide variety of needs including event notification, monitoring applications, workflow systems, time-sensitive information updates, mobile applications, and any other application that generates or consumes notifications
	SNS consists of Topics and you can publish messages to topics.
	HTTP, HTTPS, Emails, SQS, SMS, Apple Push and Android, Fire OS, Windows devies, Lambda
	Publish messages to SQS queues, trigger Lambda functions. Lambda function can then manipulate information and then send to other SNS Topics
	SNS is Push based messaging.
	Makes it easy to setup, operate and send notifications from the cloud.
	Immediate delivery to subscribers or other applications
	You can group multiple recipients using topics. Recipients can subscribe to topics to receive notifications.
	Flexible message delivery over multiple protocols.
	Is used in conjunction with CloudWatch and AutoScaling.
	EC2 instances pull SQS messages from a standard SQS queue on a FIFO (First In First out) basis. – False
	Amazon SNS does not currently support forwarding messages to Amazon SQS FIFO queues. You can use SNS to forward messages to standard queues
	The AWS HIPAA compliance program includes Amazon SNS as a HIPAA eligible Service
	At least three copies of the data are stored across multiple availability zones, which means that no single computer or network failure renders Amazon SNS inaccessible.
	Subscriber may receive duplicate messages and developer should keep this in mind and design there applications accordingly 
	SNS can be used in Auto scaling, Cloudwatch, Billing Alarms.
	Instantaneous, push based delivery(no Polling)
	SNS vs SQS - Both are messaging service.
				 SNS is Push, SQS is pull based service
	SNS - Type, MessageID, TopicARN, Subject, Message, TimeStamp, SignatureVersion, Signature, SigningCertURL, UnsubscribeURL, Message attributes

=======================================================================================================================================================================================================================================


Amazon Kinesis
 -	Streaming data is data that is generated continously by thousands of data sources – stock prices, game information, social network data, geo-spatial data, purchases from online stores, IoT sensor data.
 -	Amazon Kinesis is a AWS platform to send your streaming data too. Kinesis makes it easy to load and analyze streaming data, and also providing the ability for you to build your own custom applications for your business needs
 -	Kinesis Streams - Stores data for by default 24 hours to 7 days. - Data stored in shards. - Data consumers (EC2 instances) analyze the stream and then derive results/take next actions. - Data capacity of stream is a function of the number of shards you specify for the stream.
 -	Kinesis Firehose
	  Don’t have to worry about shards, streams – completely automated.
	  No automatic data retention window. Data is either immediately analyzed or sent to S3 and then to Redshift, elastic search cluster
	  Data is immediately analyzed via Lambda.
 -	Kinesis Analytics –
  	  Run SQL type queries on top of data contained in Streams or Firehose and store the results in S3 / Redshift and Elastic Search cluster.	
 -  Amazon Kinesis : Streams allows real-time processing of streaming big data and the ability to read and replay records to multiple Amazon Kinesis Application
	There are 2 main advantages for Kinesis (1) you can read the same message from several applications and (2) you can re-read messages in case you need to.
	Both advantages can be achieved by using SNS as a fan out to SQS. That mean that the producer of the message send only one message to SNS, Then the SNS fan-out the message to multiple SQSs, one for each consumer application.
	Kinesis can trigger a Lambda, while SQS cannot	

=======================================================================================================================================================================================================================================	
	
	
CloudWatch :
	CloudWatch is a logging and monitoring service that is used to monitor your AWS resources, as well as the applications that run on AWS
	You monitor your environment by configuring and viewing CloudWatch Metrics. Metrics are datapoint specific to each AWS service or Resource
	CloudWatch alarms – set notifications when particular metric thresholds is hit.
	AutoScaling heavily utlizes cloudwatch- relying on metric threshold and alarms to tirgger the addition (or removal) of instance from an auto scaling group.
	CloudWatch logs helps you monitor EC2 instance/application/system logs. Logs send data to CloudWatch
	Cloudwatch can monitor, AutoScaling, ELB, Route 53 Health checks, EBS, Storage Gateway, CloudFront, Dynmodb, RDS Instances, EMR , Redshift, SNS , SQS Queue,  Estimated Charges on your AWS Bill
	Cloudwatch can monitor resources at host level. CPU, Network, Disk and status check, DiskReadOps, DiskWriteOps, NetworkIn, NetworkOut, StatusCheckFailed
	RAM utilization is a custom metrics, How much storage is left on EBS volume is also a custom metric, DiskSwap utilization
	Standard monitoring 5 mins. Detailed monitoring 1 minute.

	By default 2 weeks stored. You can retrieve data  that is longer than 2 weeks using the GetMetricStatistics API. Also for terminated EC2 or ELB instance upto 2 weeks
	you can create an alarm to monitor any Amazon cloudwatch metrics in your account. ELB, EC2 CPU Utilization or charges on AWS bill
	
	System Checks the host or underlying machines : Loss of n/w connectivity, Loss of System power, Software issues on Physical host, Hardware issues on the physical host: Best way is to stopping and restarting the VM again
	Instance Status check the VM:  Failed system status check, Misconfigured networking, Exhausted memory, corrupted file system, incompatiable kernel. Troubleshoot by rebooting instance or modifying OS (Configuration file)
	
	Two types of monitoring for RDS	
		1. In CloudWatch
		2. In RDS itself, you can monitor RDS by Events
    ELB metrics : HTTPCode_Backend_2xx 2XX:Successful actions  3xx:The user agent requires action  4xx:client errors   5xx:backend errors
	
    CloudWatch events help you respond to state changes. E.g. run Lambda function in response to.    
	You can create custom dashboards all CloudWatch metrics
	Check the Cloudwatch logs for the error keywords , create an alarm and then restart the server
	You can save money by monitoring resources in your AWS account
	Cloudwatch dashboard -  Monitoring team to have a consolidated view of the monitoring of critical resources
	Get notified beforehand before the charges go beyond a certain value - Create billing alarms with the thresholds defined accordingly.
	You can create Alarm based actions on EC2 using cloudwatch metrics. Alarms allows you to set Alarms that notify you when particular thresholds are hit
	CloudWatch Events helps you to respond to state changes in your AWS resources.
	ClodWatch logs helps you to aggregate, monitor and store logs.
		- Monitor HTTP response codes in Apached logs
		- Receive alarms for errors in Kernel logs
		- Count exceptions in application logs
	  
  
CloudWatch vs Cloud Trail 
- Cloud watch is for logging and monitoring (performance). Cloud trail is for auditing (What people are doing with your environment)
=======================================================================================================================================================================================================================================  

CloudTrail: 	
	Every action that occurs on AWS is the result of a single API call
	It is used for monitoring and security processes
	Cloudtrail audits and certain compliance certifications require that you log and report every event that occurs in your environment
	UseCases of CloudTrail:
		1. Security Analysis
		2. Track and monitor changes to AWS resources
		3. Compliance Aid
		4. Troubleshoot Operational Issues
		
	Once configured CloudTrail logs all API events and delivers the log to an S3 bucket
	Cloud trail will monitor: Time of the event, Who made the event call, The source of the call, etc
	CloudTrail can integrate into SNS, CloudWatch and CloudWatch logs to send notifications when specific API events occur
	CloudTails are configured on a per region basis
	HIPPA and PCI require log files for 6 years
	
	
	
=======================================================================================================================================================================================================================================  

API Gateway
 -	Fully Managed web service which enables developers to publish, monitor and secure APIs at any scale.
 -  API Gateway acts as a front foor for your application, allowing access to data/logic/functionality from your back end services
 -	Amazon API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization and access control, monitoring, and API version management. 
 -	With Amazon API Gateway, you pay only for calls made to your APIs and data transfer ou
 
	Benifits of using API Gateways
	-	API Caching – Cache your endpoint’s responses. Reduces load on endpoints based on duration of TTLs
	-	Low cost & Efficient. Scales automatically.
	-	Set Throttle limits based on number of request per second to prevent attacks.
	-	CloudWatch can be used to monitor API Gateway activity and usage. Monitoring can be done on the API or Stage Level
	-	You can create CloudWatch alarms based on these metrics
	-	For application built on top of multiple domains, you need to enable CORS on API Gateway.
	-   Deploy API to STAGE (Dev, Beta and Production)
	-   Request/response data transformation
	-   API Version control
	-   DDoS (Distributed Denial of Service) protection via CloudFront
	-   API can be used with CloudFront to prevent DDoS attack ,reduce latency. API gateway uses API Gateway cache to reduce backend load. Use CloudWatch Monitoring to help throttle API requests.API Gateway can communicate with Other public API Endpoints
	-   AWS Identity and Access Management (IAM) and Amazon Cognito, to authorize access to your APIs
	HTTP Methods
		POST - create and other non-idempotent operations.
		PUT - update.
		GET - read a resource or collection.
		DELETE - remove a resource or collection.
	-   Run your API without servers

======================================================================================================================================================================================================================================= 

Lambda
 - AWS Lambda is a compute service that provides resizable compute capacity in the cloud to make web-scale computing easier for developers. You can upload your code to AWS Lambda and the service can run the code on your behalf using AWS infrastructure. AWS Lambda supports multiple coding languages: Node.js, Java, or Python.
   After you upload your code and create a Lambda function, AWS Lambda takes care of provisioning and managing the servers that you use to run the code. In this lab, you will use AWS Lambda as a trigger-driven compute service where AWS Lambda runs your code in response to changes to an Amazon EC2 security group. The code for the Lambda function will be provided with this lab.
   
 - AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume - there is no charge when your code is not running.
   AWS is responsible for capacity provisioning and automated scaling.
   Use Lambda is your goal is from moving server and infrastructure
 - Benifits 
   No Servers to manage, Continous Scaling, Subsecond Metering
 - Languages 
   C# Java NodeJs Python
 - Priced based on requests
 - Use Cases??
=======================================================================================================================================================================================================================================   

AWS CloudFormation:
	CloudFormation service can be used to deploy infrastructure using stacks and templates
	AWS CloudFormation is a service that gives developers and businesses an easy way to create a collection of related AWS resources and provision them in an orderly and predictable fashion
	CloudFormation gives us "Infrastructure as Code"
	We Can version control out "Infrastructure"
	We Can encourage collaboration
	We can automate our innfrastruce: Automation gives us a repeatable, reliable and consistent environment
	An AWS CloudFormation template is a JSON or YAML formatted text file. You can save these files with any extension, such as .json, .yaml, .template, or .txt. 
	AWS CloudFormation uses these templates as blueprints for building your AWS resources. For example, in a template, you can describe an Amazon EC2 instance, such as the instance type, the AMI ID, block device mappings, and its Amazon EC2 key pair name. Whenever you create a stack, you also specify a template that AWS CloudFormation uses to create whatever you described in the template.
	AWS CloudFormation templates are JSON or YAML-formatted text files that are comprised of five types of elements:
		1. An optional list of template parameters (input values supplied at stack creation time)
		2. An optional list of output values (e.g. the complete URL to a web application)
		3. An optional list of data tables used to lookup static configuration values (e.g., AMI names)
		4. The list of AWS resources and their configuration values
		5. A template file format version number
	Stacks - When you use AWS CloudFormation, you manage related resources as a single unit called a stack. You create, update, and delete a collection of resources by creating, updating, and deleting stacks. All the resources in a stack are defined by the stack's AWS CloudFormation template. Suppose you created a template that includes an Auto Scaling group, Elastic Load Balancing load balancer, and an Amazon Relational Database Service (Amazon RDS) database instance.
	Complete Rollback occurs when CloudFormation stack creation fails
	You can install software at stack creation time using AWS CloudFormation
	Cloudformation can be used with Chef and Puppet
	Cloudforation is free of cost. You only pay for the AWS resources that are created
	CloudFormation Template: Description , Version, Parameters, Resources, Mappings, Outputs (Resources is the only one required for cloud formation template to be accepted
	Command line commands list all current stacks in your CloudFormation service: AWS cloudformation list-stacks & AWS cloudformation describe-stacks
	Use intrinsic functions only in specific parts of a template
	fn:GetAtt is used on a CloudFormation template to:Return the value of an attribute from a resource on the template
	Create a script which could create duplicate resources in another region incase of a disaster
======================================================================================================================================================================================================================================= 

CloudFront 
  - A Content Delivery network (CDN) is a system of distributed servers (network) that deliver webpages and other web content to a user based on the geographic locations of the users, the origin of the webpage and a content delivery server
  - Edge location - Edge locations are used to cached frequently accessed data. Theses are different then regions and availability zones.
  - Origin - This is the origin of all the files that the CDN will disribute. 
  - Distribution - This is the name given to the CDN which consists of a collection of Edge Locations
     - Web Distribution : Typilcally used for websites
	 - RTMP Distribution :  Media Streaming
  - Edge locations are read and write
  - Objects are cached for the life of the TTL
  - You can clear cached objects, but you will be charged
======================================================================================================================================================================================================================================= 

Dynamodb 
  -  Dynamodb is a fasaat and flexible NOSQL database service for all applications that need single consistent single digit millisecond latency at any scale. It is fully managed database and supports both document and key values data      models.It is great fit for mobile, web, gaming, ad-tech, IOT
  -  Cross region is enable. Live Data Migration, Easier Traffic Management, Disaster Recovery
  -  Stored in SSD storage
  -  Spread across 3 geographically distinct data centers
  -  Eventual Consistent Reads - Read may take one second to return the latest data
  -  Strongly Consistent Reads - Read returns a result that reflects all writes
  -  Tables - Load data into
  -  Item - Think a row of data in table
  -  Attributes - Columns of table
  -  Pricing - Provisioned Trhoughtput Capacity, First 25 GB of data is free, .24Cents per Gig
  -  Primary Keys - Partition key (Hash key) - Composed of one attribute
                    Composite Keys (Patition key & sort Key (Hash & Range)) Composed of two attributes
  -  Partition key - No two items in a table can have the same partition key value!
  -  Composite key - Parition key can be same but sort key must be different. Use in forum which will have one thread and multiple comments based on date (Sort key)

  -  DynamoDB Indexes - 
			Local Seconday Index -  Has the same partition key but different sort key. Can only be created when creating a table. They cannot be removed or modified later
		        Global Secondary Index - Has different Partition key and different sort key. Can be created at table creation or added later

  -  Dynamodb Stream   
 		     Used to capture any kind of modification of the DynamoDB tables.Dynamodb stream is stored for 24 hours

  -  Query - Query finds an item based on the primary key values. You can also provide a sort key attribute name and value. Use a comparision operator to refine the search results
	     By default query returns all the data attirbutes for items with the specified primary key. However you can use the ProjectExpression parameter so that the query only returns some of the attributes, rather than all of them
             Query results are always sorted by the sort key. If the data type of the sort key is a number, The results are returned in numeric order. Default ascending order. To reverse the order set ScanIndexForward parameter to false
	     Query are always eventual consistent but can be changed to strongly consistent
  -  Scan -  A scan operation examines every item in the table, then filters out values to provide the desired result 
	     By default Scan returns all the data attirbutes for items with the specified primary key. However you can use the ProjectExpression parameter so that the Scan only returns some of the attributes, rather than all of them
	     If the total number of scanned items exceeds the maximum data set size limit of 1 MB, the scan stops and results are returned to the user as a LastEvaluatedKey value to continue the scan in a subsequent operation.
  - Dynamodb provisioned Throughput  - Read are rounded up to increments of 4KB. Eventual consistent reads (default) consists of 2 reads per second. Strongly Consistent reads consists of 1 read per second
                                       Write are 1KB. All writes consists of 1 write per second.
                                       If the provisioned throughput is exceeded your maximum allowed provisioned throughput for a table then 400 HTTP status code : ProvisionedThroughputExceededException
    Web Identity Providers :
			   1. User Authenticates with identity provider, Identity Provider returns Web identity Token
			   2. Asume role with web identity request
			   3. Temporary security Credentials ( Default 1 hour)
                           4. Access Dynamodb
  
    Conditional writes : 
    Atomic Counters : UpdateItem operation to increment or decrement the value of an existing attribute without interfering with other write requests.
                      Acceptable for a web site counter, because you can tolerate with slightly over or under counting the visitors
		      In Banking application, it would be safer to use a conditional update rather than an atomic counter       
  
  
  
  BatchGetItem : A single BatchGetItem request can retrieve uptp 1 MB of data. In addition a single BatchGetItem request can retrieve items from multiple tables


=======================================================================================================================================================================================================================================

Route 53
  Amazon Route 53 provides highly available and scalable Domain Name System (DNS), domain name registration, and health-checking web services
  With Amazon Route 53, you can create and manage your public DNS records
  Route 53 is global service
  DNS : Domain name System is used to convert human friendly domain name to IP address
  TLD : Top level domain name .com, .gov, .net 
  Domain Registrars : A registrar is an authority that can assign domain names directly under one or more TLD. Each domain name is registered in WhoIS database
  Domain Name : It is a general DNS conecpt
  Hosted zone : A hosted zone is analoogus to a traditional DNS zone file
  Registration on Domain Names
  Routing of internet traffic to domain resource
  Health check of resources
  DNS - Domain Name Servers (DNS) are the Internet's equivalent of a phone book. They maintain a directory of domain names and translate them to Internet Protocol (IP) addresses.
  IPV4 - 4 Billion different addresses
  IPV6 - 340 undecilion addresses
  TLD (Top Level Domain Name) - i.e .com, .net, .gov
      Second Level Domain name is .co in www.ind.co.in
  Domain Registers - Godaddy.com
  SOA - Start of Authority
  A record (Address) - Used by a computer to translate the name of the domain to the IP address
  AAA
  NS  - Name server records are used by TLD server to direct traffic to the content DNS server which contains the authoritative DNS records
  MX
  TTL (Time To Live) : The lenght of time that a DNS record is cached on either  the Resolving server or the users own local PC. The lower the TTL, the faster changes to DNS records take to propagate throughout the internet
  CNAMES (Canonial Name) can be used to resolve one domain name to another.
      A CNAME cant be used for naked domain names. www.acloud.guru here www is the naked domain (zone apex record)
	  You cant have a CNAME for http://acloud.guru, it must be either an A record or an Alias
  Alias Records - 
      Alias records are used to map resource record sets in you hosted zone to Elastic Load Balancer, CloudFront distribution, or S3 buckets that are configured as websites.
	  Alias records work like CNAME record in that you can map one DNS name to another target DNS name
    
  ELB's do not have pre-defined IPV4 addresses, you resolve to them using DNS name
  Route 53 Routing Polices
     - Simple   - This is the default routing policy when you create a new record set. This is used when you have a single resource that performs a given function for your domain.
	 - Weighted - Traffic is split based on the different weight assigned
	 - Latency  - Traffic is routed based on the lowest network latency for your end user.
	 - Failover - Failove routing policies are used when you want to create an active/passive set up. Route53 will monitor the health of your primary site using a health check.
	 - Geolocation - Geolocation routing lets you choose where your traffic will be send based on the geographic location of your users.
  Alias vs CNAME :  ALias acts similar to that of CNAME except Alias resolves AWS resources. ELB, Cloudfront.


=======================================================================================================================================================================================================================================

AWS Config:
	AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance
    Use Tags for managing costs
	AWS Config makes it easy to track your resource’s configuration
	Config is good for resource- management, Auditing, Compliance and troubleshoting configuration changes in AWS environment
	Any AWS customer looking to improve their security and governance posture on AWS by continuously evaluating the configuration of their resources would benefit from this capability. Administrators within larger organizations who recommend best practices for configuring resources can codify these rules as Config Rules, and enable self-governance among users.
	A rule represents desired Configuration Item (CI) attribute values for resources and are evaluated by comparing those attribute values with CIs recorded by AWS Config
=======================================================================================================================================================================================================================================  

S3 - Simple Storage Service
 - https://aws.amazon.com/s3/reduced-redundancy/
 - Secure, Durable, Highly scalable object storage.It is easy to use with a simple web services interface to store and retrieve any amount of data from anywhere on the web
 - S3 is place to store you files in cloud.
 - Object is flat file.Video, files. You can not install OS or DB
 - Unlimited storage
 - Files can be from 0 bytes to 5 TB
 - S3 name must be unique
 - Files are stored in Buckets. Buckets are folders
 - S3 is a universal namespace
 - S3-eu-wes-1.amazonaws.com/sgirish.com
 - 200 return code when object is iploaded
 - Data consistency model for S3
       Read after Write consistency for Puts of new Objects
       Eventual consistency for overwirte PUTS and DELETES (can take some time to propagate)
 - S3 is the key value store
	   Key - name of the object
	   Value - Data made up of a sequence of bytes
	   Version ID - Important for versioning
	   Meta-Data - Data about the data you are storing
       Subresources - Access Control List (Who can access the bucket), Torrent
 - Availability 99.99% 
 - Durability   99.999999999% (11 X 9's)
 - Tiered Storage Available (Different type of Storage)
 - Lifecyle Management
	Can be used in conjunction with versioning
	Can be applied to current verions and preivous versions
	Transition to the Standard - Infrequent Access Storage class ( 128KB and 30 days after the creation date)
	Transition to the Glacier Storage Class ( 30 days after IA)
	Use Lifecycle Management to permanently delete object
	
 - Versioning 
		- Versioning enables you to keep multiple versions of an object in one bucket.Once versioning is enabled you cannot disable it but you can suspend it.
		- Great Backup tool
		- MFA (Multi Factor Authentication can be used as an additional layer of security)
		- Stores all versions of an object (including all writes and even if you delete an object)
		- Once versioning is enabled  it can not be disbaled it can only be suspended
		- Stores all version of an object (including all writes and even if you delete an object)
		- When you delete a file, a file is not actually deleted but a delete marker is placed
		- Integrates with Lifecycle rules
 - Encryption
 - Secure data using ACL - Control access to buckets using either a bucket ACL ot using Bucket Polices
 - Server Access Logging -To track requests for access to your bucket, you can enable access logging. Each access log record provides details about a single access request, such as the requester, bucket name, request time, request action, response status, and error code, if any. Access log information can be useful in security and access audits. It can also help you learn about your customer base and understand your Amazon S3 bill.
 - S3 Standard : 99.99% availability and 11'9 durability. Stored redundantly accross multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently
 - S3 Infrequently Accessed - Pay slips, Logs. Lower fee than S3. but you are charged a retrieval fee.99.99% availability and 11'9 durability.
 - S3 Reduced Redundancy Storage - Reproduce images from the thumnails. 99.99% durability and 99.99% availability
 - Glacier - Data archival. It takes 3-5 hours to restore from Glacier
 - S3 Transfer Acceleration enables fast easy and secure transfers of files over long distances between your end users and an S3 bucket. It uses Amazon cloudfront's globally distributed edge locations.
 - When object is uploaded it sends return code as 200
 - By default buckets are private and all objects stored inside them are private
 
 CORS (Cross Origin Resource Sharing)
 	- Allowing javascript in one S3 bucket able to reference code in another S3 bucket
 
  - CRR (Cross Region Replication)
   -  Cross-region replication is a bucket-level configuration that enables automatic, asynchronous copying of objects across buckets in different AWS Regions
   -  Versioning must be enabled on source and destination bucket
   -  Regions must be unique
   -  Existing files will not be replicated automatically but new files after CRR is enabled will be replicated automatically
   - Delete markers are replicated
   - Deleting individual versions or delete markers will not be replicated
 
 
 S3 Encryption 
  Encryption in Transist
  - In Transit using SSL/TLS
  
  Encryption at rest
  - Client Side Encryption: You encrypt the data and upload it to S3
  - Server Side Encryption
     - SSE-S3: S3 Managed Keys where each object is encrypted using unique key and than the key itself is encrypted using master key. They regularly rotate the master key.Amazon handles all the keys. It uses AES 256(Advanced encrypion standard) encryption algorithm
	 - SSE - KMS: Same as SSE-S3 with an additional benifits.It uses envolope key which protects your data encrypion key. Order trail who is using the key. Can create own key or use default key.
	 - SSE-C  Server sude encryption with customer provided keys. Amazon manages encrypion and decryption. 
  Control access to buckets using either a bucket ACL or using Bucket Polices 
  BucketName : http://bucketnames3website.s3-website-us-east-1.amazonaws.com

Storage Gateway
	AWS storage gateway is a service that connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between and on-premises and AWS sttorage infrastructure.
	The service enables you to securely store data to the AWS cloud for scalable and cost-effective storage
	
	Storage gateway is a virtual client on on-premises data center that connects to the AWS infrastructure
	
	1.File gateway (NFS) - Stored flat file on S3. Store files as objects in Amazon S3, with a local cache for low-latency access to your most recently used data. For Flat files - Word files, image, video files	
	2.Volume Gateways (iSCSI) - block based storage
	  Block storage in Amazon S3 with point-in-time backups as Amazon EBS snapshots.
		- Stored Volumes - 	Entire Data is stored onsite and is asynchronously backed up to S3
		- Cached Volumes -  Entire Data is stored on S3 and the most frequently accessed data is cached onsite	
	3. Tape gateway(VTL)
	Back up your data to Amazon S3 and archive in Amazon Glacier using your existing tape-based processes.
        - Used for backup and uses popular backup applications like NetBackup, Backup Exec, Veeam etc
  
SnowBall
  - AWS Snowball is a service used to transfer data into the cloud at faster-than-Internet speeds or harness the power of the AWS Cloud locally using AWS-owned appliances.
    Import to S3
	Export to S3
  
S3 Transfer Acceleration : S3 Transfer Acceleration utilises the cloudfront Edge network to accelerate your uploads to S3.

Glacier 
 - It is an extremely low cost storage service for data acrhival. As low as $0.01 per gigabyte per month and is optimized for data that is infrequently accessed and for which retrieval times of 3 to 5 hours are suitable 
 - Amazon Glacier is an extremely low-cost storage service that provides secure, durable, and flexible storage for data backup and archival.
======================================================================================================================================================================================================================================= 

EC2- Elastic compute cloud 
Is a web service that provides resizable compute capacity in the cloud. Virtual server in cloud.
Main benefit of using EC2 is you can quickly scale capacity, up/down as your computing requirement change
	. On Demand 
	. Reserved - stedy state or predicatable usage.
	   Standard Reserved Instance
	   Convertible Reserved Instance
	   Schedule Reserved Instance
	. Spot Instance - You bid whatever price you for instance capacity. Flexible start and end times. Bid Data processing
    . Dedicated Hosts - Physical EC2 server dedicated for your use.Great for Licensing which does not support multi-Tenancy or cloud deployments.can be purchased on Demand(Hourly).Can be purchased as Reserved Instance
System Status Check - Check underlying hypervisor.Reboot to launch on new instance
Instance Status Check - Checks if traffic fails to instance.Reboot to launch on new instance.
Instance Meta-Data
EC2 and ELB are the building blocks for creating a basic high availability architecture in AWS
curl http://169.254.169.254/latest/meta-data/public-ipv4
yum install jq
aws ec2 describe-instances | jq '.Reservations[].Instances[].PublicIpAddress'
aws ec2 describe-instances   --query "Reservations[*].Instances[*].PublicIpAddress"   --output=text
NAT instance 
  - A NAT is used to provide internet traffic to EC2 instances in private subnets
Bastion Hosts
  - A Bastion is used to securely administer EC2 instances (using SSH or RDP) in private subnets

EC2 - types
	DIRT MCG FPX	
Three types of load balancer:
	1. Application Load Balancer - HTTP/HTTPS traffic
	2. Network Load Balancer     - Use when you need ultra-high performance and static IP addresses for your application
	3. Classic Load Balancer       ( Previous generation and AWS discourages to use it)

=======================================================================================================================================================================================================================================
EBS
What is EBS - Elastic block storage : EBS are used as root devices for EC2 instance. They are automatically replicated to protect you from the failure of a single component.
  - General Purpose SSD (GP2) - 3 IOPS per GB. Capped to 3000 IOPS
	Recommended for most workloads, Virtual Desktops, Devlopment and test environments
  - Provisioned IOPS SSD (IO1) - Designed for I/O intensive applications such as large relationsl or NoSQL databases.Generally used if need more than 10,000 IOPS. Can go upto 20,000 IOPS
    Large Database, MongoDB, Cassandra, MySQL
  - Throughput Optimized HDD (ST1)- used for big data. Large amount of sequence data. Log processing.Big data.can't be boot volumes. 
    Big Data, Data Warehouses, Log Processing
  - Cold HDD  (SC1) - Low cost storage. File server with infrequent usage. can't be boot volumes.
    Scenarios where the lowest storage cost is important   
  - HDD Magnetic (Standard) - Lowest cost per GIG of all the EBS. Can be used as boot volume.
  
  - Maximum Volume size of volumes is 16Tib
  -	You cannot mount 1 EBS volume to multiple EC2 instances instead use EFS.
  -	EC2 instance and EBS should be in the same availability zone 
  -	EBS volume sizes can be changed on the fly, including changing the size and storage type
  -	One Subnet is one availability zone
  -	Instance store volume you can reboot or Terminate. You can not start or Stop Instance Store volume
  -	An EBS volume can be attached to only one instance at a time
  -	EBS Volumes are automatically replicated within that zone to prevent data loss due to failure of any single hardware component
  - General Purpose SSD (GP2) : To increase IOPS increase volume size
  - Volume status check: 
		Warning : Degraded or severely degraded
		Imparied: Stalled or Not Available
		
=======================================================================================================================================================================================================================================		
		
Security Group
What is Security Group??
Security Group - If you add inbound rules, Outbound rules are added automatically. 
				 All inbound traffic is blocked by default
				 All Outbound traffic is Allowed
				 Security Groups are satefull
				 Cannot block traffic for specific port/IP address

Difference between NACL and Security Group.
				 

Ports
RDP - port 3389  tcp
MYSQL port 3306  tcp              
HTTP  port 80    tcp
HTTPS port 443   tcp
=======================================================================================================================================================================================================================================
Snapshots
	Take Snapshot and creating new volume from it will allow to create volume in new availability zone. Copy snapshot will allow to copy to new region.SnapShot will also encrypt an existing volume.
	SnapShots are stored in S3
	Snapshots are point in time copies of volumes
	SnapShots are incremental. Only changes since last snapshot are recorded.
	You can create AMI from both Volumes and SnapShots.
	SnapShots of encrypted volumes are encrypted automatically.
	Volumes restores from encrypted snapshots are encrypted automatically
	You can only share snapshots if they are unencrypted
	
RAID
RAID is Redundant Array of Independent Disks. Raid 0, Raid 1, Raid 5, Raid 10
RAID is used when we need higher disk I/O's or improve I/O's

=======================================================================================================================================================================================================================================	
ELB - Elastic Load Balancer
 ELB will spread the traffic accross different servers.
 Three Different types of Load Balancer
    1. Applicatio Load Balancer - Routing Decisions are made at the application layer (HTTP/HTTPS)
	2. Classic Load Balancer    - Routing Decisions are made at either the transport layer (TCP/SSL) or the application layer (HTTP/HTTPS)
 How to configure Health Check - Set the parameters for Response Timeout, Interval, Unhealthy Threshold, healthy threshold.
 ELB has DNS name and never given IP address
 Read ELB FAQ's
=======================================================================================================================================================================================================================================
  
AutoScaling Group-
 - Before creating AutoScaling group you have to create a launch confgiuration. launch confgiuration is same as starting an instance
=======================================================================================================================================================================================================================================
EC2 Placement
 - A Placement group is a logical grouping of instances within a single availability zone.
 - Used for low latency 10 Gbps network.
 - Can not span multiple availability zones
 - only certain types of instances are allowed
 
======================================================================================================================================================================================================================================= 
EFS - Elastic File System 
  - It is a file storage service for EC2. 
  - Storage capacity is elastic, growing and shrinking automatically as you add and remove files
  - NFS4   protocol
  - No Pre provising is required.
  - Can mount to multiple EC2 instances
  - Can scale up to petabytes
  - Can support thousands ot concurrent NFS connections
  - Data is stored across multiple AZ's within a region
  - EFS is block based storage vs S3 is object based storage
  - Read after write consistency
AWS EFS (Elastic File System)
	EFS is a file storage system that is accessible to Amazon EC2 instances  
	EFS is concurrently-accessible storage for up to thousands of Amazon EC2 instances.
	EFS uses the NFSv4.1 protoco
	To access your file system, you mount the file system on an Amazon EC2 Linux-based instance using the standard Linux mount command and the file system’s DNS name. 
	EFS is compatible with all Linux-based AMIs for Amazon EC2.
	Amazon EBS is a block level storage service for use with Amazon EC2. Amazon EBS can deliver performance for workloads that require the lowest-latency access to data from a single EC2 instance.
	EFS file systems can store petabytes of data. Amazon EFS file systems are elastic, and automatically grow and shrink as you add and remove files.
	Amazon EFS seamlessly offers encryption of EFS file systems. Data is transparently encrypted while being written, and transparently decrypted while being read, so you don’t have to modify your applications. Encryption keys are managed by the AWS Key Management Service (KMS), eliminating the need to build and maintain a secure key management infrastructure
	You can enable encryption for your EFS file system in the EFS console, or by using the AWS CLI or SDK
	To access EFS file systems from on-premises, you must have an AWS Direct Connect connection between your on-premises datacenter and your Amazon VPC. 
	Amazon EFS does not support access over AWS VPN
=======================================================================================================================================================================================================================================  

RDS (Relational Database)
 - Amazon provides high availability and failover support for MYSQL, Oracle and Mariadb
	
=======================================================================================================================================================================================================================================
Security Token Service: 
		Grants users limited and temporary access to AWS resources.



https://github.com/agasthik/aws-csa-2017#aws-object-storage--cdn--s3-glacier-and-cloudfront

The Well Architecture Framework
	1. Security
	2. Reliability
	3. Performance Efficiency
	4. Cost Optimization
	5. Operational Excellence
	
White Paper:
Security
 - The security pillar encompasses the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.
 - Enforcing the principle of least privilege in Security Groups is an important component in the overall security of an application

	
	
	
	
	
	























