Title : AWS Certified Solutions Architect - Associate

QUESTION 1
You are trying to launch an EC2 instance, however the instance seems to go into a terminated status
immediately. What would probably not be a reason that this is happening?
A. The AMI is missing a required part.
B. The snapshot is corrupt.
C. You need to create storage in EBS first.
D. You've reached your volume limit.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon EC2 provides a virtual computing environments, known as an instance. After you launch an instance,
AWS recommends that you check its status to confirm that it goes from the pending status to the running
status, the not terminated status. The following are a few reasons why an Amazon EBS-backed instance might
immediately terminate:
You've reached your volume limit.
The AM is missing a required part.
The snapshot is corrupt.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_|nstanceStraightToTerminated.html


QUESTION 2
You have set up an Auto Scaling group. The cool down period for the Auto Scaling group is 7 minutes. The first
instance is launched after 3 minutes, while the second instance is launched after 4 minutes. How many
minutes after the first instance is launched will Auto Scaling accept another scaling actMty request?
A. 11 minutes
B. 7 minutes
C. 10 minutes
D. 14 minutes
Correct Answer: A
Explanation
Explanation/Reference:
If an Auto Scaling group is launching more than one instance, the cool down period for each instance starts
after that instance is launched. The group remains locked until the last instance that was launched has
completed its cool down period. In this case the cool down period for the first instance starts after 3 minutes
and finishes at the 10th minute (3+7 cool down), while for the second instance it starts at the 4th minute and
finishes at the 11th minute (4+7 cool down). Thus, the Auto Scaling group will receive another request only
after 11 minutes.
http://docs.aws.amazon.com/AutoScaIing/latest/Deve|operGuide/AS_Concepts.htmI


QUESTION 3
In Amazon EC2 Container Service components, what is the name of a logical grouping of container instances
on which you can place tasks?
A. A cluster
B. A container instance
C. A container
D. A task definition
Correct Answer: A
Explanation
Explanation/Reference:
Amazon ECS contains the following components:
A Cluster is a logical grouping of container instances that you can place tasks on. A Container instance is an
Amazon EC2 instance that is running the Amazon ECS agent and has been registered into a cluster. A Task
definition is a description of an application that contains one or more container definitions. A Scheduler is the
method used for placing tasks on container instances. A Service is an Amazon ECS service that allows you to
run and maintain a specified number of instances of a task definition simultaneously. A Task is an instantiation
of a task definition that is running on a container instance. A Container is a Linux container that was created as
part of a task. http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ Welcome.html

QUESTION 4
In the context of AWS support, why must an EC2 instance be unreachable for 20 minutes rather than allowing
customers to open tickets immediately?
A. Because most reachability issues are resolved by automated processes in less than 20 minutes
B. Because all EC2 instances are unreachable for 20 minutes every day when AWS does routine maintenance
C. Because all EC2 instances are unreachable for 20 minutes when first launched
D. Because of all the reasons listed here
Correct Answer: A
Explanation
Explanation/Reference:
An EC2 instance must be unreachable for 20 minutes before opening a ticket, because most reachability
issues are resolved by automated processes in less than 20 minutes and will not require any action on the part
of the customer. If the instance is still unreachable after this time frame has passed, then you should open a
case with support.
https://aws.amazon.com/premiumsupport/faqs/


QUESTION 5
Can a user get a notification of each instance start / terminate configured with Auto Scaling?
A. Yes, if configured with the Launch Config
B. Yes, always
C. Yes, if configured with the Auto Scaling group
D. No
Correct Answer: C
Explanation
Explanation/Reference:
The user can get notifications using SNS if he has configured the notifications while creating the Auto Scaling
group.
http://docs.aws.amazon.com/AutoScaIing/latest/DeveIoperGuide/GettingStartedTutoriaI.html


QUESTION 6
Amazon EBS provides the ability to create backups of any Amazon EC2 volume into what is known as
A. snapshots
B. images
C. instance backups
D. mirrors
Correct Answer: A
Explanation
Explanation/Reference:
Amazon allows you to make backups of the data stored in your EBS volumes through snapshots that can later
be used to create a new EBS volume.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/Storage.htmI


QUESTION 7
To specify a resource in a policy statement, in Amazon EC2, can you use its Amazon Resource Name (ARN)?
A. Yes, you can.
B. No, you can't because EC2 is not related to ARN.
C. No, you can't because you can't specify a particular Amazon EC2 resource in an IAM policy.
D. Yes, you can but only for the resources that are not affected by the action.
Correct Answer: A
Explanation
Explanation/Reference:
Some Amazon EC2 API actions allow you to include specific resources in your policy that can be created or
modified by the action. To specify a resource in the statement, you need to use its Amazon Resource Name
(ARN).
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ug.pdf


QUESTION 8
After you recommend Amazon Redshift to a client as an alternative solution to paying data warehouses to
analyze his data, your client asks you to explain why you are recommending Redshift. Which of the following
would be a reasonable response to his request?
A. It has high performance at scale as data and query complexity grows.
B. It prevents reporting and analytic processing from interfering with the performance of OLTP workloads.
C. You don't have the administrative burden of running your own data warehouse and dealing with setup,
durability, monitoring, scaling, and patching.
D. All answers listed are a reasonable response to his question
Correct Answer: D
Explanation
Explanation/Reference:
Amazon Redshift delivers fast query performance by using columnar storage technology to improve I/O
efficiency and parallelizing queries across multiple nodes. Redshift uses standard PostgreSQL JDBC and
ODBC drivers, allowing you to use a wide range of familiar SQL clients. Data load speed scales linearly with
cluster size, with integrations to Amazon S3, Amazon DynamoDB, Amazon Elastic MapReduce, Amazon
Kinesis or any SSH-enabled host.
AWS recommends Amazon Redshift for customers who have a combination of needs, such as:
High performance at scale as data and query complexity grows Desire to prevent reporting and analytic
processing from interfering with the performance of OLTP workloads Large volumes of structured data to
persist and query using standard SQL and existing BI tools Desire to the administrative burden of running one's
own data warehouse and dealing with setup, durability, monitoring, scaling and patching
https://aws.amazon.com/running_databases/#redshift_anchor


QUESTION 9
One of the criteria for a new deployment is that the customer wants to use AWS Storage Gateway. However
you are not sure whether you should use gateway-cached volumes or gateway-stored volumes or even what
the differences are. Which statement below best describes those differences?
A. Gateway-cached lets you store your data in Amazon Simple Storage Service (Amazon S3) and retain a
copy of frequently accessed data subsets locally. Gateway-stored enables you to configure your onpremises
gateway to store all your data locally and then asynchronously back up point-in-time snapshots of
this data to Amazon S3.
B. Gateway-cached is free whilst gateway-stored is not.
C. Gateway-cached is up to 10 times faster than gateway-stored.
D. Gateway-stored lets you store your data in Amazon Simple Storage Service (Amazon S3) and retain a copy
of frequently accessed data subsets locally. Gateway-cached enables you to configure your on-premises
gateway to store all your data locally and then asynchronously back up point-in-time snapshots of this data
to Amazon S3.
Correct Answer: A
Explanation
Explanation/Reference:
Volume gateways provide cloud-backed storage volumes that you can mount as Internet Small Computer
System Interface (iSCSI) devices from your on-premises application sewers. The gateway supports the
following volume configurations:
Gateway-cached volumes -- You store your data in Amazon Simple Storage Service (Amazon S3) and retain a
copy of frequently accessed data subsets locally. Gateway-cached volumes offer a substantial cost savings on
primary storage and minimize the need to scale your storage on-premises. You also retain low-latency access
to your frequently accessed data. Gateway-stored volumes -- If you need low-latency access to your entire
data set, you can configure your on-premises gateway to store all your data locally and then asynchronously
back up point-in-time snapshots of this data to Amazon S3. This configuration provides durable and
inexpensive off-site backups that you can recover to your local data center or Amazon EC2. For example, if
you need replacement capacity for disaster recovery, you can recover the backups to Amazon EC2. http://
docs.aws.amazon.com/storagegateway/latest/userguide/volume-gateway.html


QUESTION 10
A user is launching an EC2 instance in the US East region. Which of the below mentioned options is
recommended by AWS with respect to the selection of the availability zone?
A. Always select the AZ while launching an instance
B. Always select the US-East-1-a zone for HA
C. Do not select the AZ; instead let AWS select the AZ
D. The user can never select the availability zone while launching an instance
Correct Answer: C
Explanation
Explanation/Reference:
When launching an instance with EC2, AWS recommends not to select the availability zone (AZ). AWS
specifies that the default Availability Zone should be accepted. This is because it enables AWS to select the
best Availability Zone based on the system health and available capacity. If the user launches additional
instances, only then an Availability Zone should be specified. This is to specify the same or different AZ from
the running instances.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html


QUESTION 11
A user is storing a large number of objects on AWS S3. The user wants to implement the search functionality
among the objects. How can the user achieve this?
A. Use the indexing feature of S3.
B. Tag the objects with the metadata to search on that.
C. Use the query functionality of S3.
D. Make your own DB system which stores the S3 metadata for the search functionality.
Correct Answer: D
Explanation
Explanation/Reference:
In Amazon Web Services, AWS S3 does not provide any query facility. To retrieve a specific object the user
needs to know the exact bucket / object key. In this case it is recommended to have an own DB system which
manages the S3 metadata and key mapping.
http://media.amazonwebservices.com/AWS_Storage_Options.pdf


QUESTION 12
After setting up a Virtual Private Cloud (VPC) network, a more experienced cloud engineer suggests that to
achieve low network latency and high network throughput you should look into setting up a placement group.
You know nothing about this, but begin to do some research about it and are especially curious about its
limitations. Which of the below statements is wrong in describing the limitations of a placement group?
A. Although launching multiple instance types into a placement group is possible, this reduces the likelihood
that the required capacity will be available for your launch to succeed.
B. A placement group can span multiple Availability Zones.
C. You can't move an existing instance into a placement group.
D. A placement group can span peered VPCs
Correct Answer: B
Explanation
Explanation/Reference:
A placement group is a logical grouping of instances within a single Availability Zone. Using placement groups
enables applications to participate in a low-latency, 10 Gbps network. Placement groups are recommended for
applications that benefit from low network latency, high network throughput, or both. To provide the lowest
latency, and the highest packet-per-second network performance for your placement group, choose an
instance type that supports enhanced networking.
Placement groups have the following limitations:
The name you specify for a placement group a name must be unique within your AWS account.
A placement group can't span multiple Availability Zones.
Although launching multiple instance types into a placement group is possible, this reduces the likelihood that
the required capacity will be available for your launch to succeed. We recommend using the same instance
type for all instances in a placement group.
You can't merge placement groups. Instead, you must terminate the instances in one placement group, and
then relaunch those instances into the other placement group. A placement group can span peered VPCs;
however, you will not get full-bisection bandwidth between instances in peered VPCs. For more information
about VPC peering connections, see VPC Peering in the Amazon VPC User Guide. You can't move an existing
instance into a placement group. You can create an AM from your existing instance, and then launch a new
instance from the AMI into a placement group. http://docs.aws.amazon.com/ AWSEC2/latest/UserGuide/
placement-groups.html


QUESTION 13
What is a placement group in Amazon EC2?
A. It is a group of EC2 instances within a single Availability Zone.
B. It the edge location of your web content.
C. It is the AWS region where you run the EC2 instance of your web content.
D. It is a group used to span multiple Availability Zones.
Correct Answer: A
Explanation
Explanation/Reference:
A placement group is a logical grouping of instances within a single Availability Zone. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html


QUESTION 14
You are migrating an internal sewer on your DC to an EC2 instance with EBS volume. Your server disk usage
is around 500GB so you just copied all your data to a 2TB disk to be used with AWS Import/Export. Where will
the data be imported once it arrives at Amazon?
A. to a 2TB EBS volume
B. to an S3 bucket with 2 objects of 1TB
C. to an 500GB EBS volume
D. to an S3 bucket as a 2TB snapshot
Correct Answer: B
Explanation
Explanation/Reference:
An import to Amazon EBS will have different results depending on whether the capacity of your storage device
is less than or equal to 1 TB or greater than 1 TB. The maximum size of an Amazon EBS snapshot is 1 TB, so
if the device image is larger than 1 TB, the image is chunked and stored on Amazon S3. The target location is
determined based on the total capacity of the device, not the amount of data on the device. http://
docs.aws.amazon.com/AWSImportExport/latest/DG/Concepts.html


QUESTION 15
A client needs you to import some existing infrastructure from a dedicated hosting provider to AWS to try and
save on the cost of running his current website. He also needs an automated process that manages backups,
software patching, automatic failure detection, and recovery. You are aware that his existing set up currently
uses an Oracle database. Which of the following AWS databases would be best for accomplishing this task?
A. Amazon RDS
B. Amazon Redshift
C. Amazon SimpIeDB
D. Amazon EIastiCache
Correct Answer: A
Explanation
Explanation/Reference:
Amazon RDS gives you access to the capabilities of a familiar MySQL, Oracle, SQL Server, or PostgreSQL
database engine. This means that the code, applications, and tools you already use today with your existing
databases can be used with Amazon RDS. Amazon RDS automatically patches the database software and
backs up your database, storing the backups for a user-defined retention period and enabling point-in-time
recovery.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html


QUESTION 16
True orfalsez A VPC contains multiple subnets, where each subnet can span multiple Availability Zones.
A. This is true only if requested during the set-up of VPC.
B. This is true.
C. This is false.
D. This is true only for US regions.
Correct Answer: C
Explanation
Explanation/Reference:
A VPC can span several Availability Zones. In contrast, a subnet must reside within a single Availability Zone.
https://aws.amazon.com/vpc/faqs/


QUESTION 17
An edge location refers to which Amazon Web Service?
A. An edge location is refered to the network configured within a Zone or Region
B. An edge location is an AWS Region
C. An edge location is the location of the data center used for Amazon CIoudFront.
D. An edge location is a Zone within an AWS Region
Correct Answer: C
Explanation
Explanation/Reference:
Amazon CIoudFront is a content distribution network. A content delivery network or content distribution network
(CDN) is a large distributed system of sewers deployed in multiple data centers across the world. The location
of the data center used for CDN is called edge location. Amazon CIoudFront can cache static content at each
edge location. This means that your popular static content (e.g., your site's logo, navigational images,
cascading style sheets, JavaScript code, etc.) will be available at a nearby edge location for the browsers to
download with low latency and improved performance for viewers. Caching popular static content with Amazon
CIoudFront also helps you offload requests for such files from your origin sever -- CIoudFront serves the
cached copy when available and only makes a request to your origin server if the edge location receMng the
browser's request does not have a copy of the file.
http://aws.amazon.com/c|oudfront/


QUESTION 18
You are looking at ways to improve some existing infrastructure as it seems a lot of engineering resources are
being taken up with basic management and monitoring tasks and the costs seem to be excessive. You are
thinking of deploying Amazon E|asticCache to help. Which of the following statements is true in regards to
EIasticCache?
A. You can improve load and response times to user actions and queries however the cost associated with
scaling web applications will be more.
B. You can't improve load and response times to user actions and queries but you can reduce the cost
associated with scaling web applications.
C. You can improve load and response times to user actions and queries however the cost associated with
scaling web applications will remain the same.
D. You can improve load and response times to user actions and queries and also reduce the cost associated
with scaling web applications.
Correct Answer: D
Explanation
Explanation/Reference:
Amazon EIastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocolcompliant
server nodes in the cloud. Amazon EIastiCache improves the performance of web applications by
allowing you to retrieve information from a fast, managed, in-memory caching system, instead of relying
entirely on slower disk-based databases. The service simplifies and offloads the management, monitoring and
operation of in-memory cache environments, enabling your engineering resources to focus on developing
applications.
Using Amazon EIastiCache, you can not only improve load and response times to user actions and queries,
but also reduce the cost associated with scaling web applications.
https://aws.amazon.com/eIasticache/faqs/


QUESTION 19
Do Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?
A. Yes, they do but only if they are detached from the instance.
B. No, you cannot attach EBS volumes to an instance.
C. No, they are dependent.
D. Yes, they do.
Correct Answer: D
Explanation
Explanation/Reference:
An Amazon EBS volume behaves like a raw, unformatted, external block device that you can attach to a single
instance. The volume persists independently from the running life of an Amazon EC2 instance. http://
docs.amazonwebservices.com/AWSEC2/latest/UserGuide/Storage.html


QUESTION 20
Your supervisor has asked you to build a simple file synchronization service for your department. He doesn't
want to spend too much money and he wants to be notified of any changes to files by email. What do you think
would be the best Amazon service to use for the email solution?
A. Amazon SES
B. Amazon CIoudSearch
C. Amazon SWF
D. Amazon AppStream
Correct Answer: A
Explanation
Explanation/Reference:
File change notifications can be sent via email to users following the resource with Amazon Simple Email
Service (Amazon SES), an easy-to-use, cost-effective email solution. http://media.amazonwebservices.com/
architecturecenter/AWS_ac_ra_fiIesync_08.pdf


QUESTION 21
Does DynamoDB support in-place atomic updates?
A. Yes
B. No
C. It does support in-place non-atomic updates
D. It is not defined
Correct Answer: A
Explanation
Explanation/Reference:
DynamoDB supports in-place atomic updates.
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/\NorkingWithItems.htmI#Working
WithItems.AtomicCounters


QUESTION 22
Your manager has just given you access to multiple VPN connections that someone else has recently set up
between all your company's offices. She needs you to make sure that the communication between the VPNs is
secure. Which of the following services would be best for providing a low-cost hub-and-spoke model for
primary or backup connectMty between these remote offices?
A. Amazon C|oudFront
B. AWS Direct Connect
C. AWS C|oudHSM
D. AWS VPN CIoudHub
Correct Answer: D
Explanation
Explanation/Reference:
If you have multiple VPN connections, you can provide secure communication between sites using the AWS
VPN CIoudHub. The VPN CIoudHub operates on a simple hub-and-spoke model that you can use with or
without a VPC. This design is suitable for customers with multiple branch offices and existing Internet
connections who would like to implement a convenient, potentially low-cost hub-and-spoke model for primary
or backup connectMty between these remote offices. http://docs.aws.amazon.com/AmazonVPC/latest/
UserGuide/VPN_CIoudHub.htmI


QUESTION 23
Amazon EC2 provides a . It is an HTTP or HTTPS request that uses the HTTP verbs GET or POST.
A. web database
B. .net framework
C. Query API
D. C library
Correct Answer: C
Explanation
Explanation/Reference:
Amazon EC2 provides a Query API. These requests are HTTP or HTTPS requests that use the HTTP verbs
GET or POST and a Query parameter named Action.
http://docs.aws.amazon.com/AWSEC2/latest/APIReference/making-api-requests.html


QUESTION 24
In Amazon AWS, which of the following statements is true of key pairs?
A. Key pairs are used only for Amazon SDKs.
B. Key pairs are used only for Amazon EC2 and Amazon CIoudFront.
C. Key pairs are used only for Elastic Load Balancing and AWS IAM.
D. Key pairs are used for all Amazon services.
Correct Answer: B
Explanation
Explanation/Reference:
Key pairs consist of a public and private key, where you use the private key to create a digital signature, and
then AWS uses the corresponding public key to validate the signature. Key pairs are used only for Amazon
EC2 and Amazon CIoudFront.
http://docs.aws.amazon.com/generaI/latest/gr/aws-sec-cred-types.html


QUESTION 25
Does Amazon DynamoDB support both increment and decrement atomic operations?
A. Only increment, since decrement are inherently impossible with DynamoDB's data model.
B. No, neither increment nor decrement operations.
C. Yes, both increment and decrement operations.
D. Only decrement, since increment are inherently impossible with DynamoDB's data model.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon DynamoDB supports increment and decrement atomic operations. http://docs.aws.amazon.com/
amazondynamodb/latest/developerguide/APISummary.html


QUESTION 26
An organization has three separate AWS accounts, one each for development, testing, and production. The
organization wants the testing team to have access to certain AWS resources in the production account. How
can the organization achieve this?
A. It is not possible to access resources of one account with another account.
B. Create the IAM roles with cross account access.
C. Create the IAM user in a test account, and allow it access to the production environment with the IAM policy.
D. Create the IAM users with cross account access.
Correct Answer: B
Explanation
Explanation/Reference:
An organization has multiple AWS accounts to isolate a development environment from a testing or production
environment. At times the users from one account need to access resources in the other account, such as
promoting an update from the development environment to the production environment. In this case the IAM
role with cross account access will provide a solution. Cross account access lets one account share access to
their resources with users in the other AWS accounts. http://media.amazonwebservices.com/
AWS_Security_Best_Practices.pdf


QUESTION 27
You need to import several hundred megabytes of data from a local Oracle database to an Amazon RDS DB
instance. What does AWS recommend you use to accomplish this?
A. Oracle export/import utilities
B. Oracle SQL Developer
C. Oracle Data Pump
D. DBMS_FILE_TRANSFER
Correct Answer: C
Explanation
Explanation/Reference:
How you import data into an Amazon RDS DB instance depends on the amount of data you have and the
number and variety of database objects in your database.
For example, you can use Oracle SQL Developer to import a simple, 20 MB database; you want to use Oracle
Data Pump to import complex databases or databases that are several hundred megabytes or several
terabytes in size.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.htmI


QUESTION 28
A user has created an EBS volume with 1000 IOPS. What is the average IOPS that the user will get for most of
the year as per EC2 SLA if the instance is attached to the EBS optimized instance?
A. 950
B. 990
C. 1000
D. 900
Correct Answer: D
Explanation
Explanation/Reference:
As per AWS SLA if the instance is attached to an EBS-Optimized instance, then the Provisioned IOPS volumes
are designed to deliver within 10% of the provisioned IOPS performance 99.9% of the time in a given year.
Thus, if the user has created a volume of 1000 IOPS, the user will get a minimum 900 IOPS 99.9% time of the
year.
http://aws.amazon.com/ec2/faqs/


QUESTION 29
You need to migrate a large amount of data into the cloud that you have stored on a hard disk and you decide
that the best way to accomplish this is with AWS Import/Export and you mail the hard disk to AWS. Which of
the following statements is inin regards to AWS Import/Export?
A. It can export from Amazon S3
B. It can Import to Amazon Glacier
C. It can export from Amazon Glacier.
D. It can Import to Amazon EBS
Correct Answer: C
Explanation
Explanation/Reference:
AWS Import/Export supports:
Import to Amazon S3
Export from Amazon S3
Import to Amazon EBS
Import to Amazon Glacier
AWS Import/Export does not currently support export from Amazon EBS or Amazon Glacier. https://
docs.aws.amazon.com/AWSImportExport/Iatest/DG/whatisdisk.html


QUESTION 30
You are in the process of creating a Route 53 DNS failover to direct traffic to two EC2 zones. Obviously, if one
fails, you would like Route 53 to direct traffic to the other region. Each region has an ELB with some instances
being distributed. What is the best way for you to configure the Route 53 health check?
A. Route 53 doesn't support ELB with an internal health check.You need to create your own Route 53 health
check of the ELB
B. Route 53 natively supports ELB with an internal health check. Turn "Eva|uate target health" off and
"Associate with Health Check" on and RS3 will use the ELB's internal health check.
C. Route 53 doesn't support ELB with an internal health check. You need to associate your resource record set
for the ELB with your own health check
D. Route 53 natively supports ELB with an internal health check. Turn "Eva|uate target health" on and
"Associate with Health Check" off and RS3 will use the ELB's internal health check.
Correct Answer: D
Explanation
Explanation/Reference:
With DNS Failover, Amazon Route 53 can help detect an outage of your website and redirect your end users to
alternate locations where your application is operating properly. When you enable this feature, Route 53 uses
health checks-regularly making Internet requests to your appIication's endpoints from multiple locations around
the world-to determine whether each endpoint of your application is up or down. To enable DNS Failover for an
ELB endpoint, create an Alias record pointing to the ELB and set the "EvaIuate Target HeaIth" parameter to
true. Route 53 creates and manages the health checks for your ELB automatically. You do not need to create
your own Route 53 health check of the ELB. You also do not need to associate your resource record set for the
ELB with your own health check, because Route 53 automatically associates it with the health checks that
Route 53 manages on your behalf. The ELB health check will also inherit the health of your backend instances
behind that ELB.
http://aws.amazon.com/about-aws/whats-new/2013/05/30/amazon-route-53-adds-elb-integration-for-dns- fai|
over/


QUESTION 31
A user wants to use an EBS-backed Amazon EC2 instance for a temporary job. Based on the input data, the
job is most likely to finish within a week. Which of the following steps should be followed to terminate the
instance automatically once the job is finished?
A. Configure the EC2 instance with a stop instance to terminate it.
B. Configure the EC2 instance with ELB to terminate the instance when it remains idle.
C. Configure the CIoudWatch alarm on the instance that should perform the termination action once the
instance is idle.
D. Configure the Auto Scaling schedule actMty that terminates the instance after 7 days.
Correct Answer: C
Explanation
Explanation/Reference:
Auto Scaling can start and stop the instance at a pre-defined time. Here, the total running time is unknown.
Thus, the user has to use the CIoudWatch alarm, which monitors the CPU utilization. The user can create an
alarm that is triggered when the average CPU utilization percentage has been lower than 10 percent for 24
hours, signaling that it is idle and no longer in use. When the utilization is below the threshold limit, it will
terminate the instance as a part of the instance action.
http://docs.aws.amazon.com/AmazonCIoudWatch/|atest/Deve|operGuide/UsingAIarmActions.html


QUESTION 32
Which of the following is true of Amazon EC2 security group?
A. You can modify the outbound rules for EC2-Classic.
B. You can modify the rules for a security group only if the security group controls the traffic for just one
instance.
C. You can modify the rules for a security group only when a new instance is created.
D. You can modify the rules for a security group at any time.
Correct Answer: D
Explanation
Explanation/Reference:
A security group acts as a virtual firewall that controls the traffic for one or more instances. When you launch
an instance, you associate one or more security groups with the instance. You add rules to each security group
that allow traffic to or from its associated instances. You can modify the rules for a security group at any time;
the new rules are automatically applied to all instances that are associated with the security group. http://
docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-network-security.htmI


QUESTION 33
An Elastic IP address (EIP) is a static IP address designed for dynamic cloud computing. With an EIP, you can
mask the failure of an instance or software by rapidly remapping the address to another instance in your
account. Your EIP is associated with your AWS account, not a particular EC2 instance, and it remains
associated with your account until you choose to explicitly release it. By default how many EIPs is each AWS
account limited to on a per region basis?
A. 1
B. 5
C. Unlimited
D. 10
Correct Answer: B
Explanation
Explanation/Reference:
By default, all AWS accounts are limited to 5 Elastic IP addresses per region for each AWS account, because
public (IPv4) Internet addresses are a scarce public resource. AWS strongly encourages you to use an EIP
primarily for load balancing use cases, and use DNS hostnames for all other inter-node communication. If you
feel your architecture warrants additional EIPs, you would need to complete the Amazon EC2 Elastic IP
Address Request Form and give reasons as to your need for additional addresses.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.htmI#using-instance-ad
dressing-limit


QUESTION 34
In Amazon EC2, partial instance-hours are billed .
A. per second used in the hour
B. per minute used
C. by combining partial segments into full hours
D. as full hours
Correct Answer: D
Explanation
Explanation/Reference:
Partial instance-hours are billed to the next hour.
http://aws.amazon.com/ec2/faqs/


QUESTION 35
In EC2, what happens to the data in an instance store if an instance reboots (either intentionally or
unintentionally)?
A. Data is deleted from the instance store for security reasons.
B. Data persists in the instance store.
C. Data is partially present in the instance store.
D. Data in the instance store will be lost.
Correct Answer: B
Explanation
Explanation/Reference:
The data in an instance store persists only during the lifetime of its associated instance. If an instance reboots
(intentionally or unintentionally), data in the instance store persists. However, data on instance store volumes is
lost under the following circumstances.
Failure of an underlying drive
Stopping an Amazon EBS-backed instance
Terminating an instance
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/InstanceStorage.html


QUESTION 36
You are setting up a VPC and you need to set up a public subnet within that VPC. Which following requirement
must be met for this subnet to be considered a public subnet?
A. Subnet's traffic is not routed to an internet gateway but has its traffic routed to a virtual private gateway.
B. Subnet's traffic is routed to an internet gateway.
C. Subnet's traffic is not routed to an internet gateway.
D. None of these answers can be considered a public subnet.
Correct Answer: B
Explanation
Explanation/Reference:
A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from
other virtual networks in the AWS cloud. You can launch your AWS resources, such as Amazon EC2
instances, into your VPC. You can configure your VPC: you can select its IP address range, create subnets,
and configure route tables, network gateways, and security settings. A subnet is a range of IP addresses in
your VPC. You can launch AWS resources into a subnet that you select. Use a public subnet for resources that
must be connected to the internet, and a private subnet for resources that won't be connected to the Internet. If
a subnet's traffic is routed to an internet gateway, the subnet is known as a public subnet. If a subnet doesn't
have a route to the internet gateway, the subnet is known as a private subnet. If a subnet doesn't have a route
to the internet gateway, but has its traffic routed to a virtual private gateway, the subnet is known as a VPNonly
subnet.
http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html


QUESTION 37
Can you specify the security group that you created for a VPC when you launch an instance in EC2-Classic?
A. No, you can specify the security group created for EC2-Classic when you launch a VPC instance.
B. No
C. Yes
D. No, you can specify the security group created for EC2-Classic to a non-VPC based instance only.
Correct Answer: B
Explanation
Explanation/Reference:
If you're using EC2-Classic, you must use security groups created specifically for EC2-Classic. When you
launch an instance in EC2-Classic, you must specify a security group in the same region as the instance. You
can't specify a security group that you created for a VPC when you launch an instance in EC2-Classic. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.htmI#ec2-classic-securit y- groups


QUESTION 38
While using the EC2 GET requests as URLs, the is the URL that serves as the entry point for the web service.
A. token
B. endpoint
C. action
D. None of these
Correct Answer: B
Explanation
Explanation/Reference:
The endpoint is the URL that serves as the entry point for the web service. http://
docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-query-api.htmI


QUESTION 39
You have been asked to build a database warehouse using Amazon Redshift. You know a little about it,
including that it is a SQL data warehouse solution, and uses industry standard ODBC and JDBC connections
and PostgreSQL drivers. However you are not sure about what sort of storage it uses for database tables.
What sort of storage does Amazon Redshift use for database tables?
A. InnoDB Tables
B. NDB data storage
C. Columnar data storage
D. NDB CLUSTER Storage
Correct Answer: C
Explanation
Explanation/Reference:
Amazon Redshift achieves efficient storage and optimum query performance through a combination of
massively parallel processing, columnar data storage, and very efficient, targeted data compression encoding
schemes.
Columnar storage for database tables is an important factor in optimizing analytic query performance because
it drastically reduces the overall disk I/O requirements and reduces the amount of data you need to load from
disk.
http://docs.aws.amazon.com/redshift/latest/dg/c_co|umnar_storage_disk_mem_mgmnt.html


QUESTION 40
You are checking the workload on some of your General Purpose (SSD) and Provisioned IOPS (SSD) volumes
and it seems that the I/O latency is higher than you require. You should probably check the to make sure that
your application is not trying to drive more IOPS than you have provisioned.
A. Amount of IOPS that are available
B. Acknowledgement from the storage subsystem
C. Average queue length
D. Time it takes for the I/O operation to complete
Correct Answer: C
Explanation
Explanation/Reference:
In EBS workload demand plays an important role in getting the most out of your General Purpose (SSD) and
Provisioned IOPS (SSD) volumes. In order for your volumes to deliver the amount of IOPS that are available,
they need to have enough I/O requests sent to them. There is a relationship between the demand on the
volumes, the amount of IOPS that are available to them, and the latency of the request (the amount of time it
takes for the I/O operation to complete). Latency is the true end-to-end client time of an I/O operation; in other
words, when the client sends a IO, how long does it take to get an acknowledgement from the storage
subsystem that the IO read or write is complete.
If your I/O latency is higher than you require, check your average queue length to make sure that your
application is not trying to drive more IOPS than you have provisioned. You can maintain high IOPS while
keeping latency down by maintaining a low average queue length (which is achieved by provisioning more
IOPS for your volume).
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-workload-demand.htmI


QUESTION 41
Which of the below mentioned options is not available when an instance is launched by Auto Scaling with EC2
Classic?
A. Public IP
B. Elastic IP
C. Private DNS
D. Private IP
Correct Answer: B
Explanation
Explanation/Reference:
Auto Scaling supports both EC2 classic and EC2-VPC. When an instance is launched as a part of EC2 classic,
it will have the public IP and DNS as well as the private IP and DNS. http://docs.aws.amazon.com/AutoScaIing/
latest/DeveIoperGuide/GettingStartedTutoriaI.html


QUESTION 42
You have been given a scope to deploy some AWS infrastructure for a large organisation. The requirements
are that you will have a lot of EC2 instances but may need to add more when the average utilization of your
Amazon EC2 fileet is high and conversely remove them when CPU utilization is low. Which AWS services
would be best to use to accomplish this?
A. Auto Scaling, Amazon CIoudWatch and AWS Elastic Beanstalk
B. Auto Scaling, Amazon CIoudWatch and Elastic Load Balancing.
C. Amazon CIoudFront, Amazon CIoudWatch and Elastic Load Balancing.
D. AWS Elastic Beanstalk , Amazon CIoudWatch and Elastic Load Balancing.
Correct Answer: B
Explanation
Explanation/Reference:
Auto Scaling enables you to follow the demand curve for your applications closely, reducing the need to
manually provision Amazon EC2 capacity in advance. For example, you can set a condition to add new
Amazon EC2 instances in increments to the Auto Scaling group when the average utilization of your Amazon
EC2 fileet is high; and similarly, you can set a condition to remove instances in the same increments when
CPU utilization is low. If you have predictable load changes, you can set a schedule through Auto Scaling to
plan your scaling actMties. You can use Amazon CIoudWatch to send alarms to trigger scaling actMties and
Elastic Load Balancing to help distribute traffic to your instances within Auto Scaling groups. Auto Scaling
enables you to run your Amazon EC2 fileet at optimal utilization.
http://aws.amazon.com/autoscaIing/


QUESTION 43
You are building infrastructure for a data warehousing solution and an extra request has come through that
there will be a lot of business reporting queries running all the time and you are not sure if your current DB
instance will be able to handle it. What would be the best solution for this?
A. DB Parameter Groups
B. Read Replicas
C. Multi-AZ DB Instance deployment
D. Database Snapshots
Correct Answer: B
Explanation
Explanation/Reference:
Read Replicas make it easy to take advantage of MySQL's built-in replication functionality to elastically scale
out beyond the capacity constraints of a single DB Instance for read-heavy database workloads. There are a
variety of scenarios where deploying one or more Read Replicas for a given source DB Instance may make
sense. Common reasons for deploying a Read Replica include:
Scaling beyond the compute or I/O capacity of a single DB Instance for read-heavy database workloads. This
excess read traffic can be directed to one or more Read Replicas. Serving read traffic while the source DB
Instance is unavailable. If your source DB Instance cannot take I/O requests (e.g. due to I/O suspension for
backups or scheduled maintenance), you can direct read traffic to your Read RepIica(s). For this use case,
keep in mind that the data on the Read Replica may be "staIe" since the source DB Instance is unavailable.
Business reporting or data warehousing scenarios; you may want business reporting queries to run against a
Read Replica, rather than your primary, production DB Instance.
https://aws.amazon.com/rds/faqs/


QUESTION 44
In DynamoDB, could you use IAM to grant access to Amazon DynamoDB resources and API actions?
A. In DynamoDB there is no need to grant access
B. Depended to the type of access
C. No
D. Yes
Correct Answer: D
Explanation
Explanation/Reference:
Amazon DynamoDB integrates with AWS Identity and Access Management (IAM). You can use AWS IAM to
grant access to Amazon DynamoDB resources and API actions. To do this, you first write an AWS IAM policy,
which is a document that explicitly lists the permissions you want to grant. You then attach that policy to an
AWS IAM user or role.
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/UsingIAMWithDDB.htmI


QUESTION 45
Much of your company's data does not need to be accessed often, and can take several hours for retrieval
time, so it's stored on Amazon Glacier. However someone within your organization has expressed concerns
that his data is more sensitive than the other data, and is wondering whether the high level of encryption that
he knows is on S3 is also used on the much cheaper Glacier service. Which of the following statements would
be most applicable in regards to this concern?
A. There is no encryption on Amazon Glacier, that's why it is cheaper.
B. Amazon Glacier automatically encrypts the data using AES-128 a lesser encryption method than Amazon
S3 but you can change it to AES-256 if you are willing to pay more.
C. Amazon Glacier automatically encrypts the data using AES-256, the same as Amazon S3.
D. Amazon Glacier automatically encrypts the data using AES-128 a lesser encryption method than Amazon
S3.
Correct Answer: C
Explanation
Explanation/Reference:
Like Amazon S3, the Amazon Glacier service provides low-cost, secure, and durable storage. But where S3 is
designed for rapid retrieval, Glacier is meant to be used as an archival service for data that is not accessed
often, and for which retrieval times of several hours are suitable. Amazon Glacier automatically encrypts the
data using AES-256 and stores it durably in an immutable form. Amazon Glacier is designed to provide
average annual durability of 99.999999999% for an archive. It stores each archive in multiple facilities and
multiple devices. Unlike traditional systems which can require laborious data verification and manual repair,
Glacier performs regular, systematic data integrity checks, and is built to be automatically self-healing. http://
d0.awsstatic.com/whitepapers/Security/AWS%20Security%20Whitepaper.pdf


QUESTION 46
Your EBS volumes do not seem to be performing as expected and your team leader has requested you look
into improving their performance. Which of the following is not a true statement relating to the performance of
your EBS volumes?
A. Frequent snapshots provide a higher level of data durability and they will not degrade the performance of
your application while the snapshot is in progress.
B. General Purpose (SSD) and Provisioned IOPS (SSD) volumes have a throughput limit of 128 MB/s per
volume.
C. There is a relationship between the maximum performance of your EBS volumes, the amount of I/O you are
drMng to them, and the amount of time it takes for each transaction to complete.
D. There is a 5 to 50 percent reduction in IOPS when you first access each block of data on a newly created or
restored EBS volume
Correct Answer: A
Explanation
Explanation/Reference:
Several factors can affect the performance of Amazon EBS volumes, such as instance configuration, I/O
characteristics, workload demand, and storage configuration. Frequent snapshots provide a higher level of
data durability, but they may slightly degrade the performance of your application while the snapshot is in
progress. This trade off becomes critical when you have data that changes rapidly. Whenever possible, plan for
snapshots to occur during off-peak times in order to minimize workload impact. http://docs.aws.amazon.com/
AWSEC2/latest/UserGuide/EBSPerformance.htmI


QUESTION 47
You've created your first load balancer and have registered your EC2 instances with the load balancer. Elastic
Load Balancing routinely performs health checks on all the registered EC2 instances and automatically
distributes all incoming requests to the DNS name of your load balancer across your registered, healthy EC2
instances. By default, the load balancer uses the _ protocol for checking the health of your instances.
A. HTTPS
B. HTTP
C. ICMP
D. IPv6
Correct Answer: B
Explanation
Explanation/Reference:
In Elastic Load Balancing a health configuration uses information such as protocol, ping port, ping path (URL),
response timeout period, and health check interval to determine the health state of the instances registered
with the load balancer.
Currently, HTTP on port 80 is the default health check.
http://docs.aws.amazon.com/E|asticLoadBaIancing/latest/DeveIoperGuide/TerminoIogyandKeyConcepts.
html


QUESTION 48
A major finance organisation has engaged your company to set up a large data mining application. Using AWS
you decide the best service for this is Amazon Elastic MapReduce(EMR) which you know uses Hadoop. Which
of the following statements best describes Hadoop?
A. Hadoop is 3rd Party software which can be installed using AMI
B. Hadoop is an open source python web framework
C. Hadoop is an open source Java software framework
D. Hadoop is an open source javascript framework
Correct Answer: C
Explanation
Explanation/Reference:
Amazon EMR uses Apache Hadoop as its distributed data processing engine. Hadoop is an open source, Java
software framework that supports data-intensive distributed applications running on large clusters of
commodity hardware. Hadoop implements a programming model named "MapReduce," where the data is
dMded into many small fragments of work, each of which may be executed on any node in the cluster. This
framework has been widely used by developers, enterprises and startups and has proven to be a reliable
software platform for processing up to petabytes of data on clusters of thousands of commodity machines.
http://aws.amazon.com/elasticmapreduce/faqs/


QUESTION 49
In Amazon EC2 Container Service, are other container types supported?
A. Yes, EC2 Container Service supports any container service you need.
B. Yes, EC2 Container Service also supports Microsoft container service.
C. No, Docker is the only container platform supported by EC2 Container Service presently.
D. Yes, EC2 Container Service supports Microsoft container service and Openstack.
Correct Answer: C
Explanation
Explanation/Reference:
In Amazon EC2 Container Service, Docker is the only container platform supported by EC2 Container Service
presently.
http://aws.amazon.com/ecs/faqs/


QUESTION 50
is a fast, filexible, fully managed push messaging service.
A. Amazon SNS
B. Amazon SES
C. Amazon SQS
D. Amazon FPS
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Simple Notification Service (Amazon SNS) is a fast, filexible, fully managed push messaging service.
Amazon SNS makes it simple and cost-effective to push to mobile devices such as iPhone, iPad, Android,
Kindle Fire, and internet connected smart devices, as well as pushing to other distributed services.
http://aws.amazon.com/sns/?nc1=h_I2_as


QUESTION 51
As AWS grows, most of your cIients' main concerns seem to be about security, especially when all of their
competitors also seem to be using AWS. One of your clients asks you whether having a competitor who hosts
their EC2 instances on the same physical host would make it easier for the competitor to hack into the cIient's
data. Which of the following statements would be the best choice to put your cIient's mind at rest?
A. Different instances running on the same physical machine are isolated from each other via a 256-bit
Advanced Encryption Standard (AES-256).
B. Different instances running on the same physical machine are isolated from each other via the Xen
hypervisor and via a 256-bit Advanced Encryption Standard (AES-256).
C. Different instances running on the same physical machine are isolated from each other via the Xen
hypervisor.
D. Different instances running on the same physical machine are isolated from each other via IAM permissions.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon Elastic Compute Cloud (EC2) is a key component in Amazon's Infrastructure as a Service (IaaS),
providing resizable computing capacity using server instances in AWS's data centers. Amazon EC2 is
designed to make web-scale computing easier by enabling you to obtain and configure capacity with minimal
friction.
You create and launch instances, which are collections of platform hardware and software. Different instances
running on the same physical machine are isolated from each other via the Xen hypervisor. Amazon is active in
the Xen community, which provides awareness of the latest developments. In addition, the AWS firewall
resides within the hypervisor layer, between the physical network interface and the instance's virtual interface.
All packets must pass through this layer, thus an instance's neighbors have no more access to that instance
than any other host on the Internet and can be treated as if they are on separate physical hosts. The physical
RAM is separated using similar mechanisms. http://d0.awsstatic.com/whitepapers/Security/AWS %20Security
%20Whitepaper.pdf


QUESTION 52
In Amazon RDS, security groups are ideally used to:
A. Define maintenance period for database engines
B. Launch Amazon RDS instances in a subnet
C. Create, describe, modify, and delete DB instances
D. Control what IP addresses or EC2 instances can connect to your databases on a DB instance
Correct Answer: D
Explanation
Explanation/Reference:
In Amazon RDS, security groups are used to control what IP addresses or EC2 instances can connect to your
databases on a DB instance.
When you first create a DB instance, its firewall prevents any database access except through rules specified
by an associated security group.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.htmI


QUESTION 53
You need to set up a complex network infrastructure for your organization that will be reasonably easy to
deploy, replicate, control, and track changes on. Which AWS service would be best to use to help you
accomplish this?
A. AWS Import/Export
B. AWS CIoudFormation
C. Amazon Route 53
D. Amazon CIoudWatch
Correct Answer: B
Explanation
Explanation/Reference:
AWS CIoudFormation is a service that helps you model and set up your Amazon Web Services resources so
that you can spend less time managing those resources and more time focusing on your applications that run
in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2
instances or Amazon RDS DB instances), and AWS CIoudFormation takes care of provisioning and
configuring those resources for you. You don't need to indMdually create and configure AWS resources and
figure out what's dependent on what. AWS CIoudFormation handles all of that. http://docs.aws.amazon.com/
AWSCIoudFormation/latest/UserGuide/WeIcome.htmI


QUESTION 54
You have just been given a scope for a new client who has an enormous amount of data(petabytes) that he
constantly needs analysed. Currently he is paying a huge amount of money for a data warehousing company
to do this for him and is wondering if AWS can provide a cheaper solution. Do you think AWS has a solution for
this?
A. Yes. Amazon SimpIeDB
B. No. Not presently
C. Yes. Amazon Redshift
D. Yes. Your choice of relational AMIs on Amazon EC2 and EBS
Correct Answer: C
Explanation
Explanation/Reference:
Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and
cost-effective to efficiently analyze all your data using your existing business intelligence tools. You can start
small for just $0.25 per hour with no commitments or upfront costs and scale to a petabyte or more for $1,000
per terabyte per year, less than a tenth of most other data warehousing solutions. Amazon Redshift delivers
fast query performance by using columnar storage technology to improve I/O efficiency and parallelizing
queries across multiple nodes. Redshift uses standard PostgreSQL JDBC and ODBC drivers, allowing you to
use a wide range of familiar SQL clients. Data load speed scales linearly with cluster size, with integrations to
Amazon S3, Amazon DynamoDB, Amazon Elastic MapReduce, Amazon Kinesis or any SSH-enabled host.
https://aws.amazon.com/running_databases/#redshift_anchor


QUESTION 55
In an experiment, if the minimum size for an Auto Scaling group is 1 instance, which of the following statements
holds true when you terminate the running instance?
A. Auto Scaling must launch a new instance to replace it.
B. Auto Scaling will raise an alarm and send a notification to the user for action.
C. Auto Scaling must configure the schedule actMty that terminates the instance after 5 days.
D. Auto Scaling will terminate the experiment.
Correct Answer: A
Explanation
Explanation/Reference:
If the minimum size for an Auto Scaling group is 1 instance, when you terminate the running instance, Auto
Scaling must launch a new instance to replace it.
http://docs.aws.amazon.com/AutoScaIing/latest/Deve|operGuide/AS_Concepts.htmI


QUESTION 56
In Amazon EC2, while sharing an Amazon EBS snapshot, can the snapshots with AWS IV|arketpIace product
codes be public?
A. Yes, but only for US-based providers.
B. Yes, they can be public.
C. No, they cannot be made public.
D. Yes, they are automatically made public by the system.
Correct Answer: C
Explanation
Explanation/Reference:
Snapshots with AWS Marketplace product codes can't be made public.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html


QUESTION 57
An organization has created an application which is hosted on the AWS EC2 instance. The application stores
images to S3 when the end user uploads to it. The organization does not want to store the AWS secure
credentials required to access the S3 inside the instance. Which of the below mentioned options is a possible
solution to avoid any security threat?
A. Use the IAM based single sign between the AWS resources and the organization application.
B. Use the IAM role and assign it to the instance.
C. Since the application is hosted on EC2, it does not need credentials to access S3.
D. Use the X.509 certificates instead of the access and the secret access keys.
Correct Answer: B
Explanation
Explanation/Reference:
The AWS IAM role uses temporary security credentials to access AWS services. Once the role is assigned to
an instance, it will not need any security credentials to be stored on the instance. http://docs.aws.amazon.com/
AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html


QUESTION 58
Can resource record sets in a hosted zone have a different domain suffix (for example, www.bIog.
acme.com and www.acme.ca)?
A. Yes, it can have for a maximum of three different TLDs.
B. Yes
C. Yes, it can have depending on the TLD.
D. No
Correct Answer: D
Explanation
Explanation/Reference:
The resource record sets contained in a hosted zone must share the same suffix. For example, the
exampIe.com hosted zone can contain resource record sets for www.exampIe.com and
wvvw.aws.exampIe.com subdomains, but it cannot contain resource record sets for a www.exampIe.ca
subdomain.
http://docs.aws.amazon.com/Route53/Iatest/DeveIoperGuide/AboutHostedZones.html


QUESTION 59
You are running PostgreSQL on Amazon RDS and it seems to be all running smoothly deployed in one
availability zone. A database administrator asks you if DB instances running PostgreSQL support MuIti-AZ
deployments. What would be a response to this question?
A. Yes.
B. Yes but only for small db instances.
C. No.
D. Yes but you need to request the service from AWS.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon RDS supports DB instances running several versions of PostgreSQL. Currently we support
PostgreSQL versions 9.3.1, 9.3.2, and 9.3.3. You can create DB instances and DB snapshots, point-in-time
restores and backups.
DB instances running PostgreSQL support MuIti-AZ deployments, Provisioned IOPS, and can be created
inside a VPC. You can also use SSL to connect to a DB instance running PostgreSQL. You can use any
standard SQL client application to run commands for the instance from your client computer. Such applications
include pgAdmin, a popular Open Source administration and development tool for PostgreSQL, or psql, a
command line utility that is part of a PostgreSQL installation. In order to deliver a managed service experience,
Amazon RDS does not provide host access to DB instances, and it restricts access to certain system
procedures and tables that require advanced prMleges. Amazon RDS supports access to databases on a DB
instance using any standard SQL client application. Amazon RDS does not allow direct host access to a DB
instance via Telnet or Secure Shell (SSH). http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/
CHAP_PostgreSQL.htmI


QUESTION 60
A user has launched 10 EC2 instances inside a placement group. Which of the below mentioned statements is
true with respect to the placement group?
A. All instances must be in the same AZ
B. All instances can be across multiple regions
C. The placement group cannot have more than 5 instances
D. All instances must be in the same region
Correct Answer: A
Explanation
Explanation/Reference:
A placement group is a logical grouping of EC2 instances within a single Availability Zone. Using placement
groups enables applications to participate in a low-latency, 10 Gbps network. Placement groups are
recommended for applications that benefit from low network latency, high network throughput or both. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html


QUESTION 61
Which of the following AWS CLI commands is syntactically incorrect?
1. $ aws ec2 describe-instances
2. $ aws ec2 start-instances --instance-ids i-1348636c
3. $ aws sns publish --topic-arn arn:aws:sns:us-east-1:546419318123:OperationsError -message "Script
Failure"
4. $ aws sqs receive-message --queue-urI https://queue.amazonaws.com/546419318123/Test
A. 3
B. 4
C. 2
D. 1
Correct Answer: A
Explanation
Explanation/Reference:
The following CLI command is missing a hyphen before "-message". aws sns publish --topic-arn
arn:aws:sns:us-east-1:546419318123:OperationsError -message "Script Failure" It has been added below in
red
aws sns publish --topic-arn arn:aws:sns:us-east-1:546419318123:OperationsError ---message "Script Failure"
http://aws.amazon.com/c|i/


QUESTION 62
An organization has developed a mobile application which allows end users to capture a photo on their mobile
device, and store it inside an application. The application internally uploads the data to AWS S3. The
organization wants each user to be able to directly upload data to S3 using their Google ID. How will the mobile
app allow this?
A. Use the AWS Web identity federation for mobile applications, and use it to generate temporary security
credentials for each user.
B. It is not possible to connect to AWS S3 with a Google ID.
C. Create an IAM user every time a user registers with their Google ID and use IAM to upload files to S3.
D. Create a bucket policy with a condition which allows everyone to upload if the login ID has a Google part to
it.
Correct Answer: A
Explanation
Explanation/Reference:
For Amazon Web Services, the Web identity federation allows you to create cloud-backed mobile apps that
use public identity providers, such as login with Facebook, Google, or Amazon. It will create temporary security
credentials for each user, which will be authenticated by the AWS services, such as S3. http://
docs.aws.amazon.com/STS/latest/UsingSTS/CreatingWIF.htmI


QUESTION 63
You are architecting an auto-scalable batch processing system using video processing pipelines and Amazon
Simple Queue Service (Amazon SQS) for a customer. You are unsure of the limitations of SQS and need to
find out. What do you think is a statement about the limitations of Amazon SQS?
A. It supports an unlimited number of queues but a limited number of messages per queue for each user but
automatically deletes messages that have been in the queue for more than 4 weeks.
B. It supports an unlimited number of queues and unlimited number of messages per queue for each user but
automatically deletes messages that have been in the queue for more than 4 days.
C. It supports an unlimited number of queues but a limited number of messages per queue for each user but
automatically deletes messages that have been in the queue for more than 4 days.
D. It supports an unlimited number of queues and unlimited number of messages per queue for each user but
automatically deletes messages that have been in the queue for more than 4 weeks.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Simple Queue Service (Amazon SQS) is a messaging queue service that handles message or
workflows between other components in a system.
Amazon SQS supports an unlimited number of queues and unlimited number of messages per queue for each
user. Please be aware that Amazon SQS automatically deletes messages that have been in the queue for
more than 4 days.
http://aws.amazon.com/documentation/sqs/


QUESTION 64
An online gaming site asked you if you can deploy a database that is a fast, highly scalable NoSQL database
service in AWS for a new site that he wants to build. Which database should you recommend?
A. Amazon DynamoDB
B. Amazon RDS
C. Amazon Redshift
D. Amazon SimpIeDB
Correct Answer: A
Explanation
Explanation/Reference:
Amazon DynamoDB is ideal for database applications that require very low latency and predictable
performance at any scale but don't need complex querying capabilities like joins or transactions. Amazon
DynamoDB is a fully-managed NoSQL database service that offers high performance, predictable throughput
and low cost. It is easy to set up, operate, and scale. With Amazon DynamoDB, you can start small, specify the
throughput and storage you need, and easily scale your capacity requirements on the fly. Amazon DynamoDB
automatically partitions data over a number of servers to meet your request capacity. In addition, DynamoDB
automatically replicates your data synchronously across multiple Availability Zones within an AWS Region to
ensure high-availability and data durability.
https://aws.amazon.com/running_databases/#dynamodb_anchor


QUESTION 65
You have been doing a lot of testing of your VPC Network by deliberately failing EC2 instances to test whether
instances are failing over properly. Your customer who will be paying the AWS bill for all this asks you if he
being charged for all these instances. You try to explain to him how the billing works on EC2 instances to the
best of your knowledge. What would be an appropriate response to give to the customer in regards to this?
A. Billing commences when Amazon EC2 AM instance is completely up and billing ends as soon as the
instance starts to shutdown.
B. Billing only commences only after 1 hour of uptime and billing ends when the instance terminates.
C. Billing commences when Amazon EC2 initiates the boot sequence of an AM instance and billing ends when
the instance shuts down.
D. Billing commences when Amazon EC2 initiates the boot sequence of an AM instance and billing ends as
soon as the instance starts to shutdown.
Correct Answer: C
Explanation
Explanation/Reference:
Billing commences when Amazon EC2 initiates the boot sequence of an AM instance. Billing ends when the
instance shuts down, which could occur through a web services command, by running "shutdown -h", or
through instance failure.
http://aws.amazon.com/ec2/faqs/#BiIIing


QUESTION 66
You log in to IAM on your AWS console and notice the following message. "Delete your root access keys."
Why do you think IAM is requesting this?
A. Because the root access keys will expire as soon as you log out.
B. Because the root access keys expire after 1 week.
C. Because the root access keys are the same for all users.
D. Because they provide unrestricted access to your AWS resources.
Correct Answer: D
Explanation
Explanation/Reference:
In AWS an access key is required in order to sign requests that you make using the command-line interface
(CLI), using the AWS SDKs, or using direct API calls. Anyone who has the access key for your root account
has unrestricted access to all the resources in your account, including billing information. One of the best ways
to protect your account is to not have an access key for your root account. We recommend that unless you
must have a root access key (this is very rare), that you do not generate one. Instead, AWS best practice is to
create one or more AWS Identity and Access Management (IAM) users, give them the necessary permissions,
and use IAM users for everyday interaction with AWS.
http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.htmI#root-password


QUESTION 67
Once again your customers are concerned about the security of their sensitive data and with their latest
enquiry ask about what happens to old storage devices on AWS. What would be the best answer to this
question?
A. AWS reformats the disks and uses them again.
B. AWS uses the techniques detailed in DoD 5220.22-M to destroy data as part of the decommissioning
process.
C. AWS uses their own proprietary software to destroy data as part of the decommissioning process.
D. AWS uses a 3rd party security organization to destroy data as part of the decommissioning process.
Correct Answer: B
Explanation
Explanation/Reference:
When a storage device has reached the end of its useful life, AWS procedures include a decommissioning
process that is designed to prevent customer data from being exposed to unauthorized indMduals. AWS uses
the techniques detailed in DoD 5220.22-M ("Nationa| Industrial Security Program Operating ManuaI ") or NIST
800-88 ("GuideIines for Media Sanitization") to destroy data as part of the decommissioning process.
All decommissioned magnetic storage devices are degaussed and physically destroyed in accordance with
industry-standard practices.
http://d0.awsstatic.com/whitepapers/Security/AWS%20Security%20Whitepaper.pdf


QUESTION 68
Your company has been storing a lot of data in Amazon Glacier and has asked for an inventory of what is in
there exactly. So you have decided that you need to download a vault inventory. Which of the following
statements is inin relation to Vault Operations in Amazon Glacier?
A. You can use Amazon Simple Notification Service (Amazon SNS) notifications to notify you when the job
completes.
B. A vault inventory refers to the list of archives in a vault.
C. You can use Amazon Simple Queue Service (Amazon SQS) notifications to notify you when the job
completes.
D. Downloading a vault inventory is an asynchronous operation.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon Glacier supports various vault operations.
A vault inventory refers to the list of archives in a vault. For each archive in the list, the inventory provides
archive information such as archive ID, creation date, and size. Amazon Glacier updates the vault inventory
approximately once a day, starting on the day the first archive is uploaded to the vault. A vault inventory must
exist for you to be able to download it.
Downloading a vault inventory is an asynchronous operation. You must first initiate a job to download the
inventory. After receMng the job request, Amazon Glacier prepares your inventory for download. After the job
completes, you can download the inventory data.
Given the asynchronous nature of the job, you can use Amazon Simple Notification Service (Amazon SNS)
notifications to notify you when the job completes. You can specify an Amazon SNS topic for each indMdual
job request or configure your vault to send a notification when specific vault events occur. Amazon Glacier
prepares an inventory for each vault periodically, every 24 hours. If there have been no archive additions or
deletions to the vault since the last inventory, the inventory date is not updated. When you initiate a job for a
vault inventory, Amazon Glacier returns the last inventory it generated, which is a point-in-time snapshot and
not real-time data. You might not find it useful to retrieve vault inventory for each archive upload. However,
suppose you maintain a database on the client-side associating metadata about the archives you upload to
Amazon Glacier. Then, you might find the vault inventory useful to reconcile information in your database with
the actual vault inventory. http://docs.aws.amazon.com/amazongIacier/latest/dev/working-with-vaults.html


QUESTION 69
A customer enquires about whether all his data is secure on AWS and is especially concerned about Elastic
Map Reduce (EMR) so you need to inform him of some of the security features in place for AWS. Which of the
below statements would be an inresponse to your customers enquiry?
A. Amazon ENIR customers can choose to send data to Amazon S3 using the HTTPS protocol for secure
transmission.
B. Amazon S3 provides authentication mechanisms to ensure that stored data is secured against unauthorized
access.
C. Every packet sent in the AWS network uses Internet Protocol Security (IPsec).
D. Customers may encrypt the input data before they upload it to Amazon S3.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon S3 provides authentication mechanisms to ensure that stored data is secured against unauthorized
access. Unless the customer who is uploading the data specifies otherwise, only that customer can access the
data. Amazon EMR customers can also choose to send data to Amazon S3 using the HTTPS protocol for
secure transmission. In addition, Amazon EMR always uses HTTPS to send data between Amazon S3 and
Amazon EC2. For added security, customers may encrypt the input data before they upload it to Amazon S3
(using any common data compression tool); they then need to add a decryption step to the beginning of their
cluster when Amazon EMR fetches the data from Amazon S3.
https://aws.amazon.com/elasticmapreduce/faqs/


QUESTION 70
You are in the process of building an online gaming site for a client and one of the requirements is that it must
be able to process vast amounts of data easily. Which AWS Service would be very helpful in processing all this
data?
A. Amazon S3
B. AWS Data Pipeline
C. AWS Direct Connect
D. Amazon EMR
Correct Answer: D
Explanation
Explanation/Reference:
Managing and analyzing high data volumes produced by online games platforms can be difficult. The back-end
infrastructures of online games can be challenging to maintain and operate. Peak usage periods, multiple
players, and high volumes of write operations are some of the most common problems that operations teams
face.
Amazon Elastic MapReduce (Amazon EMR) is a service that processes vast amounts of data easily. Input data
can be retrieved from web server logs stored on Amazon S3 or from player data stored in Amazon DynamoDB
tables to run analytics on player behavior, usage patterns, etc. Those results can be stored again on Amazon
S3, or inserted in a relational database for further analysis with classic business intelligence tools. http://
media.amazonwebservices.com/architecturecenter/AWS_ac_ra_games_10.pdf


QUESTION 71
You need to change some settings on Amazon Relational Database Service but you do not want the database
to reboot immediately which you know might happen depending on the setting that you change. Which of the
following will cause an immediate DB instance reboot to occur?
A. You change storage type from standard to PIOPS, and Apply Immediately is set to true.
B. You change the DB instance class, and Apply Immediately is set to false.
C. You change a static parameter in a DB parameter group.
D. You change the backup retention period for a DB instance from 0 to a nonzero value or from a nonzero
value to 0, and Apply Immediately is set to false.
Correct Answer: A
Explanation
Explanation/Reference:
A DB instance outage can occur when a DB instance is rebooted, when the DB instance is put into a state that
prevents access to it, and when the database is restarted. A reboot can occur when you manually reboot your
DB instance or when you change a DB instance setting that requires a reboot before it can take effect. A DB
instance reboot occurs immediately when one of the following occurs:
You change the backup retention period for a DB instance from 0 to a nonzero value or from a nonzero value
to 0 and set Apply Immediately to true.
You change the DB instance class, and Apply Immediately is set to true. You change storage type from
standard to PIOPS, and Apply Immediately is set to true. A DB instance reboot occurs during the maintenance
window when one of the following occurs:
You change the backup retention period for a DB instance from 0 to a nonzero value or from a nonzero value
to 0, and Apply Immediately is set to false.
You change the DB instance class, and Apply Immediately is set to false.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Troub|eshooting.htm|#CHAP_TroubI
eshooting.Security


QUESTION 72
What does the following policy for Amazon EC2 do?
{
"Statement":[{
"Effect":"AI|ow",
"Action":"ec2:Describe*",
"Resource":"*"
II
}
A. Allow users to use actions that start with "Describe" over all the EC2 resources.
B. Share an AMI with a partner
C. Share an AMI within the account
D. Allow a group to only be able to describe, run, stop, start, and terminate instances
Correct Answer: A
Explanation
Explanation/Reference:
You can use IAM policies to control the actions that your users can perform against your EC2 resources. For
instance, a policy with the following statement will allow users to perform actions whose name start with
"Describe" against all your EC2 resources.
{
"Statement":[{
"Effect":"AI|ow",
"Action":"ec2:Describe*",
"Resource":"*"
}l
}
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/UsingIAM.htmI


QUESTION 73
You are setting up a very complex financial services grid and so far it has 5 Elastic IP (EIP) addresses. You go
to assign another EIP address, but all accounts are limited to 5 Elastic IP addresses per region by default, so
you aren't able to. What is the reason for this?
A. For security reasons.
B. Hardware restrictions.
C. Public (IPV4) internet addresses are a scarce resource.
D. There are only 5 network interfaces per instance.
Correct Answer: C
Explanation
Explanation/Reference:
Public (IPV4) internet addresses are a scarce resource. There is only a limited amount of public IP space
available, and Amazon EC2 is committed to helping use that space efficiently. By default, all accounts are
limited to 5 Elastic IP addresses per region. If you need more than 5 Elastic IP addresses, AWS asks that you
apply for your limit to be raised. They will ask you to think through your use case and help them understand
your need for additional addresses. http://aws.amazon.com/ec2/faqs/
#How_many_instances_can_I_run_in_Amazon_EC2


QUESTION 74
Amazon RDS provides high availability and failover support for DB instances using .
A. customized deployments
B. Appstream customizations
C. log events
D. MuIti-AZ deployments
Correct Answer: D
Explanation
Explanation/Reference:
Amazon RDS provides high availability and failover support for DB instances using MuIti-AZ deployments.
MuIti-AZ deployments for Oracle, PostgreSQL, MySQL, and MariaDB DB instances use Amazon technology,
while SQL Server DB instances use SQL Server Mrroring. http://docs.aws.amazon.com/AmazonRDS/latest/
UserGuide/Concepts.IV|u|tiAZ.htmI


QUESTION 75
A major customer has asked you to set up his AWS infrastructure so that it will be easy to recover in the case
of a disaster of some sort. Which of the following is important when thinking about being able to quickly launch
resources in AWS to ensure business continuity in case of a disaster?
A. Create and maintain AM|s of key sewers where fast recovery is required.
B. Regularly run your sewers, test them, and apply any software updates and configuration changes.
C. All items listed here are important when thinking about disaster recovery.
D. Ensure that you have all supporting custom software packages available in AWS.
Correct Answer: C
Explanation
Explanation/Reference:
In the event of a disaster to your AWS infrastructure you should be able to quickly launch resources in Amazon
Web Services (AWS) to ensure business continuity.
The following are some key steps you should have in place for preparation:
1. Set up Amazon EC2 instances to replicate or mirror data.
2. Ensure that you have all supporting custom software packages available in AWS.
3. Create and maintain AMIs of key servers where fast recovery is required.
4. Regularly run these servers, test them, and apply any software updates and configuration changes.
5. Consider automating the provisioning of AWS resources.
http://d36cz9buwru1tt.cIoudfront.net/AWS_Disaster_Recovery.pdf


QUESTION 76
What does Amazon DynamoDB provide?
A. A predictable and scalable MySQL database
B. A fast and reliable PL/SQL database cluster
C. A standalone Cassandra database, managed by Amazon Web Services
D. A fast, highly scalable managed NoSQL database service
Correct Answer: D
Explanation
Explanation/Reference:
Amazon DynamoDB is a managed NoSQL database service offered by Amazon. It automatically manages
tasks like scalability for you while it provides high availability and durability for your data, allowing you to
concentrate in other aspects of your application.
check link - https://aws.amazon.com/running_databases/


QUESTION 77
You want to use AWS Import/Export to send data from your S3 bucket to several of your branch offices. What
should you do if you want to send 10 storage units to AWS?
A. Make sure your disks are encrypted prior to shipping.
B. Make sure you format your disks prior to shipping.
C. Make sure your disks are 1TB or more.
D. Make sure you submit a separate job request for each device.
Correct Answer: D
Explanation
Explanation/Reference:
When using Amazon Import/Export, a separate job request needs to be submitted for each physical device
even if they belong to the same import or export job. http://docs.aws.amazon.com/AWSImportExport/latest/DG/
Concepts.html


QUESTION 78
What would be the best way to retrieve the public IP address of your EC2 instance using the CLI?
A. Using tags
B. Using traceroute
C. Using ipconfig
D. Using instance metadata
Correct Answer: D
Explanation
Explanation/Reference:
To determine your instance's public IP address from within the instance, you can use instance metadata. Use
the following command to access the public IP address: For Linux use, $ curl http://169.254.169.254/latest/
meta-data/public-ipv4, and for Windows use, $ wget http://169.254.169.254/latest/meta-data/public-ipv4. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.htm|


QUESTION 79
You need to measure the performance of your EBS volumes as they seem to be under performing. You have
come up with a measurement of 1,024 KB I/O but your colleague tells you that EBS volume performance is
measured in IOPS. How many IOPS is equal to 1,024 KB I/O?
A. 16
B. 256
C. 8
D. 4
Correct Answer: D
Explanation
Explanation/Reference:
Several factors can affect the performance of Amazon EBS volumes, such as instance configuration, I/O
characteristics, workload demand, and storage configuration. IOPS are input/output operations per second.
Amazon EBS measures each I/O operation per second (that is 256 KB or smaller) as one IOPS. I/O operations
that are larger than 256 KB are counted in 256 KB capacity units. For example, a 1,024 KB I/O operation would
count as 4 IOPS. When you provision a 4,000 IOPS volume and attach it to an EBS-optimized instance that
can provide the necessary bandwidth, you can transfer up to 4,000 chunks of data per second (provided that
the I/O does not exceed the 128 MB/s per volume throughput limit of General Purpose (SSD) and Provisioned
IOPS (SSD) volumes).
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.htmI


QUESTION 80
Having set up a website to automatically be redirected to a backup website if it fails, you realize that there are
different types of failovers that are possible. You need all your resources to be available the majority of the
time. Using Amazon Route 53 which configuration would best suit this requirement?
A. Active-active failover.
B. None. Route 53 can't failover.
C. Active-passive failover.
D. Active-active-passive and other mixed configurations.
Correct Answer: A
Explanation
Explanation/Reference:
You can set up a variety of failover configurations using Amazon Route 53 alias: weighted, latency, geolocation
routing, and failover resource record sets.
Active-active failover: Use this failover configuration when you want all of your resources to be available the
majority of the time. When a resource becomes unavailable, Amazon Route 53 can detect that it's unhealthy
and stop including it when responding to queries. Active-passive failover: Use this failover configuration when
you want a primary group of resources to be available the majority of the time and you want a secondary group
of resources to be on standby in case all of the primary resources become unavailable. When responding to
queries, Amazon Route 53 includes only the healthy primary resources. If all of the primary resources are
unhealthy, Amazon Route 53 begins to include only the healthy secondary resources in response to DNS
queries. Active-active-passive and other mixed configurations: You can combine alias and non-alias resource
record sets to produce a variety of Amazon Route 53 behaviors. http://docs.aws.amazon.com/Route53/Iatest/
DeveIoperGuide/dns-failover.html


QUESTION 81
AWS CIoudFormation is a service that helps you model and set up your Amazon Web Services resources so
that you can spend less time managing those resources and more time focusing on your applications that run
in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2
instances or Amazon RDS DB instances), and AWS CIoudFormation takes care of provisioning and
configuring those resources for you. What formatting is required for this template?
A. JSON-formatted document
B. CSS-formatted document
C. XML-formatted document
D. HTML-formatted document
Correct Answer: A
Explanation
Explanation/Reference:
You can write an AWS CIoudFormation template (a JSON-formatted document) in a text editor or pick an
existing template. The template describes the resources you want and their settings. For example, suppose
you want to create an Amazon EC2. Your template can declare an instance Amazon EC2 and describe its
properties, as shown in the following example:
{
"AWSTemp|ateFormatVersion" :
"2010-09-O9",
"Description" : "A simple Amazon EC2 instance",
"Resources" : {
"MyEC2Instance" : {
"Type" : "AWS::EC2::Instance",
"Properties" : {
"Image|d" : "ami-2f726546",
"|nstanceType" : "t1.micro"
}}}}
http://docs.aws.amazon.com/AWSCIoudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html


QUESTION 82
True or False: In Amazon Route 53, you can create a hosted zone for a top-level domain (TLD).
A. FALSE
B. False, Amazon Route 53 automatically creates it for you.
C. True, only if you send an XML document with a CreateHostedZoneRequest element for TLD.
D. TRUE
Correct Answer: A
Explanation
Explanation/Reference:
In Amazon Route 53, you cannot create a hosted zone for a top-level domain (TLD). http://
docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.htmI


QUESTION 83
You decide that you need to create a number of Auto Scaling groups to try and save some money as you have
noticed that at certain times most of your EC2 instances are not being used. By default, what is the maximum
number of Auto Scaling groups that AWS will allow you to create?
A. 12
B. Unlimited
C. 20
D. 2
Correct Answer: C
Explanation
Explanation/Reference:
Auto Scaling is an AWS service that allows you to increase or decrease the number of EC2 instances within
your appIication's architecture. With Auto Scaling, you create collections of EC2 instances, called Auto Scaling
groups. You can create these groups from scratch, or from existing EC2 instances that are already in
production.
http://docs.aws.amazon.com/general/latest/gr/aws_service_|imits.htm|#Iimits_autoscaIing


QUESTION 84
A user needs to run a batch process which runs for 10 minutes. This will only be run once, or at maximum
twice, in the next month, so the processes will be temporary only. The process needs 15 X-Large instances.
The process downloads the code from S3 on each instance when it is launched, and then generates a
temporary log file. Once the instance is terminated, all the data will be lost. Which of the below mentioned
pricing models should the user choose in this case?
A. Spot instance.
B. Reserved instance.
C. On-demand instance.
D. EBS optimized instance.
Correct Answer: A
Explanation
Explanation/Reference:
In Amazon Web Services, the spot instance is useful when the user wants to run a process temporarily. The
spot instance can terminate the instance if the other user outbids the existing bid. In this case all storage is
temporary and the data is not required to be persistent. Thus, the spot instance is a good option to save
money.
http://aws.amazon.com/ec2/purchasing-options/spot-instances/


QUESTION 85
Which of the following is NOT a characteristic of Amazon Elastic Compute Cloud (Amazon EC2)?
A. It can be used to launch as many or as few virtual servers as you need.
B. It increases the need to forecast traffic by providing dynamic IP addresses for static cloud computing.
C. It eliminates your need to invest in hardware up front, so you can develop and deploy applications faster.
D. It offers scalable computing capacity in the Amazon Web Services (AWS) cloud.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web
Services (AWS) cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can
develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers
as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or
down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html


QUESTION 86
You have been storing massive amounts of data on Amazon Glacier for the past 2 years and now start to
wonder if there are any limitations on this. What is the answer to your question?
A. The total volume of data is limited but the number of archives you can store are unlimited.
B. The total volume of data is unlimited but the number of archives you can store are limited.
C. The total volume of data and number of archives you can store are unlimited.
D. The total volume of data is limited and the number of archives you can store are limited.
Correct Answer: C
Explanation
Explanation/Reference:
An archive is a durably stored block of information. You store your data in Amazon Glacier as archives. You
may upload a single file as an archive, but your costs will be lower if you aggregate your data. TAR and ZIP are
common formats that customers use to aggregate multiple files into a single file before uploading to Amazon
Glacier.
The total volume of data and number of archives you can store are unlimited. IndMdual Amazon Glacier
archives can range in size from 1 byte to 40 terabytes.
The largest archive that can be uploaded in a single upload request is 4 gigabytes. For items larger than 100
megabytes, customers should consider using the MuItipart upload capability. Archives stored in Amazon
Glacier are immutable, i.e. archives can be uploaded and deleted but cannot be edited or overwritten.
https://aws.amazon.com/gIacier/faqs/


QUESTION 87
You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) so you decide to use the VPC wizard
in the AWS console to help make it easier for you. Which of the following statements is regarding instances
that you launch into a default subnet via the VPC wizard?
A. Instances that you launch into a default subnet receive a public IP address and 10 private IP addresses.
B. Instances that you launch into a default subnet receive both a public IP address and a private IP address.
C. Instances that you launch into a default subnet don't receive any ip addresses and you need to define them
manually.
D. Instances that you launch into a default subnet receive a public IP address and 5 private IP addresses.
Correct Answer: B
Explanation
Explanation/Reference:
Instances that you launch into a default subnet receive both a public IP address and a private IP address.
Instances in a default subnet also receive both public and private DNS hostnames. Instances that you launch
into a nondefault subnet in a default VPC don't receive a public IP address or a DNS hostname. You can
change your subnet's default public IP addressing behavior. http://docs.aws.amazon.com/AmazonVPC/latest/
UserGuide/default-vpc.html


QUESTION 88
A user has configured ELB with two EBS backed EC2 instances. The user is trying to understand the DNS
access and IP support for ELB. Which of the below mentioned statements may not help the user understand
the IP mechanism supported by ELB?
A. The client can connect over IPV4 or IPV6 using Dualstack
B. Communication between the load balancer and back-end instances is always through IPV4
C. ELB DNS supports both IPV4 and IPV6
D. The ELB supports either IPV4 or IPV6 but not both
Correct Answer: D
Explanation
Explanation/Reference:
Elastic Load Balancing supports both Internet Protocol version 6 (IPv6) and Internet Protocol version 4 (IPv4).
Clients can connect to the user's load balancer using either IPv4 or IPv6 (in EC2-Classic) DNS. However,
communication between the load balancer and its back-end instances uses only IPv4. The user can use the
Dualstack-prefixed DNS name to enable IPv6 support for communications between the client and the load
balancers. Thus, the clients are able to access the load balancer using either IPv4 or IPv6 as their indMdual
connectMty needs dictate.
http://docs.aws.amazon.com/EIasticLoadBaIancing/latest/DeveIoperGuide/UserScenariosForEC2.html


QUESTION 89
Does AWS CIoudFormation support Amazon EC2 tagging?
A. Yes, AWS CIoudFormation supports Amazon EC2 tagging
B. No, CIoudFormation doesn't support any tagging
C. No, it doesn't support Amazon EC2 tagging.
D. It depends if the Amazon EC2 tagging has been defined in the template.
Correct Answer: A
Explanation
Explanation/Reference:
In AWS CIoudFormation, Amazon EC2 resources that support the tagging feature can also be tagged in an
AWS template. The tag values can refer to template parameters, other resource names, resource attribute
values (e.g. addresses), or values computed by simple functions (e.g., a concatenated list of strings).
http://aws.amazon.com/c|oudformation/faqs/


QUESTION 90
An existing client comes to you and says that he has heard that launching instances into a VPC (virtual private
cloud) is a better strategy than launching instances into a EC2-classic which he knows is what you currently
do. You suspect that he is and he has asked you to do some research about this and get back to him. Which of
the following statements is true in regards to what ability launching your instances into a VPC instead of EC2-
Classic gives you?
A. All of the things listed here.
B. Change security group membership for your instances while they're running
C. Assign static private IP addresses to your instances that persist across starts and stops
D. Define network interfaces, and attach one or more network interfaces to your instances
Correct Answer: A
Explanation
Explanation/Reference:
By launching your instances into a VPC instead of EC2-Classic, you gain the ability to:
Assign static private IP addresses to your instances that persist across starts and stops Assign multiple IP
addresses to your instances
Define network interfaces, and attach one or more network interfaces to your instances Change security group
membership for your instances while they're running Control the outbound traffic from your instances (egress
filtering) in addition to controlling the inbound traffic to them (ingress filtering) Add an additional layer of access
control to your instances in the form of network access control lists (ACL) Run your instances on single-tenant
hardware
http://media.amazonwebservices.com/AWS_CIoud_Best_Practices.pdf


QUESTION 91
Amazon S3 allows you to set per-file permissions to grant read and/or write access. However you have
decided that you want an entire bucket with 100 files already in it to be accessible to the public. You don't want
to go through 100 files indMdually and set permissions. What would be the best way to do this?
A. Move the bucket to a new region
B. Add a bucket policy to the bucket.
C. Move the files to a new bucket.
D. Use Amazon EBS instead of S3
Correct Answer: B
Explanation
Explanation/Reference:
Amazon S3 supports several mechanisms that give you filexibility to control who can access your data as well
as how, when, and where they can access it. Amazon S3 provides four different access control mechanisms:
AWS Identity and Access Management (IAM) policies, Access Control Lists (ACLs), bucket policies, and query
string authentication. IAM enables organizations to create and manage multiple users under a single AWS
account. With IAM policies, you can grant IAM users fine-grained control to your Amazon S3 bucket or objects.
You can use ACLs to selectively add (grant) certain permissions on indMdual objects. Amazon S3 bucket
policies can be used to add or deny permissions across some or all of the objects within a single bucket.
With Query string authentication, you have the ability to share Amazon S3 objects through URLs that are valid
for a specified period of time.
http://aws.amazon.com/s3/detai|s/#security


QUESTION 92
A user is accessing an EC2 instance on the SSH port for IP 10.20.30.40. Which one is a secure way to
configure that the instance can be accessed only from this IP?
A. In the security group, open port 22 for IP 10.20.30.40
B. In the security group, open port 22 for IP 10.20.30.40/32
C. In the security group, open port 22 for IP 10.20.30.40/24
D. In the security group, open port 22 for IP 10.20.30.40/0
Correct Answer: B
Explanation
Explanation/Reference:
In AWS EC2, while configuring a security group, the user needs to specify the IP address in CIDR notation.
The CIDR IP range 10.20.30.40/32 says it is for a single IP 10.20.30.40. If the user specifies the IP as
10.20.30.40 only, the security group will not accept and ask it in a CIRD format. http://docs.aws.amazon.com/
AWSEC2/latest/UserGuide/using-network-security.html


QUESTION 93
Which of the following statements is true of creating a launch configuration using an EC2 instance?
A. The launch configuration can be created only using the Query APIs.
B. Auto Scaling automatically creates a launch configuration directly from an EC2 instance.
C. A user should manually create a launch configuration before creating an Auto Scaling group.
D. The launch configuration should be created manually from the AWS CLI.
Correct Answer: B
Explanation
Explanation/Reference:
You can create an Auto Scaling group directly from an EC2 instance. When you use this feature, Auto Scaling
automatically creates a launch configuration for you as well.
http://docs.aws.amazon.com/AutoScaling/latest/DeveIoperGuide/create-Ic-with-instancelD.htmI


QUESTION 94
You need to set up a high level of security for an Amazon Relational Database Service (RDS) you have just
built in order to protect the confidential information stored in it. What are all the possible security groups that
RDS uses?
A. DB security groups, VPC security groups, and EC2 security groups.
B. DB security groups only.
C. EC2 security groups only.
D. VPC security groups, and EC2 security groups.
Correct Answer: A
Explanation
Explanation/Reference:
A security group controls the access to a DB instance. It does so by allowing access to IP address ranges or
Amazon EC2 instances that you specify.
Amazon RDS uses DB security groups, VPC security groups, and EC2 security groups. In simple terms, a DB
security group controls access to a DB instance that is not in a VPC, a VPC security group controls access to a
DB instance inside a VPC, and an Amazon EC2 security group controls access to an EC2 instance and can be
used with a DB instance.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html


QUESTION 95
You have been using T2 instances as your CPU requirements have not been that intensive. However you now
start to think about larger instance types and start looking at M and IV|3 instances. You are a little confused as
to the differences between them as they both seem to have the same ratio of CPU and memory. Which
statement below is inas to why you would use one over the other?
A. M3 instances are less expensive than M1 instances.
B. IV|3 instances are configured with more swap memory than M instances.
C. IV|3 instances provide better, more consistent performance that M instances for most use-cases.
D. M3 instances also offer SSD-based instance storage that delivers higher I/O performance.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon EC2 allows you to set up and configure everything about your instances from your operating system
up to your applications. An Amazon Nlachine Image (AMI) is simply a packaged-up environment that includes
all the necessary bits to set up and boot your instance. M1 and M3 Standard instances have the same ratio of
CPU and memory, some reasons below as to why you would use one over the other. IV|3 instances provide
better, more consistent performance that M instances for most use-cases. M3 instances also offer SSD-based
instance storage that delivers higher I/O performance. M3 instances are also less expensive than M1
instances. Due to these reasons, we recommend M3 for applications that require general purpose instances
with a balance of compute, memory, and network resources. However, if you need more disk storage than
what is provided in M3 instances, you may still find M1 instances useful for running your applications.
https://aws.amazon.com/ec2/faqs/


QUESTION 96
You have set up an Elastic Load Balancer (ELB) with the usual default settings, which route each request
independently to the application instance with the smallest load. However, someone has asked you to bind a
user's session to a specific application instance so as to ensure that all requests coming from the user during
the session will be sent to the same application instance. AWS has a feature to do this. What is it called?
A. Connection draining
B. Proxy protocol
C. Tagging
D. Sticky session
Correct Answer: D
Explanation
Explanation/Reference:
An Elastic Load BaIancer(ELB) by default, routes each request independently to the application instance with
the smallest load. However, you can use the sticky session feature (also known as session affinity), which
enables the load balancer to bind a user's session to a specific application instance. This ensures that all
requests coming from the user during the session will be sent to the same application instance. The key to
managing the sticky session is determining how long your load balancer should consistently route the user's
request to the same application instance. If your application has its own session cookie, then you can set
Elastic Load Balancing to create the session cookie to follow the duration specified by the appIication's session
cookie. If your application does not have its own session cookie, then you can set Elastic Load Balancing to
create a session cookie by specifying your own stickiness duration. You can associate stickiness duration for
only HTTP/HTTPS load balancer listeners. An application instance must always receive and send two cookies:
A cookie that defines the stickiness duration and a special Elastic Load Balancing cookie named AWSELB,
that has the mapping to the application instance.
http://docs.aws.amazon.com/E|asticLoadBaIancing/latest/DeveIoperGuide/TerminoIogyandKeyConcepts.
htmI#session-stickiness


QUESTION 97
A user wants to achieve High Availability with PostgreSQL DB. Which of the below mentioned functionalities
helps achieve HA?
A. Mu|ti AZ
B. Read Replica
C. Multi region
D. PostgreSQL does not support HA
Correct Answer: A
Explanation
Explanation/Reference:
The Multi AZ feature allows the user to achieve High Availability. For Multi AZ, Amazon RDS automatically
provisions and maintains a synchronous "standby" replica in a different Availability Zone. http://
docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html


QUESTION 98
A user has created an application which will be hosted on EC2. The application makes calls to DynamoDB to
fetch certain data. The application is using the DynamoDB SDK to connect with from the EC2 instance. Which
of the below mentioned statements is true with respect to the best practice for security in this scenario?
A. The user should create an IAM user with DynamoDB access and use its credentials within the application to
connect with DynamoDB
B. The user should attach an IAM role with DynamoDB access to the EC2 instance
C. The user should create an IAM role, which has EC2 access so that it will allow deploying the application
D. The user should create an IAM user with DynamoDB and EC2 access. Attach the user with the application
so that it does not use the root account credentials
Correct Answer: B
Explanation
Explanation/Reference:
With AWS IAM a user is creating an application which runs on an EC2 instance and makes requests to AWS,
such as DynamoDB or S3 calls. Here it is recommended that the user should not create an IAM user and pass
the user's credentials to the application or embed those credentials inside the application. Instead, the user
should use roles for EC2 and give that role access to DynamoDB /S3. When the roles are attached to EC2, it
will give temporary security credentials to the application hosted on that EC2, to connect with DynamoDB / S3.
http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.htmI


QUESTION 99
After setting up several database instances in Amazon Relational Database Service (Amazon RDS) you decide
that you need to track the performance and health of your databases. How can you do this?
A. Subscribe to Amazon RDS events to be notified when changes occur with a DB instance, DB snapshot, DB
parameter group, or DB security group.
B. Use the free Amazon CIoudWatch service to monitor the performance and health of a DB instance.
C. All of the items listed will track the performance and health of a database.
D. View, download, or watch database log files using the Amazon RDS console or Amazon RDS APIs.
You can also query some database log files that are loaded into database tables.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate,
and scale a relational database in the cloud. It provides cost-efficient, resizeable capacity for an industrystandard
relational database and manages common database administration tasks. There are several ways
you can track the performance and health of a database or a DB instance. You can:
Use the free Amazon CIoudWatch service to monitor the performance and health of a DB instance. Subscribe
to Amazon RDS events to be notified when changes occur with a DB instance, DB snapshot, DB parameter
group, or DB security group.
View, download, or watch database log files using the Amazon RDS console or Amazon RDS APIs. You can
also query some database log files that are loaded into database tables. Use the AWS CIoudTraiI service to
record AWS calls made by your AWS account. The calls are recorded in log files and stored in an Amazon S3
bucket.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.htmI


QUESTION 100
You are building a system to distribute confidential documents to employees. Using CIoudFront, what method
could be used to serve content that is stored in S3, but not publically accessible from S3 directly?
A. Add the CIoudFront account security group "amazon-cf/amazon-cf-sg" to the appropriate S3 bucket policy.
B. Create a S3 bucket policy that lists the C|oudFront distribution ID as the Principal and the target bucket as
the Amazon Resource Name (ARN).
C. Create an Identity and Access Management (IAM) User for CIoudFront and grant access to the objects in
your S3 bucket to that IAM User.
D. Create an Origin Access Identity (OAI) for CIoudFront and grant access to the objects in your S3 bucket to
that OAI.
Correct Answer: D
Explanation
Explanation/Reference:
You restrict access to Amazon S3 content by creating an origin access identity, which is a special CIoudFront
user. You change Amazon S3 permissions to give the origin access identity permission to access your objects,
and to remove permissions from everyone else. When your users access your Amazon S3 objects using
CIoudFront URLs, the CIoudFront origin access identity gets the objects on your users' behalf. If your users try
to access objects using Amazon S3 URLs, they're denied access. The origin access identity has permission to
access objects in your Amazon S3 bucket, but users don't.
http://docs.aws.amazon.com/AmazonCIoudFront/latest/Deve|operGuide/private-content-restricting-acces s-tos3.
htmI


QUESTION 101
A user has attached 1 EBS volume to a VPC instance. The user wants to achieve the best fault tolerance of
data possible. Which of the below mentioned options can help achieve fault tolerance?
A. Attach one more volume with RAID 1 configuration.
B. Attach one more volume with RAID 0 configuration.
C. Connect multiple volumes and stripe them with RAID 6 configuration.
D. Use the EBS volume as a root device.
Correct Answer: A
Explanation
Explanation/Reference:
The user can join multiple provisioned IOPS volumes together in a RAID 1 configuration to achieve better fault
tolerance. RAID 1 does not provide a write performance improvement; it requires more bandwidth than non-
RAID configurations since the data is written simultaneously to multiple volumes. http://docs.aws.amazon.com/
AWSEC2/latest/UserGuide/raid-config.html


QUESTION 102
A user has created a subnet in VPC and launched an EC2 instance within it. The user has not selected the
option to assign the IP address while launching the instance. The user has 3 elastic IPs and is trying to assign
one of the Elastic IPs to the VPC instance from the console. The console does not show any instance in the IP
assignment screen. What is a possible reason that the instance is unavailable in the assigned IP console?
A. The IP address may be attached to one of the instances
B. The IP address belongs to a different zone than the subnet zone
C. The user has not created an internet gateway
D. The IP addresses belong to EC2 Classic; so they cannot be assigned to VPC
Correct Answer: D
Explanation
Explanation/Reference:
A Virtual Private Cloud (VPC) is a virtual network dedicated to the user's AWS account. A user can create a
subnet with VPC and launch instances inside that subnet. When the user is launching an instance he needs to
select an option which attaches a public IP to the instance. If the user has not selected the option to attach the
public IP then it will only have a private IP when launched. If the user wants to connect to an instance from the
internet he should create an elastic IP with VPC. If the elastic IP is a part of EC2 Classic it cannot be assigned
to a VPC instance.
http://docs.aws.amazon.com/AmazonVPC/Iatest/GettingStartedGuide/LaunchInstance.htmI


QUESTION 103
A user is aware that a huge download is occurring on his instance. He has already set the Auto Scaling policy
to increase the instance count when the network I/O increases beyond a certain limit. How can the user ensure
that this temporary event does not result in scaling?
A. The network I/O are not affected during data download
B. The policy cannot be set on the network I/O
C. There is no way the user can stop scaling as it is already configured
D. Suspend scaling
Correct Answer: D
Explanation
Explanation/Reference:
The user may want to stop the automated scaling processes on the Auto Scaling groups either to perform
manual operations or during emergency situations. To perform this, the user can suspend one or more scaling
processes at any time. Once it is completed, the user can resume all the suspended processes. http://
docs.aws.amazon.com/AutoScaIing/latest/Deve|operGuide/AS_Concepts.htmI


QUESTION 104
Select a true statement about Amazon EC2 Security Groups (EC2-Classic).
A. After you launch an instance in EC2-Classic, you can't change its security groups.
B. After you launch an instance in EC2-Classic, you can change its security groups only once.
C. After you launch an instance in EC2-Classic, you can only add rules to a security group.
D. After you launch an instance in EC2-Classic, you cannot add or remove rules from a security group.
Correct Answer: A
Explanation
Explanation/Reference:
After you launch an instance in EC2-Classic, you can't change its security groups. However, you can add rules
to or remove rules from a security group, and those changes are automatically applied to all instances that are
associated with the security group.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-network-security.html


QUESTION 105
A user has created photo editing software and hosted it on EC2. The software accepts requests from the user
about the photo format and resolution and sends a message to S3 to enhance the picture accordingly. Which
of the below mentioned AWS services will help make a scalable software with the AWS infrastructure in this
scenario?
A. AWS Simple Notification Service
B. AWS Simple Queue Service
C. AWS Elastic Transcoder
D. AWS Glacier
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Simple Queue Service (SQS) is a fast, reliable, scalable, and fully managed message queuing
service. SQS provides a simple and cost-effective way to decouple the components of an application. The user
can configure SQS, which will decouple the call between the EC2 application and S3. Thus, the application
does not keep waiting for S3 to provide the data.
http://aws.amazon.com/sqs/faqs/


QUESTION 106
Which one of the following answers is not a possible state of Amazon CIoudWatch Alarm?
A. INSUFFICIENT_DATA
B. ALARM
C. OK
D. STATUS_CHECK_FAILED
Correct Answer: D
Explanation
Explanation/Reference:
Amazon CIoudWatch Alarms have three possible states:
OK: The metric is within the defined threshold
ALARM: The metric is outside of the defined threshold
INSUFFICIENT_DATA: The alarm has just started, the metric is not available, or not enough data is available
for the metric to determine the alarm state
http://docs.aws.amazon.com/AmazonCIoudWatch/latest/DeveloperGuide/AlarmThatSendsEmaiI.html


QUESTION 107
An accountant asks you to design a small VPC network for him and, due to the nature of his business, just
needs something where the workload on the network will be low, and dynamic data will be accessed
infrequently. Being an accountant, low cost is also a major factor. Which EBS volume type would best suit his
requirements?
A. Magnetic
B. Any, as they all perform the same and cost the same.
C. General Purpose (SSD)
D. Magnetic or Provisioned IOPS (SSD)
Correct Answer: A
Explanation
Explanation/Reference:
You can choose between three EBS volume types to best meet the needs of their workloads: General Purpose
(SSD), Provisioned IOPS (SSD), and Magnetic. General Purpose (SSD) is the new, SSD-backed, general
purpose EBS volume type that we recommend as the default choice for customers. General Purpose (SSD)
volumes are suitable for a broad range of workloads, including small to medium sized databases, development
and test environments, and boot volumes. Provisioned IOPS (SSD) volumes offer storage with consistent and
low-latency performance, and are designed for I/O intensive applications such as large relational or NoSQL
databases. Magnetic volumes provide the lowest cost per gigabyte of all EBS volume types. Magnetic volumes
are ideal for workloads where data is accessed infrequently, and applications where the lowest storage cost is
important.
https://aws.amazon.com/ec2/faqs/


QUESTION 108
A user is planning to launch a scalable web application. Which of the below mentioned options will not affect
the latency of the application?
A. Region.
B. Provisioned IOPS.
C. Availability Zone.
D. Instance size.
Correct Answer: C
Explanation
Explanation/Reference:
In AWS, the instance size decides the I/O characteristics. The provisioned IOPS ensures higher throughput,
and lower latency. The region does affect the latency; latency will always be less when the instance is near to
the end user. Within a region the user uses any AZ and this does not affect the latency.
The AZ is mainly for fault toleration or HA.
http://media.amazonwebservices.com/AWS_Security_Best_Practices.pdf


QUESTION 109
Which of the following strategies can be used to control access to your Amazon EC2 instances?
A. DB security groups
B. IAM policies
C. None of these
D. EC2 security groups
Correct Answer: D
Explanation
Explanation/Reference:
IAM policies allow you to specify what actions your IAM users are allowed to perform against your EC2
Instances. However, when it comes to access control, security groups are what you need in order to define and
control the way you want your instances to be accessed, and whether or not certain kind of communications
are allowed or not.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/UsingIAM.htmI


QUESTION 110
A user has launched one EC2 instance in the US East region and one in the US West region. The user has
launched an RDS instance in the US East region. How can the user configure access from both the EC2
instances to RDS?
A. It is not possible to access RDS of the US East region from the US West region
B. Configure the US West region's security group to allow a request from the US East region's instance and
configure the RDS security group's ingress rule for the US East EC2 group
C. Configure the security group of the US East region to allow traffic from the US West region's instance and
configure the RDS security group's ingress rule for the US East EC2 group
D. Configure the security group of both instances in the ingress rule of the RDS security group
Correct Answer: C
Explanation
Explanation/Reference:
The user cannot authorize an Amazon EC2 security group if it is in a different AWS Region than the RDS DB
instance. The user can authorize an IP range or specify an Amazon EC2 security group in the same region that
refers to an IP address in another region. In this case allow IP of US West inside US East's security group and
open the RDS security group for US East region.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html


QUESTION 111
In Amazon EC2, if your EBS volume stays in the detaching state, you can force the detachment by clicking .
A. Force Detach
B. Detach Instance
C. AttachVoIume
D. Attachlnstance
Correct Answer: A
Explanation
Explanation/Reference:
If your volume stays in the detaching state, you can force the detachment by clicking Force Detach. http://
docs.amazonwebservices.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html


QUESTION 112
Do you need to shutdown your EC2 instance when you create a snapshot of EBS volumes that serve as root
devices?
A. No, you only need to shutdown an instance before deleting it.
B. Yes
C. No, the snapshot would turn off your instance automatically.
D. No
Correct Answer: B
Explanation
Explanation/Reference:
Yes, to create a snapshot for Amazon EBS volumes that serve as root devices, you should stop the instance
before taking the snapshot.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html


QUESTION 113
An organization has a statutory requirement to protect the data at rest for data stored in EBS volumes. Which
of the below mentioned options can the organization use to achieve data protection?
A. Data replication.
B. Data encryption.
C. Data snapshot.
D. All the options listed here.
Correct Answer: D
Explanation
Explanation/Reference:
For protecting the Amazon EBS data at REST, the user can use options, such as Data Encryption (Windows /
Linux / third party based), Data Replication (AWS internally replicates data for redundancy), and Data
Snapshot (for point in time backup).
http://media.amazonwebservices.com/AWS_Security_Best_Practices.pdf


QUESTION 114
A client of yours has a huge amount of data stored on Amazon S3, but is concerned about someone stealing it
while it is in transit. You know that all data is encrypted in transit on AWS, but which of the following is wrong
when describing server-side encryption on AWS?
A. Amazon S3 server-side encryption employs strong multi-factor encryption.
B. Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced
Encryption Standard (AES-256), to encrypt your data.
C. In server-side encryption, you manage encryption/decryption of your data, the encryption keys, and related
tools.
D. Server-side encryption is about data encryption at rest--that is, Amazon S3 encrypts your data as it writes it
to disks.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon S3 encrypts your object before saving it on disks in its data centers and decrypts it when you
download the objects. You have two options depending on how you choose to manage the encryption keys:
Server-side encryption and client-side encryption.
Server-side encryption is about data encryption at rest--that is, Amazon S3 encrypts your data as it writes it to
disks in its data centers and decrypts it for you when you access it. As long as you authenticate your request
and you have access permissions, there is no difference in the way you access encrypted or unencrypted
objects. Amazon S3 manages encryption and decryption for you. For example, if you share your objects using
a pre-signed URL, that URL works the same way for both encrypted and unencrypted objects. In client-side
encryption, you manage encryption/decryption of your data, the encryption keys, and related tools. Server-side
encryption is an alternative to client-side encryption in which Amazon S3 manages the encryption of your data,
freeing you from the tasks of managing encryption and encryption keys. Amazon S3 server-side encryption
employs strong multi-factor encryption. Amazon S3 encrypts each object with a unique key. As an additional
safeguard, it encrypts the key itself with a master key that it regularly rotates. Amazon S3 server-side
encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-
256), to encrypt your data. http://docs.aws.amazon.com/AmazonS3/Iatest/dev/
UsingServerSideEncryption.htmI


QUESTION 115
A user is running a batch process which runs for 1 hour every day. Which of the below mentioned options is
the right instance type and costing model in this case if the user performs the same task for the whole year?
A. EBS backed instance with on-demand instance pricing.
B. EBS backed instance with heavy utilized reserved instance pricing.
C. EBS backed instance with low utilized reserved instance pricing.
D. Instance store backed instance with spot instance pricing.
Correct Answer: A
Explanation
Explanation/Reference:
For Amazon Web Services, the reserved instance helps the user save money if the user is going to run the
same instance for a longer period. Generally if the user uses the instances around 30-40% annually it is
recommended to use RI. Here as the instance runs only for 1 hour daily it is not recommended to have RI as it
will be costlier. The user should use on-demand with EBS in this case. http://aws.amazon.com/ec2/purchasingoptions/
reserved-instances/


QUESTION 116
You have just set up a large site for a client which involved a huge database which you set up with Amazon
RDS to run as a Mu|ti-AZ deployment. You now start to worry about what will happen if the database instance
fails. Which statement best describes how this database will function if there is a database failure?
A. Updates to your DB Instance are synchronously replicated across Availability Zones to the standby in order
to keep both in sync and protect your latest database updates against DB Instance failure.
B. Your database will not resume operation without manual administrative intervention.
C. Updates to your DB Instance are asynchronously replicated across Availability Zones to the standby in order
to keep both in sync and protect your latest database updates against DB Instance failure.
D. Updates to your DB Instance are synchronously replicated across S3 to the standby in order to keep both in
sync and protect your latest database updates against DB Instance failure.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Relational Database Service (Amazon RDS) is a managed service that makes it easy to set up,
operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity, while
managing time-consuming database administration tasks, freeing you up to focus on your applications and
business.
When you create or modify your DB Instance to run as a MuIti-AZ deployment, Amazon RDS automatically
provisions and maintains a synchronous "standby" replica in a different Availability Zone. Updates to your DB
Instance are synchronously replicated across Availability Zones to the standby in order to keep both in sync
and protect your latest database updates against DB Instance failure. During certain types of planned
maintenance, or in the unlikely event of DB Instance failure or Availability Zone failure, Amazon RDS will
automatically failover to the standby so that you can resume database writes and reads as soon as the standby
is promoted. Since the name record for your DB Instance remains the same, you application can resume
database operation without the need for manual administrative intervention. With Mu|ti-AZ deployments,
replication is transparent: you do not interact directly with the standby, and it cannot be used to serve read
traffic. If you are using Amazon RDS for MySQL and are looking to scale read traffic beyond the capacity
constraints of a single DB Instance, you can deploy one or more Read Replicas.
http://aws.amazon.com/rds/faqs/


QUESTION 117
Which IAM role do you use to grant AWS Lambda permission to access a DynamoDB Stream?
A. Dynamic role
B. Invocation role
C. Execution role
D. Event Source role
Correct Answer: C
Explanation
Explanation/Reference:
You grant AWS Lambda permission to access a DynamoDB Stream using an IAM role known as the
"execution ro|e".
http://docs.aws.amazon.com/|ambda/latest/dg/intro-permission-model.htm|


QUESTION 118
Name the disk storage supported by Amazon Elastic Compute Cloud (EC2).
A. None of these
B. Amazon AppStream store
C. Amazon SNS store
D. Amazon Instance Store
Correct Answer: D
Explanation
Explanation/Reference:
Amazon EC2 supports the following storage options: Amazon Elastic Block Store (Amazon EBS) Amazon EC2
Instance Store Amazon Simple Storage Service (Amazon S3) http://docs.amazonwebservices.com/AWSEC2/
latest/UserGuide/Storage.html


QUESTION 119
You are signed in as root user on your account but there is an Amazon S3 bucket under your account that you
cannot access. What is a possible reason for this?
A. An IAM user assigned a bucket policy to an Amazon S3 bucket and didn't specify the root user as a principal
B. The S3 bucket is full.
C. The S3 bucket has reached the maximum number of objects allowed.
D. You are in the wrong availability zone
Correct Answer: A
Explanation
Explanation/Reference:
With IAM, you can centrally manage users, security credentials such as access keys, and permissions that
control which AWS resources users can access.
In some cases, you might have an IAM user with full access to IAM and Amazon S3. If the IAM user assigns a
bucket policy to an Amazon S3 bucket and doesn't specify the root user as a principal, the root user is denied
access to that bucket. However, as the root user, you can still access the bucket by modifying the bucket policy
to allow root user access.
http://docs.aws.amazon.com/IAM/latest/UserGuide/iam-troubleshooting.htmI#testing2


QUESTION 120
You have a number of image files to encode. In an Amazon SQS worker queue, you create an Amazon SQS
message for each file specifying the command (jpeg-encode) and the location of the file in Amazon S3. Which
of the following statements best describes the functionality of Amazon SQS?
A. Amazon SQS is a distributed queuing system that is optimized for horizontal scalability, not for singlethreaded
sending or receMng speeds.
B. Amazon SQS is for single-threaded sending or receMng speeds.
C. Amazon SQS is a non-distributed queuing system.
D. Amazon SQS is a distributed queuing system that is optimized for vertical scalability and for single-threaded
sending or receMng speeds.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon SQS is a distributed queuing system that is optimized for horizontal scalability, not for single-threaded
sending or receMng speeds. A single client can send or receive Amazon SQS messages at a rate of about 5 to
50 messages per second. Higher receive performance can be achieved by requesting multiple messages (up
to 10) in a single call. It may take several seconds before a message that has been to a queue is available to
be received.
http://media.amazonwebservices.com/AWS_Storage_Options.pdf


QUESTION 121
A user is observing the EC2 CPU utilization metric on CIoudWatch. The user has observed some interesting
patterns while filtering over the 1 week period for a particular hour. The user wants to zoom that data point to a
more granular period. How can the user do that easily with CIoudWatch?
A. The user can zoom a particular period by selecting that period with the mouse and then releasing the mouse
B. The user can zoom a particular period by specifying the aggregation data for that period
C. The user can zoom a particular period by double clicking on that period with the mouse
D. The user can zoom a particular period by specifying the period in the Time Range
Correct Answer: A
Explanation
Explanation/Reference:
Amazon CIoudWatch provides the functionality to graph the metric data generated either by the AWS services
or the custom metric to make it easier for the user to analyse. The AWS CIoudWatch console provides the
option to change the granularity of a graph and zoom in to see data over a shorter time period. To zoom, the
user has to click in the graph details pane, drag on the graph area for selection, and then release the mouse
button.
http://docs.aws.amazon.com/AmazonCloudWatch/Iatest/Deve|operGuide/zoom_in_on_graph.htmI


QUESTION 122
A scope has been handed to you to set up a super fast gaming server and you decide that you will use
Amazon DynamoDB as your database. For efficient access to data in a table, Amazon DynamoDB creates and
maintains indexes for the primary key attributes. A secondary index is a data structure that contains a subset of
attributes from a table, along with an alternate key to support Query operations. How many types of secondary
indexes does DynamoDB support?
A. 2
B. 16
C. 4
D. As many as you need.
Correct Answer: A
Explanation
Explanation/Reference:
DynamoDB supports two types of secondary indexes:
Local secondary index -- an index that has the same hash key as the table, but a different range key. A local
secondary index is "IocaI" in the sense that every partition of a local secondary index is scoped to a table
partition that has the same hash key.
Global secondary index -- an index with a hash and range key that can be different from those on the table. A
global secondary index is considered "gIobaI" because queries on the index can span all of the data in a table,
across all partitions.
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Secondarylndexes.html


QUESTION 123
Select the statement: Within Amazon EC2, when using Linux instances, the device name /dev/sda1 is .
A. reserved for EBS volumes
B. recommended for EBS volumes
C. recommended for instance store volumes
D. reserved for the root device
Correct Answer: D
Explanation
Explanation/Reference:
Within Amazon EC2, when using a Linux instance, the device name /dev/sda1 is reserved for the root device.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.htmI


QUESTION 124
The common use cases for DynamoDB Fine-Grained Access Control (FGAC) are cases in which the end user
wants .
A. to change the hash keys of the table directly
B. to check if an IAM policy requires the hash keys of the tables directly
C. to read or modify any codecommit key of the table directly, without a middle-tier service
D. to read or modify the table directly, without a middle-tier service
Correct Answer: D
Explanation
Explanation/Reference:
FGAC can benefit any application that tracks information in a DynamoDB table, where the end user (or
application client acting on behalf of an end user) wants to read or modify the table directly, without a middletier
service. For instance, a developer of a mobile app named Acme can use FGAC to track the top score of
every Acme user in a DynamoDB table. FGAC allows the application client to modify only the top score for the
user that is currently running the application.
http://aws.amazon.com/dynamodb/faqs/#security_anchor


QUESTION 125
A user has set up the CIoudWatch alarm on the CPU utilization metric at 50%, with a time interval of 5 minutes
and 10 periods to monitor. What will be the state of the alarm at the end of 90 minutes, if the CPU utilization is
constant at 80%?
A. ALERT
B. ALARM
C. OK
D. INSUFFICIENT_DATA
Correct Answer: B
Explanation
Explanation/Reference:
In this case the alarm watches a metric every 5 minutes for 10 intervals. Thus, it needs at least 50 minutes to
come to the "OK" state.
Till then it will be in the |NSUFFUCIENT_DATA state.
Since 90 minutes have passed and CPU utilization is at 80% constant, the state of alarm will be "ALARNI".
http://docs.aws.amazon.com/AmazonCIoudWatch/latest/DeveloperGuide/AlarmThatSendsEmaiI.html


QUESTION 126
You need to set up security for your VPC and you know that Amazon VPC provides two features that you can
use to increase security for your VPC: security groups and network access control lists (ACLs). You have
already looked into security groups and you are now trying to understand ACLs. Which statement below is inin
relation to ACLs?
A. Supports allow rules and deny rules.
B. Is stateful: Return traffic is automatically allowed, regardless of any rules.
C. Processes rules in number order when deciding whether to allow traffic.
D. Operates at the subnet level (second layer of defense).
Correct Answer: B
Explanation
Explanation/Reference:
Amazon VPC provides two features that you can use to increase security for your VPC:
Security groups--Act as a firewall for associated Amazon EC2 instances, controlling both inbound and
outbound traffic at the instance level
Network access control lists (ACLs)--Act as a firewall for associated subnets, controlling both inbound and
outbound traffic at the subnet level
Security groups are stateful: (Return traffic is automatically allowed, regardless of any rules) Network ACLs are
stateless: (Return traffic must be explicitly allowed by rules) http://docs.aws.amazon.com/AmazonVPC/latest/
UserGuide/VPC_Security.html


QUESTION 127
A user comes to you and wants access to Amazon CIoudWatch but only wants to monitor a specific
LoadBaIancer. Is it possible to give him access to a specific set of instances or a specific LoadBaIancer?
A. No because you can't use IAM to control access to CIoudWatch data for specific resources.
B. Yes. You can use IAM to control access to CIoudWatch data for specific resources.
C. No because you need to be Sysadmin to access CIoudWatch data.
D. Yes. Any user can see all CIoudWatch data and needs no access rights.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon CIoudWatch integrates with AWS Identity and Access Management (IAM) so that you can specify
which CIoudWatch actions a user in your AWS Account can perform. For example, you could create an IAM
policy that gives only certain users in your organization permission to use GetMetricStatistics. They could then
use the action to retrieve data about your cloud resources. You can't use IAM to control access to CIoudWatch
data for specific resources. For example, you can't give a user access to CIoudWatch data for only a specific
set of instances or a specific LoadBaIancer. Permissions granted using IAM cover all the cloud resources you
use with CIoudWatch. In addition, you can't use IAM roles with the Amazon CIoudWatch command line tools.
Using Amazon CIoudWatch with IAM doesn't change how you use CIoudWatch. There are no changes to
CIoudWatch actions, and no new CIoudWatch actions related to users and access control. http://
docs.aws.amazon.com/AmazonC|oudWatch/latest/DeveloperGuide/UsingIAM.htmI


QUESTION 128
A user is planning to make a mobile game which can be played online or offline and will be hosted on EC2.
The user wants to ensure that if someone breaks the highest score or they achieve some milestone they can
inform all their colleagues through email. Which of the below mentioned AWS services helps achieve this goal?
A. AWS Simple Workflow Service.
B. AWS Simple Email Service.
C. Amazon Cognito
D. AWS Simple Queue Service.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Simple Email Service (Amazon SES) is a highly scalable and cost-effective email-sending service for
businesses and developers. It integrates with other AWS services, making it easy to send emails from
applications that are hosted on AWS.
http://aws.amazon.com/ses/faqs/


QUESTION 129
You have multiple VPN connections and want to provide secure communication between sites using the AWS
VPN CIoudHub. Which statement is the most accurate in describing what you must do to set this up correctly?
A. Create a virtual private gateway with multiple customer gateways, each with unique Border Gateway
Protocol (BGP) Autonomous System Numbers (ASNs)
B. Create a virtual private gateway with multiple customer gateways, each with a unique set of keys
C. Create a virtual public gateway with multiple customer gateways, each with a unique Private subnet
D. Create a virtual private gateway with multiple customer gateways, each with unique subnet id
Correct Answer: A
Explanation
Explanation/Reference:
If you have multiple VPN connections, you can provide secure communication between sites using the AWS
VPN CIoudHub. The VPN CIoudHub operates on a simple hub-and-spoke model that you can use with or
without a VPC. This design is suitable for customers with multiple branch offices and existing Internet
connections who'd like to implement a convenient, potentially low-cost hub-and-spoke model for primary or
backup connectMty between these remote offices. To use the AWS VPN CIoudHub, you must create a virtual
private gateway with multiple customer gateways, each with unique Border Gateway Protocol (BGP)
Autonomous System Numbers (ASNs). Customer gateways advertise the appropriate routes (BGP prefixes)
over their VPN connections. These routing advertisements are received and re-advertised to each BGP peer,
enabling each site to send data to and receive data from the other sites. The routes for each spoke must have
unique ASNs and the sites must not have overlapping IP ranges. Each site can also send and receive data
from the VPC as if they were using a standard VPN connection. http://docs.aws.amazon.com/AmazonVPC/
latest/UserGuide/VPN_CIoudHub.htmI


QUESTION 130
You need to create an Amazon Machine Image (AM) for a customer for an application which does not appear
to be part of the standard AWS AM template that you can see in the AWS console. What are the alternative
possibilities for creating an AM on AWS?
A. You can purchase an AMs from a third party but cannot create your own AM.
B. You can purchase an AMIs from a third party or can create your own AMI.
C. Only AWS can create AMIs and you need to wait till it becomes available.
D. Only AWS can create AMIs and you need to request them to create one for you.
Correct Answer: B
Explanation
Explanation/Reference:
You can purchase an AMIs from a third party, including AMIs that come with service contracts from
organizations such as Red Hat. You can also create an AMI and sell it to other Amazon EC2 users. After you
create an AMI, you can keep it private so that only you can use it, or you can share it with a specified list of
AWS accounts. You can also make your custom AMI public so that the community can use it. Building a safe,
secure, usable AMI for public consumption is a fairly straightforward process, if you follow a few simple
guidelines.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.htm|


QUESTION 131
While creating an Amazon RDS DB, your first task is to set up a DB that controls which IP address or EC2
instance can access your DB Instance.
A. security token pool
B. security token
C. security pool
D. security group
Correct Answer: D
Explanation
Explanation/Reference:
While creating an Amazon RDS DB, your first task is to set up a DB Security Group that controls what IP
addresses or EC2 instances have access to your DB Instance.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html


QUESTION 132
Which one of the below is not an AWS Storage Service?
A. Amazon S3
B. Amazon Glacier
C. Amazon CIoudFront
D. Amazon EBS
Correct Answer: C
Explanation
Explanation/Reference:
AWS Storage Services are:
Amazon S3
Amazon Glacier
Amazon EBS
AWS Storage Gateway
https://consoIe.aws.amazon.com/console


QUESTION 133
You are very concerned about security on your network because you have multiple programmers testing APIs
and SDKs and you have no idea what is happening. You think C|oudTrai| may help but are not sure what it
does. Which of the following statements best describes the AWS service CIoudTraiI?
A. With AWS CIoudTraiI you can get a history of AWS API calls and related events for your account.
B. With AWS CIoudTraiI you can get a history of IAM users for your account.
C. With AWS CIoudTraiI you can get a history of S3 Iogfiles for your account.
D. With AWS CIoudTraiI you can get a history of CIoudFormation JSON scripts used for your account.
Correct Answer: A
Explanation
Explanation/Reference:
With AWS CIoudTraiI, you can get a history of AWS API calls for your account, including API calls made via
the AWS IV|anagement Console, the AWS SDKs, the command line tools, and higher-level AWS services. You
can also identify which users and accounts called AWS APIs for services that support CIoudTraiI, the source IP
address the calls were made from, and when the calls occurred. You can identify which users and accounts
called AWS for services that support CIoudTraiI, the source IP address the calls were made from, and when
the calls occurred. You can integrate CIoudTraiI into applications using the API, automate trail creation for your
organization, check the status of your trails, and control how administrators turn CIoudTraiI logging on and off.
http://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cIoud_traiI_top_IeveI.html


QUESTION 134
A user has deployed an application on his private cloud. The user is using his own monitoring tool. He wants to
configure it so that whenever there is an error, the monitoring tool will notify him via SMS. Which of the below
mentioned AWS services will help in this scenario?
A. AWS SES
B. AWS SNS
C. None because the user infrastructure is in the private cloud.
D. AWS SMS
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Simple Notification Service (Amazon SNS) is a fast, filexible, and fully managed push messaging
service. Amazon SNS can be used to make push notifications to mobile devices. Amazon SNS can deliver
notifications by SMS text message or email to the Amazon Simple Queue Service (SQS) queues or to any
HTTP endpoint. In this case user can use the SNS apis to send SMS.
http://aws.amazon.com/sns/


QUESTION 135
After setting up an EC2 security group with a cluster of 20 EC2 instances, you find an error in the security
group settings. You quickly make changes to the security group settings. When will the changes to the settings
be effective?
A. The settings will be effective immediately for all the instances in the security group.
B. The settings will be effective only when all the instances are restarted.
C. The settings will be effective for all the instances only after 30 minutes.
D. The settings will be effective only for the new instances added to the security group.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Redshift applies changes to a cluster security group immediately. So if you have associated the
cluster security group with a cluster, inbound cluster access rules in the updated cluster security group apply
immediately.
http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.htm|


QUESTION 136
Regarding Amazon Route 53, if your application is running on Amazon EC2 instances in two or more Amazon
EC2 regions and if you have more than one Amazon EC2 instance in one or more regions, you can use to
route traffic to the region and then use to route traffic to instances within the region, based on probabilities that
you specify.
A. weighted-based routing; alias resource record sets
B. latency-based routing; weighted resource record sets
C. weighted-based routing; weighted resource record sets
D. latency-based routing; alias resource record sets
Correct Answer: B
Explanation
Explanation/Reference:
Regarding Amazon Route 53, if your application is running on Amazon EC2 instances in two or more Amazon
EC2 regions, and if you have more than one Amazon EC2 instance in one or more regions, you can use
latency-based routing to route traffic to the region and then use weighted resource record sets to route traffic to
instances within the region based on weights that you specify. http://docs.aws.amazon.com/Route53/Iatest/
DeveIoperGuide/Tutorials.html


QUESTION 137
You have a lot of data stored in the AWS Storage Gateway and your manager has come to you asking about
how the billing is calculated, specifically the Virtual Tape Shelf usage. What would be a response to this?
A. You are billed for the virtual tape data you store in Amazon Glacier and are billed for the size of the virtual
tape.
B. You are billed for the virtual tape data you store in Amazon Glacier and billed for the portion of virtual tape
capacity that you use, not for the size of the virtual tape.
C. You are billed for the virtual tape data you store in Amazon S3 and billed for the portion of virtual tape
capacity that you use, not for the size of the virtual tape.
D. You are billed for the virtual tape data you store in Amazon S3 and are billed for the size of the virtual tape.
Correct Answer: B
Explanation
Explanation/Reference:
The AWS Storage Gateway is a service connecting an on-premises software appliance with cloud-based
storage to provide seamless and secure integration between an organization's on-premises IT environment
and AWS's storage infrastructure.
AWS Storage Gateway billing is as follows.
Volume storage usage (per GB per month):
You are billed for the Cached volume data you store in Amazon S3. You are only billed for volume capacity you
use, not for the size of the volume you create. Snapshot Storage usage (per GB per month): You are billed for
the snapshots your gateway stores in Amazon S3. These snapshots are stored and billed as Amazon EBS
snapshots. Snapshots are incremental backups, reducing your storage charges. When taking a new snapshot,
only the data that has changed since your last snapshot is stored.
Virtual Tape Library usage (per GB per month):
You are billed for the virtual tape data you store in Amazon S3. You are only billed for the portion of virtual tape
capacity that you use, not for the size of the virtual tape.
Virtual Tape Shelf usage (per GB per month):
You are billed for the virtual tape data you store in Amazon Glacier. You are only billed for the portion of virtual
tape capacity that you use, not for the size of the virtual tape.
https://aws.amazon.com/storagegateway/faqs/


QUESTION 138
You are configuring a new VPC for one of your clients for a cloud migration project, and only a public VPN will
be in place. After you created your VPC, you created a new subnet, a new internet gateway, and attached your
internet gateway to your VPC. When you launched your first instance into your VPC, you realized that you
aren't able to connect to the instance, even if it is configured with an elastic IP. What should be done to access
the instance?
A. A route should be created as 0.0.0.0/0 and your internet gateway as target.
B. Attach another ENI to the instance and connect via new ENI.
C. A NAT instance should be created and all traffic should be forwarded to NAT instance.
D. A NACL should be created that allows all outbound traffic.
Correct Answer: A
Explanation
Explanation/Reference:
All traffic should be routed via Internet Gateway. So, a route should be created with 0.0.0.0/0 as a source, and
your Internet Gateway as your target.
http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario1.htmI


QUESTION 139
A user is currently building a website which will require a large number of instances in six months, when a
demonstration of the new site will be given upon launch.
Which of the below mentioned options allows the user to procure the resources beforehand so that they need
not worry about infrastructure availability during the demonstration?
A. Procure all the instances as reserved instances beforehand.
B. Launch all the instances as part of the cluster group to ensure resource availability.
C. Pre-warm all the instances one month prior to ensure resource availability.
D. Ask AWS now to procure the dedicated instances in 6 months.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Web Services has massive hardware resources at its data centers, but they are finite. The best way
for users to maximize their access to these resources is by reserving a portion of the computing capacity that
they require. This can be done through reserved instances. With reserved instances, the user literally reserves
the computing capacity in the Amazon Web Services cloud. http://media.amazonwebservices.com/
AWS_Building_FauIt_To|erant_AppIications.pdf
QUESTION 140
You receive a bill from AWS but are confused because you see you are incurring different costs for the exact
same storage size in different regions on Amazon S3. You ask AWS why this is so. What response would you
expect to receive from AWS?
A. We charge less in different time zones.
B. We charge less where our costs are less.
C. This will balance out next bill.
D. It must be a mistake.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon S3 is storage for the internet. |t's a simple storage service that offers software developers a highlyscalable,
reliable, and low-latency data storage infrastructure at very low costs.
AWS charges less where their costs are less.
For example, their costs are lower in the US Standard Region than in the US West (Northern California)
Region.
https://aws.amazon.com/s3/faqs/
QUESTION 141
You are setting up some EBS volumes for a customer who has requested a setup which includes a RAID
(redundant array of inexpensive disks). AWS has some recommendations for RAID setups. Which RAID setup
is not recommended for Amazon EBS?
A. RAID 5 only
B. RAID 5 and RAID 6
C. RAID 1 only
D. RAID 1 and RAID 6
Correct Answer: B
Explanation
Explanation/Reference:
With Amazon EBS, you can use any of the standard RAID configurations that you can use with a traditional
bare metal server, as long as that particular RAID configuration is supported by the operating system for your
instance. This is because all RAID is accomplished at the software level. For greater I/O performance than you
can achieve with a single volume, RAID 0 can stripe multiple volumes together; for on-instance redundancy,
RAID 1 can mirror two volumes together. RAID 5 and RAID 6 are not recommended for Amazon EBS because
the parity write operations of these RAID modes consume some of the IOPS available to your volumes. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/raid-config.html
QUESTION 142
You receive the following request from a client to quickly deploy a static website for them, specifically on AWS.
The requirements are low-cost, reliable, online storage, and a reliable and cost-effective way to route
customers to the website, as well as a way to deliver content with low latency and high data transfer speeds so
that visitors to his website don't experience unnecessary delays. What do you think would be the minimum
AWS services that could fulfill the cIient's request?
A. Amazon Route 53, Amazon CIoudFront and Amazon VPC.
B. Amazon S3, Amazon Route 53 and Amazon RDS
C. Amazon S3, Amazon Route 53 and Amazon CIoudFront
D. Amazon S3 and Amazon Route 53.
Correct Answer: C
Explanation
Explanation/Reference:
You can easily and inexpensively use AWS to host a website that uses client-side technologies (such as
HTML, CSS, and JavaScript) and does not require server-side technologies (such as PHP and ASP.NET). This
type of site is called a static website, and is used to display content that does not change frequently. Before
you create and deploy a static website, you must plan your architecture to ensure that it meets your
requirements. Amazon S3, Amazon Route 53, and Amazon CIoudFront would be required in this instance.
http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html
QUESTION 143
What is the default maximum number of Access Keys per user?
A. 10
B. 15
C. 2
D. 20
Correct Answer: C
Explanation
Explanation/Reference:
The default maximum number of Access Keys per user is 2.
http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.htmI
QUESTION 144
What is the network performance offered by the c4.8xIarge instance in Amazon EC2?
A. 20 Gigabit
B. 10 Gigabit
C. Very High but variable
D. 5 Gigabit
Correct Answer: B
Explanation
Explanation/Reference:
Networking performance offered by the c4.8xIarge instance is 10 Gigabit.
http://aws.amazon.com/ec2/instance-types/
QUESTION 145
Doug has created a VPC with CIDR 10.201.0.0/16 in his AWS account. In this VPC he has created a public
subnet with CIDR block 10.201.31.0/24. While launching a new EC2 from the console, he is not able to assign
the private IP address 10.201.31.6 to this instance. Which is the most likely reason for this issue?
A. Private IP address 10.201.31.6 is blocked via ACLs in Amazon infrastructure as a part of platform security.
B. Private address IP 10.201.31.6 is currently assigned to another interface.
C. Private IP address 10.201.31.6 is not part of the associated subnet's IP address range.
D. Private IP address 10.201.31.6 is reserved by Amazon for IP networking purposes.
Correct Answer: B
Explanation
Explanation/Reference:
In Amazon VPC, you can assign any Private IP address to your instance as long as it is:
Part of the associated subnet's IP address range
Not reserved by Amazon for IP networking purposes
Not currently assigned to another interface
http://aws.amazon.com/vpc/faqs/
QUESTION 146
You need to create a JSON-formatted text file for AWS CIoudFormation. This is your first template and the only
thing you know is that the templates include several major sections but there is only one that is required for it to
work. What is the only section required?
A. Mappings
B. Outputs
C. Resources
D. Conditions
Correct Answer: C
Explanation
Explanation/Reference:
AWS CIoudFormation is a service that helps you model and set up your Amazon Web Services resources so
that you can spend less time managing those resources and more time focusing on your applications that run
in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2
instances or Amazon RDS DB instances), and AWS CIoudFormation takes care of provisioning and
configuring those resources for you.
A template is a JSON-formatted text file that describes your AWS infrastructure. Templates include several
major sections.
The Resources section is the only section that is required. The first character in the template must be an open
brace ({), and the last character must be a closed brace (}). The following template fragment shows the
template structure and sections. http://docs.aws.amazon.com/AWSCIoudFormation/latest/UserGuide/templateanatomy.
html
QUESTION 147
You are planning and configuring some EBS volumes for an application. In order to get the most performance
out of your EBS volumes, you should attach them to an instance with enough to support your volumes.
A. Redundancy
B. Storage
C. Bandwidth
D. Memory
Correct Answer: C
Explanation
Explanation/Reference:
When you plan and configure EBS volumes for your application, it is important to consider the configuration of
the instances that you will attach the volumes to. In order to get the most performance out of your EBS
volumes, you should attach them to an instance with enough bandwidth to support your volumes, such as an
EBS-optimized instance or an instance with 10 Gigabit network connectMty. This is especially important when
you use General Purpose (SSD) or Provisioned IOPS (SSD) volumes, or when you stripe multiple volumes
together in a RAID configuration. http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-ec2-config.htmI
QUESTION 148
Can a single EBS volume be attached to multiple EC2 instances at the same time?
A. Yes
B. No
C. Only for high-performance EBS volumes.
D. Only when the instances are located in the US regions.
Correct Answer: B
Explanation
Explanation/Reference:
You can't attach an EBS volume to multiple EC2 instances. This is because it is equivalent to using a single
hard drive with many computers at the same time.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.htmI
QUESTION 149
How long does an AWS free usage tier EC2 last for?
A. Forever
B. 12 Months upon signup
C. 1 Month upon signup
D. 6 Months upon signup
Correct Answer: B
Explanation
Explanation/Reference:
The AWS free usage tier will expire 12 months from the date you sign up. When your free usage expires or if
your application use exceeds the free usage tiers, you simply pay the standard, pay-as-you-go service rates.
http://aws.amazon.com/free/faqs/
QUESTION 150
A user is hosting a website in the US West-1 region. The website has the highest client base from the Asia-
Pacific (Singapore / Japan) region. The application is accessing data from S3 before serving it to client. Which
of the below mentioned regions gives a better performance for S3 objects?
A. Japan
B. Singapore
C. US East
D. US West-1
Correct Answer: D
Explanation
Explanation/Reference:
Access to Amazon S3 from within Amazon EC2 in the same region is fast. In this aspect, though the client
base is Singapore, the application is being hosted in the US West-1 region. Thus, it is recommended that S3
objects be stored in the US-West-1 region.
http://media.amazonwebservices.com/AWS_Storage_Options.pdf
QUESTION 151
Which of the following statements is true of tagging an Amazon EC2 resource?
A. You don't need to specify the resource identifier while terminating a resource.
B. You can terminate, stop, or delete a resource based solely on its tags.
C. You can't terminate, stop, or delete a resource based solely on its tags.
D. You don't need to specify the resource identifier while stopping a resource.
Correct Answer: C
Explanation
Explanation/Reference:
You can assign tags only to resources that already exist. You can't terminate, stop, or delete a resource based
solely on its tags; you must specify the resource identifier. http://docs.amazonwebservices.com/AWSEC2/
latest/UserGuide/Using_Tags.html
QUESTION 152
You have been setting up an Amazon Virtual Private Cloud (Amazon VPC) for your company, including setting
up subnets. Security is a concern, and you are not sure which is the best security practice for securing subnets
in your VPC. Which statement below is in describing the protection of AWS resources in each subnet?
A. You can use multiple layers of security, including security groups and network access control lists (ACL).
B. You can only use access control lists (ACL).
C. You don't need any security in subnets.
D. You can use multiple layers of security, including security groups, network access control lists (ACL) and
CIoudHSM.
Correct Answer: A
Explanation
Explanation/Reference:
A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a subnet that you select.
Use a public subnet for resources that must be connected to the Internet, and a private subnet for resources
that won't be connected to the Internet.
To protect the AWS resources in each subnet, you can use multiple layers of security, including security
groups and network access control lists (ACL).
http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_|ntroduction.htmI
QUESTION 153
You have been asked to tighten up the password policies in your organization after a serious security breach,
so you need to consider every possible security measure. Which of the following is not an account password
policy for IAM Users that can be set?
A. Force IAM users to contact an account administrator when the user has allowed his or her password to
expue.
B. A minimum password length.
C. Force IAM users to contact an account administrator when the user has entered his password incorrectly.
D. Prevent IAM users from reusing previous passwords.
Correct Answer: C
Explanation
Explanation/Reference:
IAM users need passwords in order to access the AWS Management Console. (They do not need passwords if
they will access AWS resources programmatically by using the CLI, AWS SDKs, or the APIs.) You can use a
password policy to do these things:
Set a minimum password length.
Require specific character types, including uppercase letters, lowercase letters, numbers, and nonalphanumeric
characters. Be sure to remind your users that passwords are case sensitive.
Allow all IAM users to change their own passwords.
Require IAM users to change their password after a specified period of time (enable password expiration).
Prevent IAM users from reusing previous passwords.
Force IAM users to contact an account administrator when the user has allowed his or her password to expue.
http://docs.aws.amazon.com/|AM/Iatest/UserGuide/Using_ManagingPasswordPoIicies.htm|
QUESTION 154
Your organization is in the business of architecting complex transactional databases. For a variety of reasons,
this has been done on EBS. What is AWS's recommendation for customers who have architected databases
using EBS for backups?
A. Backups to Amazon S3 be performed through the database management system.
B. Backups to AWS Storage Gateway be performed through the database management system.
C. If you take regular snapshots no further backups are required.
D. Backups to Amazon Glacier be performed through the database management system.
Correct Answer: A
Explanation
Explanation/Reference:
Data stored in Amazon EBS volumes is redundantly stored in multiple physical locations as part of normal
operation of those services and at no additional charge.
However, Amazon EBS replication is stored within the same availability zone, not across multiple zones;
therefore, it is highly recommended that you conduct regular snapshots to Amazon S3 for long-term data
durability.
For customers who have architected complex transactional databases using EBS, it is recommended that
backups to Amazon S3 be performed through the database management system so that distributed
transactions and logs can be checkpointed.
AWS does not perform backups of data that are maintained on virtual disks attached to running instances on
Amazon EC2.
http://d0.awsstatic.com/whitepapers/Security/AWS%20Security%20Whitepaper.pdf
QUESTION 155
You have three Amazon EC2 instances with Elastic IP addresses in the US East (Virginia) region, and you
want to distribute requests across all three IPs evenly for users for whom US East (Virginia) is the appropriate
region.
How many EC2 instances would be sufficient to distribute requests in other regions?
A. 3
B. 9
C. 2
D. 1
Correct Answer: D
Explanation
Explanation/Reference:
If your application is running on Amazon EC2 instances in two or more Amazon EC2 regions, and if you have
more than one Amazon EC2 instance in one or more regions, you can use latency-based routing to route traffic
to the region and then use weighted resource record sets to route traffic to instances within the region based
on weights that you specify.
For example, suppose you have three Amazon EC2 instances with Elastic IP addresses in the US East
(Virginia) region and you want to distribute requests across all three IPs evenly for users for whom US East
(Virginia) is the appropriate region. Just one Amazon EC2 instance is sufficient in the other regions, although
you can apply the same technique to many regions at once. http://docs.aws.amazon.com/Route53/Iatest/
DeveIoperGuide/Tutorials.html
QUESTION 156
A user has created a CIoudFormation stack. The stack creates AWS services, such as EC2 instances, ELB,
AutoScaIing, and RDS. While creating the stack it created EC2, ELB and AutoScaIing but failed to create RDS.
What will C|oudFormation do in this scenario?
A. Rollback all the changes and terminate all the created services
B. It will wait for the user's input about the error and the mistake after the input
C. CIoudFormation can never throw an error after launching a few services since it verifies all the steps before
launching
D. It will warn the user about the error and ask the user to manually create RDS
Correct Answer: A
Explanation
Explanation/Reference:
AWS CIoudFormation is an application management tool which provides application modeling, deployment,
configuration, management and related actMties. The AWS CIoudFormation stack is a collection of AWS
resources which are created and managed as a single unit when AWS CIoudFormation instantiates a template.
If any of the services fails to launch, C|oudFormation will rollback all the changes and terminate or delete all the
created services.
http://aws.amazon.com/c|oudformation/faqs/
QUESTION 157
A major client who has been spending a lot of money on his internet service provider asks you to set up an
AWS Direct Connection to try and save him some money. You know he needs high-speed connectMty. Which
connection port speeds are available on AWS Direct Connect?
A. 500Mbps and 1Gbps
B. 1Gbps and 10Gbps
C. 100Mbps and 1Gbps
D. 1Gbps
Correct Answer: B
Explanation
Explanation/Reference:
AWS Direct Connect is a network service that provides an alternative to using the internet to utilize AWS cloud
services.
Using AWS Direct Connect, data that would have previously been transported over the Internet can now be
delivered through a private network connection between AWS and your datacenter or corporate network.
1Gbps and 10Gbps ports are available. Speeds of 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, and
500Mbps can be ordered from any APN partners supporting AWS Direct Connect.
https://aws.amazon.com/directconnect/faqs/
QUESTION 158
In Amazon EC2, what is the limit of Reserved Instances per Availability Zone each month?
A. 5
B. 20
C. 50
D. 10
Correct Answer: B
Explanation
Explanation/Reference:
There are 20 Reserved Instances per Availability Zone in each month. http://docs.aws.amazon.com/generaI/
latest/gr/aws_service_Iimits.html
QUESTION 159
You have just finshed setting up an advertisement server in which one of the obvious choices for a service was
Amazon Elastic Map Reduce( EMR) and are now troubleshooting some weird cluster states that you are
seeing. Which of the below is not an Amazon EMR cluster state?
A. STARTING
B. STOPPED
C. RUNNING
D. WAITING
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Elastic Map Reduce (EMR) is a web service that enables businesses, researchers, data analysts, and
developers to easily and cost-effectively process vast amounts of data. Amazon EMR historically referred to an
Amazon EMR cluster (and all processing steps assigned to it) as a "c|uster". Every cluster has a unique
identifier that starts with "j-". The different cluster states of an Amazon EMR cluster are listed below.
STARTING -- The cluster provisions, starts, and configures EC2 instances. BOOTSTRAPPING -- Bootstrap
actions are being executed on the cluster.
RUNNING -- A step for the cluster is currently being run.
WAITING -- The cluster is currently active, but has no steps to run. TERMINATING - The cluster is in the
process of shutting down.
TERMINATED - The cluster was shut down without error.
TERMINATED_W|TH_ERRORS - The cluster was shut down with errors.
https://aws.amazon.com/elasticmapreduce/faqs/
QUESTION 160
The AWS CIoudHSM service defines a resource known as a high-availability (HA) , which is a virtual partition
that represents a group of partitions, typically distributed between several physical HSMs for high-availability.
A. proxy group
B. partition group
C. functional group
D. relational group
Correct Answer: B
Explanation
Explanation/Reference:
The AWS CIoudHSNI service defines a resource known as a high-availability (HA) partition group, which is a
virtual partition that represents a group of partitions, typically distributed between several physical HSMs for
high-availability.
http://docs.aws.amazon.com/cloudhsm/latest/userguide/configuring-ha.htmI
QUESTION 161
Is it possible to get a history of all EC2 API calls made on your account for security analysis and operational
troubleshooting purposes?
A. Yes, by default, the history of your API calls is logged.
B. Yes, you should turn on the CIoudTraiI in the AWS console.
C. No, you can only get a history of VPC API calls.
D. No, you cannot store history of EC2 API calls on Amazon.
Correct Answer: B
Explanation
Explanation/Reference:
To get a history of all EC2 API calls (including VPC and EBS) made on your account, you simply turn on C|
oudTrai| in the AWS Management Console.
https://aws.amazon.com/ec2/faqs/
QUESTION 162
You have just set up yourfirst Elastic Load Balancer (ELB) but it does not seem to be configured properly. You
discover that before you start using ELB, you have to configure the listeners for your load balancer. Which
protocols does ELB use to support the load balancing of applications?
A. HTTP and HTTPS
B. HTTP, HTTPS , TCP, SSL and SSH
C. HTTP, HTTPS , TCP, and SSL
D. HTTP, HTTPS , TCP, SSL and SFTP
Correct Answer: C
Explanation
Explanation/Reference:
Before you start using Elastic Load BaIancing(ELB), you have to configure the listeners for your load balancer.
A listener is a process that listens for connection requests. It is configured with a protocol and a port number
for front-end (client to load balancer) and back-end (load balancer to back-end instance) connections. Elastic
Load Balancing supports the load balancing of applications using HTTP, HTTPS (secure HTTP), TCP, and
SSL (secure TCP) protocols. The HTTPS uses the SSL protocol to establish secure connections over the
HTTP layer. You can also use SSL protocol to establish secure connections over the TCP layer. The
acceptable ports for both HTTPS/SSL and HTTP/TCP connections are 25, 80, 443, 465, 587, and 1024-
65S35.
http://docs.aws.amazon.com/E|asticLoadBaIancing/latest/DeveIoperGuide/elb-listener-config.htmI
QUESTION 163
After setting up some EC2 instances you now need to set up a monitoring solution to keep track of these
instances and to send you an email when the CPU hits a certain threshold. Which statement below best
describes what thresholds you can set to trigger a CIoudWatch Alarm?
A. Set a target value and choose whether the alarm will trigger when the value is greater than (>), greater than
or equal to (>=), less than (<), or less than or equal to (<=) that value.
B. Thresholds need to be set in IAM not CIoudWatch
C. Only default thresholds can be set you can't choose your own thresholds.
D. Set a target value and choose whether the alarm will trigger when the value hits this threshold
Correct Answer: A
Explanation
Explanation/Reference:
Amazon CIoudWatch is a monitoring service for AWS cloud resources and the applications you run on AWS.
You can use Amazon CIoudWatch to collect and track metrics, collect and monitor log files, and set alarms.
When you create an alarm, you first choose the Amazon CIoudWatch metric you want it to monitor. Next, you
choose the evaluation period (e.g., five minutes or one hour) and a statistical value to measure (e.g., Average
or Maximum).
To set a threshold, set a target value and choose whether the alarm will trigger when the value is greater than
(>), greater than or equal to (>=), less than (<), or less than or equal to (<=) that value.
http://aws.amazon.com/cIoudwatch/faqs/
QUESTION 164
After moving an E-Commerce website for a client from a dedicated server to AWS you have also set up auto
scaling to perform health checks on the instances in your group and replace instances that fail these checks.
Your client has come to you with his own health check system that he wants you to use as it has proved to be
very useful prior to his site running on AWS. What do you think would be an appropriate response to this given
all that you know about auto scaling?
A. It is not possible to implement your own health check system. You need to use AWSs health check system.
B. It is not possible to implement your own health check system due to compatibility issues.
C. It is possible to implement your own health check system and then send the instance's health information
directly from your system to Cloud Watch.
D. It is possible to implement your own health check system and then send the instance's health information
directly from your system to Cloud Watch but only in the US East (N. Virginia) region.
Correct Answer: C
Explanation
Explanation/Reference:
Auto Scaling periodically performs health checks on the instances in your group and replaces instances that
fail these checks. By default, these health checks use the results of EC2 instance status checks to determine
the health of an instance. If you use a load balancer with your Auto Scaling group, you can optionally choose to
include the results of Elastic Load Balancing health checks. Auto Scaling marks an instance unhealthy if the
calls to the Amazon EC2 action DescribeInstanceStatus returns any other state other than running, the system
status shows impaired, or the calls to Elastic Load Balancing action DescribeInstanceHeaIth returns
OutOfService in the instance state field. After an instance is marked unhealthy because of an Amazon EC2 or
Elastic Load Balancing health check, it is scheduled for replacement. You can customize the health check
conducted by your Auto Scaling group by specifying additional checks or by having your own health check
system and then sending the instance's health information directly from your system to Auto Scaling.
http://docs.aws.amazon.com/AutoScaIing/latest/Deve|operGuide/healthcheck.html
QUESTION 165
When does the billing of an Amazon EC2 system begin?
A. It starts when the Status column for your distribution changes from Creating to Deployed.
B. It starts as soon as you click the create instance option on the main EC2 console.
C. It starts when your instance reaches 720 instance hours.
D. It starts when Amazon EC2 initiates the boot sequence of an AM instance.
Correct Answer: D
Explanation
Explanation/Reference:
Billing commences when Amazon EC2 initiates the boot sequence of an AM instance. Billing ends when the
instance terminates, which could occur through a web services command, by running "shutdown -h", or
through instance failure. When you stop an instance, Amazon shuts it down but doesn/Et charge hourly usage
for a stopped instance, or data transfer fees, but charges for the storage for any Amazon EBS volumes.
http://aws.amazon.com/ec2/faqs/
QUESTION 166
You havejust discovered that you can upload your objects to Amazon S3 using MuItipart Upload API. You start
to test it out but are unsure of the benefits that it would provide. Which of the following is not a benefit of using
multipart uploads?
A. You can begin an upload before you know the final object size.
B. Quick recovery from any network issues.
C. Pause and resume object uploads.
D. It's more secure than normal upload.
Correct Answer: D
Explanation
Explanation/Reference:
MuItipart upload in Amazon S3 allows you to upload a single object as a set of parts. Each part is a contiguous
portion ofthe object's data. You can upload these object parts independently and in any order. If transmission
of any part fails, you can re-transmit that part without affecting other parts. After all parts of your object are
uploaded, Amazon S3 assembles these parts and creates the object. In general, when your object size
reaches 100 MB, you should consider using multipart uploads instead of uploading the object in a single
operation.
Using multipart upload provides the following advantages:
Improved throughput--You can upload parts in parallel to improve throughput. Quick recovery from any network
issues--SmaIIer part size minimizes the impact of restarting a failed upload due to a network error. Pause and
resume object upIoads--You can upload object parts over time. Once you initiate a multipart upload there is no
expiry; you must explicitly complete or abort the multipart upload. Begin an upload before you know the final
object size--You can upload an object as you are creating it. http://docs.aws.amazon.com/AmazonS3/ latest/
dev/uploadobjusingmpu.htmI
QUESTION 167
What is the data model of DynamoDB?
A. Since DynamoDB is schema-less, there is no data model.
B. "Items", with Keys and one or more Attribute; and "Attribute", with Name and Value.
C. "TabIe", a collection of Items; "Items", with Keys and one or more Attribute; and "Attribute", with Name and
Value.
D. "Database", which is a set of "TabIes", which is a set of "Items", which is a set of "Attributes".
Correct Answer: C
Explanation
Explanation/Reference:
The data model of DynamoDB is:
"TabIe", a collection of Items;
"Items", with Keys and one or more Attribute;
"Attribute", with Name and Value.
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModeI.html
QUESTION 168
What happens to Amazon EBS root device volumes, by default, when an instance terminates?
A. Amazon EBS root device volumes are moved to IAM.
B. Amazon EBS root device volumes are copied into Amazon RDS.
C. Amazon EBS root device volumes are automatically deleted.
D. Amazon EBS root device volumes remain in the database until you delete them.
Correct Answer: C
Explanation
Explanation/Reference:
By default, Amazon EBS root device volumes are automatically deleted when the instance terminates. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html
QUESTION 169
Which of the following would you use to list your AWS Import/Exportjobs?
A. Amazon RDS
B. AWS Import/Export Web Service Tool
C. Amazon S3 REST API
D. AWS Elastic Beanstalk
Correct Answer: C
Explanation
Explanation/Reference:
You can list AWS Import/Export jobs with the ListJobs command using the command line client or REST API.
http://docs.aws.amazon.com/AWSImportExport/latest/DG/ListingYourJobs.html
QUESTION 170
A gaming company comes to you and asks you to build them infrastructure for their site. They are not sure how
big they will be as with all start ups they have limited money and big ideas. What they do tell you is that if the
game becomes successful, like one of their previous games, it may rapidly grow to millions of users and
generate tens (or even hundreds) of thousands of writes and reads per second. After considering all of this,
you decide that they need a fully managed NoSQL database service that provides fast and predictable
performance with seamless scalability. Which of the following databases do you think would best fit their
needs?
A. Amazon DynamoDB
B. Amazon Redshift
C. Any non-relational database.
D. Amazon SimpIeDB
Correct Answer: A
Explanation
Explanation/Reference:
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable
performance with seamless scalability. Amazon DynamoDB enables customers to offload the administrative
burdens of operating and scaling distributed databases to AWS, so they don't have to worry about hardware
provisioning, setup and configuration, replication, software patching, or cluster scaHng. Today's web-based
applications generate and consume massive amounts of data. For example, an online game might start out
with only a few thousand users and a light database workload consisting of 10 writes per second and 50 reads
per second. However, if the game becomes successful, it may rapidly grow to millions of users and generate
tens (or even hundreds) of thousands of writes and reads per second. It may also create terabytes or more of
data per day. Developing your applications against Amazon DynamoDB enables you to start small and simply
dial-up your request capacity for a table as your requirements scale, without incurring downtime. You pay
highly cost-efficient rates for the request capacity you provision, and let Amazon DynamoDB do the work over
partitioning your data and traffic over sufficient server capacity to meet your needs. Amazon DynamoDB does
the database management and administration, and you simply store and request your data. Automatic
replication and failover provides built-in fault tolerance, high availability, and data durability. Amazon
DynamoDB gives you the peace of mind that your database is fully managed and can grow with your
application requirements.
http://aws.amazon.com/dynamodb/faqs/
QUESTION 171
Mike is appointed as Cloud Consultant in Netcrak Inc. Netcrak has the following VPCs set-up in the US East
Region:
A VPC with CIDR block 10.10.0.0/16, a subnet in that VPC with CIDR block 10.10.1.0/24 A VPC with CIDR
block 10.40.0.0/16, a subnet in that VPC with CIDR block 10.40.1.0/24 Netcrak Inc is trying to establish
network connection between two subnets, a subnet with CIDR block 10.10.1.0/24 and another subnet with
CIDR block 10.40.1.0/24. Which one of the following solutions should Mke recommend to Netcrak Inc?
A. Create 2 Virtual Private Gateways and configure one with each VPC.
B. Create one EC2 instance in each subnet, assign Elastic IPs to both instances, and configure a set up Siteto-
Site VPN connection between both EC2 instances.
C. Create a VPC Peering connection between both VPCs.
D. Create 2 Internet Gateways, and attach one to each VPC.
Correct Answer: C
Explanation
Explanation/Reference:
A VPC peering connection is a networking connection between two VPCs that enables you to route traffic
between them using private IP addresses. EC2 instances in either VPC can communicate with each other as if
they are within the same network. You can create a VPC peering connection between your own VPCs, or with
a VPC in another AWS account within a single region. AWS uses the existing infrastructure of a VPC to create
a VPC peering connection; it is neither a gateway nor a VPN connection, and does not rely on a separate piece
of physical hardware. http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-peering.htm|
QUESTION 172
A favored client needs you to quickly deploy a database that is a relational database service with minimal
administration as he wants to spend the least amount of time administering it. Which database would be the
best option?
A. Amazon Simp|eDB
B. Your choice of relational AMs on Amazon EC2 and EBS.
C. Amazon RDS
D. Amazon Redshift
Correct Answer: C
Explanation
Explanation/Reference:
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easy to set up, operate,
and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing
time-consuming database administration tasks, freeing you up to focus on your applications and business.
Amazon RDS gives you access to the capabilities of a familiar MySQL, Oracle, SQL Server, or PostgreSQL
database engine. This means that the code, applications, and tools you already use today with your existing
databases can be used with Amazon RDS. Amazon RDS automatically patches the database software and
backs up your database, storing the backups for a user-defined retention period and enabling point-in-time
recovery.
https://aws.amazon.com/running_databases/#rds_anchor
QUESTION 173
You're trying to delete an SSL certificate from the IAM certificate store, and you're getting the message
"Certificate: <certificate-id> is being used by CIoudFront." Which of the following statements is probably the
reason why you are getting this error?
A. Before you can delete an SSL certificate, you need to either rotate SSL certificates or revert from using a
custom SSL certificate to using the default CIoudFront certificate.
B. You can't delete SSL certificates . You need to request it from AWS.
C. Before you can delete an SSL certificate, you need to set up the appropriate access level in IAM
D. Before you can delete an SSL certificate you need to set up https on your server.
Correct Answer: A
Explanation
Explanation/Reference:
CIoudFront is a web service that speeds up distribution of your static and dynamic web content, for
example, .htmI, .css, .php, and image files, to end users. Every CIoudFront web distribution must be
associated either with the default CIoudFront certificate or with a custom SSL certificate. Before you can delete
an SSL certificate, you need to either rotate SSL certificates (replace the current custom SSL certificate with
another custom SSL certificate) or revert from using a custom SSL certificate to using the default CIoudFront
certificate.
http://docs.aws.amazon.com/AmazonCIoudFront/latest/Deve|operGuide/Troubleshooting.htm|
QUESTION 174
How many types of block devices does Amazon EC2 support?
A. 4
B. 5
C. 2
D. 1
Correct Answer: C
Explanation
Explanation/Reference:
Amazon EC2 supports 2 types of block devices.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html
QUESTION 175
You need to set up security for your VPC and you know that Amazon VPC provides two features that you can
use to increase security for your VPC: Security groups and network access control lists (ACLs). You start to
look into security groups first. Which statement below is inin relation to security groups?
A. Are stateful: Return traffic is automatically allowed, regardless of any rules.
B. Evaluate all rules before deciding whether to allow traffic.
C. Support allow rules and deny rules.
D. Operate at the instance level (first layer of defense).
Correct Answer: C
Explanation
Explanation/Reference:
Amazon VPC provides two features that you can use to increase security for your VPC:
Security groups--Act as a firewall for associated Amazon EC2 instances, controlling both inbound and
outbound traffic at the instance level and supports allow rules only. Network access control lists (ACLs)--Act as
a firewall for associated subnets, controlling both inbound and outbound traffic at the subnet level and supports
allow rules and deny rules. http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html
QUESTION 176
You are setting up some IAM user policies and have also become aware that some services support resourcebased
permissions, which let you attach policies to the service's resources instead of to IAM users or groups.
Which of the below statements is true in regards to resource-level permissions?
A. All services support resource-level permissions for all actions.
B. Resource-level permissions are supported by Amazon CIoudFront
C. All services support resource-level permissions only for some actions.
D. Some services support resource-level permissions only for some actions.
Correct Answer: D
Explanation
Explanation/Reference:
AWS Identity and Access Management is a web service that enables Amazon Web Services (AWS) customers
to manage users and user permissions in AWS. The service is targeted at organizations with multiple users or
systems that use AWS products such as Amazon EC2, Amazon RDS, and the AWS Management Console.
With IAM, you can centrally manage users, security credentials such as access keys, and permissions that
control which AWS resources users can access. In addition to supporting IAM user policies, some services
support resource-based permissions, which let you attach policies to the service's resources instead of to IAM
users or groups. Resource-based permissions are supported by Amazon S3, Amazon SNS, and Amazon SQS.
The resource-level permissions service supports IAM policies in which you can specify indMdual resources
using Amazon Resource Names (ARNs) in the poIicy's Resource element. Some services support resourcelevel
permissions only for some actions. http://docs.aws.amazon.com/IAM/latest/UserGuide/
Using_SpecificProducts.html
QUESTION 177
A user wants to increase the durability and availability of the EBS volume. Which of the below mentioned
actions should he perform?
A. Take regular snapshots.
B. Create an AMI.
C. Create EBS with higher capacity.
D. Access EBS regularly.
Correct Answer: A
Explanation
Explanation/Reference:
In Amazon Web Services, Amazon EBS volumes that operate with 20 GB or less of modified data since their
most recent snapshot can expect an annual failure rate (AFR) between 0.1% and 0.5%. For this reason, to
maximize both durability and availability of their Amazon EBS data, the user should frequently create
snapshots of the Amazon EBS volumes.
http://media.amazonwebservices.com/AWS_Storage_Options.pdf
QUESTION 178
In relation to AWS CIoudHSM, High-availability (HA) recovery is hands-off resumption by failed HA group
members.
Prior to the introduction of this function, the HA feature provided redundancy and performance, but required
that a failed/lost group member be reinstated.
A. automatically
B. periodically
C. manually
D. continuosly
Correct Answer: C
Explanation
Explanation/Reference:
In relation to AWS CIoudHS|VI, High-availability (HA) recovery is hands-off resumption by failed HA group
members.
Prior to the introduction of this function, the HA feature provided redundancy and performance, but required
that a failed/lost group member be manually reinstated. http://docs.aws.amazon.com/cloudhsm/latest/
userguide/ha-best-practices.html
QUESTION 179
You have created a Route 53 latency record set from your domain to a machine in Northern Virginia and a
similar record to a machine in Sydney.
When a user located in U S visits your domain he will be routed to:
A. Northern Virginia
B. Sydney
C. Both, Northern Virginia and Sydney
D. Depends on the Weighted Resource Record Sets
Correct Answer: A
Explanation
Explanation/Reference:
If your application is running on Amazon EC2 instances in two or more Amazon EC2 regions, and if you have
more than one Amazon EC2 instance in one or more regions, you can use latency-based routing to route traffic
to the region and then use weighted resource record sets to route traffic to instances within the region based
on weights that you specify.
For example, suppose you have three Amazon EC2 instances with Elastic IP addresses in the US East
(Virginia) region and you want to distribute requests across all three IPs evenly for users for whom US East
(Virginia) is the appropriate region. Just one Amazon EC2 instance is sufficient in the other regions, although
you can apply the same technique to many regions at once. http://docs.aws.amazon.com/Route53/Iatest/
DeveIoperGuide/Tutorials.html
QUESTION 180
Any person or application that interacts with AWS requires security credentials. AWS uses these credentials to
identify who is making the call and whether to allow the requested access. You have just set up a VPC network
for a client and you are now thinking about the best way to secure this network. You set up a security group
called vpcsecuritygroup. Which following statement is true in respect to the initial settings that will be applied to
this security group if you choose to use the default settings for this group?
A. Allow all inbound traffic and allow no outbound traffic.
B. Allow no inbound traffic and allow all outbound traffic.
C. Allow inbound traffic on port 80 only and allow all outbound traffic.
D. Allow all inbound traffic and allow all outbound traffic.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon VPC provides advanced security features such as security groups and network access control lists to
enable inbound and outbound filtering at the instance level and subnet level. AWS assigns each security group
a unique ID in the form sg-xxxxxxxx. The following are the initial settings for a security group that you create:
Allow no inbound traffic
Allow all outbound traffic
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html
QUESTION 181
You are using Amazon SES as an email solution but are unsure of what its limitations are. Which statement
below is in regards to that?
A. New Amazon SES users who have received production access can send up to 1,000 emails per 24-hour
period, at a maximum rate of 10 emails per second.
B. Every Amazon SES sender has a the same set of sending limits
C. Sending limits are based on messages rather than on recipients
D. Every Amazon SES sender has a unique set of sending limits
Correct Answer: D
Explanation
Explanation/Reference:
Amazon Simple Email Service (Amazon SES) is a highly scalable and cost-effective email-sending service for
businesses and developers. Amazon SES eliminates the complexity and expense of building an in-house email
solution or licensing, installing, and operating a third-party email service for this type of email communication.
Every Amazon SES sender has a unique set of sending limits, which are calculated by Amazon SES on an
ongoing basis:
Sending quota -- the maximum number of emails you can send in a 24-hour period. Maximum send rate -- the
maximum number of emails you can send per second. New Amazon SES users who have received production
access can send up to 10,000 emails per 24-hour period, at a maximum rate of 5 emails per second. Amazon
SES automatically adjusts these limits upward, as long as you send high-quality email. If your existing quota is
not adequate for your needs and the system has not automatically increased your quota, you can submit an
SES Sending Quota Increase case at any time.
Sending limits are based on recipients ratherthan on messages. You can check your sending limits at any time
by using the Amazon SES console.
Note that if your email is detected to be of poor or questionable quality (e.g., high complaint rates, high bounce
rates, spam, or abusive content), Amazon SES might temporarily or permanently reduce your permitted send
volume, or take other action as AWS deems appropriate.
https://aws.amazon.com/ses/faqs/
QUESTION 182
Having just set up your first Amazon Virtual Private Cloud (Amazon VPC) network, which defined a default
network interface, you decide that you need to create and attach an additional network interface, known as an
elastic network interface (ENI) to one of your instances. Which of the following statements is true regarding
attaching network interfaces to your instances in your VPC?
A. You can attach 5 EN|s per instance type.
B. You can attach as many ENIs as you want.
C. The number of ENIs you can attach varies by instance type.
D. You can attach 100 ENIs total regardless of instance type.
Correct Answer: C
Explanation
Explanation/Reference:
Each instance in your VPC has a default network interface that is assigned a private IP address from the IP
address range of your VPC. You can create and attach an additional network interface, known as an elastic
network interface (ENI), to any instance in your VPC. The number of EN|s you can attach varies by instance
type.
QUESTION 183
A for a VPC is a collection of subnets (typically private) that you may want to designate for your backend RDS
DB Instances.
A. DB Subnet Set
B. RDS Subnet Group
C. DB Subnet Group
D. DB Subnet Collection
Correct Answer: C
Explanation
Explanation/Reference:
DB Subnet Groups are a set of subnets (one per Availability Zone of a particular region) designed for your DB
instances that reside in a VPC. They make easy to manage Multi-AZ deployments as well as the conversion
from a Single-AZ to a Mut|i-AZ one.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSVPC.htmI
QUESTION 184
Amazon Elastic Load Balancing is used to manage traffic on a fileet of Amazon EC2 instances, distributing
traffic to instances across all availability zones within a region. Elastic Load Balancing has all the advantages
of an on-premises load balancer, plus several security benefits. Which of the following is not an advantage of
ELB over an on-premise load balancer?
A. ELB uses a four-tier, key-based architecture for encryption.
B. ELB offers clients a single point of contact, and can also serve as the first line of defense against attacks on
your network.
C. ELB takes over the encryption and decryption work from the Amazon EC2 instances and manages it
centrally on the load balancer.
D. ELB supports end-to-end traffic encryption using TLS (previously SSL) on those networks that use secure
HTTP (HTTPS) connections.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Elastic Load Balancing is used to manage traffic on a fileet of Amazon EC2 instances, distributing
traffic to instances across all availability zones within a region. Elastic Load Balancing has all the advantages
of an on-premises load balancer, plus several security benefits:
Takes over the encryption and decryption work from the Amazon EC2 instances and manages it centrally on
the load balancer
Offers clients a single point of contact, and can also serve as the first line of defense against attacks on your
network
When used in an Amazon VPC, supports creation and management of security groups associated with your
Elastic Load Balancing to provide additional networking and security options Supports end-to-end traffic
encryption using TLS (previously SSL) on those networks that use secure HTTP (HTTPS) connections. When
TLS is used, the TLS server certificate used to terminate client connections can be managed centrally on the
load balancer, rather than on every indMdual instance. http://d0.awsstatic.com/whitepapers/Security/AWS%
20Security%20Whitepaper.pdf
QUESTION 185
You have set up an S3 bucket with a number of images in it and you have decided that you want anybody to be
able to access these images, even anonymous users. To accomplish this you create a bucket policy. You will
need to use an Amazon S3 bucket policy that specifies a in the principal element, which means anyone can
access the bucket.
A. hash tag (#)
B. anonymous user
C. wildcard (*)
D. S3 user
Correct Answer: C
Explanation
Explanation/Reference:
You can use the AWS Policy Generator to create a bucket policy for your Amazon S3 bucket. You can then
use the generated document to set your bucket policy by using the Amazon S3 console, by a number of thirdparty
tools, or via your application.
You use an Amazon S3 bucket policy that specifies a wildcard (*) in the principal element, which means
anyone can access the bucket. With anonymous access, anyone (including users without an AWS account) will
be able to access the bucket.
http://docs.aws.amazon.com/IAM/|atest/UserGuide/iam-troubleshooting.htm|#d0e20565
QUESTION 186
You have been asked to build AWS infrastructure for disaster recovery for your local applications and within
that you should use an AWS Storage Gateway as part of the solution. Which of the following best describes the
function of an AWS Storage Gateway?
A. Accelerates transferring large amounts of data between the AWS cloud and portable storage devices .
B. A web service that speeds up distribution of your static and dynamic web content.
C. Connects an on-premises software appliance with cloud-based storage to provide seamless and secure
integration between your on-premises IT environment and AWS's storage infrastructure.
D. Is a storage service optimized for infrequently used data, or "cold data."
Correct Answer: C
Explanation
Explanation/Reference:
AWS Storage Gateway connects an on-premises software appliance with cloud-based storage to provide
seamless integration with data security features between your on-premises IT environment and the Amazon
Web Services (AWS) storage infrastructure. You can use the service to store data in the AWS cloud for
scalable and cost-effective storage that helps maintain data security. AWS Storage Gateway offers both
volume-based and tape-based storage solutions:
Volume gateways
Gateway-cached volumes
Gateway-stored volumes
Gateway-virtual tape library (VTL)
http://media.amazonwebservices.com/architecturecenter/AWS_ac_ra_disasterrecovery_07.pdf
QUESTION 187
An organization has a statutory requirement to protect the data at rest for the S3 objects. Which of the below
mentioned options need not be enabled by the organization to achieve data security?
A. MFA delete for S3 objects
B. Client side encryption
C. Bucket versioning
D. Data replication
Correct Answer: D
Explanation
Explanation/Reference:
AWS S3 provides multiple options to achieve the protection of data at REST. The options include Permission
(Policy), Encryption (Client and Server Side), Bucket Versioning and MFA based delete. The user can enable
any of these options to achieve data protection. Data replication is an internal facility by AWS where S3
replicates each object across all the Availability Zones and the organization need not enable it in this case.
http://media.amazonwebservices.com/AWS_Security_Best_Practices.pdf
QUESTION 188
In Amazon CIoudFront, if you use Amazon EC2 instances and other custom origins with CIoudFront, it is
recommended to .
A. not use Elastic Load Balancing
B. restrict Internet communication to private instances while allowing outgoing traffic
C. enable access key rotation for CIoudWatch metrics
D. specify the URL of the load balancer for the domain name of your origin server
Correct Answer: D
Explanation
Explanation/Reference:
In Amazon CIoudFront, you should use an Elastic Load Balancing load balancer to handle traffic across
multiple Amazon EC2 instances and to isolate your application from changes to Amazon EC2 instances. When
you create your C|oudFront distribution, specify the URL of the load balancer for the domain name of your
origin server.
http://docs.aws.amazon.com/AmazonC|oudFront/latest/DeveIoperGuide/CustomOriginBestPractices.htmI
QUESTION 189
What is the time period with which metric data is sent to CIoudWatch when detailed monitoring is enabled on
an Amazon EC2 instance?
A. 15 minutes
B. 5 minutes
C. 1 minute
D. 45 seconds
Correct Answer: C
Explanation
Explanation/Reference:
By default, Amazon EC2 metric data is automatically sent to CIoudWatch in 5-minute periods. However, you
can, enable detailed monitoring on an Amazon EC2 instance, which sends data to CIoudWatch in 1-minute
periods
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.htmI
QUESTION 190
A government client needs you to set up secure cryptographic key storage for some of their extremely
confidential data. You decide that the AWS CIoudHSM is the best service for this. However, there seem to be a
few pre-requisites before this can happen, one of those being a security group that has certain ports open.
Which of the following is in regards to those security groups?
A. A security group that has port 22 (for SSH) or port 3389 (for RDP) open to your network.
B. A security group that has no ports open to your network.
C. A security group that has only port 3389 (for RDP) open to your network.
D. A security group that has only port 22 (for SSH) open to your network.
Correct Answer: A
Explanation
Explanation/Reference:
AWS CIoudHSM provides secure cryptographic key storage to customers by making hardware security
modules (HSMs) available in the AWS cloud.
AWS C|oudHSM requires the following environment before an HSM appliance can be provisioned. A virtual
private cloud (VPC) in the region where you want the AWS CIoudHSM service. One private subnet (a subnet
with no Internet gateway) in the VPC. The HSM appliance is provisioned into this subnet. One public subnet (a
subnet with an Internet gateway attached). The control instances are attached to this subnet.
An AWS Identity and Access Management (IAM) role that delegates access to your AWS resources to AWS
CIoudHSM.
An EC2 instance, in the same VPC as the HSM appliance, that has the SafeNet client software installed. This
instance is referred to as the control instance and is used to connect to and manage the HSM appliance. A
security group that has port 22 (for SSH) or port 3389 (for RDP) open to your network. This security group is
attached to your control instances so you can access them remotely.
QUESTION 191
Which of the following features are provided by Amazon EC2?
A. Exadata Database Machine, Optimized Storage Management, Flashback Technology, and Data
Warehousing
B. Instances, Amazon Machine Images (AMIs), Key Pairs, Amazon EBS Volumes, Firewall, Elastic IP address,
Tags, and Virtual Private Clouds (VPCs)
C. Real Application Clusters (RAC), Elasticache Machine Images (EMIs), Data Warehousing, Flashback
Technology, Dynamic IP address
D. Exadata Database Machine, Real Application Clusters (RAC), Data Guard, Table and Index Partitioning,
and Data Pump Compression
Correct Answer: B
Explanation
Explanation/Reference:
Amazon EC2 provides the following features:
· Virtual computing environments, known as instances;
· Pre-configured templates for your instances, known as Amazon Nlachine Images (AMIs), that package the
bits you need for your server (including the operating system and additional software) · Various configurations
of CPU, memory, storage, and networking capacity for your instances, known as instance types · Secure login
information for your instances using key pairs (AWS stores the public key, and you store the private key in a
secure place)
· Storage volumes for temporary data that's deleted when you stop or terminate your instance, known as
instance store volumes
· Persistent storage volumes for your data using Amazon Elastic Block Store (Amazon EBS), known as
Amazon EBS volumes
· MuItipIe physical locations for your resources, such as instances and Amazon EBS volumes, known as
regions and Availability Zones
· A firewall that enables you to specify the protocols, ports, and source IP ranges that can reach your instances
using security groups
· Static IP addresses for dynamic cloud computing, known as Elastic IP addresses · Metadata, known as tags,
that you can create and assign to your Amazon EC2 resources · Virtual networks you can create that are
logically isolated from the rest of the AWS cloud, and that you can optionally connect to your own network,
known as virtual private clouds (VPCs). http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
QUESTION 192
In Amazon Elastic Compute Cloud, which ofthe following is used for communication between instances in the
same network (EC2-Classic or a VPC)?
A. Private IP addresses
B. Elastic IP addresses
C. Static IP addresses
D. Public IP addresses
Correct Answer: A
Explanation
Explanation/Reference:
A private IP address is an IP address that's not reachable over the Internet. You can use private IP addresses
for communication between instances in the same network (EC2-Classic or a VPC).
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-instance-addressing.htmI
QUESTION 193
A friend tells you he is being charged $100 a month to host his WordPress website, and you tell him you can
move it to AWS for him and he will only pay a fraction of that, which makes him very happy. He then tells you
he is being charged $50 a month for the domain, which is registered with the same people that set it up, and he
asks if it's possible to move that to AWS as well. You tell him you aren't sure, but will look into it. Which of the
following statements is true in regards to transferring domain names to AWS?
A. You can't transfer existing domains to AWS.
B. You can transfer existing domains into Amazon Route 53's management.
C. You can transfer existing domains via AWS Direct Connect.
D. You can transfer existing domains via AWS Import/Export.
Correct Answer: B
Explanation
Explanation/Reference:
With Amazon Route 53, you can create and manage your public DNS records with the AWS Management
Console or with an easy-to-use API. If you need a domain name, you can find an available name and register it
using Amazon Route 53. You can also transfer existing domains into Amazon Route 53's management.
http://aws.amazon.com/Route53/
QUESTION 194
Are penetration tests allowed as long as they are limited to the customer's instances?
A. Yes, they are allowed but only for selected regions.
B. No, they are never allowed.
C. Yes, they are allowed without any permission.
D. Yes, they are allowed but only with approval.
Correct Answer: D
Explanation
Explanation/Reference:
Penetration tests are allowed after obtaining permission from AWS to perform them.
http://aws.amazon.com/security/penetration-testing/
QUESTION 195
A user has created an ELB with the availability zone US-East-1A. The user wants to add more zones to ELB to
achieve High Availability. How can the user add more zones to the existing ELB?
A. The user should stop the ELB and add zones and instances as required
B. The only option is to launch instances in different zones and add to ELB
C. It is not possible to add more zones to the existing ELB
D. The user can add zones on the fly from the AWS console
Correct Answer: D
Explanation
Explanation/Reference:
The user has created an Elastic Load Balancer with the availability zone and wants to add more zones to the
existing ELB. The user can do so in two ways:
From the console or CLI, add new zones to ELB;
Launch instances in a separate AZ and add instances to the existing ELB.
http://docs.aws.amazon.com/EIasticLoadBaIancing/latest/DeveIoperGuide/enable-disable-az.html
QUESTION 196
What happens to data on an ephemeral volume of an EBS-backed EC2 instance if it is terminated or if it fails?
A. Data is automatically copied to another volume.
B. The volume snapshot is saved in S3.
C. Data persists.
D. Data is deleted.
Correct Answer: D
Explanation
Explanation/Reference:
Any data on the instance store volumes persists as long as the instance is running, but this data is deleted
when the instance is terminated or if it fails (such as if an underlying drive has issues). After an instance storebacked
instance fails or terminates, it cannot be restored. http://docs.aws.amazon.com/AWSEC2/latest/
UserGuide/RootDeviceStorage.htmI
QUESTION 197
A user is sending bulk emails using AWS SES. The emails are not reaching some of the targeted audience
because they are not authorized by the ISPs. How can the user ensure that the emails are all delivered?
A. Send an email using DKINI with SES.
B. Send an email using SMTP with SES.
C. Open a ticket with AWS support to get it authorized with the ISP.
D. Authorize the ISP by sending emails from the development account.
Correct Answer: A
Explanation
Explanation/Reference:
Domain Keys Identified MaiI (DKIM) is a standard that allows senders to sign their email messages and ISPs,
and use those signatures to verify that those messages are legitimate and have not been modified by a third
party in transit.
http://docs.aws.amazon.com/ses/latest/DeveloperGuide/dkim.html
QUESTION 198
In AWS CIoudHSM, in addition to the AWS recommendation that you use two or more HSM appliances in a
high-availability configuration to prevent the loss of keys and data, you can also perform a remote backup/
restore of a Luna SA partition if you have purchased a:
A. Luna Restore HSNI.
B. Luna Backup HSM.
C. Luna HSNI.
D. Luna SA HSM.
Correct Answer: B
Explanation
Explanation/Reference:
In AWS CIoudHSM, you can perform a remote backup/restore of a Luna SA partition if you have purchased a
Luna Backup HSM.
http://docs.aws.amazon.com/cloudhsm/latest/userguide/cloud-hsm-backup-restore.html
QUESTION 199
A user has launched a large EBS backed EC2 instance in the US-East-1a region. The user wants to achieve
Disaster Recovery (DR) for that instance by creating another small instance in Europe. How can the user
achieve DR?
A. Copy the instance from the US East region to the EU region
B. Use the "Launch more like this" option to copy the instance from one region to another
C. Copy the running instance using the "|nstance Copy" command to the EU region
D. Create an AMI of the instance and copy the AMI to the EU region. Then launch the instance from the EU
AMI
Correct Answer: D
Explanation
Explanation/Reference:
To launch an EC2 instance it is required to have an AMI in that region. If the AMI is not available in that region,
then create a new AMI or use the copy command to copy the AMI from one region to the other region. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.htmI
QUESTION 200
AWS Identity and Access Management is a web service that enables Amazon Web Services (AWS) customers
to manage users and user permissions in AWS. In addition to supporting IAM user policies, some services
support resource-based permissions. Which of the following services are supported by resource-based
permissions?
A. Amazon SNS, and Amazon SQS and AWS Direct Connect.
B. Amazon S3 and Amazon SQS and Amazon EIastiCache.
C. Amazon S3, Amazon SNS, Amazon SQS, Amazon Glacier and Amazon EBS.
D. Amazon Glacier, Amazon SNS, and Amazon CIoudWatch
Correct Answer: C
Explanation
Explanation/Reference:
In addition to supporting IAM user policies, some services support resource-based permissions, which let you
attach policies to the service's resources instead of to IAM users or groups. Resource-based permissions are
supported by Amazon S3, Amazon SNS, Amazon SQS, Amazon Glacier and Amazon EBS. http://
docs.aws.amazon.com/IAM/latest/UserGuide/Using_SpecificProducts.htm|
QUESTION 201
Content and IV|edia Server is the latest requirement that you need to meet for a client. The client has been
very specific about his requirements such as low latency, high availability, durability, and access control.
Potentially there will be millions of views on this server and because of "spiky" usage patterns, operations
teams will need to provision static hardware, network, and management resources to support the maximum
expected need. The Customer base will be initially low but is expected to grow and become more
geographically distributed.
Which of the following would be a good solution for content distribution?
A. Amazon S3 as both the origin server and for caching
B. AWS Storage Gateway as the origin server and Amazon EC2 for caching
C. AWS CIoudFront as both the origin server and for caching
D. Amazon S3 as the origin server and Amazon CIoudFront for caching
Correct Answer: D
Explanation
Explanation/Reference:
As your customer base grows and becomes more geographically distributed, using a high- performance edge
cache like Amazon CIoudFront can provide substantial improvements in latency, fault tolerance, and cost. By
using Amazon S3 as the origin server for the Amazon CIoudFront distribution, you gain the advantages of fast
in-network data transfer rates, simple publishing/caching workflow, and a unified security framework. Amazon
S3 and Amazon CIoudFront can be configured by a web service, the AWS Management Console, or a host of
third-party management tools.
http://media.amazonwebservices.com/architecturecenter/AWS_ac_ra_media_02.pdf
QUESTION 202
You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) network so you decide you should
probably use the AWS Management Console and the VPC Wizard. Which of the following is not an option for
network architectures after launching the "Start VPC Wizard" in Amazon VPC page on the AWS Management
Console?
A. VPC with a Single Public Subnet Only
B. VPC with a Public Subnet Only and Hardware VPN Access
C. VPC with Public and Private Subnets and Hardware VPN Access
D. VPC with a Private Subnet Only and Hardware VPN Access
Correct Answer: B
Explanation
Explanation/Reference:
Amazon VPC enables you to build a virtual network in the AWS cloud - no VPNs, hardware, or physical
datacenters required.
Your AWS resources are automatically provisioned in a ready-to-use default VPC. You can choose to create
additional VPCs by going to Amazon VPC page on the AWS Management Console and click on the "Start VPC
Wizard" button.
You'II be presented with four basic options for network architectures. After selecting an option, you can modify
the size and IP address range of the VPC and its subnets. If you select an option with Hardware VPN Access,
you will need to specify the IP address of the VPN hardware on your network. You can modify the VPC to add
more subnets or add or remove gateways at any time after the VPC has been created.
The four options are:
VPC with a Single Public Subnet Only
VPC with Public and Private Subnets
VPC with Public and Private Subnets and Hardware VPN Access VPC with a Private Subnet Only and
Hardware VPN Access
https://aws.amazon.com/vpc/faqs/
QUESTION 203
An EC2 instance is connected to an ENI (Elastic Network Interface) in one subnet. What happens when you
attach an ENI of a different subnet to this EC2 instance?
A. The EC2 instance follows the rules of the older subnet
B. The EC2 instance follows the rules of both the subnets
C. Not possible, cannot be connected to 2 ENIs
D. The EC2 instance follows the rules of the newer subnet
Correct Answer: B
Explanation
Explanation/Reference:
AWS allows you create an elastic network interface (ENI), attach an ENI to an EC2 instance, detach an ENI
from an EC2 instance and attach this ENI to another EC2 instance. The attributes of a network traffic follow the
ENI which is attached to an EC2 instance or detached from an EC2 instance. When you move an ENI from one
EC2 instance to another, network traffic is redirected to the new EC2 instance. You can create and attach
additional ENIs to an EC2 instance.
Attaching multiple network interfaces (ENIs) to an EC2 instance is useful to:
Create a management network.
Use network and security appliances in your VPC.
Create dual-homed instances with workloads/roles on distinct subnets Create a low-budget, high-availability
solution.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.htm|
QUESTION 204
Which one of the below doesn't affect Amazon CIoudFront billing?
A. Distribution Type
B. Data Transfer Out
C. Dedicated IP SSL Certificates
D. Requests
Correct Answer: A
Explanation
Explanation/Reference:
Amazon CIoudFront is a web service for content delivery. C|oudFront delivers your content using a global
network of edge locations and works seamlessly with Amazon S3 which durably stores the original and
definitive versions of your files.
Amazon CIoudFront billing is maily affected by
Data Transfer Out
Edge Location Traffic Distribution
Requests
Dedicated IP SSL Certificates
http://calcu|ator.s3.amazonaws.com/index.htmI
QUESTION 205
A user is trying to launch a similar EC2 instance from an existing instance with the option "Launch More like
this". The AMI ofthe selected instance is deleted. What will happen in this case?
A. AWS does not need an AMI for the "Launch more like this" option
B. AWS will launch the instance but will not create a new AMI
C. AWS will create a new AMI and launch the instance
D. AWS will throw an error saying that the AMI is deregistered
Correct Answer: D
Explanation
Explanation/Reference:
If the user has deregistered the AMI of an EC2 instance and is trying to launch a similar instance with the
option "Launch more like this", AWS will throw an error saying that the AMI is deregistered or not available.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html
QUESTION 206
Your company has multiple IT departments, each with their own VPC. Some VPCs are located within the same
AWS account, and others in a different AWS account. You want to peer together all VPCs to enable the IT
departments to have full access to each others' resources. There are certain limitations placed on VPC
peering. Which of the following statements is inin relation to VPC peering?
A. Private DNS values cannot be resolved between instances in peered VPCs.
B. You can have up to 3 VPC peering connections between the same two VPCs at the same time.
C. You cannot create a VPC peering connection between VPCs in different regions.
D. You have a limit on the number active and pending VPC peering connections that you can have per VPC.
Correct Answer: B
Explanation
Explanation/Reference:
To create a VPC peering connection with another VPC, you need to be aware of the following limitations and
rules:
You cannot create a VPC peering connection between VPCs that have matching or overlapping CIDR blocks.
You cannot create a VPC peering connection between VPCs in different regions. You have a limit on the
number active and pending VPC peering connections that you can have per VPC. VPC peering does not
support transitive peering relationships; in a VPC peering connection, your VPC will not have access to any
other VPCs that the peer VPC may be peered with. This includes VPC peering connections that are
established entirely within your own AWS account. You cannot have more than one VPC peering connection
between the same two VPCs at the same time. The Maximum Transmission Unit (MTU) across a VPC peering
connection is 1500 bytes. A placement group can span peered VPCs; however, you will not get full-bisection
bandwidth between instances in peered VPCs.
Unicast reverse path forwarding in VPC peering connections is not supported. You cannot reference a security
group from the peer VPC as a source or destination for ingress or egress rules in your security group. Instead,
reference CIDR blocks of the peer VPC as the source or destination of your security group's ingress or egress
rules.
Private DNS values cannot be resolved between instances in peered VPCs.
http://docs.aws.amazon.com/AmazonVPC/Iatest/PeeringGuide/vpc-peering-overview.htmI#vpc-peering-Ii
mitations
QUESTION 207
A company wants to review the security requirements of Glacier. Which of the below mentioned statements is
true with respect to the AWS Glacier data security?
A. All data stored on Glacier is protected with AES-256 serverside encryption.
B. All data stored on Glacier is protected with AES-128 serverside encryption.
C. The user can set the serverside encryption flag to encrypt the data stored on Glacier.
D. The data stored on Glacier is not encrypted by default.
Correct Answer: A
Explanation
Explanation/Reference:
For Amazon Web Services, all the data stored on Amazon Glacier is protected using serverside encryption.
AWS generates separate unique encryption keys for each Amazon Glacier archive, and encrypts it using AES-
256. The encryption key then encrypts itself using AES-256 with a master key that is stored in a secure
location.
http://media.amazonwebservices.com/AWS_Security_Best_Practices.pdf
QUESTION 208
You are architecting a highly-scalable and reliable web application which will have a huge amount of content
.You have decided to use Cloudfront as you know it will speed up distribution of your static and dynamic web
content and know that Amazon C|oudFront integrates with Amazon CIoudWatch metrics so that you can
monitor your web application. Because you live in Sydney you have chosen the the Asia Pacific (Sydney)
region in the AWS console. However you have set up this up but no CIoudFront metrics seem to be appearing
in the CIoudWatch console. What is the most likely reason from the possible choices below for this?
A. Metrics for CIoudWatch are available only when you choose the same region as the application you are
monitoring.
B. You need to pay for CIoudWatch for it to become active.
C. Metrics for CIoudWatch are available only when you choose the US East (N. Virginia)
D. Metrics for CIoudWatch are not available for the Asia Pacific region as yet.
Correct Answer: C
Explanation
Explanation/Reference:
CIoudFront is a global service, and metrics are available only when you choose the US East (N. Virginia)
region in the AWS console. If you choose another region, no CIoudFront metrics will appear in the CIoudWatch
console.
http://docs.aws.amazon.com/AmazonCIoudFront/latest/Deve|operGuide/monitoring-using-cloudwatch.ht ml
QUESTION 209
A friend wants you to set up a small BitTorrent storage area for him on Amazon S3. You tell him it is highly
unlikely that AWS would allow such a thing in their infrastructure. However you decide to investigate. Which of
the following statements best describes using BitTorrent with Amazon S3?
A. Amazon S3 does not support the BitTorrent protocol because it is used for pirated software.
B. You can use the BitTorrent protocol but only for objects that are less than 100 GB in size.
C. You can use the BitTorrent protocol but you need to ask AWS for specific permissions first.
D. You can use the BitTorrent protocol but only for objects that are less than 5 GB in size.
Correct Answer: D
Explanation
Explanation/Reference:
BitTorrent is an open, peer-to-peer protocol for distributing files. You can use the BitTorrent protocol to retrieve
any publicly-accessible object in Amazon S3.
Amazon S3 supports the BitTorrent protocol so that developers can save costs when distributing content at
high scale. Amazon S3 is useful for simple, reliable storage of any data. The default distribution mechanism for
Amazon S3 data is via client/server download. In client/server distribution, the entire object is transferred pointto-
point from Amazon S3 to every authorized user who requests that object. While client/server delivery is
appropriate for a wide variety of use cases, it is not optimal for everybody. Specifically, the costs of client/
server distribution increase linearly as the number of users downloading objects increases. This can make it
expensive to distribute popular objects. BitTorrent addresses this problem by recruiting the very clients that are
downloading the object as distributors themselves: Each client downloads some pieces of the object from
Amazon S3 and some from other clients, while simultaneously uploading pieces of the same object to other
interested "peers." The benefit for publishers is that for large, popular files the amount of data actually supplied
by Amazon S3 can be substantially lower than what it would have been sewing the same clients via client/
server download. Less data transferred means lower costs for the publisher of the object. http://
docs.aws.amazon.com/AmazonS3/latest/dev/S3Torrent.html
QUESTION 210
After a major security breach your manager has requested a report of all users and their credentials in AWS.
You discover that in IAM you can generate and download a credential report that lists all users in your account
and the status of their various credentials, including passwords, access keys, MFA devices, and signing
certificates. Which following statement is inin regards to the use of credential reports?
A. Credential reports are downloaded XML files.
B. You can get a credential report using the AWS Management Console, the AWS CLI, or the IAM API.
C. You can use the report to audit the effects of credential lifecycle requirements, such as password rotation.
D. You can generate a credential report as often as once every four hours.
Correct Answer: A
Explanation
Explanation/Reference:
To access your AWS account resources, users must have credentials. You can generate and download a
credential report that lists all users in your account and the status of their various credentials, including
passwords, access keys, MFA devices, and signing certificates. You can get a credential report using the AWS
Management Console, the AWS CLI, or the IAM API. You can use credential reports to assist in your auditing
and compliance efforts. You can use the report to audit the effects of credential lifecycle requirements, such as
password rotation. You can provide the report to an external auditor, or grant permissions to an auditor so that
he or she can download the report directly.
You can generate a credential report as often as once every four hours. When you request a report, IAM first
checks whether a report for the account has been generated within the past four hours. If so, the most recent
report is downloaded. If the most recent report for the account is more than four hours old, or if there are no
previous reports for the account, IAM generates and downloads a new report. Credential reports are
downloaded as comma-separated values (CSV) files. You can open CSV files with common spreadsheet
software to perform analysis, or you can build an application that consumes the CSV files programmatically
and performs custom analysis. http://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html
QUESTION 211
In the most recent company meeting, your CEO focused on the fact that everyone in the organization needs to
make sure that all of the infrastructure that is built is truly scalable. Which of the following statements is inin
reference to scalable architecture?
A. A scalable service is capable of handling heterogeneity.
B. A scalable service is resilient.
C. A scalable architecture won't be cost effective as it grows.
D. Increasing resources results in a proportional increase in performance.
Correct Answer: C
Explanation
Explanation/Reference:
In AWS it is critical to build a scalable architecture in order to take advantage of a scalable infrastructure. The
cloud is designed to provide conceptually infinite scalability. However, you cannot leverage all that scalability in
infrastructure if your architecture is not scalable. Both have to work together. You will have to identify the
monolithic components and bottlenecks in your architecture, identify the areas where you cannot leverage the
on-demand provisioning capabilities in your architecture, and work to refactor your application, in order to
leverage the scalable infrastructure and take advantage of the cloud.
Characteristics of a truly scalable application:
Increasing resources results in a proportional increase in performance A scalable service is capable of
handling heterogeneity
A scalable service is operationally efficient
A scalable service is resilient
A scalable service should become more cost effective when it grows (Cost per unit reduces as the number of
units increases)
http://media.amazonwebservices.com/AWS_CIoud_Best_Practices.pdf
QUESTION 212
A user has defined an AutoScaIing termination policy to first delete the instance with the nearest billing hour.
AutoScaIing has launched 3 instances in the US-East-1A region and 2 instances in the US-East-1 B region.
One of the instances in the US-East-1B region is running nearest to the billing hour. Which instance will
AutoScaIing terminate first while executing the termination action?
A. Random Instance from US-East-1A
B. Instance with the nearest billing hour in US-East-1 B
C. Instance with the nearest billing hour in US-East-1A
D. Random instance from US-East-1B
Correct Answer: C
Explanation
Explanation/Reference:
Even though the user has configured the termination policy, before AutoScaIing selects an instance to
terminate, it first identifies the Availability Zone that has more instances than the other Availability Zones used
by the group. Within the selected Availability Zone, it identifies the instance that matches the specified
termination policy.
http://docs.aws.amazon.com/AutoScaIing/latest/DeveIoperGuide/us-termination-policy.html
QUESTION 213
A user has configured a website and launched it using the Apache web server on port 80. The user is using
ELB with the EC2 instances for Load Balancing. What should the user do to ensure that the EC2 instances
accept requests only from ELB?
A. Configure the security group of EC2, which allows access to the ELB source security group
B. Configure the EC2 instance so that it only listens on the ELB port
C. Open the port for an ELB static IP in the EC2 security group
D. Configure the security group of EC2, which allows access only to the ELB listener
Correct Answer: A
Explanation
Explanation/Reference:
When a user is configuring ELB and registering the EC2 instances with it, ELB will create a source security
group. If the user wants to allow traffic only from ELB, he should remove all the rules set for the other requests
and open the port only for the ELB source security group.
http://docs.aws.amazon.com/EIasticLoadBaIancing/latest/DeveIoperGuide/using-elb-security-groups.htmI
QUESTION 214
A user is planning a highly available application deployment with EC2. Which of the below mentioned options
will not help to achieve HA?
A. Elastic IP address
B. PIOPS
C. AMI
D. Availability Zones
Correct Answer: B
Explanation
Explanation/Reference:
In Amazon Web Service, the user can achieve HA by deploying instances in multiple zones. The elastic IP
helps the user achieve HA when one of the instances is down but still keeps the same URL. The AM helps
launching the new instance. The PIOPS is for the performance of EBS and does not help for HA. http://
media.amazonwebservices.com/AWS_Web_Hosting_Best_Practices.pdf
QUESTION 215
You are playing around with setting up stacks using JSON templates in C|oudFormation to try and understand
them a little better. You have set up about 5 or 6 but now start to wonder if you are being charged for these
stacks. What is AWS's billing policy regarding stack resources?
A. You are not charged for the stack resources if they are not taking any traffic.
B. You are charged for the stack resources for the time they were operating (even if you deleted the stack right
away)
C. You are charged for the stack resources for the time they were operating (but not if you deleted the stack
within 60 minutes)
D. You are charged for the stack resources for the time they were operating (but not if you deleted the stack
within 30 minutes)
Correct Answer: B
Explanation
Explanation/Reference:
A stack is a collection of AWS resources that you can manage as a single unit. In other words, you can create,
update, or delete a collection of resources by creating, updating, or deleting stacks. All the resources in a stack
are defined by the stack's AWS CIoudFormation template. A stack, for instance, can include all the resources
required to run a web application, such as a web server, a database, and networking rules. If you no longer
require that web application, you can simply delete the stack, and all of its related resources are deleted. You
are charged for the stack resources for the time they were operating (even if you deleted the stack right away).
http://docs.aws.amazon.com/AWSCIoudFormation/latest/UserGuide/stacks.html
QUESTION 216
You have been given a scope to set up an AWS Media Sharing Framework for a new start up photo sharing
company similar to flickr. The first thing that comes to mind about this is that it will obviously need a huge
amount of persistent data storage for this framework. Which of the following storage options would be
appropriate for persistent storage?
A. Amazon Glacier or Amazon S3
B. Amazon Glacier or AWS Import/Export
C. AWS Import/Export or Amazon C|oudFront
D. Amazon EBS volumes or Amazon S3
Correct Answer: D
Explanation
Explanation/Reference:
Persistent storage-If you need persistent virtual disk storage similar to a physical disk drive for files or other
data that must persist longer than the lifetime of a single Amazon EC2 instance, Amazon EBS volumes or
Amazon S3 are more appropriate.
http://media.amazonwebservices.com/AWS_Storage_Options.pdf
QUESTION 217
After deploying a new website for a client on AWS, he asks if you can set it up so that if it fails it can be
automatically redirected to a backup website that he has stored on a dedicated server elsewhere. You are
wondering whether Amazon Route 53 can do this. Which statement below is in regards to Amazon Route 53?
A. Amazon Route 53 can't help detect an outage. You need to use another service.
B. Amazon Route 53 can help detect an outage of your website and redirect your end users to alternate
locations.
C. Amazon Route 53 can help detect an outage of your website but can't redirect your end users to alternate
locations.
D. Amazon Route 53 can't help detect an outage of your website, but can redirect your end users to alternate
locations.
Correct Answer: B
Explanation
Explanation/Reference:
With DNS Failover, Amazon Route 53 can help detect an outage of your website and redirect your end users to
alternate locations where your application is operating properly.
http://aws.amazon.com/about-aws/whats-new/2013/02/11/announcing-dns-faiIover-for-route-53/
QUESTION 218
In Route 53, what does a Hosted Zone refer to?
A. A hosted zone is a collection of geographical load balancing rules for Route 53.
B. A hosted zone is a collection of resource record sets hosted by Route 53.
C. A hosted zone is a selection of specific resource record sets hosted by CIoudFront for distribution to Route
S3.
D. A hosted zone is the Edge Location that hosts the Route 53 records for a user.
Correct Answer: B
Explanation
Explanation/Reference:
A Hosted Zone refers to a selection of resource record sets hosted by Route 53. http://docs.aws.amazon.com/
Route53/Iatest/DeveIoperGuide/AboutHostedZones.html
QUESTION 219
Which of the following statements is true of Amazon EC2 security groups?
A. You can change the outbound rules for EC2-Classic. Also, you can add and remove rules to a group at any
time.
B. You can modify an existing rule in a group. However, you can't add and remove rules to a group.
C. None of the statements are correct.
D. You can't change the outbound rules for EC2-Classic. However, you can add and remove rules to a group at
any time.
Correct Answer: D
Explanation
Explanation/Reference:
When dealing with security groups, bear in mind that you can freely add and remove rules from a group, but
you can't change the outbound rules for EC2-Classic. If you're using the Amazon EC2 console, you can modify
existing rules, and you can copy the rules from an existing security group to a new security group. http://
docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-network-security.htmI
QUESTION 220
Which DNS name can only be resolved within Amazon EC2?
A. Public DNS name
B. Internal DNS name
C. External DNS name
D. Global DNS name
Correct Answer: B
Explanation
Explanation/Reference:
Only Internal DNS name can be resolved within Amazon EC2.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-instance-addressing.htmI
QUESTION 221
While creating a network in the VPC, which of the following is true of a NAT device?
A. You have to administer the NAT Gateway Service provided by AWS.
B. You can choose to use any of the three kinds of NAT devices offered by AWS for special purposes.
C. You can use a NAT device to enable instances in a private subnet to connect to the Internet.
D. You are recommended to use AWS NAT instances over NAT gateways, as the instances provide better
availability and bandwidth.
Correct Answer: C
Explanation
Explanation/Reference:
You can use a NAT device to enable instances in a private subnet to connect to the Internet (for example, for
software updates) or other AWS services, but prevent the Internet from initiating connections with the
instances. AWS offers two kinds of NAT devices u a NAT gateway or a NAT instance. We recommend NAT
gateways, as they provide better availability and bandwidth over NAT instances. The NAT Gateway service is
also a managed service that does not require your administration efforts. A NAT instance is launched from a
NAT AM. You can choose to use a NAT instance for special purposes. http://docs.aws.amazon.com/
AmazonVPC/latest/UserGuide/vpc-nat.html
QUESTION 222
You need to create a management network using network interfaces for a virtual private cloud (VPC) network.
Which of the following statements is inpertaining to Best Practices for Configuring Network Interfaces.
A. You can detach secondary (ethN) network interfaces when the instance is running or stopped.
However, you can't detach the primary (eth0) interface.
B. Launching an instance with multiple network interfaces automatically configures interfaces, private IP
addresses, and route tables on the operating system of the instance.
C. You can attach a network interface in one subnet to an instance in another subnet in the same VPC,
however, both the network interface and the instance must reside in the same Availability Zone.
D. Attaching another network interface to an instance is a valid method to increase or double the network
bandwidth to or from the dual-homed instance
Correct Answer: D
Explanation
Explanation/Reference:
Best Practices for Configuring Network Interfaces
You can attach a network interface to an instance when it's running (hot attach), when it's stopped (warm
attach), or when the instance is being launched (cold attach). You can detach secondary (ethN) network
interfaces when the instance is running or stopped. However, you can't detach the primary (eth0) interface.
You can attach a network interface in one subnet to an instance in another subnet in the same VPC, however,
both the network interface and the instance must reside in the same Availability Zone. When launching an
instance from the CLI or API, you can specify the network interfaces to attach to the instance for both the
primary (eth0) and additional network interfaces. Launching an instance with multiple network interfaces
automatically configures interfaces, private IP addresses, and route tables on the operating system of the
instance. A warm or hot attach of an additional network interface may require you to manually bring up the
second interface, configure the private IP address, and modify the route table accordingly. (Instances running
Amazon Linux automatically recognize the warm or hot attach and configure themselves.) Attaching another
network interface to an instance is not a method to increase or double the network bandwidth to or from the
dual-homed instance.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.htmI#use-network-and-security-applia ncesin-
your-vpc
QUESTION 223
All Amazon EC2 instances are assigned two IP addresses at launch. Which are those?
A. 2 Elastic IP addresses
B. A private IP address and an Elastic IP address
C. A public IP address and an Elastic IP address
D. A private IP address and a public IP address
Correct Answer: D
Explanation
Explanation/Reference:
In Amazon EC2-Classic every instance is given two IP Addresses: a private IP address and a public IP
address
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.htmI#differences
QUESTION 224
Your manager has asked you to set up a public subnet with instances that can send and receive internet traffic,
and a private subnet that can't receive traffic directly from the internet, but can initiate traffic to the internet (and
receive responses) through a NAT instance in the public subnet. Hence, the following 3 rules need to be
allowed:
Inbound SSH traffic.
Web sewers in the public subnet to read and write to MS SQL servers in the private subnet Inbound RDP traffic
from the Microsoft Terminal Services gateway in the public private subnet What are the respective ports that
need to be opened for this?
A. Ports 22,1433,3389
B. Ports 21,1433,3389
C. Ports 25,1433,3389
D. Ports 22,1343,3999
Correct Answer: A
Explanation
Explanation/Reference:
A network access control list (ACL) is an optional layer of security that acts as a firewall for controlling traffic in
and out of a subnet. You might set up network ACLs with rules similar to your security groups in order to add
an additional layer of security to your VPC.
The following ports are recommended by AWS for a single subnet with instances that can receive and send
Internet traffic and a private subnet that can't receive traffic directly from the Internet. However, it can initiate
traffic to the Internet (and receive responses) through a NAT instance in the public subnet.
Inbound SSH traffic. Port 22
Web sewers in the public subnet to read and write to MS SQL sewers in the private subnet. Port 1433 Inbound
RDP traffic from the Microsoft Terminal Sewices gateway in the public private subnet. Port 3389
http://docs.aws.amazon.com/AmazonVPC/Iatest/UserGuide/VPC_Appendix_NACLs.htm|#VPC_Appendi
x_NAC Ls_Scenario_2
QUESTION 225
You want to establish a dedicated network connection from your premises to AWS in order to save money by
transferring data directly to AWS rather than through your internet service provider. You are sure there must be
some other benefits beyond cost savings. Which of the following would not be considered a benefit if you were
to establish such a connection?
A. Elasticity
B. Compatibility with all AWS services.
C. Private connectMty to your Amazon VPC.
D. Everything listed is a benefit.
Correct Answer: D
Explanation
Explanation/Reference:
AWS Direct Connect makes it easy to establish a dedicated network connection from your premises to AWS.
Using AWS Direct Connect, you can establish private connectMty between AWS and your datacenter, office, or
colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput,
and provide a more consistent network experience than internet-based connections. You could expect the
following benefits if you use AWS Direct Connect.
Reduced bandwidth costs
Consistent network performance
Compatibility with all AWS services
Private connectMty to your Amazon VPC
Elasticity
Simplicity
http://aws.amazon.com/directconnect/
QUESTION 226
A user has launched an EC2 instance. The instance got terminated as soon as it was launched. Which of the
below mentioned options is not a possible reason for this?
A. The user account has reached the maximum volume limit
B. The AM is missing. It is the required part
C. The snapshot is corrupt
D. The user account has reached the maximum EC2 instance limit
Correct Answer: D
Explanation
Explanation/Reference:
When the user account has reached the maximum number of EC2 instances, it will not be allowed to launch an
instance. AWS will throw an `Instance Limit Exceeded' error. For all other reasons, such as "AMI is missing
part", "Corrupt Snapshot" or "VoIume limit has reached" it will launch an EC2 instance and then terminate it.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_|nstanceStraightToTerminated.html
QUESTION 227
Can I change the EC2 security groups after an instance is launched in EC2-Classic?
A. Yes, you can change security groups after you launch an instance in EC2-Classic.
B. No, you cannot change security groups after you launch an instance in EC2-Classic.
C. Yes, you can only when you remove rules from a security group.
D. Yes, you can only when you add rules to a security group.
Correct Answer: B
Explanation
Explanation/Reference:
After you launch an instance in EC2-Classic, you can't change its security groups. However, you can add rules
to or remove rules from a security group, and those changes are automatically applied to all instances that are
associated with the security group.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-network-security.htmI
QUESTION 228
You can seamlessly join an EC2 instance to your directory domain. What connectMty do you need to be able
to connect remotely to this instance?
A. You must have IP connectMty to the instance from the network you are connecting from.
B. You must have the encryption keys to connect to the instance remotely.
C. You must have enough bandwidth to connect to the instance.
D. You must use MFA authentication to be able to connect to the instance remotely.
Correct Answer: A
Explanation
Explanation/Reference:
You can seamlessly join an EC2 instance to your directory domain when the instance is launched using the
Amazon EC2 Simple Systems Manager. If you need to manuallyjoin an EC2 instance to your domain, you must
launch the instance in the proper region and security group or subnet, then join the instance to the domain. To
be able to connect remotely to these instances, you must have IP connectMty to the instances from the
network you are connecting from. In most cases, this requires that an Internet gateway be attached to your
VPC and that the instance has a public IP address. http://docs.aws.amazon.com/directoryservice/latest/adminguide/
join_a_directory.html
QUESTION 229
George has launched three EC2 instances inside the US-East-1a zone with his AWS account. Ray has
launched two EC2 instances in the US-East-Ia zone with his AWS account. Which of the below mentioned
statements will help George and Ray understand the availability zone (AZ) concept better?
A. All the instances of George and Ray can communicate over a private IP with a minimal cost
B. The US-East-1a region of George and Ray can be different availability zones
C. All the instances of George and Ray can communicate over a private IP without any cost
D. The instances of George and Ray will be running in the same data centre
Correct Answer: B
Explanation
Explanation/Reference:
Each AWS region has multiple, isolated locations known as Availability Zones. To ensure that the AWS
resources are distributed across the Availability Zones for a region, AWS independently maps the Availability
Zones to identifiers for each account. In this case the Availability Zone US-East-Ia where George's EC2
instances are running might not be the same location as the US-East-Ia zone of Ray's EC2 instances. There is
no way for the user to coordinate the Availability Zones between accounts. http://docs.aws.amazon.com/
AWSEC2/latest/UserGuide/using-regions-availability-zones.html
QUESTION 230
You are in the process of moving your friend's WordPress site onto AWS to try and save him some money, and
you have told him that he should probably also move his domain name. He asks why he can't leave his domain
name where it is and just have his infrastructure on AWS. What would be an inresponse to his question?
A. Route 53 offers low query latency for your end users.
B. Route 53 is designed to automatically answer queries from the optimal location depending on network
conditions.
C. The globally distributed nature of AWS's DNS servers helps ensure a consistent ability to route your end
users to your application.
D. Route 53 supports Domain Name System Security Extensions (DNSSEC).
Correct Answer: D
Explanation
Explanation/Reference:
Amazon Route 53 provides highly available and scalable Domain Name System (DNS), domain name
registration, and health-checking web services.
Route 53 is built using AWS's highly available and reliable infrastructure. The globally distributed nature of our
DNS servers helps ensure a consistent ability to route your end users to your application by circumventing any
internet or network related issues. Route 53 is designed to provide the level of dependability required by
important applications. Using a global anycast network of DNS servers around the world, Route 53 is designed
to automatically answer queries from the optimal location depending on network conditions. As a result, the
service offers low query latency for your end users. Amazon Route 53 does not support Domain Name System
Security Extensions (DNSSEC) at this time.
https://aws.amazon.com/Route53/faqs/
QUESTION 231
Can you encrypt EBS volumes?
A. Yes, you can enable encryption when you create a new EBS volume using the AWS Management Console,
API, or CLI.
B. No, you should use a third-party software to perform raw block-level encryption of an EBS volume.
C. Yes, but you must use a third-party API for encrypting data before it's loaded on EBS.
D. Yes, you can encrypt with the special "ebs_encrypt" command through Amazon APIs.
Correct Answer: A
Explanation
Explanation/Reference:
With Amazon EBS encryption, you can now create an encrypted EBS volume and attach it to a supported
instance type. Data on the volume, disk I/O, and snapshots created from the volume are then all encrypted.
The encryption occurs on the servers that host the EC2 instances, providing encryption of data as it moves
between EC2 instances and EBS storage. EBS encryption is based on the industry standard AES-256
cryptographic algorithm.
To get started, simply enable encryption when you create a new EBS volume using the AWS Management
Console, API, or CLI. Amazon EBS encryption is available for all the latest EC2 instances in all commercially
available AWS regions.
https://aws.amazon.com/about-aws/whats-new/2014/05/21/Amazon-EBS-encryption-now-avai|abIe/
QUESTION 232
In Amazon EC2, you are billed instance-hours when .
A. your EC2 instance is in a running state
B. the instance exits from Amazon S3 console
C. your instance still exits the EC2 console
D. EC2 instances stop
Correct Answer: A
Explanation
Explanation/Reference:
You are billed instance-hours as long as your EC2 instance is in a running state.
http://aws.amazon.com/ec2/faqs/
QUESTION 233
A user has created an ELB with Auto Scaling. Which of the below mentioned offerings from ELB helps the user
to stop sending new requests traffic from the load balancer to the EC2 instance when the instance is being
deregistered while continuing in-flight requests?
A. ELB sticky session
B. ELB deregistration check
C. ELB auto registration Off
D. ELB connection draining
Correct Answer: D
Explanation
Explanation/Reference:
The Elastic Load Balancer connection draining feature causes the load balancer to stop sending new requests
to the back-end instances when the instances are deregistering or become unhealthy, while ensuring that inflight
requests continue to be served.
http://docs.aws.amazon.com/EIasticLoadBaIancing/latest/DeveIoperGuide/config-conn-drain.htmI
QUESTION 234
While controlling access to Amazon EC2 resources, which of the following acts as a firewall that controls the
traffic allowed to reach one or more instances?
A. A security group
B. An instance type
C. A storage cluster
D. An object
Correct Answer: A
Explanation
Explanation/Reference:
A security group acts as a firewall that controls the traffic allowed to reach one or more instances. When you
launch an instance, you assign it one or more security groups. http://docs.amazonwebservices.com/AWSEC2/
latest/UserGuide/UsingIAM.htmI
QUESTION 235
A user is running a webserver on EC2. The user wants to receive the SMS when the EC2 instance utilization is
above the threshold limit. Which AWS services should the user configure in this case?
A. AWS C|oudWatch + AWS SQS.
B. AWS CIoudWatch + AWS SNS.
C. AWS CIoudWatch + AWS SES.
D. AWS EC2 + AWS Cloudwatch.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon SNS makes it simple and cost-effective to push to mobile devices, such as iPhone, iPad, Android,
Kindle Fire, and internet connected smart devices, as well as pushing to other distributed services. In this case,
the user can configure that Cloudwatch sends an alarm on when the threshold is crossed to SNS which will
trigger an SMS.
http://aws.amazon.com/sns/
QUESTION 236
Just when you thought you knew every possible storage option on AWS you hear someone mention Reduced
Redundancy Storage (RRS) within Amazon S3. What is the ideal scenario to use Reduced Redundancy
Storage (RRS)?
A. Huge volumes of data
B. Sensitve data
C. Non-critical or reproducible data
D. Critical data
Correct Answer: C
Explanation
Explanation/Reference:
Reduced Redundancy Storage (RRS) is a new storage option within Amazon S3 that enables customers to
reduce their costs by storing non-critical, reproducible data at lower levels of redundancy than Amazon S3's
standard storage. RRS provides a lower cost, less durable, highly available storage option that is designed to
sustain the loss of data in a single facility.
RRS is ideal for non-critical or reproducible data.
For example, RRS is a cost-effective solution for sharing media content that is durably stored elsewhere. RRS
also makes sense if you are storing thumbnails and other resized images that can be easily reproduced from
an original image.
https://aws.amazon.com/s3/faqs/
QUESTION 237
A user is making a scalable web application with compartmentalization. The user wants the log module to be
able to be accessed by all the application functionalities in an asynchronous way. Each module of the
application sends data to the log module, and based on the resource availability it will process the logs.
Which AWS service helps this functionality?
A. AWS Simple Queue Service.
B. AWS Simple Notification Service.
C. AWS Simple Workflow Service.
D. AWS Simple Email Service.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Simple Queue Service (SQS) is a highly reliable distributed messaging system for storing messages
as they travel between computers. By using Amazon SQS, developers can simply move data between
distributed application components. It is used to achieve compartmentalization or loose coupling. In this case
all the modules will send a message to the logger queue and the data will be processed by queue as per the
resource availability.
http://media.amazonwebservices.com/AWS_Building_FauIt_To|erant_AppIications.pdf
QUESTION 238
You have some very sensitive data stored on AWS S3 and want to try every possible alternative to keeping it
secure in regards to access control. What are the mechanisms available for access control on AWS S3?
A. (IAM) policies, Access Control Lists (ACLs), bucket policies, and query string authentication.
B. (IAM) policies, Access Control Lists (ACLs) and bucket policies.
C. Access Control Lists (ACLs), bucket policies, and query string authentication
D. (IAM) policies, Access Control Lists (ACLs), bucket policies, query string authentication and encryption.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon S3 supports several mechanisms that give you filexibility to control who can access your data as well
as how, when, and where they can access it.
Amazon S3 provides four different access control mechanisms:
AWS Identity and Access Management (IAM) policies, Access Control Lists (ACLs), bucket policies, and query
string authentication.
IAM enables organizations to create and manage multiple users under a single AWS account. With IAM
policies, you can grant IAM users fine-grained control to your Amazon S3 bucket or objects. You can use ACLs
to selectively add (grant) certain permissions on indMdual objects. Amazon S3 bucket policies can be used to
add or deny permissions across some or all of the objects within a single bucket. With Query string
authentication, you have the ability to share Amazon S3 objects through URLs that are valid for a specified
period of time.
QUESTION 239
Your manager has come to you saying that he is very confused about the bills he is receMng from AWS as he
is getting different bills for every user and needs you to look into making it more understandable. Which of the
following would be the best solution to meet his request?
A. AWS Billing Aggregation
B. Consolidated Billing
C. Deferred Billing
D. Aggregated Billing
Correct Answer: B
Explanation
Explanation/Reference:
Consolidated Billing enables you to consolidate payment for multiple AWS accounts within your company by
designating a single paying account. Consolidated Billing enables you to see a combined view of AWS costs
incurred by all accounts, as well as obtain a detailed cost report for each of the indMdual AWS accounts
associated with your "Paying Account". Consolidated Billing is offered at no additional charge.
https://aws.amazon.com/bi|Iing/faqs/
QUESTION 240
A user is planning to host a mobile game on EC2 which sends notifications to active users on either high score
or the addition of new features. The user should get this notification when he is online on his mobile device.
Which of the below mentioned AWS services can help achieve this functionality?
A. AWS Simple Notification Service.
B. AWS Simple Email Service.
C. AWS Nlobile Communication Service.
D. AWS Simple Queue Service.
Correct Answer: A
Explanation
Explanation/Reference:
Amazon Simple Notification Service (Amazon SNS) is a fast, filexible, and fully managed push messaging
service. Amazon SNS makes it simple and cost-effective to push to mobile devices, such as iPhone, iPad,
Android, Kindle Fire, and internet connected smart devices, as well as pushing to other distributed services.
http://aws.amazon.com/sns
QUESTION 241
Which one of the following can't be used as an origin server with Amazon CIoudFront?
A. A web server running in your infrastructure
B. Amazon S3
C. Amazon Glacier
D. A web server running on Amazon EC2 instances
Correct Answer: C
Explanation
Explanation/Reference:
Amazon CIoudFront is designed to work with Amazon S3 as your origin server, customers can also use
Amazon C|oudFront with origin sewers running on Amazon EC2 instances or with any other custom origin.
http://docs.aws.amazon.com/AmazonCIoudFront/latest/DeveIoperGuide/distribution-web.html
QUESTION 242
You have written a CIoudFormation template that creates I Elastic Load Balancer fronting 2 EC2 Instances.
Which section of the template should you edit so that the DNS of the load balancer is returned upon creation of
the stack?
A. Resources
B. Outputs
C. Parameters
D. Mappings
Correct Answer: B
Explanation
Explanation/Reference:
You can use AWS CIoudFormation's sample templates or create your own templates to describe the AWS
resources, and any associated dependencies or runtime parameters, required to run your application.
http://docs.aws.amazon.com/AWSCIoudFormation/latest/UserGuide/outputs-section-structure.html
QUESTION 243
You have been asked to set up a database in AWS that will require frequent and granular updates. You know
that you will require a reasonable amount of storage space but are not sure of the best option. What is the
recommended storage option when you run a database on an instance with the above criteria?
A. Amazon S3
B. Amazon EBS
C. AWS Storage Gateway
D. Amazon Glacier
Correct Answer: B
Explanation
Explanation/Reference:
Amazon EBS provides durable, block-level storage volumes that you can attach to a running Amazon EC2
instance. You can use Amazon EBS as a primary storage device for data that requires frequent and granular
updates. For example, Amazon EBS is the recommended storage option when you run a database on an
instance.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html
QUESTION 244
You have been asked to set up monitoring of your network and you have decided that Cloudwatch would be
the best service to use. Amazon CIoudWatch monitors your Amazon Web Services (AWS) resources and the
applications you run on AWS in real-time. You can use CIoudWatch to collect and track metrics, which are the
variables you want to measure for your resources and applications. Which of the following items listed can
AWS Cloudwatch monitor?
A. Log files your applications generate.
B. All of the items listed on this page.
C. System-wide visibility into resource utilization, application performance, and operational health.
D. Custom metrics generated by your applications and services .
Correct Answer: B
Explanation
Explanation/Reference:
Amazon CIoudWatch can monitor AWS resources such as Amazon EC2 instances, Amazon DynamoDB
tables, and Amazon RDS DB instances, as well as custom metrics generated by your applications and
services, and any log files your applications generate. You can use Amazon CIoudWatch to gain system-wide
visibility into resource utilization, application performance, and operational health. You can use these insights
to react and keep your application running smoothly.
http://aws.amazon.com/cIoudwatch/
QUESTION 245
A user has hosted an application on EC2 instances. The EC2 instances are configured with ELB and Auto
Scaling. The application server session time out is 2 hours. The user wants to configure connection draining to
ensure that all in-flight requests are supported by ELB even though the instance is being deregistered. What
time out period should the user specify for connection draining?
A. 1 hour
B. 30 minutes
C. 5 minutes
D. 2 hours
Correct Answer: A
Explanation
Explanation/Reference:
The Elastic Load Balancer connection draining feature causes the load balancer to stop sending new requests
to the back-end instances when the instances are deregistering or become unhealthy, while ensuring that inflight
requests continue to be served. The user can specify a maximum time of 3600 seconds (1 hour) for the
load balancer to keep the connections alive before reporting the instance as deregistered. If the user does not
specify the maximum timeout period, by default, the load balancer will close the connections to the
deregistering instance after 300 seconds.
http://docs.aws.amazon.com/EIasticLoadBaIancing/latest/DeveIoperGuide/config-conn-drain.htmI
QUESTION 246
How can you apply more than 100 rules to an Amazon EC2-Classic?
A. By adding more security groups
B. You need to create a default security group specifying your required rules if you need to use more than 100
rules per security group.
C. By default the Amazon EC2 security groups support 500 rules.
D. You can't add more than 100 rules to security groups for an Amazon EC2 instance.
Correct Answer: D
Explanation
Explanation/Reference:
In EC2-Classic, you can associate an instance with up to 500 security groups and add up to 100 rules to a
security group.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/using-network-security.htmI
QUESTION 247
You need to quickly set up an email-sending service because a client needs to start using it in the next hour.
Amazon Simple Email Service (Amazon SES) seems to be the logical choice but there are several options
available to set it up. Which of the following options to set up SES would best meet the needs of the client?
A. Amazon SES console
B. AWS CIoudFormation
C. SMTP Interface
D. AWS Elastic Beanstalk
Correct Answer: A
Explanation
Explanation/Reference:
Amazon SES is an outbound-only email-sending service that provides an easy, cost-effective way for you to
send email.
There are several ways that you can send an email by using Amazon SES. You can use the Amazon SES
console, the Simple Mail Transfer Protocol (SMTP) interface, or you can call the Amazon SES API. Amazon
SES consoIe--This method is the quickest way to set up your system http://docs.aws.amazon.com/ses/latest/
DeveIoperGuide/\NeIcome.html
QUESTION 248
Identify a true statement about the On-Demand instances purchasing option provided by Amazon EC2.
A. Pay for the instances that you use by the hour, with no long-term commitments or up-front payments.
B. Make a low, one-time, up-front payment for an instance, reserve it for a one- or three-year term, and pay a
significantly lower hourly rate for these instances.
C. Pay for the instances that you use by the hour, with long-term commitments or up-front payments.
D. Make a high, one-time, all-front payment for an instance, reserve it for a one- or three-year term, and pay a
significantly higher hourly rate for these instances.
Correct Answer: A
Explanation
Explanation/Reference:
On-Demand instances allow you to pay for the instances that you use by the hour, with no long-term
commitments or up-front payments.
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-offerings.html
QUESTION 249
Which of the following statements is NOT true about using Elastic IP Address (EIP) in EC2-Classic and EC2-
VPC platforms?
A. In the EC2-VPC platform, the Elastic IP Address (EIP) does not remain associated with the instance when
you stop it.
B. In the EC2-Classic platform, stopping the instance disassociates the Elastic IP Address (EIP) from it.
C. In the EC2-VPC platform, if you have attached a second network interface to an instance, when you
disassociate the Elastic IP Address (EIP) from that instance, a new public IP address is not assigned to the
instance automatically; you'II have to associate an EIP with it manually.
D. In the EC2-Classic platform, if you disassociate an Elastic IP Address (EIP) from the instance, the instance
is automatically assigned a new public IP address within a few minutes.
Correct Answer: A
Explanation
Explanation/Reference:
In the EC2-Classic platform, when you associate an Elastic IP Address (EIP) with an instance, the instance's
current public IP address is released to the EC2-Classic public IP address pool. If you disassociate an EIP
from the instance, the instance is automatically assigned a new public IP address within a few minutes. In
addition, stopping the instance also disassociates the EIP from it. But in the EC2-VPC platform, when you
associate an EIP with an instance in a default Virtual Private Cloud (VPC), or an instance in which you
assigned a public IP to the eth0 network interface during launch, its current public IP address is released to the
EC2-VPC public IP address pool. If you disassociate an EIP from the instance, the instance is automatically
assigned a new public IP address within a few minutes. However, if you have attached a second network
interface to the instance, the instance is not automatically assigned a new public IP address; you'II have to
associate an EIP with it manually. The EIP remains associated with the instance when you stop it. http://
docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.htmI
QUESTION 250
You have a Business support plan with AWS. One of your EC2 instances is running Mcrosoft Windows Server
2008 R2 and you are having problems with the software. Can you receive support from AWS for this software?
A. Yes
B. No, AWS does not support any third-party software.
C. No, Mcrosoft Windows Server 2008 R2 is not supported.
D. No, you need to be on the enterprise support plan.
Correct Answer: A
Explanation
Explanation/Reference:
Third-party software support is available only to AWS Support customers enrolled for Business or Enterprise
Support. Third-party support applies only to software running on Amazon EC2 and does not extend to assisting
with on-premises software. An exception to this is a VPN tunnel configuration running supported devices for
Amazon VPC.
https://aws.amazon.com/premiumsupport/features/
QUESTION 251
In Amazon EC2, how many Elastic IP addresses can you have by default?
A. 10
B. 2
C. 5
D. 20
Correct Answer: C
Explanation
Explanation/Reference:
The number of Elastic IP addresses you can have in EC2 is 5. http://docs.aws.amazon.com/generaI/latest/gr/
aws_service_Iimits.htmI#|imits_ec2
QUESTION 252
After deciding that EMR will be useful in analysing vast amounts of data for a gaming website that you are
architecting you have just deployed an Amazon EMR Cluster and wish to monitor the cluster performance.
Which of the following tools cannot be used to monitor the cluster performance?
A. Kinesis
B. Ganglia
C. C|oudWatch Metrics
D. Hadoop Web Interfaces
Correct Answer: A
Explanation
Explanation/Reference:
Amazon EMR provides several tools to monitor the performance of your cluster.
Hadoop Web Interfaces
Every cluster publishes a set of web interfaces on the master node that contain information about the cluster.
You can access these web pages by using an SSH tunnel to connect them on the master node. For more
information, see View Web Interfaces Hosted on Amazon EMR Clusters.
CIoudWatch Metrics
Every cluster reports metrics to CIoudWatch. CIoudWatch is a web service that tracks metrics, and which you
can use to set alarms on those metrics. For more information, see Monitor Metrics with CIoudWatch.
Ganglia
Ganglia is a cluster monitoring tool. To have this available, you have to install Ganglia on the cluster when you
launch it. After you've done so, you can monitor the cluster as it runs by using an SSH tunnel to connect to the
Ganglia UI running on the master node. For more information, see Monitor Performance with Ganglia.
http://docs.aws.amazon.com/EIasticMapReduce/latest/DeveIoperGuide/emr-troubleshoot-tooIs.htmI
QUESTION 253
A user has launched one EC2 instance in the US West region. The user wants to access the RDS instance
launched in the US East region from that EC2 instance. How can the user configure the access for that EC2
instance?
A. Configure the IP range of the US West region instance as the ingress security rule of RDS
B. It is not possible to access RDS of the US East region from the US West region
C. Open the security group of the US West region in the RDS security group's ingress rule
D. Create an IAM role which has access to RDS and launch an instance in the US West region with it
Correct Answer: A
Explanation
Explanation/Reference:
The user cannot authorize an Amazon EC2 security group if it is in a different AWS Region than the RDS DB
instance. The user can authorize an IP range or specify an Amazon EC2 security group in the same region that
refers to an IP address in another region.
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html
QUESTION 254
You need to create a load balancer in a VPC network that you are building. You can make your load balancer
internal (private) or internet-facing (public). When you make your load balancer internal, a DNS name will be
created, and it will contain the private IP address of the load balancer. An internal load balancer is not exposed
to the internet. When you make your load balancer internet-facing, a DNS name will be created with the public
IP address. If you want the Internet-facing load balancer to be connected to the Internet, where must this load
balancer reside?
A. The load balancer must reside in a subnet that is connected to the internet using the internet gateway.
B. The load balancer must reside in a subnet that is not connected to the internet.
C. The load balancer must not reside in a subnet that is connected to the internet.
D. The load balancer must be completely outside of your VPC.
Correct Answer: A
Explanation
Explanation/Reference:
When you create an internal Elastic Load Balancer in a VPC, you need to select private subnets that are in the
same Availability Zone as your instances. If the VPC Elastic Load Balancer is to be public facing, you need to
create the Elastic Load Balancer in a public subnet. A subnet is a public subnet if it is attached to an Internet
Gateway (IGW) with a defined route to that gateway. Selecting more than one public subnet increases the
availability of your Elastic Load Balancer. NB - Elastic Load Balancers in EC2-Classic are always Internetfacing
load balancers.
http://docs.aws.amazon.com/EIasticLoadBaIancing/|atest/DeveIoperGuide/elb-internet-facing-load-baIan
cers.htmI
QUESTION 255
Can you move a Reserved Instance from one Availability Zone to another?
A. Yes, but each Reserved Instance is associated with a specific Region that cannot be changed.
B. Yes, only in US-West-2.
C. Yes, only in US-East-1.
D. No
Correct Answer: A
Explanation
Explanation/Reference:
Each Reserved Instance is associated with a specific Region, which is fixed for the lifetime of the reservation
and cannot be changed. Each reservation can, however, be used in any of the available AZs within the
associated Region.
https://aws.amazon.com/rds/faqs/
QUESTION 256
An application hosted at the EC2 instance receives an HTTP request from ELB. The same request has an XForvvarded-
For header, which has three IP addresses. Which system's IP will be a part of this header?
A. Previous Request IP address.
B. Client IP address.
C. All of the answers listed here.
D. Load Balancer IP address.
Correct Answer: C
Explanation
Explanation/Reference:
When a user sends a request to ELB over HTTP/HTTPS, the request header log at the instance will only
receive the IP of ELB. This is because ELB is the interceptor between the EC2 instance and the client request.
To get the client IP, use the header X-Forvvarded-For in header. The client IP address in the X-Fonzvarded-
For request header is followed by the IP addresses of each successive proxy that passes along the request.
The last IP address is the IP address that connects to the back-end application instance. e.g. if the HTTP
request already has a header when it reaches the Load Balancer, the IP address from which the request came
is appended at the end of the header followed by the IP address of the Load Balancer. In such cases, the XForvvarded-
For request header takes the following form:
X-Fonzvarded-For: cIientIPAddress, previousRequestIPAddress, LoadBaIancerIPAddress.
http://docs.aws.amazon.com/E|asticLoadBaIancing/Iatest/DeveIoperGuide/TerminologyandKeyConcepts.
html
QUESTION 257
You need to develop and run some new applications on AWS and you know that Elastic Beanstalk and
CIoudFormation can both help as a deployment mechanism for a broad range of AWS resources. Which of the
following statements best describes the differences between Elastic Beanstalk and C|oudFormation?
A. Elastic Beanstalk uses Elastic load balancing and CIoudFormation doesn't.
B. CIoudFormation is faster in deploying applications than Elastic Beanstalk.
C. Elastic Beanstalk is faster in deploying applications than C|oudFormation.
D. CIoudFormation is much more powerful than Elastic Beanstalk, because you can actually design and script
custom resources
Correct Answer: D
Explanation
Explanation/Reference:
These services are designed to complement each other. AWS Elastic Beanstalk provides an environment to
easily develop and run applications in the cloud. It is integrated with developer tools and provides a one-stop
experience for you to manage the lifecycle of your applications. AWS CIoudFormation is a convenient
deployment mechanism for a broad range of AWS resources. It supports the infrastructure needs of many
different types of applications such as existing enterprise applications, legacy applications, applications built
using a variety of AWS resources and container-based solutions (including those built using AWS Elastic
Beanstalk).
AWS CIoudFormation introduces two new concepts: The template, a JSON-format, text-based file that
describes all the AWS resources you need to deploy to run your application and the stack, the set of AWS
resources that are created and managed as a single unit when AWS CIoudFormation instantiates a template.
http://aws.amazon.com/c|oudformation/faqs/
QUESTION 258
You need to set up a security certificate for a cIient's e-commerce website as it will use the HTTPS protocol.
Which of the below AWS services do you need to access to manage your SSL server certificate?
A. AWS Directory Service
B. AWS Identity & Access Management
C. AWS CIoudFormation
D. Amazon Route 53
Correct Answer: B
Explanation
Explanation/Reference:
AWS Identity and Access Management (IAM) is a web service that enables Amazon Web Services (AWS)
customers to manage users and user permissions in AWS.
All your SSL server certificates are managed by AWS Identity and Access management (IAM). http://
docs.aws.amazon.com/IAM/latest/UserGuide/ManagingServerCerts.htm|
QUESTION 259
When controlling access to Amazon EC2 resources, each Amazon EBS Snapshot has a attribute that controls
which AWS accounts can use the snapshot.
A. createVoIumePermission
B. LaunchPermission
C. SharePermission
D. RequestPermission
Correct Answer: A
Explanation
Explanation/Reference:
Each Amazon EBS Snapshot has a createVoIumePermission attribute that you can set to one or more AWS
Account IDs to share the AM with those AWS Accounts. To allow several AWS Accounts to use a particular
EBS snapshot, you can use the snapshots's createVoIumePermission attribute to include a list of the accounts
that can use it.
http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/UsingIAM.html
QUESTION 260
A 3-tier e-commerce web application is current deployed on-premises and will be migrated to AWS for greater
scalability and elasticity The web server currently shares read-only data using a network distributed file system
The app server tier uses a clustering mechanism for discovery and shared session state that depends on I P
multicast The database tier uses shared-storage clustering to provide database fail over capability, and uses
several read slaves for scaling Data on all sewers and the distributed file system directory is backed up weekly
to off-site tapes
Which AWS storage and database architecture meets the requirements of the application?
A. Web sewers: store read-only data in S3, and copy from S3 to root volume at boot time. App servers:
share state using a combination of DynamoDB and IP unicast. Database: use RDS with multi-AZ
deployment and one or more read replicas. Backup: web servers, app servers, and database backed up
weekly to Glacier using snapshots.
B. Web sewers: store read-only data in an EC2 NFS server, mount to each web server at boot time. App
servers: share state using a combination of DynamoDB and IP multicast. Database: use RDS with multi-AZ
deployment and one or more Read Replicas. Backup: web and app servers backed up weekly via AM Is,
database backed up via DB snapshots.
C. Web servers: store read-only data in S3, and copy from S3 to root volume at boot time. App servers:
share state using a combination of DynamoDB and IP unicast. Database: use RDS with multi-AZ
deployment and one or more Read Replicas. Backup: web and app servers backed up weekly via AM Is,
database backed up via DB snapshots.
D. Web servers: store read-only data in S3, and copy from S3 to root volume at boot time. App servers:
share state using a combination of DynamoDB and IP unicast. Database: use RDS with multi-AZ
deployment. Backup: web and app sewers backed up weekly via ANI Is, database backed up via DB
snapshots.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) Instances,
making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance,
Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby
instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent
infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure (for example, instance
hardware failure, storage failure, or network disruption), Amazon RDS performs an automatic failover to the
standby, so that you can resume database operations as soon as the failover is complete. Since the endpoint
for your DB Instance remains the same after a failover, your application can resume database operation
without the need for manual administrative intervention.
Benefits
Enhanced Durability
MuIti-AZ deployments for the MySQL, Oracle, and PostgreSQL engines utilize synchronous physical
replication to keep data on the standby up-to-date with the primary. MuIti-AZ deployments for the SQL Server
engine use synchronous logical replication to achieve the same result, employing SQL Server-native Mrroring
technology. Both approaches safeguard your data in the event of a DB Instance failure or loss of an Availability
Zone.
If a storage volume on your primary fails in a Multi-AZ deployment, Amazon RDS automatically initiates a
failover to the up-to-date standby. Compare this to a Single-AZ deployment: in case of a Single-AZ database
failure, a user-initiated point-in-time-restore operation will be required. This operation can take several hours to
complete, and any data updates that occurred after the latest restorable time (typically within the last five
minutes) will not be available.
Amazon Aurora employs a highly durable, SSD-backed virtualized storage layer purpose-built for database
workloads. Amazon Aurora automatically replicates your volume six ways, across three Availability Zones.
Amazon Aurora storage is fault-tolerant, transparently handling the loss of up to two copies of data without
affecting database write availability and up to three copies without affecting read availability. Amazon Aurora
storage is also self-healing. Data blocks and disks are continuously scanned for errors and replaced
automatically.
Increased Availability
You also benefit from enhanced database availability when running Multi-AZ deployments. If an Availability
Zone failure or DB Instance failure occurs, your availability impact is limited to the time automatic failover takes
to complete: typically under one minute for Amazon Aurora and one to two minutes for other database engines
(see the RDS FAQ for details). The availability benefits of MuIti-AZ deployments also extend to planned
maintenance and backups. In the case of system upgrades like OS patching or DB Instance scaling, these
operations are applied first on the standby, prior to the automatic failover. As a result, your availability impact
is, again, only the time required for automatic fail over to complete. Unlike Single-AZ deployments, 1/0 actMty
is not suspended on your primary during backup for MuIti-AZ deployments for the MySOL, Oracle, and
PostgreSQL engines, because the backup is taken from the standby. However, note that you may still
experience elevated latencies for a few minutes during backups for Mu|ti-AZ deployments.
On instance failure in Amazon Aurora deployments, Amazon RDS uses RDS MuIti-AZ technology to automate
failover to one of up to 15 Amazon Aurora Replicas you have created in any of three Availability Zones. If no
Amazon Aurora Replicas have been provisioned, in the case of a failure, Amazon RDS will attempt to create a
new Amazon Aurora DB instance for you automatically.
No Administrative Intervention
DB Instance failover is fully automatic and requires no administrative intervention. Amazon RDS monitors the
health of your primary and standbys, and initiates a failover automatically in response to a variety of failure
conditions.
Failover conditions
Amazon RDS detects and automatically recovers from the most common failure scenarios for Multi-AZ
deployments so that you can resume database operations as quickly as possible without administrative
intervention. Amazon RDS automatically performs a failover in the event of any of the following:
Loss of availability in primary Availability Zone
Loss of network connectMty to primary
Compute unit failure on primary
Storage failure on primary
Note: When operations such as DB Instance scaling or system upgrades like OS patching are initiated for
Multi-AZ deployments, for enhanced availability, they are applied first on the standby prior to an automatic
failover. As a result, your availability impact is limited only to the time required for automatic failover to
complete. Note that Amazon RDS Multi-AZ deployments do not failover automatically in response to database
operations such as long running queries, deadlocks or database corruption errors.
QUESTION 261
Your customer wishes to deploy an enterprise application to AWS which will consist of several web servers,
several application servers and a small (50GB) Oracle database information is stored, both in the database
and the file systems of the various servers. The backup system must support database recovery whole server
and whole disk restores, and indMdual file restores with a recovery time of no more than two hours. They have
chosen to use RDS Oracle as the database
Which backup architecture will meet these requirements?
A. Backup RDS using automated daily DB backups Backup the EC2 instances using AMs and supplement with
file-level backup to S3 using traditional enterprise backup software to provide fi Ie level restore
B. Backup RDS using a Multi-AZ Deployment Backup the EC2 instances using Amis, and supplement by
copying file system data to S3 to provide file level restore.
C. Backup RDS using automated daily DB backups Backup the EC2 instances using EBS snapshots and
supplement with file-level backups to Amazon Glacier using traditional enterprise backup software to
provide file level restore
D. Backup RDS database to S3 using Oracle RMAN Backup the EC2 instances using Amis, and supplement
with EBS snapshots for indMdual volume restore.
Correct Answer: A
Explanation
Explanation/Reference:
Point-In-Time Recovery
In addition to the daily automated backup, Amazon RDS archives database change logs. This enables you to
recover your database to any point in time during the backup retention period, up to the last five minutes of
database usage.
Amazon RDS stores multiple copies of your data, but for Single-AZ DB instances these copies are stored in a
single availability zone. If for any reason a Single-AZ DB instance becomes unusable, you can use point-intime
recovery to launch a new DB instance with the latest restorable data. For more information on working
with point-in-time recovery, go to Restoring a DB Instance to a Specified Time.
Note
Mu|ti-AZ deployments store copies of your data in different Availability Zones for greater levels of data
durability. For more information on Multi-AZ deployments, see High Availability (MuIti-AZ).
QUESTION 262
Your company has HQ in Tokyo and branch offices all over the world and is using a logistics software with a
multi-regional deployment on AWS in Japan, Europe and USA, The logistic software has a 3- tier architecture
and currently uses MySQL 5.6 for data persistence. Each region has deployed its own database In the HQ
region you run an hourly batch process reading data from every region to compute cross regional reports that
are sent by email to all offices this batch process must be completed as fast as possible to quickly optimize
logistics how do you build the database architecture in order to meet the requirements'?
A. For each regional deployment, use RDS MySQL with a master in the region and a read replica in the HQ
region
B. For each regional deployment, use MySQL on EC2 with a master in the region and send hourly EBS
snapshots to the HQ region
C. For each regional deployment, use RDS MySQL with a master in the region and send hourly RDS
snapshots to the HQ region
D. For each regional deployment, use MySQL on EC2 with a master in the region and use S3 to copy data files
hourly to the HQ region
E. Use Direct Connect to connect all regional MySQL deployments to the HQ region and reduce network
latency for the batch process
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 263
A customer has a 10 GB AWS Direct Connect connection to an AWS region where they have a web
application hosted on Amazon Elastic Computer Cloud (EC2). The application has dependencies on an onpremises
mainframe database that uses a BASE (Basic Available. Sort stale Eventual consistency) rather than
an ACID (Atomicity. Consistency isolation. Durability) consistency model. The application is exhibiting
undesirable behavior because the database is not able to handle the volume of writes. How can you reduce the
load on your on-premises database resources in the most cost-effective way?
A. Use an Amazon Elastic Map Reduce (EMR) S3DistCp as a synchronization mechanism between the onpremises
database and a Hadoop cluster on AWS.
B. Modify the application to write to an Amazon SQS queue and develop a worker process to flush the queue
to the on-premises database.
C. Modify the application to use DynamoDB to feed an EMR cluster which uses a map function to write to the
on-premises database.
D. Provision an RDS read-replica database on AWS to handle the writes and synchronize the two databases
using Data Pipeline.
Correct Answer: A
Explanation
Explanation/Reference:
https://aws.amazon.com/blogs/aws/category/amazon-elastic-map-reduce/
QUESTION 264
Company B is launching a new game app for mobile devices. Users will log into the game using their existing
social media account to streamline data capture. Company B would like to directly save player data and
scoring information from the mobile app to a DynamoDS table named Score Data When a user saves their
game the progress data will be stored to the Game state S3 bucket. What is the best approach for storing data
to DynamoDB and S3?
A. Use an EC2 Instance that is launched with an EC2 role providing access to the Score Data DynamoDB
table and the GameState S3 bucket that communicates with the mobile app via web services.
B. Use temporary security credentials that assume a role providing access to the Score Data DynamoDB table
and the Game State S3 bucket using web identity federation.
C. Use Login with Amazon allowing users to sign in with an Amazon account providing the mobile app with
access to the Score Data DynamoDB table and the Game State S3 bucket.
D. Use an IAM user with access credentials assigned a role providing access to the Score Data DynamoDB
table and the Game State S3 bucket for distribution with the mobile app.
Correct Answer: B
Explanation
Explanation/Reference:
Web Identity Federation
Imagine that you are creating a mobile app that accesses AWS resources, such as a game that runs on a
mobile device and stores player and score information using Amazon S3 and DynamoDB. When you write
such an app, you'II make requests to AWS services that must be signed with an AWS access key. However,
we strongly recommend that you do not embed or distribute long-term AWS credentials with apps that a user
downloads to a device, even in an encrypted store. Instead, build your app so that it requests temporary AWS
security credentials dynamically when needed using web identity federation. The supplied temporary
credentials map to an AWS role that has only the permissions needed to perform the tasks required by the
mobile app.
With web identity federation, you don't need to create custom sign-in code or manage your own user identities.
Instead, users of your app can sign in using a well-known identity provider (IdP) - such as Login with Amazon,
Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP, receive an authentication token, and
then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions
to use the resources in your AWS account. Using an IdP helps you keep your AWS account secure, because
you don't have to embed and distribute longterm security credentials with your application. For most scenarios,
we recommend that you use Amazon Cognito because it acts as an identity broker and does much of the
federation work for you. For details, see the following section, Using Amazon Cognito for MobiIe Apps.
If you don't use Amazon Cognito, then you must write code that interacts with a web IdP (Login with Amazon,
Facebook, Google, or any other OIDC-compatible IdP) and then calls the Assume Role With Web Identity API
to trade the authentication token you get from those IdPs for AWS temporary security credentials. If you have
already used this approach for existing apps, you can continue to use it.
Using Amazon Cognito for Nlobile Apps
The preferred way to use web identity federation is to use Amazon Cognito. For example, Adele the developer
is building a game for a mobile device where user data such as scores and profiles is stored in Amazon S3 and
Amazon DynamoDB. Adele could also store this data locally on the device and use Amazon Cognito to keep it
synchronized across devices. She knows that for security and maintenance reasons, long-term AWS security
credentials should not be distributed with the game. She also knows that the game might have a large number
of users. For all of these reasons, she does not want to create new user identities in IAM for each player.
Instead, she builds the game so that users can sign in using an identity that they've already established with a
well-known identity provider, such as Login with Amazon, Facebook, Google, or any OpenID Connect {OIDC)-
compatible identity provider. Her game can take advantage of the authentication mechanism from one of these
providers to validate the user's identity.
To enable the mobile app to access her AWS resources, Adele first registers for a developer 10 with her
chosen IdPs. She also configures the application with each of these providers. In her AWS account that
contains the Amazon S3 bucket and DynamoDB table for the game, Adele uses Amazon Cognito to create IAM
roles that precisely define permissions that the game needs. If she is using an OIDC IdP, she also creates an
IAM OIDC identity provider entity to establish t rust between her AWS account and the IdP. In the app's code,
Adele calls the sign-in interface for the IdP that she configured previously. The IdP handles all the details of
letting the user sign in, and the app gets an OAuth access token or OIDC ID token from the provider. AdeIe's
app can trade this authentication information for a set of temporary security credentials that consist of an AWS
access key 10, a secret access key, and a session token. The app can then use these credentials to access
web services offered by AWS. The app is limited to the permissions that are defined in the role that it assumes.
The following figure shows a simplified flow for how this might work, using Login with Amazon as the IdP. For
Step 2, the app can also use Facebook, Google, or any OIDC-compatible identity provider, but that's not shown
here.
Sample workflow using Amazon Cognito to federate users for a mobile application
A customer starts your app on a mobile device. The app asks the user to sign in. The app uses Login with
Amazon resources to accept the user's credentials. The app uses Cognito APIs to exchange the Login with
Amazon 10 token for a Cognito token. The app requests temporary security credentials from AWS STS,
passing the Cognito token. The temporary security credentials can be used by the app to access any AWS
resources required by the app to operate. The role associated with the temporary security credentials and its
assigned policies determines what can be accessed.
Use the following process to configure your app to use Amazon Cognito to authenticate users and give your
app access to AWS resources. For specific steps to accomplish this scenario, consult the documentation for
Amazon Cognito.
(Optional) Sign up as a developer with Login with Amazon, Facebook, Google, or any other OpenID Connect
(OIDC}-compatible identity provider and configure one or more apps with the provider. This step is optional
because Amazon Cognito also supports unauthenticated (guest) access for your users. Go to Amazon Cognito
in the AWS IV|anagement Console. Use the Amazon Cognito wizard to create an identity pool, which is a
container that Amazon Cognito uses to keep end user identities organized for your apps. You can share
identity pools between apps. When you set up an identity pool, Amazon Cognito creates one or two IAM roles
(one for authenticated identities, and one for unauthenticated "guest" identities) that define permissions for
Amazon Cognito users. Download and integrate the AWS SDK for iOS or the AWS SDK for Android with your
app, and import the files required to use Amazon Cognito.
Create an instance of the Amazon Cognito credentials provider, passing the identity pool ID, your AWS
account number, and the Amazon Resource Name (ARN) of the ro les that you associated with the identity
pool. The Amazon Cognito wizard in the AWS Management Console provides sample code to help you get
started.
When your app accesses an AWS resource, pass the credentials provider instance to the client object, which
passes temporary security credentials to the client. The permissions for the credentials are based on the role
or roles that you defined earlier.
QUESTION 265
Your company plans to host a large donation website on Amazon Web Services (AWS). You anticipate a large
and undetermined amount of traffic that will create many database writes. To be certain that you do not drop
any writes to a database hosted on AWS. Which service should you use?
A. Amazon RDS with provisioned IOPS up to the anticipated peak write throughput.
B. Amazon Simple Queue Service (SOS) for capturing the writes and draining the queue to write to the
database.
C. Amazon EIastiCache to store the writes until the writes are committed to the database.
D. Amazon DynamoDB with provisioned write throughput up to the anticipated peak write throughput.
Correct Answer: B
Explanation
Explanation/Reference:
Amazon Simple Queue Service (Amazon SQS) offers a reliable, highly scalable hosted queue for storing
messages as they travel between computers. By using Amazon SQS, developers can simply move data
between distributed application components performing different tasks, without losing messages or requiring
each component to be always available. Amazon SQS makes it easy to build a distributed, decoupled
application, working in close conjunction with the Amazon Elastic Compute Cloud (Amazon EC2) and the other
AWS infrastructure web services.
What can I do with Amazon SQS?
Amazon SQS is a web service that gives you access to a message queue that can be used to store messages
while waiting for a computer to process them. This allows you to quickly build message queuing applications
that can be run on any computer on the internet. Since Amazon SQS is highly scalable and you only pay for
what you use, you can start small and grow your application as you wish, with no compromise on performance
or reliability. This lets you focus on building sophisticated message-based applications, without worrying about
how the messages are stored and managed. You can use Amazon SQS with software applications in various
ways. For example, you can: Integrate Amazon SQS with other AWS infrastructure web services to make
applications more reliable and filexible. Use Amazon SQS to create a queue of work where each message is a
task that needs to be completed by a process. One or many computers can read tasks from the queue and
perform them. Build a microservices architecture, using queues to connect your microservices. Keep
notifications of significant events in a business process in an Amazon SQS queue. Each event can have a
corresponding message in a queue, and applications that need to be aware of the event can read and process
the messages.
QUESTION 266
You have launched an EC2 instance with four (4) 500GB EBS Provisioned IOPS volumes attached The EC2
Instance Is EBS-Optimized and supports 500 Mbps throughput between EC2 and EBS The two EBS volumes
are configured as a single RAID o device, and each Provisioned IOPS volume is provisioned with 4.000 IOPS
(4 000 16KB reads or writes) for a total of 16.000 random IOPS on the instance The EC2 Instance initially
delivers the expected 16 000 IOPS random read and write performance Sometime later in order to increase the
total random 1/0 performance of the instance, you add an additional two 500 GB EBS Provisioned IOPS
volumes to the RAID Each volume Is provisioned to 4.000 IOPs like the original four for a total of 24.000 IOPS
on the EC2 instance Monitoring shows that the EC2 instance CPU utilization increased from 50% to 70%. but
the total random IOPS measured at the instance level does not increase at all.
What is the problem and a valid solution?
A. Larger storage volumes support higher Provisioned IOPS rates: increase the provisioned volume storage of
each of the 6 EBS volumes to ITB
B. The EBS-Optimized throughput limits the total IOPS that can be utilized use an EBS-Optimized instance that
provides larger throughput.
C. Small block sizes cause performance degradation, limiting the 1'0 throughput, configure the instance device
driver and file system to use 64KB blocks to increase throughput.
D. RAID 0 only scales linearly to about 4 devices, use RAID 0 with 4 EBS Provisioned IOPS volumes but
increase each Provisioned IOPS EBS volume to 6.000 IOPS.
E. The standard EBS instance root volume limits the total IOPS rate, change the instant root volume to also be
a 500GB 4.000 Provisioned IOPS volume.
Correct Answer: E
Explanation
Explanation/Reference:
QUESTION 267
You have recently joined a startup company building sensors to measure street noise and air quality in urban
areas. The company has been running a pilot deployment of around 100 sensors for 3 months each sensor
uploads 1KB of sensor data every minute to a backend hosted on AWS. During the pilot, you measured a peak
or 10 IOPS on the database, and you stored an average of 3GB of sensor data per month in the database. The
current deployment consists of a load-balanced auto scaled Ingestion layer using EC2 instances and a
PostgreSQL RDS database with 500GB standard storage.
The pilot is considered a success and your CEO has managed to get the attention or some potential investors.
The business plan requires a deployment of at least IOOK sensors which needs to be supported by the
backend. You also need to store sensor data for at least two years to be able to compare year over year
Improvements.
To secure funding, you have to make sure that the platform meets these requirements and leaves room for
further scaling. Which setup win meet the requirements?
A. Add an SQS queue to the ingestion layer to buffer writes to the RDS instance
B. Ingest data into a DynamoDB table and move old data to a Redshift cluster
C. Replace the RDS instance with a 6 node Redshift cluster with 96TB of storage
D. Keep the current architecture but upgrade RDS storage to 3TB and IOK provisioned IOPS
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 268
Your company is in the process of developing a next generation pet collar that collects biometric information to
assist families with promoting healthy lifestyles for their pets Each collar will push 30kb of biometric data In
JSON format every 2 seconds to a collection platform that will process and analyze the data providing health
trending information back to the pet owners and veterinarians via a web portal Management has tasked you to
architect the collection platform ensuring the following requirements are met. Provide the ability for real-time
analytics of the inbound biometric data Ensure processing of the biometric data is highly durable. Elastic and
parallel The results of the analytic processing should be persisted for data mining Which architecture outlined
below win meet the initial requirements for the collection platform?
A. Utilize S3 to collect the inbound sensor data analyze the data from S3 with a daily scheduled Data Pipeline
and save the results to a Redshift Cluster.
B. Utilize Amazon Kinesis to collect the inbound sensor data, analyze the data with Kinesis clients and save
the results to a Red shift cluster using EMR.
C. Utilize SQS to collect the inbound sensor data analyze the data from SQS with Amazon Kinesis and save
the results to a Mcrosoft SQL Server RDS instance.
D. Utilize EMR to collect the inbound sensor data, analyze the data from EUR with Amazon Kinesis and save
me results to Dynamo DB.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 269
You need a persistent and durable storage to trace call actMty of an IVR (Interactive Voice Response) system.
Call duration is mostly in the 2-3 minutes timeframe. Each traced call can be either active or terminated. An
external application needs to know each minute the list of currently active calls, which are usually a few calls/
second. Put once per month there is a periodic peak up to 1000 calls/second for a few hours. The system is
open 24/7 and any downtime should be avoided. Historical data is periodically archived to files. Cost saving is
a priority for this project. What database implementation would better fit this scenario, keeping costs as low as
possible?
A. Use RDS Multi-AZ with two tables, one for -Active calls" and one for -Terminated ca Ils". In this way the
"Active caIIs_ table is always small and effective to access.
B. Use DynamoDB with a "Calls" table and a Global Secondary Index on a "IsActive"' attribute that is present
for active calls only In this way the Global Secondary index is sparse and more effective.
C. Use DynamoDB with a 'Calls" table and a Global secondary index on a 'State" attribute that can equal to
"active" or "terminated" in this way the Global Secondary index can be used for all Items in the table.
D. Use RDS Multi-AZ with a "CALLS" table and an Indexed "STATE* field that can be equal to 'ACTIVE" or -
TERMNATED" In this way the SOL query Is optimized by the use of the Index.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 270
A web design company currently runs several FTP servers that their 250 customers use to upload and
download large graphic files They wish to move this system to AWS to make it more scalable, but they wish to
maintain customer privacy and Keep costs to a minimum.
What AWS architecture would you recommend?
A. ASK their customers to use an S3 client instead of an FTP client. Create a single S3 bucket Create an IAM
user for each customer Put the IAM Users in a Group that has an IAM policy that permits access to subdirectories
within the bucket via use of the 'username' Policy variable.
B. Create a single S3 bucket with Reduced Redundancy Storage turned on and ask their customers to use an
S3 client instead of an FTP client Create a bucket for each customer with a Bucket Policy that permits
access only to that one customer.
C. Create an auto-scaling group of FTP servers with a scaling policy to automatically scale-in when minimum
network traffic on the auto-scaling group is below a given threshold. Load a central list of ftp users from S3
as part of the user Data startup script on each Instance.
D. Create a single S3 bucket with Requester Pays turned on and ask their customers to use an S3 client
instead of an FTP client Create a bucket tor each customer with a Bucket Policy that permits access only to
that one customer.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 271
You have been asked to design the storage layer for an application. The application requires disk performance
of at least 100,000 IOPS in addition, the storage layer must be able to survive the loss of an indMdual disk.
EC2 instance, or Availability Zone without any data loss. The volume you provide must have a capacity of at
least 3 TB. Which of the following designs will meet these objectives'?
A. Instantiate a c3.8x|arge instance in us-east-1. Provision 4x1TB EBS volumes, attach them to the instance,
and configure them as a single RAID 5 volume. Ensure that EBS snapshots are performed every 15
minutes.
B. Instantiate a c3.8xIarge instance in us-east-1. Provision 3xiTB EBS volumes, attach them to the Instance,
and configure them as a single RAID 0 volume. Ensure that EBS snapshots are performed every 15
minutes.
C. Instantiate an i2.8xIarge instance in us-east-Ia. Create a RAID 0 volume using the four 800GB SSD
ephemeral disks provided with the instance. Provision 3x1TB EBS volumes, attach them to the instance,
and configure them as a second RAID 0 volume. Configure synchronous, block-level replication from the
ephemeral-backed volume to the EBS-backed volume.
D. Instantiate a c3.8xIarge instance in us-east-1. Provision an AWS Storage Gateway and configure it for 3 TB
of storage and 100,000 IOPS. Attach the volume to the instance. E. Instantiate an i2.8x|arge instance in useast-
Ia. Create a RAID 0 volume using the four 800GB SSD ephemeral disks provided with the instance.
Configure synchronous, block- level replication to an identically configured instance in us-east-Ib.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 272
You would like to create a mirror image of your production environment in another region for disaster recovery
purposes. Which of the following AWS resources do not need to be recreated in the second region? (Choose 2
answers)
A. Route 53 Record Sets
B. IM Roles
C. Elastic IP Addresses (EIP)
D. EC2 Key Pairs
E. Launch configurations
F. Security Groups
Correct Answer: AB
Explanation
Explanation/Reference:
http://tech.com/wp-content/themes/optimize/download/AWSDisaster_Recovery.pdf (page 6)
QUESTION 273
Your company runs a customer facing event registration site This site is built with a 3-tier architecture with web
and application tier servers and a MySQL database The application requires 6 web tier servers and 6
application tier servers for normal operation, but can run on a minimum of 65% server capacity and a single
MySQL database. When deploying this application in a region with three availability zones (AZs) which
architecture provides high availability?
A. A web tier deployed across 2 AZs with 3 EC2 (Elastic Compute Cloud) instances in each AZ inside an Auto
Scaling Group behind an ELB (elastic load balancer), and an application tier deployed across 2 AZs with 3
EC2 instances in each AZ inside an Auto Scaling Group behind an ELB, and one RDS (Relational Database
Service) instance deployed with read replicas in the other AZ.
B. A web tier deployed across 3 AZs with 2 EC2 (Elastic Compute Cloud) instances in each AZ inside an Auto
Scaling Group behind an ELB (elastic load balancer) and an application tier deployed across 3 AZs with 2
EC2 instances in each AZ inside an Auto Scaling Group behind an ELB and one RDS (Relational Database
Service) Instance deployed with read replicas in the two other AZs.
C. A web tier deployed across 2 AZs with 3 EC2 (Elastic Compute Cloud) instances in each AZ inside an Auto
Scaling Group behind an ELB (elastic load balancer) and an application tier deployed across 2 AZs with 3
EC2 instances m each AZ inside an Auto Scaling Group behind an ELS and a Multi-AZ RDS (Relational
Database Service) deployment.
D. A web tier deployed across 3 AZs with 2 EC2 (Elastic Compute Cloud) instances in each AZ Inside an Auto
Scaling Group behind an ELB (elastic load balancer). And an application tier deployed across 3 AZs with 2
EC2 instances in each AZ inside an Auto Scaling Group behind an ELB. And a MuIti-AZ RDS (Relational
Database services) deployment.
Correct Answer: D
Explanation
Explanation/Reference:
Amazon RDS MuIti-AZ Deployments
Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) Instances,
making them a natural fit for production database workloads. When you provision a MuIti-AZ DB Instance,
Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby
instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent
infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure (for example, instance
hardware failure, storage failure, or network disruption), Amazon RDS performs an automatic failover to the
standby, so that you can resume database operations as soon as the failover is complete. Since the endpoint
for your DB Instance remains the same after a failover, your application can resume database operation
without the need for manual administrative intervention.
Enhanced Durability
MuIti-AZ deployments for the MySQL, Oracle, and PostgreSQL engines utilize synchronous physical
replication to keep data on the standby up-to-date with the primary. MuIti-AZ deployments for the SQL Server
engine use synchronous logical replication to achieve the same result, employing SQL Server-native Mrroring
technology. Both approaches safeguard your data in the event of a DB Instance failure or loss of an Availability
Zone.
If a storage volume on your primary fails in a Multi-AZ deployment, Amazon RDS automatically initiates a
failover to the up-to-date standby. Compare this to a Single-AZ deployment: in case of a Single-AZ database
failure, a user-initiated point-in-time-restore operation will be required. This operation can take several hours to
complete, and any data updates that occurred after the latest restorable time (typically within the last five
minutes) will not be available.
Amazon Aurora employs a highly durable, SSD-backed virtualized storage layer purpose-built for database
workloads. Amazon Aurora automatically replicates your volume six ways, across three Availability Zones.
Amazon Aurora storage is fault-tolerant, transparently handling the loss of up to two copies of data without
affecting database write availability and up to three copies without affecting read availability. Amazon Aurora
storage is also self-healing. Data blocks and disks are continuously scanned for errors and replaced
automatically.
Increased Availability
You also benefit from enhanced database availability when running Multi-AZ deployments. If an Availability
Zone failure or DB Instance failure occurs, your availability impact is limited to the time automatic failover takes
to complete: typically under one minute for Amazon Aurora and one to two minutes for other database engines
(see the RDS FAQ for details). The availability benefits of MuIti-AZ deployments also extend to planned
maintenance and backups. In the case of system upgrades like QS patching or DB Instance scaling, these
operations are applied first on the standby, prior to the automatic failover. As a result, your availability impact
is, again, only the time required for automatic failover to complete. Unlike Single-AZ deployments, 1/0 actMty is
not suspended on your primary during backup for MuIti-AZ deployments for the MySQL, Oracle, and
PostgreSQL engines, because the backup is taken from the standby. However, note that you may still
experience elevated latencies for a few minutes during backups for MuIti-AZ deployments.
On instance failure in Amazon Aurora deployments, Amazon RDS uses RDS MuIti-AZ technology to automate
failover to one of up to 15 Amazon Aurora Replicas you have created in any of three Availability Zones. If no
Amazon Aurora Replicas have been provisioned, in the case of a failure, Amazon RDS will attempt to create a
new Amazon Aurora DB instance for you automatically.
QUESTION 274
Your application is using an ELB in front of an Auto Scaling group of web/application sewers deployed across
two AZs and a MuIti-AZ RDS Instance for data persistence. The database CPU is often above 80% usage and
90% of 1/0 operations on the database are reads. To improve performance you recently added a single-node
Memcached EIastiCache Cluster to cache frequent DB query results. In the next weeks the overall workload is
expected to grow by 30%. Do you need to change anything in the architecture to maintain the high availability
or the application with the anticipated additional load? Why?
A. Yes, you should deploy two Memcached EIastiCache Clusters in different AZs because the RDS instance
will not be able to handle the load if the cache node fails.
B. No, if the cache node fails you can always get the same data from the DB without having any availability
impact.
C. No, if the cache node fails the automated EIastiCache node recovery feature will prevent any availability
impact.
D. Yes, you should deploy the Memcached EIastiCache Cluster with two nodes in the same AZ as the RDS DB
master instance to handle the load if one cache node fails.
Correct Answer: A
Explanation
Explanation/Reference:
EIastiCache for Memcached
The primary goal of caching is typically to offload reads from your database or other primary data source. In
most apps, you have hot spots of data that are regularly queried, but only updated periodically. Think of the
front page of a blog or news site, or the top 100 leaderboard in an online game. In this type of case, your app
can receive dozens, hundreds, or even thousands of requests for the same data before it's updated again.
Having your caching layer handle these queries has several advantages. First, it's considerably cheaper to add
an in-memory cache than to scale up to a larger database cluster. Second, an in-memory cache is also easier
to scale out, because it's easier to distribute an in-memory cache horizontally than a relational database. Last,
a caching layer provides a request buffer in the event of a sudden spike in usage. If your app or game ends up
on the front page of Reddit or the App Store, it's not unheard of to see a spike that is 10 to 100 times your
normal application load. Even if you autoscale your application instances, a IOx request spike will likely make
your database very unhappy.
Let's focus on EIastiCache for Memcached first, because it is the best fit for a caching focused solution. We'II
revisit Redislater in the paper, and weigh its advantages and disadvantages.
Architecture with EIastiCache for Memcached
When you deploy an EIastiCache Memcached cluster, it sits in your application as a separate tier alongside
your database. As mentioned previously, Amazon EIastiCache does not directly communicate with your
database tier, or indeed have any particular knowledge of your database. A simplified deployment for a web
application looks something like this:

In this architecture diagram, the Amazon EC2 application instances are in an Auto Scaling group, located
behind a load balancer using Elastic Load Balancing, which distributes requests among the instances. As
requests come into a given EC2 instance, that EC2 instance is responsible for communicating with
EIastiCache and the database tier. For development purposes, you can begin with a single EIastiCache node
to test your application, and then scale to additional cluster nodes by modifying t he EIastiCache cluster. As
you add additional cache nodes, the EC2 application instances are able to distribute cache keys across
multiple EIastiCache nodes. The most common practice is to use client-side sharding to distribute keys across
cache nodes, which we will discuss later in this paper.

When you launch an EIastiCache cluster, you can choose the Availability Zone(s) that the cluster lives in. For
best performance, you should configure your cluster to use the same Availability Zones as your application
servers. To launch an EIastiCache cluster in a specific Availability Zone, make sure to specify the Preferred
Zone(s) option during cache cluster creation. The Availability Zones that you specify will be where EIastiCache
will launch your cache nodes. We recommend that you select Spread Nodes Across Zones, which tells
EIastiCache to distribute cache nodes across these zones as evenly as possible. This distribution will mitigate
the impact of an Availability Zone disruption on your E|astiCache nodes. The trade-off is that some of the
requests from your application to EIastiCache will go to a node in a different Availability Zone, meaning latency
will be slightly higher. For more details, refer to Creating a Cache Cluster in the Amazon EIastiCache User
Guide. As mentioned at the outset, EIastiCache can be coupled with a wide variety of databases. Here is an
example architecture that uses Amazon DynamoDB instead of Amazon RDS and IV|ySQL:

This combination of DynamoDB and EIastiCache is very popular with mobile and game companies, because
DynamoDB allows for higher write throughput at lower cost than traditional relational databases. In addition,
DynamoDB uses a key-value access pattern similar to EIastiCache, which also simplifies the programming
model. Instead of using relational SQL for the primary database but then key-value patterns for the cache, both
the primary database and cache can be programmed similarly. In this architecture pattern, DynamoDB remains
the source of truth for data, but application reads are offloaded to EIastiCache for a speed boost.
QUESTION 275
You are responsible for a legacy web application whose server environment is approaching end of life You
would like to migrate this application to AWS as quickly as possible, since the application environment currently
has the following limitations:
The VM's single 10GB VMDK is almost full Me virtual network interface still uses the 10Mbps driver, which
leaves your 100Mbps WAN connection completely underutilized It is currently running on a highly customized.
Windows VM within a VMware environment:
You do not have me installation media
This is a mission critical application with an RTO (Recovery Time Objective) of 8 hours. RPO (Recovery Point
Objective) of 1 hour. How could you best migrate this application to AWS while meeting your business
continuity requirements?
A. Use the EC2 VM Import Connector for vCenter to import the VM into EC2.
B. Use Import/Export to import the VM as an ESS snapshot and attach to EC2.
C. Use S3 to create a backup of the VM and restore the data into EC2.
D. Use me ec2-bundle-instance API to Import an Image of the VM into EC2
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 276
An International company has deployed a multi-tier web application that relies on DynamoDB in a single region
For regulatory reasons they need disaster recovery capability In a separate region with a Recovery Time
Objective of 2 hours and a Recovery Point Objective of 24 hours They should synchronize their data on a
regular basis and be able to provision me web application rapidly using CIoudFormation. The objective is to
minimize changes to the existing web application, control the throughput of DynamoDB used for the
synchronization of data and synchronize only the modified elements.
Which design would you choose to meet these requirements?
A. Use AWS data Pipeline to schedule a DynamoDB cross region copy once a day. create a Last updated'
attribute in your DynamoDB table that would represent the timestamp of the last update and use it as a filter.
B. Use EMR and write a custom script to retrieve data from DynamoDB in the current region using a SCAN
operation and push it to Dynamo DB in the second region.
C. Use AWS data Pipeline to schedule an export of the DynamoDB table to S3 in the current region once a day
then schedule another task immediately after it that will import data from S3 to DynamoDB in the other
region.
D. Send also each Ante into an SOS queue in me second region; use an auto-scaling group behind the SOS
queue to replay the write in the second region.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 277
Refer to the architecture diagram above of a batch processing solution using Simple Queue Service (SQS) to
set up a message queue between EC2 instances which are used as batch processors Cloud Watch monitors
the number of Job requests (queued messages) and an Auto Scaling group adds or deletes batch sewers
automatically based on parameters set in Cloud Watch alarms. You can use this architecture to implement
which of the following features in a cost effective and efficient manner?
A. Reduce the overall lime for executing jobs through parallel processing by allowing a busy EC2 instance that
receives a message to pass it to the next instance in a daisy-chain setup.
B. Implement fault tolerance against EC2 instance failure since messages would remain in SQS and worn can
continue with recovery of EC2 instances implement fault tolerance against SQS failure by backing up
messages to S3.
C. Implement message passing between EC2 instances within a batch by exchanging messages through SQS.
D. Coordinate number of EC2 instances with number of job requests automatically thus Improving cost
effectiveness.
E. Handle high priority jobs before lower priority jobs by assigning a priority metadata fie Id to SQS messages.
Correct Answer: D
Explanation
Explanation/Reference:
There are cases where a large number of batch jobs may need processing, and where the jobs may need to be
re-prioritized.
For example, one such case is one where there are differences between different levels of services for unpaid
users versus subscriber users (such as the time until publication) in services enabling, for example,
presentation fi les to be uploaded for publication from a web browser. When the user uploads a presentation
file, the conversion processes, for example, for publication are performed as batch processes on the system
side, and the file is published after the conversion. Is it then necessary to be able to assign the level of priority
to the batch processes for each type of subscriber.
of the Cloud Solution/Pattern
A queue is used in controlling batch jobs. The queue need only be provided with priority numbers. Job requests
are controlled by the queue, and the job requests in the queue are processed by a batch server. In Cloud
computing, a highly reliable queue is provided as a service, which you can use to structure a highly reliable
batch system with ease. You may prepare multiple queues depending on priority levels, with job requests put
into the queues depending on their priority levels, to apply prioritization to batch processes. The performance
(number) of batch servers corresponding to a queue must be in accordance with the priority level thereof.
Implementation
In AWS, the queue service is the Simple Queue Service (SQS). MuItipIe SQS queues may be prepared to
prepare queues for indMdual priority levels (with a priority queue and a secondary queue). Moreover, you may
also use the message Delayed Send function to delay process execution. Use SQS to prepare multiple queues
for the indMdual priority levels. Place those processes to be executed immediately (job requests) in the high
priority queue. Prepare numbers of batch servers, for processing the job requests of the queues, depending on
the priority levels.
Queues have a message "Delayed Send" function. You can use this to delay the time for starting a process.
Configuration
Benefits
You can increase or decrease the number of servers for processing jobs to change automatically the
processing speeds of the priority queues and secondary queues. You can handle performance and service
requirements through merely increasing or decreasing the number of EC2 instances used in job processing.
Even if an EC2 were to fail, the messages (jobs) would remain in the queue service, enabling processing to be
continued immediately upon recovery of the EC2 instance, producing a system that is robust to failure.
Cautions
Depending on the balance between the number of EC2 instances for performing the processes and the
number of messages that are queued, there may be cases where processing in the secondary queue may be
completed first, so you need to monitor the processing speeds in the primary queue and the secondary queue.
QUESTION 278
Your company currently has a 2-tier web application running in an on-premises data center. You have
experienced several infrastructure failures in the past two months resu Iting in significant financial losses. Your
CIO is strongly agreeing to move the application to AWS. While working on achieving buy-in from the other
company executives, he asks you to develop a disaster recovery plan to help improve Business continuity in
the short term. He specifies a target Recovery Time Objective (RTO) of 4 hours and a Recovery Point
Objective (RPO) of 1 hour or less. He also asks you to implement the solution within 2 weeks. Your database is
200GB in size and you have a 20Mbps Internet connection.
How would you do this while minimizing costs?
A. Create an EBS backed private AMI which includes a fresh install of your application. Develop a
CIoudFormation template which includes your AMI and the required EC2, AutoScaIing, and ELB resources
to support deploying the application across Multiple- Availability-Zones. Asynchronously replicate
transactions from your on-premises database to a database instance in AWS across a secure VPN
connection.
B. Deploy your application on EC2 instances within an Auto Scaling group across multiple availability zones.
Asynchronously replicate transactions from your on-premises database to a database instance in AWS
across a secure VPN connection.
C. Create an EBS backed private AMI which includes a fresh install of your application. Setup a script in your
data center to backup the local database every 1 hour and to encrypt and copy the resulting file to an S3
bucket using multi-part upload.
D. Install your application on a compute-optimized EC2 instance capable of supporting the application 's
average load. Synchronously replicate transactions from your on-premises database to a database instance
in AWS across a secure Direct Connect connection.
Correct Answer: A
Explanation
Explanation/Reference:
Overview of Creating Amazon EBS-Backed AMIs
First, launch an instance from an AMI that's similar to the AMI that you'd like to create. You can connect to your
instance and customize it. When the instance is configured correctly, ensure data integrity by stopping the
instance before you create an AMI, then create the image. When you create an Amazon EBS-backed AMI, we
automatically register it for you.
Amazon EC2 powers down the instance before creating the AMI to ensure that everything on the instance is
stopped and in a consistent state during the creation process. If you're confident that your instance is in a
consistent state appropriate for AMI creation, you can tell Amazon EC2 not to power down and reboot the
instance. Some file systems, such as XFS, can freeze and unfreeze actMty, making it safe to create the image
without rebooting the instance.
During the AMI-creation process, Amazon EC2 creates snapshots of your instance's root volume and any other
EBS volumes attached to your instance. If any volumes attached to the instance are encrypted, the new AMI
only launches successfully on instances that support Amazon EBS encryption. For more information, see
Amazon EBS Encryption.
Depending on the size of the volumes, it can take several minutes for the AMI-creation process to complete
(sometimes up to 24 hours).You may find it more efficient to create snapshots of your volumes prior to creating
your AMI. This way, only small, incremental snapshots need to be created when the AMI is created, and the
process completes more quickly (the total time for snapshot creation remains the same). For more information,
see Creating an Amazon EBS Snapshot. After the process completes, you have a new AMI and snapshot
created from the root volume of the instance. When you launch an instance using the new AMI, we create a
new EBS volume for its root volume using the snapshot. Both the AMI and the snapshot incur charges to your
account until you delete them. For more information, see Deregistering Your AMI. If you add instance-store
volumes or EBS volumes to your instance in addition to the root device volume, the block device mapping for
the new AMI contains information for these volumes, and the block device mappings for instances that you
launch from the new AMI automatically contain information for these volumes. The instance-store volumes
specified in the block device mapping for the new instance are new and don't contain any data from the
instance store volumes of the instance you used to create the AMI. The data on EBS volumes persists. For
more information, see Block Device Mapping.
QUESTION 279
An ERP application is deployed across multiple AZs in a single region. In the event of failure, the Recovery
Time Objective (RTO) must be less than 3 hours, and the Recovery Point Objective (RPO) must be 15 minutes
the customer realizes that data corruption occurred roughly 1.5 hours ago. What DR strategy could be used to
achieve this RTO and RPO in the event of this kind of failure?
A. Take hourly DB backups to S3, with transaction logs stored in S3 every 5 minutes.
B. Use synchronous database master-slave replication between two availability zones.
C. Take hourly DB backups to EC2 Instance store volumes with transaction logs stored In S3 every 5 minutes.
D. Take 15 minute DB backups stored In Glacier with transaction logs stored in S3 every 5 minutes.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 280
Your startup wants to implement an order fulfillment process for selling a personalized gadget that needs an
average of 3-4 days to produce with some orders taking up to 6 months you expect 10 orders per day on your
first day. 1000 orders per day after 6 months and 10,000 orders after 12 months. Orders coming in are
checked for consistency men dispatched to your manufacturing plant for production quality control packaging
shipment and payment processing If the product does not meet the quality standards at any stage of the
process employees may force the process to repeat a step Customers are notified via email about order status
and any critical issues with their orders such as payment failure. Your case architecture includes AWS Elastic
Beanstalk for your website with an RDS MySQL instance for customer data and orders. How can you
implement the order fulfillment process while making sure that the emails are delivered reliably?
A. Add a business process management application to your Elastic Beanstalk app servers and re-use the ROS
database for tracking order status use one of the Elastic Beanstalk instances to send emails to customers.
B. Use SWF with an Auto Scaling group of actMty workers and a decider instance in another Auto Scaling
group with min/max=I Use the decider instance to send emails to customers.
C. Use SWF with an Auto Scaling group of actMty workers and a decider instance in another Auto Scaling
group with min/max=I use SES to send emails to customers.
D. Use an SOS queue to manage all process tasks Use an Auto Scaling group of EC2 Instances that poll the
tasks and execute them. Use SES to send emails to customers.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 281
You have deployed a web application targeting a global audience across multiple AWS Regions under the
domain name.exampIe.com. You decide to use Route53 Latency-Based Routing to serve web requests to
users from the region closest to the user. To provide business continuity in the event of server downtime you
configure weighted record sets associated with two web servers in separate Availability Zones per region.
Dunning a DR test you notice that when you disable all web sewers in one of the regions Route53 does not
automatically direct all users to the other region. What could be happening? {Choose 2 answers)
A. Latency resource record sets cannot be used in combination with weighted resource record sets.
B. You did not setup an HTIP health check tor one or more of the weighted resource record sets associated
with me disabled web sewers.
C. The value of the weight associated with the latency alias resource record set in the region with the disabled
sewers is higher than the weight for the other region.
D. One of the two working web sewers in the other region did not pass its HTIP health check.
E. You did not set "Evaluate Target Health" to "Yes" on the latency alias resource record set associated with
example com in the region where you disabled the sewers.
Correct Answer: BE
Explanation
Explanation/Reference:
How Health Checks Work in Complex Amazon Route 53 Configurations Checking the health of resources in
complex configurations works much the same way as in simple configurations. However, in complex
configurations, you use a combination of alias resource record sets (including weighted alias, latency alias, and
failover alias) and nonalias resource record sets to build a decision tree that gives you greater control over how
Amazon Route 53 responds to requests. For more information, see How Health Checks Work in Simple
Amazon Route 53 Configurations. For example, you might use latency alias resource record sets to select a
region close to a user and use weighted resource record sets for two or more resources within each region to
protect against the failure of a single endpoint or an Availability Zone. The following diagram shows this
configuration.
Here's how Amazon EC2 and Amazon Route 53 are configured:
You have Amazon EC2 instances in two regions, us-east-1 and ap-southeast-2. You want Amazon Route 53 to
respond to queries by using the resource record sets in the region that provides the lowest latency for your
customers, so you create a latency alias resource record set for each region. (You create the latency alias
resource record sets after you create resource record sets for the indMdual Amazon EC2 instances.) Within
each region, you have two Amazon EC2 instances. You create a weighted resource record set for each
instance. The name and the type are the same for both of the weighted resource record sets in each region.
When you have multiple resources in a region, you can create weighted or failover resource record sets for
your resources. You can also create even more complex configurations by creating weighted alias or failover
alias resource record sets that, in turn, refer to multiple resources. Each weighted resource record set has an
associated health check. The IP address for each health check matches the I P address for the corresponding
resource record set. This isn't required, but it's the most common configuration. For both latency alias resource
record sets, you set the value of Evaluate Target Health to Yes. You use the Evaluate Target Health setting for
each latency alias resource record set to make Amazon Route 53 evaluate the health of the alias targets-the
weighted resource record sets-and respond accordingly.
The preceding diagram illustrates the following sequence of events:
Amazon Route 53 receives a query for exampIe.com. Based on the latency for the user making the request,
Amazon Route 53 selects the latency alias resource record set for the us-east-1 region. Amazon Route 53
selects a weighted resource record set based on weight. Evaluate Target Health is Yes for the latency alias
resource record set, so Amazon Route 53 checks the health of the selected weighted resource record set. The
health check failed, so Amazon Route 53 chooses another weighted resource record set based on weight and
checks its health. That resource record set also is unhealthy. Amazon Route 53 backs out of that branch of the
tree, looks for the latency alias resource record set with the next-best latency, and chooses the resource record
set for ap-southeast-2. Amazon Route 53 again selects a resource record set based on weight, and then
checks the health of the selected resource record set . The health check passed, so Amazon Route 53 returns
the applicable value in response to the query.
What Happens When You Associate a Health Check with an Alias Resource Record Set? You can associate a
health check with an alias resource record set instead of or in addition to setting the value of Evaluate Target
Health to Yes. However, it's generally more useful if Amazon Route 53 responds to queries based on the
health of the underlying resources- the HTTP sewers, database servers, and other resources that your alias
resource record sets refer to. For example, suppose the following configuration:
You assign a health check to a latency alias resource record set for which the alias target is a group of
weighted resource record sets.
You set the value of Evaluate Target Health to Yes for the latency alias resource record set. In this
configuration, both of the following must be true before Amazon Route 53 will return the applicable value for a
weighted resource record set:
The health check associated with the latency alias resource record set must pass. At least one weighted
resource record set must be considered healthy, either because it's associated with a health check that passes
or because it's not associated with a health check. In the latter case, Amazon Route 53 always considers the
weighted resource record set healthy.
If the health check for the latency alias resource record set fails, Amazon Route 53 stops responding to queries
using any of the weighted resource record sets in the alias target, even if they're all healthy. Amazon Route 53
doesn't know the status of the weighted resource record sets because it never looks past the failed health
check on the alias resource record set.
What Happens When You Omit Health Checks?
In a complex configuration, it's important to associate health checks with all of the non-alias resource record
sets. Let's return to the preceding example, but assume that a health check is missing on one of the weighted
resource record sets in the us-east-1 region:
Here's what happens when you omit a health check on a non-alias resource record set in this configuration:
Amazon Route 53 receives a query for exampIe.com. Based on the latency for the user making the request,
Amazon Route 53 selects the latency alias resource record set for the us-east-1 region. Amazon Route 53
looks up the alias target for the latency alias resource record set, and checks the status of the corresponding
health checks. The health check for one weighted resource record set failed, so that resource record set is
omitted from consideration.
The other weighted resource record set in the alias target for the us-east-1 region has no health check. The
corresponding resource might or might not be healthy, but without a health check, Amazon Route 53 has no
way to know. Amazon Route 53 assumes that the resource is healthy and returns the applicable value in
response to the query.
What Happens When You Set Evaluate Target Health to No?
In general, you also want to set Evaluate Target Health to Yes for all of the alias resource record sets. In the
following example, all of the weighted resource record sets have associated health checks, but Evaluate Target
Health is set to No for the latency alias resource record set for the us-east-1 region:
Here's what happens when you set Evaluate Target Health to No for an alias resource record set in this
configuration:
Amazon Route 53 receives a query for exampIe.com. Based on the latency for the user making the request,
Amazon Route 53 selects the latency alias resource record set for the us-east-1 region. Amazon Route 53
determines what the alias target is for the latency alias resource record set, and checks the corresponding
health checks. They're both failing.
Because the value of Evaluate Target Health is No for the latency alias resource record set for the us-east-1
region, Amazon Route 53 must choose one resource record set in this branch instead of backing out of the
branch and looking for a healthy resource record set in the ap-southeast-2 region.
QUESTION 282
Your company hosts a social media site supporting users in multiple countries. You have been asked to
provide a highly available design tor the application that leverages multiple regions tor the most recently
accessed content and latency sensitive portions of the wet) site The most latency sensitive component of the
application involves reading user preferences to support web site personalization and ad selection. In addition
to running your application in multiple regions, which option will support this app|ication's requirements?
A. Serve user content from S3. CIoudFront and use Route53 latency-based routing between ELBs in each
region Retrieve user preferences from a local DynamoDB table in each region and leverage SQS to capture
changes to user preferences with 505 workers for propagating updates to each table.
B. Use the S3 Copy API to copy recently accessed content to multiple regions and serve user content from S3.
C|oudFront with dynamic content and an ELB in each region Retrieve user preferences from an
EIasticCache cluster in each region and leverage SNS notifications to propagate user preference changes
to a worker node in each region.
C. Use the S3 Copy API to copy recently accessed content to multiple regions and serve user content from S3
CIoudFront and Route53 latency-based routing Between ELBs In each region Retrieve user preferences
from a DynamoDB table and leverage SQS to capture changes to user preferences with 505 workers for
propagating DynamoDB updates.
D. Serve user content from S3. CIoudFront with dynamic content, and an ELB in each region Retrieve user
preferences from an EIastiCache cluster in each region and leverage Simple Workflow (SWF) to manage
the propagation of user preferences from a centralized OB to each EIastiCache cluster.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 283
Your system recently experienced down time during the troubleshooting process. You found that a new
administrator mistakenly terminated several production EC2 instances. Which of the following strategies will
help prevent a similar situation in the future? The administrator still must be able to:
- launch, start stop, and terminate development resources.
- launch and start production instances.
A. Create an IAM user, which is not allowed to terminate instances by leveraging production EC2 termination
protection.
B. Leverage resource based tagging along with an IAM user, which can prevent specific users from terminating
production EC2 resources.
C. Leverage EC2 termination protection and multi-factor authentication, which together require users to
authenticate before terminating EC2 instances
D. Create an IAM user and apply an IAM role which prevents users from terminating production EC2 instances.
Correct Answer: B
Explanation
Explanation/Reference:
Working with volumes
When an API action requires a caller to specify multiple resources, you must create a policy statement that
allows users to access all required resources. If you need to use a Condition element with one or more of these
resources, you must create multiple statements as shown in this example. The following policy allows users to
attach volumes with the tag "volume_user=iam-user-name" to instances with the tag "department=dev", and to
detach those volumes from those instances. If you attach this policy to an IAM group, the aws:username policy
variable gives each IAM user in the group permission to attach or detach volumes from the instances with a tag
named voIume_ user that has his or her IAM user name as a value.
{
"Version": "2012-10-I7",
"Statement": [{
"Effect": "A||ow",
"Action": [
"ec2:AttachVoIume",
"ec2:DetachVoIume"
I,
"Resource": "arn :aws:ec2:us-east-1:123456789012:instanee/*", "Condition": { "StringEqua|s": {
"ec2:ResourceTag/department": "dev"
II
I,
{
"Effect": "A||ow",
"Action": [
"ec2:AttachVoIume",
"ec2:DetachVoIume"
I,
"Resource": "arn:aws:ec2:us-east-1:123456789012:voIume/*", "Condition": { "StringEqua|s": {
"ec2:ResourceTag/voIume_user": "${aws:username}"
IIIII
Launching instances (Runlnstances)
The Runlnstances API action launches one or more instances. Runlnstances requires an AM and creates an
instance; and users can specify a key pair and security group in the request. Launching into EC2-VPC requires
a subnet, and creates a network interface. Launching from an Amazon EBS-backed AM creates a volume.
Therefore, the user must have permission to use these Amazon EC2 resources. The caller can also configure
the instance using optional parameters to Run Instances, such as the instance type and a subnet. You can
create a policy statement that requires users to specify an optional parameter, or restricts users to particular
values for a parameter. The examples in this section demonstrate some of the many possible ways that you
can control the configuration of an instance that a user can launch. Note that by default, users don't have
permission to describe, start, stop, or terminate the resulting instances. One way to grant the users permission
to manage the resulting instances is to create a specific tag for each instance, and then create a statement that
enables them to manage instances with that tag.
For more information, see 2: Working with instances.
a. AMI
The following policy allows users to launch instances using only the AM|s that have the specified tag,
"department=dev", associated with them. The users can't launch instances using other ANI Is because the
Condition element of the first statement requires that users specify an AM that has this tag. The users also
can't launch into a subnet, as the policy does not grant permissions for the subnet and network interface
resources. They can, however, launch into EC2-Ciassic. The second statement uses a wildcard to enable
users to create instance resources, and requires users to specify the key pair project_keypair and the security
group sg-1a2b3c4d. Users are still able to launch instances without a key pair.
{
"Version": "2012-10-I7",
"Statement": [{
I,
{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region::image/ami-*"
I,
"Condition": {
"StringEqua|s": {
"ec2:ResourceTag/department": "dev"
II
I,
{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region:account:instance/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region:account:key-pair/project_keypair",
"arn :aws :ec2: region: account:security-group/sg-1a 2b3c4d" I I
}
Alternatively, the following policy allows users to launch instances using only the specified AMIs, ami-9e1670f7
and ami-45cf5c3c. The users can't launch an instance using other AMIs (unless another statement grants the
users permission to do so), and the users can't launch an instance into a subnet.
{
"Version": "2012-10-17",
"Statement": [{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region::image/ami-9e1670f7",
"arn:aws:ec2:region::image/ami-45cf5c3c",
"arn:aws:ec2:region:account:instance/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region:account:key-pair/*",
"arn:aws:ec2:region:account:security-group/*"
}}
Alternatively, the following policy allows users to launch instances from all AMs owned by Amazon. The
Condition element of the first statement tests whether ec2:0wner is amazon. The users can't launch an
instance using other AM Is (unless another statement grants the users permission to do so).
The users are able to launch an instance into a subnet.
"Version": "2012-10-17",
"Statement": [{
"Effect": "A| low",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region::image/ami-*"
l,
"Condition": {
"StringEqua|s": {
"ec2:0wner": "amazon"
}
},
{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource" : [
"arn:aws:ec2:region:account:instance/*",
"arn:aws:ec2:region:account:subnet/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region:account:network-interface/*",
"arn:aws:ec2:region:account:key-pair/*",
"arn:aws:ec2:region:account:security-group/*"
I
}I
}
b. Instance type
The following policy allows users to launch instances using only the t2.micro or t2.sma|I instance type, which
you might do to control costs. The users can't launch larger instances because the Condition element of the
first statement tests whether ec2:1nstanceType is either t2.micro or t2.smaII.
{
"Version": "2012-10-I7",
"Statement": [{
"Effect": "A| low",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region:account:instance/*"
I,
"Condition": {
"StringEqua|s": {
"ec2:1nstanceType": ["t2.micro", "t2.smaII"]
}}
},
{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region::image/ami-*",
"arn:aws:ec2:region:account:subnet/*",
"arn:aws:ec2:region:account:network-interface/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region:account:key-pair/*",
"arn:aws:ec2:region:account:security-group/*"
I
}I
}
Alternatively, you can create a policy that denies users permission to launch any instances except t2.micro and
t2.sma|I instance types.
{
"Version": "2012-10-17",
"Statement": [{
"Effect": "Deny",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region:account:instance/*"
l,
"Condition": {
"StringNotEqua|s": {
"ec2:1nstanceType": ["t2.micro", "t2.smaII"]
}}
},
{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region::image/ami-*",
"arn:aws:ec2:region:account:network-interface/*
"arn:aws:ec2:region:account:instance/*",
"arn:aws:ec2:region:account:subnet/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region:account:key-pair/*",
"arn:aws:ec2:region:account:security-group/*"
}}
c. Subnet
The following policy allows users to launch instances using only the specified subnet, subnet-12345678. The
group can't launch instances into any another subnet (unless another statement grants the users permission to
do so). Users are still able to launch instances into EC2-Ciassic.
{
"Version": "2012-10-17",
"Statement": [{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn :aws :ec2: region:account:subnet/subnet-123456 78",
"arn:aws:ec2:region:account:network-interface/*",
"arn:aws:ec2:region:account:instance/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region::image/ami-*",
"arn:aws:ec2:region:account:key-pair/*",
"arn:aws:ec2:region:account:security-group/*"
}}
Alternatively, you could create a policy that denies users permission to launch an instance into any other
subnet. The statement does this by denying permission to create a network interface, except where subnet
subnet-12345678 is specified. This denial overrides any other policies that are created to allow launching
instances into other subnets. Users are still able to launch instances into EC2-Classic.
{
"Version": "2012-10-17",
"Statement": [{
"Effect": "Deny",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region:account:network-interface/*"
l,
"Condition": {
"ArnNotEquaIs": {
"ec2:Subnet": "arn :aws:ec2:region:account:subnet/subnet-12345678" } }
},
{
"Effect": "A||ow",
"Action": "ec2:RunInstances",
"Resource": [
"arn:aws:ec2:region::image/ami-*",
"arn:aws:ec2:region:account:network-interface/*",
"arn:aws:ec2:region:account:instance/*",
"arn:aws:ec2:region:account:subnet/*",
"arn:aws:ec2:region:account:voIume/*",
"arn:aws:ec2:region:account:key-pair/*",
"arn:aws:ec2:region:account:security-group/*"
}}
QUESTION 284
A customer has established an AWS Direct Connect connection to AWS. The link is up and routes are being
advertised from the customer's end, however the customer is unable to connect from EC2 instances inside its
VPC to servers residing in its datacenter.
Which of the following options provide a viable solution to remedy this situation? (Choose 2 answers)
A. Add a route to the route table with an IPsec VPN connection as the target.
B. Enable route propagation to the virtual pinnate gateway (VGW).
C. Enable route propagation to the customer gateway (CGW).
D. Modify the route table of all Instances using the 'route' command.
E. Modify the Instances VPC subnet route table by adding a route back to the customer's on-premises
environment.
Correct Answer: AC
Explanation
Explanation/Reference:
QUESTION 285
Your company previously configured a heavily used, dynamically routed VPN connection between your onpremises
data center and AWS. You recently provisioned a DirectConnect connection and would like to start
using the new connection. After configuring DirectConnect settings in the AWS Console, which of the following
options win provide the most seamless transition for your users?
A. Delete your existing VPN connection to avoid routing loops configure your DirectConnect router with the
appropriate settings and verity network traffic is leveraging DirectConnect.
B. Configure your DirectConnect router with a higher 8GP priority man your VPN router, verify network traffic is
leveraging Directconnect and then delete your existing VPN connection.
C. Update your VPC route tables to point to the DirectConnect connection configure your DirectConnect router
with the appropriate settings verify network traffic is leveraging DirectConnect and then delete the VPN
connection.
D. Configure your DirectConnect router, update your VPC route tables to point to the DirectConnect
connection, configure your VPN connection with a higher BGP pointy. And verify network traffic is leveraging
the DirectConnect connection.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 286
A web company is looking to implement an external payment service into their highly available application
deployed in a VPC Their application EC2 instances are behind a public lacing ELB Auto scaling is used to add
additional instances as traffic increases under normal load the application runs 2 instances in the Auto Scaling
group but at peak it can scale 3x in size. The application instances need to communicate with the payment
service over the Internet which requires whitelisting of all public IP addresses used to communicate with it. A
maximum of 4 whitelisting IP addresses are allowed at a time and can be added through an API.
How should they architect their solution?
A. Route payment requests through two NAT instances setup for High Availability and whitelist the Elastic IP
addresses attached to the MAT instances.
B. Whitelist the VPC Internet Gateway Public IP and route payment requests through the Internet Gateway.
C. Whitelist the ELB IP addresses and route payment requests from the Application servers through the ELB.
D. Automatically assign public IP addresses to the application instances in the Auto Scaling group and run a
script on boot that adds each instances public IP address to the payment validation whitelist API.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 287
You are designing the network infrastructure for an application sewer in Amazon VPC Users will access all the
application instances from the Internet as well as from an on-premises network The on-premises network is
connected to your VPC over an AWS Direct Connect link. How would you design routing to meet the above
requirements?
A. Configure a single routing Table with a default route via the Internet gateway Propagate a default route via
BGP on the AWS Direct Connect customer router. Associate the routing table with all VPC subnets.
B. Configure a single routing table with a default route via the internet gateway Propagate specific routes for
the on-premises networks via BGP on the AWS Direct Connect customer router Associate the routing table
with all VPC subnets.
C. Configure a single routing table with two default routes: one to the inte rnet via an Internet gateway the other
to the on-premises network via the VPN gateway use this routing table across all subnets in your VPC,
D. Configure two routing tables one that has a default route via the Internet gateway and another that has a
default route via the VPN gateway Associate both routing tables with each VPC subnet.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 288
You are implementing AWS Direct Connect. You intend to use AWS public service end points such as Amazon
S3, across the AWS Direct Connect link. You want other Internet traffic to use your existing link to an Internet
Service Provider.
What is the way to configure AW5 Direct connect for access to services such as Amazon S3?
A. Configure a public Interface on your AW5 Direct Connect link Configure a static route via your AW5 Direct
Connect link that points to Amazon S3 Advertise a default route to AW5 using BGP.
B. Create a private interface on your AW5 Direct Connect link. Configure a static route via your AW5 Direct
connect link that points to Amazon S3 Configure specific routes to your network in your VPC,
C. Create a public interface on your AW5 Direct Connect link Redistribute BGP routes into your existing routing
infrastructure advertise specific routes for your network to AW5.
D. Create a private interface on your AW5 Direct connect link. Redistribute BGP routes into your existing
routing infrastructure and advertise a default route to AW5.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 289
You have deployed a three-tier web application in a VPC with a CIOR block of 10 0 0 0/ 28 You initially deploy
two web servers, two application sewers, two database sewers and one NAT instance tor a total of seven EC2
instances The web. Application and database servers are deployed across two availability zones (AZs). You
also deploy an ELB in front of the two web sewers, and use Route53 for DN5 Web (raffile gradually increases
in the first few days following the deployment, so you attempt to double the number of instances in each tier of
the application to handle the new load unfortunately some of these new instances fail to launch. Which of the
following could De the root caused? (Choose 2 answers)
A. AW5 resewes the first and the last private IP address in each subnet's CIDR block so you do not have
enough addresses left to launch all of the new EC2 instances
B. The Internet Gateway (IGW) of your VPC has scaled-up, adding more instances to handle the traffic spike,
reducing the number of available private IP addresses for new instance launches
C. The ELB has scaled-up, adding more instances to handle the traffic spike, reducing the number of available
private IP addresses for new instance launches
D. AW5 reserves one IP address in each subnet's CIDR block for Route53 so you do not have enough
addresses left to launch all of the new EC2 instances
E. AW5 reserves the first four and the last IP address in each subnet's CIDR block so you do not have enough
addresses left to launch all of the new EC2 instances
Correct Answer: CE
Explanation
Explanation/Reference:
QUESTION 290
You've been brought in as solutions architect to assist an enterprise customer with their migration of an ecommerce
platform to Amazon Virtual Private Cloud (VPC) The previous architect has already deployed a 3-
tier VPC, The configuration is as follows:
VPC: vpc-2f8bc447
IGW: igw-2d8bc445
NACL: ad-208bc448
5ubnets and Route Tables:
Web sewers: subnet-258bc44d
Application servers: subnet-248bc44c
Database sewers: subnet-9189c6f9
Route Tables:
rrb-218bc449
rtb-238bc44b
Associations:
subnet-258bc44d : rtb-218bc449
subnet-248bc44c : rtb-238bc44b
subnet-9189c6f9 : rtb-238bc44b
You are now ready to begin deploying EC2 instances into the VPC Web servers must have direct access to the
internet Application and database sewers cannot have direct access to the internet. Which configuration below
will allow you the ability to remotely administer your application and database servers, as well as allow these
sewers to retrieve updates from the Internet?
A. Create a bastion and NAT instance in subnet-258bc44d, and add a route from rtb- 238bc44b to the NAT
instance.
B. Add a route from rtb-238bc44b to igw-2d8bc445 and add a bastion and NAT instance within subnet-
248bc44c.
C. Create a bastion and NAT instance in subnet-248bc44c, and add a route from rtb- 238bc44b to
subneb258bc44d.
D. Create a bastion and NAT instance in subnet-258bc44d, add a route from rtb-238bc44b to Igw- 2d8bc445,
and a new NACL that allows access between subnet-258bc44d and subnet -248bc44c.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 291
You are designing Internet connectMty for your VPC. The Web servers must be available on the Internet. The
application must have a highly available architecture. Which alternatives should you consider? (Choose 2
answers)
A. Configure a NAT instance in your VPC Create a default route via the NAT instance and associate it with all
subnets Configure a DNS A record that points to the NAT instance public IP address.
B. Configure a C|oudFront distribution and configure the origin to point to the private IP addresses of your Web
sewers Configure a Route53 CNAME record to your Cloud Front distribution.
C. Place all your web servers behind EL8 Configure a Route53 CNME to point to the ELB DNS name.
D. Assign EIPs to all web sewers. Configure a Route53 record set with all EIPs. With health checks and DNS
failover.
E. Configure ELB with an EIP Place all your Web servers behind ELB Configure a Route53 A record that points
to the EIP.
Correct Answer: CD
Explanation
Explanation/Reference:
QUESTION 292
You are tasked with moving a legacy application from a virtual machine running Inside your datacenter to an
Amazon VPC Unfortunately this app requires access to a number of on-premises services and no one who
configured the app still works for your company. Even worse there's no documentation for it. What will allow the
application running inside the VPC to reach back and access its internal dependencies without being
reconfigured? {Choose 3 answers)
A. An AWS Direct Connect link between the VPC and the network housing the internal services.
B. An Internet Gateway to allow a VPN connection.
C. An Elastic IP address on the VPC instance
D. An IP address space that does not conflict with the one on-premises
E. Entries in Amazon Route 53 that allow the Instance to resolve its dependencies' IP addresses
F. A VM Import of the current virtual machine
Correct Answer: ADF
Explanation
Explanation/Reference:
AWS Direct Connect
AWS Direct Connect makes it easy to establish a dedicated network connection from your premises to AWS.
Using AWS Direct Connect, you can establish private connectMty between AWS you're your datacenter, office,
or colocation environment, which in many cases can reduce your network costs, increase bandwidth
throughput, and provide a more consistent network experience than Internet based connections. AWS Direct
Connect lets you establish a dedicated network connection between your network and one of the AWS Direct
Connect locations. Using industry standard 802.1q VLANs, this dedicated connection can be partitioned into
multiple virtual interfaces. This allows you to use the same connection to access public resources such as
objects stored in Amazon S3 using public IP address space, and private resources such as Amazon EC2
instances running within an Amazon Virtual Private Cloud (VPC) using private IP space, while maintaining
network separation between the public and private environments. Virtual interfaces can be reconfigured at any
time to meet your changing needs.
What is AWS Direct Connect?
AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard I gigabit or
10 gigabit Ethernet fiber-optic cable. One end of the cab Ie is connected to your router, the other to an AWS
Direct Connect router. With this connection in place, you can create virtual interfaces directly to the AWS cloud
(for example, to Amazon Elastic Compute Cloud {Amazon EC2) and Amazon Simple Storage Service (Amazon
S3)) and to Amazon Virtual Private Cloud (Amazon VPC), bypassing Internet service providers in your network
path. An AWS Direct Connect location provides access to Amazon Web Services in the region it is associated
with, as well as access to other US regions. For example, you can provision a single connection to any AWS
Direct Connect location in the US and use it to access public AWS services in all US Regions and AWS
GovCIoud (US).
The following diagram shows how AWS Direct Connect interfaces with your network.

Requirements
To use AWS Direct Connect, your network must meet one of the following conditions:
Your network is colocated with an existing AWS Direct Connect location. For more information on available
AWS Direct Connect locations, go to http://aws.amazon.com/directconnect/. You are working with an AWS
Direct Connect partner who is a member of the AWS Partner Network (APN). For a list of AWS Direct Connect
partners who can help you connect, go to http://aws.amazon.com/directconnect You are working with an
independent service provider to connect to AWS Direct Connect. In addition, your network must meet the
following conditions:
Connections to AWS Direct Connect require single mode fiber, 1000BASE-LX (1310nm) for 1 gigabit Ethernet,
or 10GBASE-LR {1310nm) for 10 gigabit Ethernet. Auto Negotiation for the port must be disabled. You must
support 802.1Q VLANs across these connections. Your network must support Border Gateway Protocol (BGP)
and BGP MD5 authentication. Optionally, you may configure Bidirectional Forwarding Detection (BFD). To
connect to Amazon Virtual Private Cloud (Amazon VPC), you must first do the following:
Provide a private Autonomous System Number (ASN). Amazon allocates a private IP address in the 169.x.x.x
range to you.
Create a virtual private gateway and attach it to your VPC. For more information about creating a virtual private
gateway, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon VPC User Guide. To
connect to public AWS products such as Amazon EC2 and Amazon S3, you need to provide the following:
A public ASN that you own (preferred) or a private ASN.
Public IP addresses (/31) (that is, one for each end of the BGP session) for each BGP session. If you do not
have public I P addresses to assign to this connection, log on to AWS and then open a ticket with AWS
Support.
The public routes that you will advertise over BGP.
QUESTION 293
You are migrating a legacy client-server application to AWS. The application responds to a specific DNS
domain (e.g. www.examp|e.com) and has a 2-tier architecture, with multiple application sewers and a database
server. Remote clients use TCP to connect to the application sewers. The application servers need to know the
IP address of the clients in order to function properly and are currently taking that information from the TCP
socket. A MuIti-AZ RDS MySQL instance will be used for the database. During the migration you can change
the application code, but you have to file a change request. How would you implement the architecture on
AWS in order to maximize scalability and high availability?
A. File a change request to implement Alias Resource support in the application. Use Route 53 Alias Resource
Record to distribute load on two application servers in different AZs.
B. File a change request to implement Latency Based Routing support in the application. Use Route 53 with
Latency Based Routing enabled to distribute load on two application servers in different AZs.
C. File a change request to implement Cross-Zone support in the application. Use an ELB with a TCP Listener
and Cross-Zone Load Balancing enabled, two application servers in different AZs.
D. File a change request to implement Proxy Protocol support in the application. Use an ELB with a TCP
Listener and Proxy Protocol enabled to distribute load on two application servers in different AZs.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 294
A newspaper organization has a on-premises application which allows the public to search its back catalogue
and retrieve indMdual newspaper pages via a website written in Java They have scanned the old newspapers
into JPEGs (approx 17TB) and used Optical Character Recognition (OCR) to populate a commercial search
product. The hosting platform and software are now end of life and the organization wants to migrate Its
archive to AW5 and produce a cost efficient architecture and still be designed for availability and durability.
Which is the most appropriate?
A. Use S3 with reduced redundancy Io store and serve the scanned files, install the commercial search
application on EC2 Instances and configure with auto-scaling and an Elastic Load Balancer.
B. Model the environment using CIoudFormation use an EC2 instance running Apache webserver and an open
source search application, stripe multiple standard EB5 volumes together to store the JPEGs and search
index.
C. Use S3 with standard redundancy to store and serve the scanned files, use CIoud5earch for query
processing, and use Elastic Beanstalk to host the website across multiple availability zones.
D. Use a single-AZ RD5 My5QL instance Io store the search index 33d the JPEG images use an EC2 instance
to serve the website and translate user queries into 5QL.
E. Use a CIoudFront download distribution to serve the JPEGs to the end users and Install the current
commercial search product, along with a Java Container Tor the website on EC2 instances and use
Route53 with DNS round-robin.
Correct Answer: C
Explanation
Explanation/Reference:
There is no such thing as "NIost appropriate" without knowing all your goals. I find your scenarios very fuzzy,
since you can obviously mix-n-match between them. I think you should decide by layers instead:
Load Balancer Layer: ELB or just DNS, or roll-your-own. (Using DNS+EIPs is slightly cheaper, but less reliable
than ELB.)
Storage Layer for 17TB of Images: This is the perfect use case for S3. Off-load all the web requests directly to
the relevant JPEGs in S3. Your EC2 boxes just generate links to them. If your app already serves it's own
images (not links to images), you might start with EFS. But more than likely, you can just setup a web server to
re-write or re-direct all JPEG links to S3 pretty easily. If you use S3, don't serve directly from the bucket- Serve
via a CNAME in domain you control. That way, you can switch in C|oudFront easily. EBS will be way more
expensive, and you'II need 2x the drives if you need 2 boxes. Yuck. Consider a smaller storage format. For
example, JPEG200 or WebP or other tools might make for smaller images.
There is also the DejaVu format from a while back.
Cache Layer: Adding Cloud Front in front of S3 will help people on the other side of the world-- well, possibly.
Typical archives follow a power law. The long tail of requests means that most JPEGs won't be requested
enough to be in the cache. So you are only speeding up the most popular objects. You can always wait, and
switch in CF later after you know your costs better. (In some cases, it can actually lower costs.) You can also
put CIoudFront in front of your app, since your archive search results should be fairly static. This will also allow
you to run with a smaller instance type, since CF will handle much of the load if you do it right.
Database Layer: A few options:
Use whatever your current server does for now, and replace with something else down the road. Don't underestimate
this approach, sometimes it's better to start now and optimize later.
Use RDS to run MySQL/ Postgres
I'm not as familiar with EIasticSearch I Cloudsearch, but obviously Cloudsearch will be less maintenance
+setup.
App Layer:
When creating the app layer from scratch, consider Cloud Formation and/or OpsWorks. It's extra stuff to learn,
but helps down the road.
Java+ Tomcat is right up the alley of E|asticBeanstaIk. (Basically EC2 + Autoscale + ELB). Preventing Abuse:
When you put something in a public S3 bucket, people will hot-link it from their web pages. If you want to
prevent that, your app on the EC2 box can generate signed links to S3 that expire in a few hours. Now
everyone will be forced to go thru the app, and the app can apply rate limiting, etc.
Saving money: If you don't mind having downtime:
run everything in one AZ (both DBs and EC2s). You can always add servers and AZs down the road, as long
as it's architected to be stateless. In fact, you should use multiple regions if you want it to be really robust. use
Reduced Redundancy in S3 to save a few hundred bucks per month (Someone will have to "go fix it" every
time it breaks, including having an off-line copy to repair S3.) Buy Reserved Instances on your EC2 boxes to
make them cheaper. (Start with the RI market and buy a partially used one to get started.) It's just a coupon
saying "if you run this type of box in this AZ, you will save on the per-hour costs." You can get 1/2 to 1/3 off
easily. Rewrite the application to use less memory and CPU -that way you can run on fewer/ smaller boxes.
(Nlay or may not be worth the investment.)
If your app will be used very infrequently, you will save a lot of money by using Lambda. I'd be worried that it
would be quite slow if you tried to run a Java application on it though .. We're missing some information like
load, latency expectations from search, indexing speed, size of the search index, etc. But with what you've
given us, I would go with S3 as the storage for the files (S3 rocks. It is really, really awesome). If you're stuck
with the commercial search application, then on EC2 instances with autoscaling and an ELB. If you are allowed
an alternative search engine, Elasticsearch is probably your best bet. I'd run it on EC2 instead ofthe AWS
Elasticsearch service, as IMHO it's not ready yet. Don't autoscale Elasticsearch automatically though, it'II
cause all sorts of issues. I have zero experience with CIoudSearch so I can't comment on that. Regardless of
which option, I'd use Cloud Formation for all of it.
QUESTION 295
A corporate web application is deployed within an Amazon Virtual Private Cloud (VPC) and is connected to the
corporate data center via an IPsec VPN. The application must authenticate against the on-premises LDAP
server. After authentication, each logged-in user can only access an Amazon Simple Storage Space (S3)
keyspace specific to that user.
Which two approaches can satisfy these objectives? (Choose 2 answers)
A. Develop an identity broker that authenticates against IAM security Token service to assume a Lam role in
order to get temporary AWS security credentials The application calls the identity broker to get AWS
temporary security credentials with access to the appropriate S3 bucket.
B. The application authenticates against LDAP and retrieves the name of an IAM role associated with the user.
The application then ca Ils the IAM Security Token Service to assume that IAM role The application can use
the temporary credentials to access the appropriate S3 bucket.
C. Develop an identity broker that authenticates against LDAP and then calls IAM Security To ken Service to
get IAM federated user credentials The application calls the identity broker to get IAM federated user
credentials with access to the appropriate S3 bucket.
D. The application authenticates against LDAP the application then calls the AWS identity and Access
Management (IAM) Security service to log in to IAM using the LDAP credentials the application can use the
IAM temporary credentials to access the appropriate S3 bucket.
E. The application authenticates against IAM Security Token Service using the LDAP credentials the
application uses those temporary AWS security credentials to access the appropriate S3 bucket.
Correct Answer: BC
Explanation
Explanation/Reference:
QUESTION 296
You are designing a multi-platform web application for AWS The application will run on EC2 instances and will
be accessed from PCs. tablets and smart phones Supported accessing platforms are Windows. MACOS. IOS
and Android Separate sticky session and SSL certificate setups are required for different platform types which
of the following describes the most cost effective and performance efficient architecture setup?
A. Setup a hybrid architecture to handle session state and SSL certificates on-prem and separate EC2
Instance groups running web applications for different platform types running in a VPC
B. Set up one ELB for all platforms to distribute load among multiple instance under it Each EC2 instance
implements ail functionality for a particular platform.
C. Set up two ELBs The first ELB handles SSL certificates for all platforms and the second ELB handles
session stickiness for all platforms for each ELB run separate EC2 instance groups to handle the web
application for each platform.
D. Assign multiple ELBS to an EC2 instance or group of EC2 instances running the common components of
the web application, one ELB for each platform type Session stickiness and SSL termination are done at the
ELBs.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 297
Your company has an on-premises multi-tier PHP web application, which recently experienced downtime due
to a large burst In web traffic due to a company announcement Over the coming days, you are expecting
similar announcements to drive similar unpredictable bursts, and are looking to find ways to quickly improve
your infrastructures ability to handle unexpected increases in traffic. The application currently consists of 2 tiers
a web tier which consists of a load balancer and several Linux Apache web servers as well as a database tier
which hosts a Linux server hosting a MySQL database. Which scenario below will provide full site functionality,
while helping to improve the ability of your application in the short timeframe required?
A. Failover environment: Create an S3 bucket and configure it for website hosting. Migrate your DNS to
Route53 using zone file import, and leverage Route53 DNS failover to failover to the S3 hosted website.
B. Hybrid environment: Create an AMI, which can be used to launch web servers in EC2. Create an Auto
Scaling group, which uses the AMI to scale the web tier based on incoming traffic. Leverage Elastic Load
Balancing to balance traffic between on-premises web servers and those hosted In AWS.
C. Offload traffic from on-premises environment: Setup a C|oudFront distribution, and configure CIoudFront to
cache objects from a custom origin. Choose to customize your object cache behavior, and select a TIL that
objects should exist in cache.
D. Migrate to AWS: Use VM Import/Export to quickly convert an on-premises web server to an AMI.
Create an Auto Scaling group, which uses the imported AMI to scale the web tier based on incoming traffic.
Create an RDS read replica and setup replication between the RDS instance and on-premises MySQL
server to migrate the database.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 298
Your company produces customer commissioned one-of-a-kind skiing helmets combining nigh fashion with
custom technical enhancements Customers can show off their IndMduality on the ski slopes and have access
to head-up-displays. GPS rear-view cams and any other technical innovation they wish to embed in the helmet.
The current manufacturing process is data rich and complex including assessments to ensure that the custom
electronics and materials used to assemble the helmets are to the highest standards Assessments are a
mixture of human and automated assessments you need to add a new set of assessment to model the failure
modes of the custom electronics using GPUs with CUDA, across a cluster of servers with low latency
networking.
What architecture would allow you to automate the existing process using a hybrid approach and ensure that
the architecture can support the evolution of processes over time?
A. Use AWS Data Pipeline to manage movement of data & meta-data and assessments Use an autoscaling
group of G2 instances in a placement group.
B. Use Amazon Simple Workflow {SWF) to manages assessments, movement of data & meta-data Use an
auto-scaling group of G2 instances in a placement group.
C. Use Amazon Simple Workflow (SWF) to manages assessments movement of data & meta-data Use an
auto-scaling group of C3 instances with SR-IOV {Single Root 1/0 Virtualization).
D. Use AWS data Pipeline to manage movement of data & meta-data and assessments use autoscaling group
of C3 with SR-IOV (Single Root 1/0 virtualization).
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 299
You're running an application on-premises due to its dependency on non-x86 hardware and want to use AWS
for data backup. Your backup application is only able to write to POSIX-compatible blockbased storage. You
have 140TB of data and would like to mount it as a single folder on your file server Users must be able to
access portions of this data while the backups are taking place. What backup solution would be most
appropriate for this use case?
A. Use Storage Gateway and configure it to use Gateway Cached volumes.
B. Configure your backup software to use S3 as the target for your data backups.
C. Configure your backup software to use Glacier as the target for your data backups.
D. Use Storage Gateway and configure it to use Gateway Stored volumes.
Correct Answer: A
Explanation
Explanation/Reference:
Gateway-Cached Volume Architecture
Gateway-cached volumes let you use Amazon Simple Storage Service (Amazon S3) as your primary data
storage while retaining frequently accessed data locally in your storage gateway. Gateway cached volumes
minimize the need to scale your on-premises storage infrastructure, while still providing your applications with
low-latency access to their frequently accessed data. You can create storage volumes up to 32 TIB in size and
attach to them as iSCSI devices from your on-premises application servers. Your gateway stores data that you
write to these volumes in Amazon S3 and retains recently read data in your on-premises storage gateway's
cache and upload buffer storage. Gateway-cached volumes can range from 1 GIB to 32 TIB in size and must
be rounded to the nearest GIB. Each gateway configured for gateway-cached volumes can support up to 32
volumes for a total maximum storage volume of 1,024 TIB (1 Pi B). In the gateway-cached volume solution,
AWS Storage Gateway stores all your on-premises application data in a storage volume in Amazon S3.
The following diagram provides an overview of the AWS Storage Gateway-cached volume deployment.
After you've installed the AWS Storage Gateway software appliance-the virtual machine (VM)-on a host in your
data center and activated it, you can use the AWS Management Console to provision storage volumes backed
by Amazon S3. You can also provision storage volumes programmatically using the AWS Storage Gateway
API or the AWS SDK libraries. You then mount these storage volumes to your on-premises application servers
as iSCSI devices.
You also al locate disks on-premises for the VM. These on-premises disks serve the following purposes:
Disks for use by the gateway as cache storage - As your applications write data to the storage volumes in
AWS, the gateway initially stores the data on the on-premises disks referred to as cache storage before
uploading the data to Amazon S3. The cache storage acts as the on-premises durable store for data that is
waiting to upload to Amazon S3 from the upload buffer.
The cache storage also lets the gateway store your appIication's recently accessed data on-premises for lowlatency
access. If your application requests data, the gateway first checks the cache storage for the data
before checking Amazon S3.
You can use the following guidelines to determine the amount of disk space to allocate for cache storage.
Generally, you should allocate at least 20 percent of your existing file store size as cache storage. Cache
storage should also be larger than the upload buffer. This latter guideline helps ensure cache storage is large
enough to persistently hold all data in the upload buffer that has not yet been uploaded to Amazon S3. Disks
for use by the gateway as the upload buffer - To prepare for upload to Amazon S3, your gateway also stores
incoming data in a staging area, referred to as an upload buffer. Your gateway uploads this buffer data over an
encrypted Secure Sockets Layer (SSL) connection to AWS, where it is stored encrypted in Amazon S3.
You can take incremental backups, called snapshots, of your storage volumes in Amazon S3. These point-intime
snapshots are also stored in Amazon S3 as Amazon EBS snapshots. When you take a new snapshot,
only the data that has changed since your last snapshot is stored. You can initiate snapshots on a scheduled
or one-time basis. When you delete a snapshot, only the data not needed for any other snapshots is removed.
You can restore an Amazon EBS snapshot to a gateway storage volume if you need to recover a backup of
your data. Alternatively, for snapshots up to 16 TiB in size, you can use the snapshot as a starting point for a
new Amazon EBS volume. You can then attach this new Amazon EBS volume to an Amazon EC2 instance. All
gateway-cached volume data and snapshot data is stored in Amazon S3 encrypted at rest using server-side
encryption (SSE). However, you cannot access this data with the Amazon S3 API or other tools such as the
Amazon S3 console.
QUESTION 300
You require the ability to analyze a large amount of data, which is stored on Amazon S3 using Amazon Elastic
Map Reduce. You are using the cc2 8x large Instance type, whose CPUs are mostly idle during processing.
Which of the below would be the most cost efficient way to reduce the runtime of the job?
A. Create more smaller flies on Amazon S3.
B. Add additional cc2 8x large instances by introducing a task group.
C. Use smaller instances that have higher aggregate 1/0 performance.
D. Create fewer, larger fi les on Amazon S3.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 301
Your department creates regular analytics reports from your company's log files All log data is collected in
Amazon S3 and processed by daily Amazon Elastic MapReduce (EMR) jobs that generate daily PDF reports
and aggregated tables in CSV format for an Amazon Redshift data warehouse. Your CFO requests that you
optimize the cost structure for this system. Which of the following alternatives will lower costs without
compromising average performance of the system or data integrity for the raw data?
A. Use reduced redundancy storage (RRS) for all data In S3. Use a combination of Spot Instances and
Reserved Instances for Amazon EMR jobs. Use Reserved Instances for Amazon Redshift.
B. Use reduced redundancy storage (RRS) for PDF and .csv data in S3. Add Spot Instances to EMR jobs.
Use Spot Instances for Amazon Redshift.
C. Use reduced redundancy storage (RRS) for PDF and .csv data In Amazon S3. Add Spot Instances to
Amazon EMR jobs. Use Reserved Instances for Amazon Redshift.
D. Use reduced redundancy storage (RRS) for all data in Amazon S3. Add Spot Instances to Amazon EMR
jobs. Use Reserved Instances for Amazon Redshift.
Correct Answer: C
Explanation
Explanation/Reference:
Using Reduced Redundancy Storage
Amazon S3 stores objects according to their storage class. It assigns the storage class to an object when it is
written to Amazon S3. You can assign objects a specific sto rage class (standard or reduced redundancy) only
when you write the objects to an Amazon S3 bucket or when you copy objects that are already stored in
Amazon S3. Standard is the default storage class. For information about storage classes, see Object Key and
Metadata.
In order to reduce storage costs, you can use reduced redundancy storage for noncritical, reproducible data at
lower levels of redundancy than Amazon S3 provides with standard storage. The lower level of redundancy
results in less durability and availability, but in many cases, the lower costs can make reduced redundancy
storage an acceptable storage solution. For example, it can be a cost effective solution for sharing media
content that is durably stored elsewhere. It can also make sense if you are storing thumbnails and other
resized images that can be easily reproduced from an original image. Reduced redundancy storage is
designed to provide 99.99% durability of objects over a given year. This durability level corresponds to an
average annual expected loss of 0.01% of objects. For example, if you store 10,000 objects using the RRS
option, you can, on average, expect to incur an annual loss of a single object per year (0.01% of 10,000
objects).
Note
This annual loss represents an expected average and does not guarantee the loss of less than 0.01% of
objects in a given year.
Reduced redundancy storage stores objects on multiple devices across multiple facilities, providing 400 times
the durability of a typical disk drive, but it does not replicate objects as many times as Amazon S3 standard
storage. In addition, reduced redundancy storage is designed to sustain the loss of data in a single facility. If an
object in reduced redundancy storage has been lost, Amazon S3 will return a 405 error on requests made to
that object. Amazon S3 also offers notifications for reduced redundancy storage object loss: you can configure
your bucket so that when Amazon S3 detects the loss of an RRS object, a notification will be sent through
Amazon Simple Notification Service (Amazon SNS). You can then replace the lost object. To enable
notifications, you can use the Amazon S3 console to set the Notifications property of your bucket.
QUESTION 302
You are the new IT architect in a company that operates a mobile sleep tracking application When activated at
night, the mobile app is sending collected data points of 1 kilobyte every 5 minutes to your backend The
backend takes care of authenticating the user and writing the data points into an Amazon DynamoDB table.
Every morning, you scan the table to extract and aggregate last night's data on a per user basis, and store the
results in Amazon S3.
Users are notified via Amazon 5NI5 mobile push notifications that new data is available, which is parsed and
visualized by (The mobile app Currently you have around IOOk users who are mostly based out of North
America.
You have been tasked to optimize the architecture of the backend system to lower cost what would you
recommend? (Choose 2 answers}
A. Create a new Amazon DynamoDB (able each day and drop the one for the previous day after its data is on
Amazon S3.
B. Have the mobile app access Amazon DynamoDB directly instead of J50N files stored on Amazon S3.
C. Introduce an Amazon SQS queue to buffer writes to the Amazon DynamoDB table and reduce provisioned
write throughput.
D. Introduce Amazon Elasticache Io cache reads from the Amazon DynamoDB table and reduce provisioned
read throughput.
E. Write data directly into an Amazon Redshift cluster replacing both Amazon DynamoDB and Amazon S3.
Correct Answer: BD
Explanation
Explanation/Reference:
QUESTION 303
Your website is serving on-demand training videos to your workforce. Videos are uploaded monthly in high
resolution MP4 format. Your workforce is distributed globally often on the move and using company-provided
tablets that require the HTTP Live Streaming (HLS) protocol to watch a video. Your company has no video
transcoding expertise and it required you may need to pay for a consultant. How do you implement the most
cost-efficient architecture without compromising high availability and quality of video delivery'?
A. A video transcoding pipeline running on EC2 using SQS to distribute tasks and Auto Scaling to adjust the
number of nodes depending on the length of the queue. EBS volumes to host videos and EBS snapshots to
incrementally backup original files after a few days. CIoudFront to serve HLS transcoded videos from EC2.
B. Elastic Transcoder to transcode original high-resolution MP4 videos to HLS. EBS volumes to host videos
and EBS snapshots to incrementally backup original files after a few days. CIoudFront to serve HLS
transcoded videos from EC2.
C. Elastic Transcoder to transcode original high-resolution NIP4 videos to HLS. S3 to host videos with Lifecycle
Management to archive original files to Glacier after a few days. C|oudFront to serve HLS transcoded videos
from S3.
D. A video transcoding pipeline running on EC2 using SQS to distribute tasks and Auto Scaling to adjust the
number of nodes depending on the length of the queue. S3 to host videos with Lifecycle Management to
archive all files to Glacier after a few days. CIoudFront to serve HLS transcoded videos from Glacier.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 304
You've been hired to enhance the overall security posture for a very large e-commerce site They have a well
architected multi-tier application running in a VPC that uses ELBs in front of both the web and the app tier with
static assets served directly from S3 They are using a combination of RDS and DynamoOB for their dynamic
data and then archMng nightly into S3 for further processing with EMR They are concerned because they
found questionable log entries and suspect someone is attempting to gain unauthorized access. Which
approach provides a cost effective scalable mitigation to this kind of attack?
A. Recommend that they lease space at a DirectConnect partner location and establish a IG DirectConnect
connection to their vPC they would then establish Internet connectMty into their space, filter the traffic in
hardware Web Application Firewall (WAF). And then pass the traffic through the DirectConnect connection
into their application running in their VPC,
B. Add previously identified hostile source IPs as an explicit INBOUND DENY NACL to the web tier sub net.
C. Add a WAF tier by creating a new ELB and an AutoScaIing group of EC2 Instances running a host based
WAF They would redirect Route 53 to resolve to the new WAF tier ELB The WAF tier would thier pass the
traffic to the current web tier The web tier Security Groups would be updated to only allow traffic from the
WAF tier Security Group
D. Remove all but TLS 1 2 from the web tier ELB and enable Advanced Protocol Filtering This will enable the
ELB itself to perform WAF functionality.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 305
You currently operate a web application In the AWS US-East region The application runs on an autoscaled
layer of EC2 instances and an RDS Multi-AZ database Your IT security compliance officer has tasked you to
develop a reliable and durable logging solution to track changes made to your EC2.1AM And RDS resources.
The solution must ensure the integrity and confidentiality of your log data. Which of these solutions would you
recommend?
A. Create a new C|oudTraiI trail with one new S3 bucket to store the logs and with the global services option
selected Use IAM roles S3 bucket policies and Multi Factor Authentication (MFA) Delete on the S3 bucket
that stores your logs.
B. Create a new CIoudTraiI with one new S3 bucket to store the logs Configure SNS to send log file delivery
notifications to your management system Use IAM roles and S3 bucket policies on the S3 bucket mat stores
your logs.
C. Create a new CIoudTraiI trail with an existing S3 bucket to store the logs and with the global services option
selected Use S3 ACLs and Multi Factor Authentication (MFA) Delete on the S3 bucket that stores your logs.
D. Create three new C|oudTrai| trails with three new S3 buckets to store the logs one for the AWS
Management console, one for AWS 5DKs and one for command line tools Use IAM roles and S3 bucket
policies on the S3 buckets that store your logs.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 306
An enterprise wants to use a third-party SaaS application. The SaaS application needs to have access to issue
several API commands to discover Amazon EC2 resources running within the enterprise's account The
enterprise has internal security policies that require any outside access to their environment must conform to
the principles of least prMlege and there must be controls in place to ensure that the credentials used by the
5aa5 vendor cannot be used by any other third party. Which of the following would meet all of these
conditions?
A. From the AW5 Management Console, navigate to the Security Credentials page and retrieve the access
and secret key for your account.
B. Create an IAM user within the enterprise account assign a user policy to the IAM user that allows only the
actions required by the SaaS application create a new access and secret key for the user and provide these
credentials to the 5aa5 provider.
C. Create an IAM role for cross-account access allows the SaaS provider's account to assume the role and
assign it a policy that allows only the actions required by the SaaS application.
D. Create an IAM role for EC2 instances, assign it a policy that allows only the actions required tor the Saas
application to work, provide the role ARM to the SaaS provider to use when launching their application
instances.
Correct Answer: C
Explanation
Explanation/Reference:
Granting Cross-account Permission to objects It Does Not Own In this example scenario, you own a bucket
and you have enabled other AWS accounts to upload objects. That is, your bucket can have objects that other
AWS accounts own. Now, suppose as a bucket owner, you need to grant cross-account permission on objects,
regardless of who the owner is, to a user in another account. For example, that user could be a billing
application that needs to access object metadata. There are two core issues:
The bucket owner has no permissions on those objects created by other AWS accounts. So for the bucket
owner to grant permissions on objects it does not own, the object owner, the AWS account that created the
objects, must first grant permission to the bucket owner. The bucket owner can then delegate those
permissions.
Bucket owner account can delegate permissions to users in its own account but it cannot delegate permissions
to other AWS accounts, because cross-account delegation is not supported. In this scenario, the bucket owner
can create an AWS Identity and Access Management (IAM) role with permission to access objects, and grant
another AWS account permission to assume the role temporarily enabling it to access objects in the bucket.
Background: Cross-Account Permissions and Using IAM Roles
IAM roles enable several scenarios to delegate access to your resources, and cross-account access is one of
the key scenarios. In this example, the bucket owner, Account A, uses an IAM role to temporarily delegate
object access cross-account to users in another AWS account, Account C. Each IAM role you create has two
policies attached to it:
A trust policy identifying another AWS account that can assume the role. An access policy defining what
permissions-for example, s3:Get0bject-are allowed when someone assumes the role. For a list of permissions
you can specify in a policy, see Specifying Permissions in a Policy. The AWS account identified in the trust
policy then grants its user permission to assume the role. The user can then do the following to access objects:
Assume the role and, in response, get temporary security credentials. Using the temporary security credentials,
access the objects in the bucket. For more information about IAM roles, go to Roles (Delegation and
Federation) in IAM User Guide.
The following is a summary of the walkthrough steps:
Account A administrator user attaches a bucket policy granting Account B conditional permission to upload
objects.
Account A administrator creates an IAM role, establishing trust with Account C, so users in that account can
access Account A. The access policy attached to the ro Ie limits what user in Account C can do when the user
accesses Account A.
Account B administrator uploads an object to the bucket owned by Account A, granting full --controI permission
to the bucket owner.
Account C administrator creates a user and attaches a user policy that allows the user to assume the role.
User in Account C first assumes the role, which returns the user temporary security credentials. Using those
temporary credentials, the user then accesses objects in the bucket. For this example, you need three
accounts. The following table shows how we refer to these accounts and the administrator users in these
accounts. Per IAM guidelines (see About Using an Administrator User to Create Resources and Grant
Permissions) we do not use the account root credentials in this walkthrough. Instead, you create an
administrator user in each account and use those credentials in creating resources and granting them
permissions
QUESTION 307
You are designing a data leak prevention solution for your VPC environment. You want your VPC Instances to
be able to access software depots and distributions on the Internet for product updates. The depots and
distributions are accessible via third party CONs by their URLs. You want to explicitly deny any other outbound
connections from your VPC instances to hosts on the internet.
Which of the following options would you consider?
A. Configure a web proxy server in your VPC and enforce URL-based ru les for outbound access Remove
default routes.
B. Implement security groups and configure outbound rules to only permit traffic to software depots.
C. Move all your instances into private VPC subnets remove default routes from all routing tables and add
specific routes to the software depots and distributions only.
D. Implement network access control lists to all specific destinations, with an Implicit deny as a rule.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 308
An administrator is using Amazon CIoudFormation to deploy a three tier web application that consists of a web
tier and application tier that will utilize Amazon DynamoDB for storage when creating the CIoudFormation
template which of the following would allow the application instance access to the DynamoDB tables without
exposing API credentials?
A. Create an Identity and Access Management Role that has the required permissions to read and write from
the required DynamoDB table and associate the Role to the application instances by referencing an
instance profile.
B. Use the Parameter section in the Cloud Formation template to nave the user input Access and Secret Keys
from an already created IAM user that has me permissions required to read and write from the required
DynamoDB table.
C. Create an Identity and Access Management Role that has the required permissions to read and write from
the required DynamoDB table and reference the Role in the instance profile property of the application
instance.
D. Create an identity and Access Management user in the CIoudFormation template that has permissions to
read and write from the required DynamoDB table, use the GetAtt function to retrieve the Access and secret
keys and pass them to the application instance through user-data.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 309
An AWS customer is deploying an application mat is composed of an AutoScaIing group of EC2 Instances.
The customers security policy requires that every outbound connection from these instances to any other
service within the customers Virtual Private Cloud must be authenticated using a unique x 509 certificate that
contains the specific instance-id.
In addition an x 509 certificates must Designed by the customer's Key management service in order to be
trusted for authentication.
Which of the following configurations will support these requirements?
A. Configure an IAM Role that grants access to an Amazon S3 object containing a signed certificate and
configure me Auto Scaling group to launch instances with this role Have the instances bootstrap get the
certificate from Amazon S3 upon first boot.
B. Embed a certificate into the Amazon Machine Image that is used by the Auto Scaling group Have the
launched instances generate a certificate signature request with the instance's assigned instance- id to the
Key management service for signature.
C. Configure the Auto Scaling group to send an SNS notification of the launch of a new instance to the trusted
key management service. Have the Key management service generate a signed certificate and send it
directly to the newly launched instance.
D. Configure the launched instances to generate a new certificate upon first boot Have the Key management
service poll the AutoScaIing group for associated instances and send new instances a certificate signature
(hat contains the specific instance-id.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 310
Your company has recently extended its datacenter into a VPC on AVVS to add burst computing capacity as
needed Members of your Network Operations Center need to be able to go to the AWS Management Console
and administer Amazon EC2 instances as necessary You don't want to create new IAM users for each NOC
member and make those users sign in again to the AWS Management Console Which option below will meet
the needs for your NOC members?
A. Use OAuth 2 0 to retrieve temporary AWS security credentials to enable your NOC members to sign in to
the AVVS Management Console.
B. Use web Identity Federation to retrieve AWS temporary security credentials to enable your NOC members
to sign in to the AWS Management Console.
C. Use your on-premises SAML 2.0-compliant identity provider (IOP) to grant the NOC members federated
access to the AWS Management Console via the AWS sing Ie sign-on (550) endpoint.
D. Use your on-premises SAML2.0-comp|iam identity provider (IOP) to retrieve temporary security credentials
to enable NOC members to sign in to the AWS Management Console.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 311
You are designing an SSUTLS solution that requires HTIPS clients to be authenticated by the Web server
using client certificate authentication. The solution must be resilient. Which of the following options would you
consider for configuring the web server infrastructure? (Choose 2 answers)
A. Configure ELB with TCP listeners on TCP/4d3. And place the Web servers behind it.
B. Configure your Web servers with EIPS Place the Web servers in a Route53 Record Set and configure
health checks against all Web servers.
C. Configure ELB with HTIPS listeners, and place the Web servers behind it.
D. Configure your web servers as the origins for a Cloud Front distribution. Use custom SSL certificates on
your Cloud Front distribution.
Correct Answer: AB
Explanation
Explanation/Reference:
QUESTION 312
You are designing a connectMty solution between on-premises infrastructure and Amazon VPC. Your server's
on-premises will De communicating with your VPC instances. You will De establishing IPSec tunnels over the
internet You will be using VPN gateways and terminating the IPsec tunnels on AWS supported customer
gateways.
Which of the following objectives would you achieve by implementing an IPSec tunnel as outlined above?
(Choose 4 answers)
A. End-to-end protection of data in transit
B. End-to-end Identity authentication
C. Data encryption across the Internet
D. Protection of data in transit over the Internet
E. Peer identity authentication between VPN gateway and customer gateway
F. Data integrity protection across the Internet
Correct Answer: CEF
Explanation
Explanation/Reference:
QUESTION 313
You are designing an intrusion detection prevention (IDS/IPS) solution for a customer web application in a
single VPC. You are considering the options for implementing IOS IPS protection for traffic coming from the
Internet.
Which of the following options would you consider? (Choose 2 answers)
A. Implement IDS/IPS agents on each Instance running In VPC
B. Configure an instance in each subnet to switch its network interface card to promiscuous mode and analyze
network traffic.
C. Implement Elastic Load Balancing with SSL listeners In front of the web applications
D. Implement a reverse proxy layer in front of web servers and configure IDS/ IPS agents on each reverse
proxy server.
Correct Answer: BD
Explanation
Explanation/Reference:
QUESTION 314
You are designing a photo sharing mobile app the application will store all pictures in a single Amazon S3
bucket.
Users will upload pictures from their mobile device directly to Amazon S3 and will be able to view and
download their own pictures directly from Amazon S3.
You want to configure security to handle potentially millions of users in the most secure manner possible. What
should your server-side application do when a new user registers on the photo sharing mobile application?
A. Create a set of long-term credentials using AWS Security Token Service with appropriate permissions Store
these credentials in the mobile app and use them to access Amazon S3.
B. Record the user's Information in Amazon RDS and create a role in IAM with appropriate permissions.
When the user uses their mobile app create temporary credentials using the AWS Security Token Service
'Assume Role' function Store these credentials in the mobile app's memory and use them to access Amazon
S3 Generate new credentials the next time the user runs the mobile app.
C. Record the user's Information In Amazon DynamoDB. When the user uses their mobile app create
temporary credentials using AWS Security Token Service with appropriate permissions Store these
credentials in the mobile app's memory and use them to access Amazon S3 Generate new credentials the
next time the user runs the mobile app.
D. Create IAM user. Assign appropriate permissions to the IAM user Generate an access key and secret key
for the IAM user, store them in the mobile app and use these credentials to access Amazon S3.
E. Create an IAM user. Update the bucket policy with appropriate permissions for the IAM user Generate an
access Key and secret Key for the IAM user, store them In the mobile app and use these credentials to
access Amazon S3.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 315
You have an application running on an EC2 Instance which will allow users to download fl ies from a private S3
bucket using a pre-assigned URL. Before generating the URL the application should verify the existence of the
fi Ie in S3.
How should the application use AWS credentials to access the S3 bucket securely?
A. Use the AWS account access Keys the application retrieves the credentials from the source code of the
application.
B. Create an IAM user for the application with permissions that allow list access to the S3 bucket launch the
instance as the IAM user and retrieve the IAM user's credentials from the EC2 instance user data.
C. Create an IAM role for EC2 that allows list access to objects in the S3 bucket. Launch the instance with the
role, and retrieve the roIe's credentials from the EC2 Instance metadata
D. Create an IAM user for the application with permissions that allow list access to the S3 bucket. The
application retrieves the IAM user credentials from a temporary directory with permissions that allow read
access only to the application user.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 316
You are designing a social media site and are considering how to mitigate distributed denial-of service (DDoS)
attacks. Which of the below are viable mitigation techniques? (Choose 3 answers)
A. Add multiple elastic network interfaces (ENis) to each EC2 instance to increase the network bandwidth.
B. Use dedicated instances to ensure that each instance has the maximum performance possible.
C. Use an Amazon C|oudFront distribution for both static and dynamic content.
D. Use an Elastic Load Balancer with auto scaling groups at the web. App and Amazon Relational Database
Service (RDS) tiers
E. Add alert Amazon CIoudWatch to look for high Network in and CPU utilization.
F. Create processes and capabilities to quickly add and remove rules to the instance OS firewall.
Correct Answer: BCE
Explanation
Explanation/Reference:
QUESTION 317
A benefits enrollment company is hosting a 3-tier web application running in a VPC on AWS which includes a
NAT (Network Address Translation) instance in the public Web tier. There is enough provisioned capacity for
the expected workload tor the new fiscal year benefit enrollment period plus some extra overhead Enrollment
proceeds nicely for two days and then the web tier becomes unresponsive, upon investigation using
CIoudWatch and other monitoring tools it is discovered that there is an extremely large and unanticipated
amount of inbound traffic coming from a set of 15 specific IP addresses over port 80 from a country where the
benefits company has no customers. The web tier instances are so overloaded that benefit enrollment
administrators cannot even SSH into them. Which actMty would be useful in defending against this attack?
A. Create a custom route table associated with the web tier and block the attacking IP addresses from the IGW
(Internet Gateway)
B. Change the EIP (Elastic IP Address) of the NAT instance in the web tier subnet and update the Main Route
Table with the new EIP
C. Create 15 Security Group rules to block the attacking IP addresses over port 80
D. Create an inbound NACL (Network Access control list) associated with the web tier subnet with deny rules
to block the attacking IP addresses
Correct Answer: D
Explanation
Explanation/Reference:
Use AWS Identity and Access Management (IAM) to control who in your organization has permission to create
and manage security groups and network ACLs (NACL). Isolate the responsibilities and roles for better
defense. For example, you can give only your network administrators or security ad min the permission to
manage the security groups and restrict other roles.
QUESTION 318
Your fortune 500 company has under taken a TCO analysis evaluating the use of Amazon S3 versus acquiring
more hardware The outcome was that ail employees would be granted access to use Amazon S3 for storage
of their personal documents.
Which of the following will you need to consider so you can set up a solution that incorporates single sign-on
from your corporate AD or LDAP directory and restricts access for each user to a designated user folder in a
bucket? (Choose 3 Answers)
A. Setting up a federation proxy or identity provider
B. Using AWS Security Token Service to generate temporary tokens
C. Tagging each folder in the bucket
D. Configuring IAM role
E. Setting up a matching IAM user for every user in your corporate directory that needs access to a folder in
the bucket
Correct Answer: ABD
Explanation
Explanation/Reference:
QUESTION 319
Your company policies require encryption of sensitive data at rest. You are considering the possible options for
protecting data while storing it at rest on an EBS data volume, attached to an EC2 instance. Which of these
options would allow you to encrypt your data at rest? (Choose 3 answers)
A. Implement third party volume encryption tools
B. Do nothing as EBS volumes are encrypted by default
C. Encrypt data inside your applications before storing it on EBS
D. Encrypt data using native data encryption drivers at the file system level
E. Implement SSL/TLS for all services running on the server
Correct Answer: ACD
Explanation
Explanation/Reference:
QUESTION 320
You have a periodic Image analysis application that gets some files In Input analyzes them and tor each file
writes some data in output to a ten file the number of files in input per day is high and concentrated in a few
hours of the day.
Currently you have a server on EC2 with a large EBS volume that hosts the input data and the results it takes
almost 20 hours per day to complete the process
What services could be used to reduce the elaboration time and improve the availability of the solution?
A. S3 to store 1/0 files. SOS to distribute elaboration commands to a group of hosts working in parallel.
Auto scaling to dynamically size the group of hosts depending on the length of the SOS queue
B. EBS with Provisioned IOPS (PIOPS) to store 1/0 files. SNS to distribute elaboration commands to a group of
hosts working in parallel Auto Scaling to dynamically size the group of hosts depending on the number of
SNS notifications
C. S3 to store 1/0 files, SNS to distribute evaporation commands to a group of hosts working in parallel.
Auto scaling to dynamically size the group of hosts depending on the number of SNS notifications
D. EBS with Provisioned IOPS (PIOPS) to store 1/0 files SOS to distribute elaboration commands to a group of
hosts working in parallel Auto Scaling to dynamically size the group ot hosts depending on the length of the
SOS queue.
Correct Answer: D
Explanation
Explanation/Reference:
Amazon EBS allows you to create storage volumes and attach them to Amazon EC2 instances. Once
attached, you can create a file system on top of these volumes, run a database, or use them in any other way
you would use a block device. Amazon EBS volumes are placed in a specific Availability Zone, where they are
automatically replicated to protect you from the failure of a single component. Amazon EBS provides three
volume types: General Purpose (SSD), Provisioned IOPS (SSD), and Magnetic. The three volume types differ
in performance characteristics and cost, so you can choose the right storage performance and price for the
needs of your applications. All EBS volume types offer the same durable snapshot capabilities and are
designed for 99.999% availability.
QUESTION 321
You require the ability to analyze a customer's clickstream data on a website so they can do behavioral
analysis. Your customer needs to know what sequence of pages and ads their customer clicked on. This data
will be used in real time to modify the page layouts as customers click through the site to increase stickiness
and advertising click-through. Which option meets the requirements for captioning and analyzing this data?
A. Log clicks in weblogs by URL store to Amazon S3, and then analyze with Elastic MapReduce
B. Push web clicks by session to Amazon Kinesis and analyze behavior using Kinesis workers
C. Write click events directly to Amazon Redshift and then analyze with SQL
D. Publish web clicks by session to an Amazon SQS queue men periodically drain these events to Amazon
RDS and analyze with sol
Correct Answer: B
Explanation
Explanation/Reference:
http:/ /www.slideshare.net/AmazonWebServices/aws-webcast-introduction-to-amazon-kinesis
QUESTION 322
An AWS customer runs a public blogging website. The site users upload two million blog entries a month. The
average blog entry size is 200 KB. The access rate to blog entries drops to negligible 6 months after
publication and users rarely access a blog entry 1 year after publication. Additionally, blog entries have a high
update rate during the first 3 months following publication, this drops to no updates after 6 months. The
customer wants to use CIoudFront to improve his user's load times. Which of the following recommendations
would you make to the customer?
A. Duplicate entries into two different buckets and create two separate CIoudFront distributions where S3
access is restricted only to Cloud Front identity
B. Create a CIoudFront distribution with "US" Europe price class for US/ Europe users and a different
CIoudFront distribution with AI I Edge Locations' for the remaining users.
C. Create a CIoudFront distribution with S3 access restricted only to the CIoudFront identity and partition the
blog entry's location in S3 according to the month it was uploaded to be used with CIoudFront behaviors.
D. Create a CIoudFronI distribution with Restrict Viewer Access Forward Query string set to true and minimum
TTL of 0.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 323
Your company is getting ready to do a major public announcement of a social media site on AWS. The website
is running on EC2 instances deployed across multiple Availability Zones with a MuIti-AZ RDS MySQL Extra
Large DB Instance. The site performs a high number of small reads and writes per second and relies on an
eventual consistency model. After comprehensive tests you discover that there is read contention on RDS
MySQL. Which are the best approaches to meet these requirements? (Choose 2 answers)
A. Deploy EIasticCache in-memory cache running in each availability zone
B. Implement sharding to distribute load to multiple RDS MySQL instances
C. Increase the RDS MySQL Instance size and Implement provisioned IQPS
D. Add an RDS MySQL read replica in each availability zone
Correct Answer: AC
Explanation
Explanation/Reference:
QUESTION 324
A company is running a batch analysis every hour on their main transactional DB. running on an RDS MySQL
instance to populate their central Data Warehouse running on Redshift During the execution of the batch their
transactional applications are very slow When the batch completes they need to update the top management
dashboard with the new data The dashboard is produced by another system running on-premises that is
currently started when a manually-sent email notifies that an update is required The on-premises system
cannot be modified because is managed by another team. How would you optimize this scenario to solve
performance issues and automate the process as much as possible?
A. Replace RDS with Redshift for the batch analysis and SNS to notify the on-premises system to update the
dashboard
B. Replace ROS with Redshift for the oaten analysis and SQS to send a message to the on-premises system
to update the dashboard
C. Create an RDS Read Replica for the batch analysis and SNS to notify me on-premises system to update the
dashboard
D. Create an RDS Read Replica for the batch analysis and SQS to send a message to the on-premises system
to update the dashboard.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 325
You are implementing a URL whitelisting system for a company that wants to restrict outbound HTTP'S
connections to specific domains from their EC2-hosted applications you deploy a single EC2 instance running
proxy software and configure It to accept traffic from all subnets and EC2 instances in the VPC. You configure
the proxy to only pass through traffic to domains that you define in its whitelist configuration You have a nightly
maintenance window or 10 minutes where all instances fetch new software updates. Each update Is about
200MB In size and there are 500 instances In the VPC that routinely fetch updates After a few days you notice
that some machines are failing to successfully download some, but not all of their updates within the
maintenance window. The download URLs used for these updates are correctly listed in the proxy's whitelist
configuration and you are able to access them manually using a web browser on the instances. What might be
happening? {Choose 2 answers)
A. You are running the proxy on an undersized EC2 instance type so network throughput is not sufficient for all
instances to download their updates in time.
B. You are running the proxy on a sufficiently-sized EC2 instance in a private subnet and its network
throughput is being throttled by a NAT running on an undersized EC2 instance.
C. The route table for the subnets containing the affected EC2 instances is not configured to direct network
traffic for the software update locations to the proxy.
D. You have not allocated enough storage to t he EC2 instance running the proxy so the network buffer is filling
up, causing some requests to fail.
E. You are running the proxy in a public subnet but have not allocated enough EIPs to support the needed
network throughput through the Internet Gateway {IGW).
Correct Answer: AB
Explanation
Explanation/Reference:
QUESTION 326
To serve Web traffic for a popular product your chief financial officer and IT director have purchased 10 ml
large heavy utilization Reserved Instances (Rls) evenly spread across two availability zones:
Route 53 is used to deliver the traffic to an Elastic Load Balancer (ELB). After several months, the product
grows even more popular and you need additional capacity As a result, your company purchases two C3.2x|
arge medium utilization Rls You register the two c3 2xIarge instances with your ELB and quickly find that the
ml large instances are at 100% of capacity and the c3 2xIarge instances have significant capacity that's unused
Which option is the most cost effective and uses EC2 capacity most effectively?
A. Use a separate ELB for each instance type and distribute load to ELBs with Route 53 weighted round robin
B. Configure Autoscaning group and Launch Configuration with ELB to add up to 10 more on-demand ml large
instances when triggered by Cloudwatch shut off c3 2xIarge instances
C. Route traffic to EC2 ml large and c3 2xIarge instances directly using Route 53 latency based routing and
health checks shut off ELB
D. Configure ELB with two c3 2xiarge Instances and use on-demand Autoscaling group for up to two additional
c3.2x|arge instances Shut on mi .|arge instances.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 327
A read only news reporting site with a combined web and application tier and a database tier that receives
large and unpredictable traffic demands must be able to respond to these traffic fluctuations automatically.
What AWS services should be used meet these requirements?
A. Stateless instances for the web and application tier synchronized using Elasticache Memcached in an
autoscaimg group monitored with CIoudWatch. And RDSwith read replicas.
B. Stateful instances for the web and application tier in an autoscaling group monitored with CIoudWatch and
RDS with read replicas.
C. Stateful instances for the web and application tier in an autoscaling group monitored with CIoudWatch.
And multi-AZ RDS.
D. Stateless instances for the web and application tier synchronized using EIastiCache Memcached in an
autoscaling group monitored with CIoudWatch and multi-AZ RDS.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 328
You are running a news website in the eu-west-1 region that updates every 15 minutes. The website has a
world-wide audience it uses an Auto Scaling group behind an Elastic Load Balancer and an Amazon RDS
database Static content resides on Amazon S3, and is distributed through Amazon CIoudFront. Your Auto
Scaling group is set to trigger a scale up event at 60% CPU utilization, you use an Amazon RDS extra large
DB instance with 10.000 Provisioned IOPS its CPU utilization is around 80%.
While freeable memory is in the 2GB range.
Web analytics reports show that the average load time of your web pages is around 1 5 to 2 seconds, but your
SEO consultant wants to bring down the average load time to under 0.5 seconds. How would you improve
page load times for your users? (Choose 3 answers)
A. Lower the scale up trigger of your Auto Scaling group to 30% so it scales more aggressively.
B. Add an Amazon EIastiCache caching layer to your application for storing sessions and frequent DB quenes
C. Configure Amazon CIoudFront dynamic content support to enable caching of re-usable content from your
site
D. Switch Amazon RDS database to the high memory extra large Instance type
E. Set up a second installation in another region, and use the Amazon Route 53 latency-based routing feature
to select the right region.
Correct Answer: ABD
Explanation
Explanation/Reference:
QUESTION 329
A large real -estate brokerage is exploring the option o( adding a cost-effective location based alert to their
existing mobile application The application backend infrastructure currently runs on AWS Users who opt in to
this service will receive alerts on their mobile device regarding real-estate otters in proximity to their location.
For the alerts to be relevant delivery time needs to be in the low minute count the existing mobile app has 5
million users across the us Which one of the following architectural suggestions would you make to the
customer?
A. The mobile application will submit its location to a web service endpoint utilizing Elastic Load Balancing and
EC2 instances: DynamoDB will be used to store and retrieve relevant otters EC2 instances will
communicate with mobile earners/device providers to push alerts back to mobile application.
B. Use AWS DirectConnect or VPN to establish connectMty with mobile carriers EC2 instances will receive the
mobile applications ' location through carrier connection: ROS will be used to store and relevant relevant
offers EC2 instances will communicate with mobile carriers to push alerts back to the mobile application
C. The mobile application will send device location using SOS. EC2 instances will retrieve the re Ievant others
from DynamoDB AWS MobiIe Push will be used to send offers to the mobile application
D. The mobile application will send device location using AWS Nlobile Push EC2 instances will retrieve the
relevant offers from DynamoDB EC2 instances will communicate with mobile carriers/device providers to
push alerts back to the mobile application.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 330
A company is building a voting system for a popular TV show, viewers win watch the performances then visit
the show's website to vote for their favorite performer. It is expected that in a short period of time after the show
has finished the site will receive millions of visitors. The visitors will first login to the site using their
Amazon.com credentials and then submit their vote. After the voting is completed the page will display the vote
totals. The company needs to build the site such that can handle the rapid influx of traffic while maintaining
good performance but also wants to keep costs to a minimum. Which of the design patterns below should they
use?
A. Use Cloud Front and an Elastic Load balancer in front of an auto-scaled set of web servers, the web servers
will first can the Login With Amazon service to authenticate the user then process the users vote and store
the result into a multi-AZ Relational Database Service instance.
B. Use CIoudFront and the static website hosting feature of S3 with the Javascript SDK to call the Login With
Amazon service to authenticate the user, use IAM Roles to gain permissions to a DynamoDB table to store
the users vote.
C. Use Cloud Front and an Elastic Load Balancer in front of an auto-scaled set of web servers, the web servers
will first call the Login with Amazon service to authenticate the user, the web servers will process the users
vote and store the result into a DynamoDB table using IAM Roles for EC2 instances to gain permissions to
the DynamoDB table.
D. Use Cloud Front and an Elastic Load Balancer in front of an auto-scaled set of web servers, the web servers
will first call the Login. With Amazon service to authenticate the user, the web sewers win process the users
vote and store the result into an SQS queue using IAM Roles for EC2 Instances to gain permissions to the
SQS queue. A set of application sewers will then retrieve the items from the queue and store the result into
a DynamoDB table.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 331
You are developing a new mobile application and are considering storing user preferences in AWS.2w This
would provide a more uniform cross-device experience to users using multiple mobile devices to access the
application. The preference data for each user is estimated to be SOKB in size Additionally 5 million customers
are expected to use the application on a regular basis. The solution needs to be cost-effective, highly available,
scalable and secure, how would you design a solution to meet the above requirements?
A. Setup an RDS MySQL instance in 2 availability zones to store the user preference data. Deploy a public
facing application on a server in front of the database to manage security and access credentials
B. Setup a DynamoDB table with an item for each user having the necessary attributes to hold the user
preferences. The mobile application will query the user preferences directly from the DynamoDB table.
Utilize STS. Web Identity Federation, and DynamoDB Fine Grained Access Control to authenticate and
authorize access.
C. Setup an RDS MySQL instance with multiple read replicas in 2 availability zones to store the user
preference data .The mobile application will query the user preferences from the read replicas.
Leverage the MySQL user management and access prMlege system to manage security and access
credentials.
D. Store the user preference data in S3 Setup a DynamoDB table with an item for each user and an item
attribute pointing to the user' S3 object. The mobile application will retrieve the S3 URL from DynamoDB
and then access the S3 object directly utilize STS, Web identity Federation, and S3 ACLs to authenticate
and authorize access.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 332
Your team has a tomcat-based Java application you need to deploy into development, test and production
environments. After some research, you opt to use Elastic Beanstalk due to its tight integration with your
developer tools and RDS due to its ease of management. Your QA team lead points out that you need to roll a
sanitized set of production data into your environment on a nightly basis. Similarly, other software teams in
your org want access to that same restored data via their EC2 instances in your VPC .The optimal setup for
persistence and security that meets the above requirements would be the following.
A. Create your RDS instance as part of your Elastic Beanstalk definition and alter its security group to allow
access to it from hosts in your application subnets.
B. Create your RDS instance separately and add its IP address to your appIication's DB connection strings in
your code Alter its security group to allow access to it from hosts within your VPC's IP address block.
C. Create your RDS instance separately and pass its DNS name to your app's DB connection string as an
environment variable. Create a security group for client machines and add it as a valid source for DB traffic
to the security group of the RDS instance itself.
D. Create your RDS instance separately and pass its DNS name to your's DB connection string as an
environment variable Alter its security group to allow access to It from hosts In your application subnets.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 333
You are looking to migrate your Development (Dev) and Test environments to AWS. You have decided to use
separate AWS accounts to host each environment. You plan to link each accounts bill to a Master AWS
account using Consolidated Billing. To make sure you Keep within budget you would like to implement a way
for administrators in the Master account to have access to stop, delete and/or terminate resources in both the
Dev and Test accounts. Identify which option will allow you to achieve this goal.
A. Create IAM users in the Master account with full Admin permissions. Create cross-account roles in the Dev
and Test accounts that grant the Master account access to the resources in the account by inheriting
permissions from the Master account.
B. Create IAM users and a cross-account role in the Master account that grants full Admin permissions to the
Dev and Test accounts.
C. Create IAM users in the Master account Create cross-account roles in the Dev and Test accounts that have
full Admin permissions and grant the Master account access.
D. Link the accounts using Consolidated Billing. This will give IAM users in the Master account access to
resources in the Dev and Test accounts
Correct Answer: C
Explanation
Explanation/Reference:
Bucket Owner Granting Cross-account Permission to objects It Does Not Own In this example scenario, you
own a bucket and you have enabled other AWS accounts to upload objects. That is, your bucket can have
objects that other AWS accounts own. Now, suppose as a bucket owner, you need to grant cross-account
permission on objects, regardless of who the owner is, to a user in another account. For example, that user
could be a billing application that needs to access object metadata. There are two core issues:
The bucket owner has no permissions on those objects created by other AWS accounts. So for the bucket
owner to grant permissions on objects it does not own, the object owner, the AWS account that created the
objects, must first grant permission to the bucket owner. The bucket owner can then delegate those
permissions.
Bucket owner account can delegate permissions to users in its own account but it cannot delegate permissions
to other AWS accounts, because cross-account delegation is not supported. In this scenario, the bucket owner
can create an AWS Identity and Access Management (IAM) role with permission to access objects, and grant
another AWS account permission to assume the role temporarily enabling it to access objects in the bucket.
Background: Cross-Account Permissions and Using IAM Roles
IAM roles enable several scenarios to delegate access to your resources, and cross-account access is one of
the key scenarios. In this example, the bucket owner, Account A, uses an IAM role to temporarily delegate
object access cross-account to users in another AWS account, Account C. Each IAM role you create has two
policies attached to it:
A trust policy identifying another AWS account that can assume the role. An access policy defining what
permissions-for example, s3:Get0bject-are allowed when someone assumes the role. For a list of permissions
you can specify in a policy, see Specifying Permissions in a Policy. The AWS account identified in the trust
policy then grants its user permission to assume the role. The user can then do the following to access objects:
Assume the role and, in response, get temporary security credentials. Using the temporary security credentials,
access the objects in the bucket. For more information about IAM roles, go to Roles (Delegation and
Federation) in IAM User Guide.
The following is a summary of the walkthrough steps:
Account A administrator user attaches a bucket policy granting Account B conditional permission to upload
objects.
Account A administrator creates an IAM role, establishing trust with Account C, so users in t hat account can
access Account A. The access policy attached to the role limits what user in Account C can do when the user
accesses Account A.
Account B administrator uploads an object to the bucket owned by Account A, granting full-control permission
to the bucket owner.
Account C administrator creates a user and attaches a user policy that al lows the user to assume the role.
User in Account C first assumes the role, which returns the user temporary security credentials. Using those
temporary credentials, the user then accesses objects in the bucket. For this example, you need three
accounts. The following tab Ie shows how we refer to these accounts and the administrator users in these
accounts. Per IAM guidelines (see About Using an Administrator User to Create Resources and Grant
Permissions) we do not use the account root credentials in this walkthrough. Instead, you create an
administrator user in each account and use those credentials in creating resources and granting them
permissions
QUESTION 334
Your customer is willing to consolidate their log streams (access logs application logs security logs etc.) in one
single system. Once consolidated, the customer wants to analyze these logs in real time based on heuristics.
From time to time, the customer needs to validate heuristics, which requires going back to data samples
extracted from the last 12 hours?
What is the best approach to meet your customer's requirements?
A. Send all the log events to Amazon SQS. Setup an Auto Scaling group of EC2 sewers to consume the logs
and apply the heuristics.
B. Send all the log events to Amazon Kinesis develop a client process to apply heuristics on the logs
C. Configure Amazon Cloud Trail to receive custom logs, use EMR to apply heuristics the logs
D. Setup an Auto Scaling group of EC2 syslogd servers, store the logs on S3 use EMR to apply heuristics on
the logs
Correct Answer: B
Explanation
Explanation/Reference:
The throughput of an Amazon Kinesis stream is designed to scale without limits via increasing the number of
shards within a stream. However, there are certain limits you should keep in mind while using Amazon Kinesis
Streams:
By default, Records of a stream are accessible for up to 24 hours from the time they are added to the stream.
You can raise this limit to up to 7 days by enabling extended data retention. The maximum size of a data blob
(the data payload before Base64-encoding) within one record is 1 megabyte (MB).
Each shard can support up to 1000 PUT records per second.
For more information about other API level limits, see Amazon Kinesis Streams Limits.
QUESTION 335
You deployed your company website using Elastic Beanstalk and you enabled log file rotation to S3. An Elastic
Map Reduce job is periodically analyzing the logs on S3 to build a usage dashboard that you share with your
CIO.
You recently improved overall performance of the website using Cloud Front for dynamic content delivery and
your website as the origin.
After this architectural change, the usage dashboard shows that the traffic on your website dropped by an
order of magnitude. How do you fix your usage dashboard'?
A. Enable Cloud Front to deliver access logs to S3 and use them as input of the Elastic Map Reduce job.
B. Turn on Cloud Trail and use trail log tiles on S3 as input of the Elastic Map Reduce job
C. Change your log collection process to use Cloud Watch ELB metrics as input of the Elastic Map Reducejob
D. Use Elastic Beanstalk "Rebuild Environment" option to update log delivery to the Elastic Map Reduce job.
E. Use Elastic Beanstalk 'Restart App server(s)" option to update log delivery to the Elastic Map Reduce job.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 336
You are running a successful multitier web application on AWS and your marketing department has asked you
to add a reporting tier to the application. The reporting tier will aggregate and publish status reports every 30
minutes from user-generated information that is being stored in your web application s database. You are
currently running a MuIti-AZ RDS MySQL instance for the database tier. You also have implemented
Elasticache as a database caching layer between the application tier and database tier. Please select the
answer that will allow you to successful ly implement the reporting tier with as little impact as possible to your
database.
A. Continually send transaction logs from your master database to an S3 bucket and generate the reports off
the S3 bucket using S3 byte range request s.
B. Generate the reports by querying the synchronously replicated standby RDS MySQL instance maintained
through Multi-AZ.
C. Launch a RDS Read Replica connected to your MuIti AZ master database and generate reports by querying
the Read Replica.
D. Generate the reports by querying the EIastiCache database caching tier.
Correct Answer: C
Explanation
Explanation/Reference:
Amazon RDS allows you to use read replicas with MuIti-AZ deployments. In Multi-AZ deployments for MySQL,
Oracle, SQL Server, and PostgreSQL, the data in your primary DB Instance is synchronously replicated to a
standby instance in a different Availability Zone (AZ). Because of their synchronous replication, MuIti-AZ
deployments for these engines offer greater data durability benefits than do read replicas. (In all Amazon RDS
for Aurora deployments, your data is automatically replicated across 3 Availability Zones.) You can use MuIti-
AZ deployments and read replicas in conjunction to enjoy the complementary benefits of each. You can simply
specify that a given Multi-AZ deployment is the source DB Instance for your Read replicas. That way you gain
both the data durability and availability benefits of Multi -AZ deployments and the read scaling benefits of read
replicas.
Note that for MuIti-AZ deployments, you have the option to create your read replica in an AZ other than that of
the primary and the standby for even more redundancy. You can identify the AZ corresponding to your standby
by looking at the "Secondary Zone" field of your DB Instance in the AWS Management Console.
QUESTION 337
A web company is looking to implement an intrusion detection and prevention system into their deployed VPC.
This platform should have the ability to scale to thousands of instances running inside of the VPC, How should
they architect t heir solution to achieve these goals?
A. Configure an instance with monitoring software and the elastic network interface (ENI) set to promiscuous
mode packet sniffing to see an traffic across the VPC,
B. Create a second VPC and route all traffic from the primary application VPC through the second VPC where
the scalable virtualized IDS/IPS platform resides.
C. Configure servers running in the VPC using the host-based 'route' commands to send all traffic through the
platform to a scalable virtualized IDS/IPS.
D. Configure each host with an agent that collects all network traffic and sends that traffic to the IDS/IPS
platform for inspection.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 338
A web-startup runs its very successful social news application on Amazon EC2 with an Elastic Load Balancer,
an Auto-Scaling group of Java/Tomcat application-servers, and DynamoDB as data store. The main webapplication
best runs on m2 x large instances since it is highly memory- bound Each new deployment requires
semi-automated creation and testing of a new AM for the application servers which takes quite a while ana is
therefore only done once per week. Recently, a new chat feature has been implemented in nodejs and wails to
be integrated in the architecture. First tests show that the new component is CPU bound Because the company
has some experience with using Chef, they decided to streamline the deployment process and use AWS Ops
Works as an application life cycle tool to simplify management of the application and reduce the deployment
cycles.
What configuration in AWS Ops Works is necessary to integrate the new chat module in the most cost-efficient
and filexible way?
A. Create one AWS OpsWorks stack, create one AWS Ops Works layer, create one custom recipe
B. Create one AWS OpsWorks stack create two AWS Ops Works layers create one custom recipe
C. Create two AWS OpsWorks stacks create two AWS Ops Works layers create one custom recipe
D. Create two AWS OpsWorks stacks create two AWS Ops Works layers create two custom recipe
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 339
Your firm has uploaded a large amount of aerial image data to S3 In the past, in your on-premises
environment, you used a dedicated group of servers to oaten process this data and used Rabbit MOAn open
source messaging system to get job information to the servers. Once processed the data would go to tape and
be shipped offsite. Your manager told you to stay with the current design, and leverage AWS archival storage
and messaging services to minimize cost. Which is correct?
A. Use SOS for passing job messages use Cloud Watch alarms to terminate EC2 worker instances when they
become idle. Once data is processed, change the storage class of the S3 objects to Reduced Redundancy
Storage.
B. Setup Auto-Scaled workers triggered by queue depth that use spot instances to process messages in SOS
Once data is processed,
C. Change the storage class of the S3 objects to Reduced Redundancy Storage. Setup Auto-Scaled workers
triggered by queue depth that use spot instances to process messages in SOS Once data is processed,
change the storage class of the S3 objects to Glacier.
D. Use SNS to pass job messages use Cloud Watch alarms to terminate spot worker instances when they
become idle. Once data is processed, change the storage class of the S3 object to Glacier.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 340
What does Amazon S3 stand for?
A. Simple Storage Solution.
B. Storage Storage Storage (triple redundancy Storage).
C. Storage Sewer Solution.
D. Simple Storage Sewice.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 341
You must assign each sewer to at least _ security group
A. 3
B. 2
C. 4
D. 1
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 342
Before I delete an EBS volume, what can I do if I want to recreate the volume later?
A. Create a copy of the EBS volume (not a snapshot)
B. Store a snapshot of the volume
C. Download the content to an EC2 instance
D. Back up the data in to a physical disk
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 343
Select the most correct
The device name /dev/sdal (within Amazon EC2) is _
A. Possible for EBS volumes
B. Reserved for the root device
C. Recommended for EBS volumes
D. Recommended for instance store volumes
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 344
If I want an instance to have a public IP address, which IP address should I use'?
A. Elastic I P Address
B. Class B IP Address
C. Class A IP Address
D. Dynamic IP Address
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 345
What does RRS stand for when talking about S3?
A. Redundancy Removal System
B. Relational Rights Storage
C. Regional Rights Standard
D. Reduced Redundancy Storage
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 346
All Amazon EC2 instances are assigned two IP addresses at launch, out of which one can only be reached
from within the Amazon EC2 network?
A. Multiple IP address
B. Public IP address
C. Private IP address
D. Elastic I P Address
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 347
What does Amazon SWF stand for?
A. Simple Web Flow
B. Simple Work Flow
C. Simple Wireless Forms
D. Simple Web Form
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 348
What is the Reduced Redundancy option in Amazon S3?
A. Less redundancy for a lower cost.
B. It doesn't exist in Amazon S3, but in Amazon EBS.
C. It allows you to destroy any copy of your files outside a specific jurisdiction.
D. It doesn't exist at all
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 349
Fill in the blanks: Resources that are created in AWS are identified by a unique identifier called an
A. Amazon Resource Number
B. Amazon Resource Nametag
C. Amazon Resource Name
D. Amazon Resource Namespace
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 350
If I write the below command, what does it do?
ec2-run ami-e3a5408a -n 20 -g appserver
A. Start twenty instances as members of appserver group.
B. Creates 20 rules in the security group named appserver
C. Terminate twenty instances as members of appserver group.
D. Start 20 security groups
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 351
While creating an Amazon RDS DB, your first task is to set up a DB _ that controls what IP addresses or EC2
instances have access to your DB Instance.
A. Security Pool
B. Secure Zone
C. Security Token Pool
D. Security Group
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 352
When you run a DB Instance as a Multi-AZ deployment, the " _ " serves database writes and reads
A. secondary
B. backup
C. stand by
D. primary
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 353
Every user you create in the IAM system starts with _ _
A. Partial permissions
B. Full permissions
C. No permissions
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 354
Can you create IAM security credentials for existing users?
A. Yes, existing users can have security credentials associated with their account.
B. No, IAM requires that all users who have credentials set up are not existing users
C. No, security credentials are created within GROUPS, and then users are associated to GROUPS at a later
time.
D. Yes, but only IAM credentials, not ordinary security credentials.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 355
What does Amazon EC2 provide?
A. Virtual sewers in the Cloud.
B. A platform to run code (Java, PHP, Python), paying on an hourly basis.
C. Computer Clusters in the Cloud.
D. Physical sewers, remotely managed by the customer.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 356
Amazon SWF is designed to help users
A. Design graphical user interface interactions
B. Manage user identification and authorization
C. Store Web content
D. Coordinate synchronous and asynchronous tasks which are distributed and fault tolerant.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 357
Can I control if and when MySQL based RDS Instance is upgraded to new supported versions?
A. No
B. Only in VPC
C. Yes
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 358
If I modify a DB Instance or the DB parameter group associated with the instance, should I reboot the instance
for the changes to take effect?
A. No
B. Yes
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 359
When you view the block device mapping for your instance, you can see only the EBS volumes, not the
instance store volumes.
A. Depends on the instance type
B. FALSE
C. Depends on whether you use API call
D. TRUE
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 360
By default, EBS volumes that are created and attached t o an instance at launch are deleted when t hat
instance is terminated. You can modify this behavior by changing the value of the flag _ to false when you
launch the instance
A. Delete On Termination
B. Remove On Deletion
C. Remove On Termination
D. Terminate On Deletion
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 361
What are the initial settings of an user created security group?
A. Allow all inbound traffic and Allow no outbound traffic
B. AI low no inbound traffic and AI low no outbound traffic
C. AI low no inbound traffic and AI low all outbound traffic
D. Allow all inbound traffic and Allow all outbound traffic
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 362
Will my standby RDS instance be in the same Region as my primary?
A. Only for Oracle RDS types
B. Yes
C. Only if configured at launch
D. No
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 363
What does Amazon Elastic Beanstalk provide?
A. A scalable storage appliance on top of Amazon Web Services.
B. An application container on top of Amazon Web Services.
C. A service by this name doesn't exist.
D. A scalable cluster of EC2 instances.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 364
True or False: When using IAM to control access to your RDS resources, the key names that can be used are
case sensitive. For example, aws:CurrentTime is NOT equivalent to AWS:currenttime.
A. TRUE
B. FALSE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 365
What will be the status of the snapshot until the snapshot is complete.
A. running
B. working
C. progressing
D. pending
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 366
Can we attach an EBS volume to more than one EC2 instance at the same time?
A. No
B. Yes.
C. Only EC2-optimized EBS volumes.
D. Only in read mode.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 367
True or False: Automated backups are enabled by default for a new DB Instance.
A. TRUE
B. FALSE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 368
What does the AWS Storage Gateway provide?
A. It allows to integrate on-premises IT environments with Cloud Storage.
B. A direct encrypted connection to Amazon S3.
C. It's a backup solution that provides an on-premises Cloud storage.
D. It provides an encrypted SSL endpoint for backups in the Cloud.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 369
Amazon RDS automated backups and DB Snapshots are currently supported for only the _ _ storage engine
A. InnoDB
B. MyISAM
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 370
How many relational database engines does RDS currently support?
A. Three: MySQL, Oracle and Microsoft SQL Sewer.
B. Just two: MySQL and Oracle.
C. Five: MySQL, PostgreSQL, MongoDB, Cassandra and SQLite.
D. Just one: MySQL.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 371
Fill in the blanks: The base URI for all requests for instance metadata is _ _
A. http://254.169.169.254/Iatest/
B. http://169.169.254.254/|atesU
C. http://127.0.0.1/|atest/
D. http://I69.254.169.254/|atest/
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 372
While creating the snapshots using the command line tools, which command should I be using?
A. ec2-deploy-snapshot
B. ec2-fresh-snapshot
C. ec2-create-snapshot
D. ec2-new-snapshot
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 373
Typically, you want your application to check whether a request generated an error before you spend any time
processing results. The easiest way to find out if an error occurred is to look for an _ node in the response from
the Amazon RDS API.
A. Incorrect
B. Error
C. FALSE
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 374
What are the two permission types used by AWS'?
A. Resource-based and Product-based
B. Product-based and Service-based
C. Service-based
D. User-based and Resource-based
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 375
In the Amazon cloudwatch, which metric should I be checking to ensure that your DB Instance has enough free
storage space?
A. Free Storage
B. Free Storage Space
C. Free Storage Volume
D. Free DB Storage Space
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 376
Amazon RDS DB snapshots and automated backups are stored in
A. Amazon S3
B. Amazon ECS Volume
C. Amazon RDS
D. Amazon EMR
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 377
What is the maximum key length of a tag'?
A. 512 Unicode characters
B. 64 Unicode characters
C. 256 Unicode characters
D. 128 Unicode characters
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 378
Groups can't _.
A. be nested more than 3 levels
B. be nested at all
C. be nested more than 4 levels
D. be nested more than 2 levels
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 379
You must increase storage size in increments of at least _ %
A. 40
B. 20
C. 50
D. 10
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 380
Changes to the backup window take effect _ _
A. from the next billing cycle
B. after 30 minutes
C. immediately
D. after 24 hours
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 381
Using Amazon C|oudWatch's Free Tier, what is the frequency of metric updates which you receive?
A. 5 minutes
B. 500 milliseconds.
C. 30 seconds
D. 1 minute
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 382
Which is the default region in AWS?
A. eu-west-1
B. us-east-1
C. us-east-2
D. ap-southeast-1
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 383
What are the Amazon EC2 API tools?
A. They don't exist. The Amazon EC2 AMI tools, instead, are used to manage permissions.
B. Command-line tools to the Amazon EC2 web service.
C. They are a set of graphical tools to manage EC2 instances.
D. They don't exist. The Amazon API tools are a client interface to Amazon Web Senrices.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 384
What are the two types of licensing options available for using Amazon RDS for Oracle?
A. BYOL and Enterprise License
B. BYOL and License Included
C. Enterprise License and License Included
D. Role based License and License Included
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 385
What does a "Domain" refer to in Amazon SWF?
A. A security group in which only tasks inside can communicate with each other
B. A special type of worker
C. A collection of related Workflows
D. The DNS record for the Amazon SWF service
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 386
EBS Snapshots occur _
A. Asynchronously
B. Synchronously
C. Weekly
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 387
Disabling automated backups _ disable the point-in-time recovery.
A. if configured to can
B. will never
C. will
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 388
Out of the stripping options available for the EBS volumes, which one has the following disadvantage :
'Doubles the amount of 1/0 required from the instance to EBS compared to RAID 0, because you're mirroring
all writes to a pair of volumes, limiting how much you can stripe.'?
A. Raid 0
B. RAID 1+0 (RAID 10)
C. Raid 1
D. Raid
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 389
Is creating a Read Replica of another Read Replica supported?
A. Only in certain regions
B. Only with MSSQL based RDS
C. Only for Oracle RDS types
D. No
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 390
Can Amazon S3 uploads resume on failure or do they need to restart?
A. Restart from beginning
B. You can resume them, if you flag the "resume on fai lure" option before uploading.
C. Resume on failure
D. Depends on the file size
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 391
Which of the following cannot be used in Amazon EC2 to control who has access to specific Amazon EC2
instances?
A. Security Groups
B. IAM System
C. SSH keys
D. Windows passwords
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 392
Fill in the blanks: _ let you categorize your EC2 resources in different ways, for example, by purpose, owner, or
environment.
A. wildcards
B. pointers
C. Tags
D. special filters
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 393
How can I change the security group membership for interfaces owned by other AWS, such as Elastic Load
Balancing?
A. By using the service specific console or API\CLI commands
B. None of these
C. Using Amazon EC2 API/CLI
D. using all these methods
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 394
What is the maximum write throughput I can provision for a single Dynamic DB table?
A. 1,000 write capacity units
B. 100,000 write capacity units
C. Dynamic DB is designed to scale without limits, but if you go beyond 10,000 you have to contact AWS first.
D. 10,000 write capacity units
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 395
What does the following command do with respect to the Amazon EC2 security groups? ec2-revoke
RevokeSecurityGroup Ingress
A. Removes one or more security groups from a rule.
B. Removes one or more security groups from an Amazon EC2 instance.
C. Removes one or more rules from a security group.
D. Removes a security group from our account.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 396
Can a 'user' be associated with multiple AWS accounts?
A. No
B. Yes
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 397
True or False: Manually created DB Snapshots are deleted after the DB Instance is deleted.
A. TRUE
B. FALSE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 398
Can I move a Reserved Instance from one Region to another?
A. No
B. Only if they are moving into GovC|oud
C. Yes
D. Only if they are moving to US East from another region
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 399
What is Amazon Glacier?
A. You mean Amazon "Iceberg": it's a low-cost storage service.
B. A security tool that allows to "freeze" an EBS volume and perform computer forensics on it.
C. A low-cost storage service that provides secure and durable storage for data archMng and backup.
D. It's a security tool that allows to "freeze" an EC2 instance and perform computer forensics on it.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 400
What is the durability of S3 RRS?
A. 99.99%
B. 99.95%
C. 99.995%
D. 99.999999999%
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 401
What does specifying the mapping /dev/sdc=none when launching an instance do'?
A. Prevents /dev/sdc from creating the instance.
B. Prevents /dev/sdc from deleting the instance.
C. Set the value of /dev/sdc to 'zero'.
D. Prevents /dev/sdc from attaching to the instance.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 402
Is Federated Storage Engine currently supported by Amazon RDS for MySQL?
A. Only for Oracle RDS instances
B. No
C. Yes
D. Only in VPC
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 403
Is there a limit to how many groups a user can be in?
A. Yes for all users
B. Yes for all users except root
C. No
D. Yes unless special permission granted
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 404
True or False: When you perform a restore operation to a point in time or from a DB Snapshot, a new DB
Instance is created with a new endpoint.
A. FALSE
B. TRUE
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 405
A/An _ acts as a firewall that controls the traffic allowed to reach one or more instances.
A. security group
B. ACL
C. IAM
D. Private IP Addresses
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 406
Will my standby RDS instance be in the same Availability Zone as my primary?
A. Only for Oracle RDS types
B. Yes
C. Only if configured at launch
D. No
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 407
While launching an RDS DB instance, on which page I can select the Availability Zone?
A. REVIEW
B. DB INSTANCE DETAILS
C. MANAGEMENT OPTIONS
D. ADDITIONAL CONFIGURATION
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 408
What does t he following command do with respect to the Amazon EC2 security groups? ec2-create-group
CreateSecurityGroup
A. Groups the user created security groups in to a new group for easy access.
B. Creates a new security group for use with your account.
C. Creates a new group inside the security group.
D. Creates a new rule inside the security group.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 409
In the Launch Db Instance Wizard, where can I select the backup and maintenance options?
A. Under DB INSTANCE DETAILS
B. Under REVI EW
C. Under MANAGEMENT OPTIONS
D. Under ENGINE SELECTION
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 410
What happens to the data on an instance if the instance reboots (intentionally or unintentionally)?
A. Data will be lost
B. Data persists
C. Data may persist however cannot be sure
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 411
How many types of block devices does Amazon EC2 support A
A. 2
B. 3
C. 4
D. 1
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 412
Provisioned IOPS Costs: you are charged for the IOPS and storage whether or not you use them in a given
month.
A. FALSE
B. TRUE
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 413
IAM provides several policy templates you can use to automatically assign permissions to the groups you
create. The _ policy template gives the Admins group permission to access all account resources, except your
AWS account information
A. Read Only Access
B. Power User Access
C. AWS Cloud Formation Read Only Access
D. Administrator Access
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 414
While performing the volume status checks, if the status is insufficient-data, what does it mean?
A. the checks may still be in progress on the volume
B. the check has passed
C. the check has failed
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 415
IAM's Policy Evaluation Logic always starts with a default _ for every request, except for those that use the
AWS account's root security credentials b
A. Permit
B. Deny
C. Cancel
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 416
By default, when an EBS volume is attached to a Windows instance, it may show up as any drive letter on the
instance. You can change the settings of the _ Senrice to set the drive letters of the EBS volumes per your
specifications.
A. EBS Config Senrice
B. AMI Config Senrice
C. Ec2 Config Senrice
D. Ec2-AMI Config Senrice
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 417
For each DB Instance class, what is the maximum size of associated storage capacity?
A. 5GB
B. 1 TB
C. 2TB
D. 500GB
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 418
SQL Sewer _ store log ins and passwords in the master database.
A. can be configured to but by default does not
B. doesn't
C. does
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 419
What is Oracle SQL Developer?
A. An AWS developer who is an expert in Amazon RDS using both the Oracle and SQL Server DB engines
B. A graphical Java tool distributed without cost by Oracle.
C. It is a variant of the SQL Sewer Management Studio designed by Microsoft to support Oracle DBMS
functionalities
D. A different DBMS released by Microsoft free of cost
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 420
Does Amazon RDS allow direct host access via Telnet, Secure Shell (SSH), or Windows Remote Desktop
Connection?
A. Yes
B. No
C. Depends on if it is in VPC or not
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 421
To view information about an Amazon EBS volume, open the Amazon EC2 console at https://
console.aws.amazon.com/ec2/, click in the Navigation pane.
A. EBS
B. Describe
C. Details
D. Volumes
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 422
Using Amazon IAM, can I give permission based on organizational groups?
A. Yes but only in certain cases
B. No
C. Yes always
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 423
While creating the snapshots using the API, which Action should I be using?
A. MakeSnapShot
B. FreshSnapshot
C. Dep|oySnapshot
D. CreateSnapshot
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 424
What is an isolated database environment running in the cloud (Amazon RDS) called?
A. DB Instance
B. DB Sewer
C. DB Unit
D. DB Volume
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 425
While signing in REST/ Query requests, for additional security, you should transmit your requests using Secure
Sockets Layer (SSL) by using __
A. HTIP
B. Internet Protocol Security(IPsec)
C. TLS (Transport Layer Security)
D. HTIPS
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 426
What happens to the 1/0 operations while you take a database snapshot?
A. 1/0 operations to the database are suspended for a few minutes while the backup is in progress.
B. 1/0 operations to the database are sent to a Replica (if available) for a few minutes while the backup is in
progress.
C. 1/0 operations will be functioning normally
D. 1/0 operations to the database are suspended for an hour while the backup is in progress
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 427
Read Replicas require a transactional storage engine and are only supported for the _ _ storage engine
A. OracIeISAM
B. MSSQLDB
C. InnoDB
D. IV|y|SAIV|
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 428
When running my DB Instance as a MuIti-AZ deployment, can I use the standby for read or write operations?
A. Yes
B. Only with MSSQL based RDS
C. Only for Oracle RDS instances
D. No
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 429
When should I choose Provisioned IOPS over Standard RDS storage?
A. If you have batch-oriented workloads
B. If you use production online transaction processing (OLTP) workloads.
C. If you have workloads that are not sensitive to consistent performance
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 430
In the 'DetaiIed' monitoring data available for your Amazon EBS volumes, Provisioned IOPS volumes
automatically send _ minute metrics to Amazon CIoudWatch.
A. 3
B. 1
C. 5
D. 2
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 431
What is the minimum charge for the data transferred between Amazon RDS and Amazon EC2 Instances in the
same Availability Zone?
A. USD 0.10 per GB
B. No charge. It is free.
C. USD 0.02 per GB
D. USD 0.01 per GB
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 432
Are Resenred Instances available for Multi-AZ Deployments?
A. Only for Cluster Compute instances
B. Yes for all instance types
C. Only for M3 instance types
D. No
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 433
Which service enables AWS customers to manage users and permissions in AWS?
A. AWS Access Control Service (ACS}
B. AWS Identity and Access Management (IAM}
C. AWS Identity Manager (AIM}
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 434
Which Amazon Storage behaves like raw, unformatted, external block devices that you can attach to your
instances?
A. None of these.
B. Amazon Instance Storage
C. Amazon EBS
D. All of these
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 435
Which Amazon service can I use to define a virtual network that closely resembles a traditional data center?
A. Amazon VPC
B. Amazon Service Bus
C. Amazon EMR
D. Amazon RDS
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 436
What is the command line instruction for running the remote desktop client in Windows?
A. desk.cpI
B. mstsc
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 437
Amazon RDS automated backups and DB Snapshots are currently supported for only the _ _ storage engine
A. MyISAM
B. InnoDB
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 438
MySQL installations default to port _.
A. 3306
B. 443
C. 80
D. 1158
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 439
If you have chosen Multi-AZ deployment, in the event of a planned or unplanned outage of your primary DB
Instance, Amazon RDS automatically switches to the standby replica. The automatic failover mechanism
simply changes the record of the main DB Instance to point to the standby DB Instance.
A. DNAME
B. CNAME
C. TXT
D. MX
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 440
If I modify a DB Instance or the DB parameter group associated with the instance, should I reboot the instance
for the changes to take effect?
A. No
B. Yes
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 441
If I want to run a database in an Amazon instance, which is the most recommended Amazon storage opHon?
A. Amazon Instance Storage
B. Amazon EBS
C. You can't run a database inside an Amazon instance.
D. Amazon S3
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 442
In regards to IAM you can edit user properties later, but you cannot use the console to change the
A. user name
B. password
C. default group
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 443
Can I test my DB Instance against a new version before upgrading?
A. No
B. Yes
C. Only in VPC
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 444
True or False: If you add a tag that has the same key as an existing tag on a DB Instance, the new value
ovenrvrites the old value.
A. FALSE
B. TRUE
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 445
Can I use Provisioned IOPS with VPC?
A. Only Oracle based RDS
B. No
C. Only with MSSQL based RDS
D. Yes for all RDS instances
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 446
Making your snapshot public shares all snapshot data with everyone. Can the snapshots with AWS Market
place product codes be made public?
A. No
B. Yes
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 447
Fill in the blanks: "To ensure failover capabilities, consider using a _ for incoming traffic on a network
interface".
A. primary public IP
B. secondary private I P
C. secondary public I P
D. add on secondary IP
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 448
If I have multiple Read Replicas for my master DB Instance and I promote one of them, what happens to the
rest of the Read Replicas?
A. The remaining Read Replicas will still replicate from the older master DB Instance
B. The remaining Read Replicas will be deleted
C. The remaining Read Replicas will be combined to one read replica
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 449
What does Amazon Cloud Formation provide?
A. The ability to setup Autoscaling for Amazon EC2 instances.
B. None of these.
C. A templated resource creation for Amazon Web Services.
D. A template to map network resources for Amazon Web Services.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 450
Can I encrypt connections between my application and my DB Instance using SSL?
A. No
B. Yes
C. Only in VPC
D. Only in certain regions
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 451
What are the four levels of AWS Premium Support?
A. Basic, Developer, Business, Enterprise
B. Basic, Startup, Business, Enterprise
C. Free, Bronze, Silver, Gold
D. All support is free
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 452
What can I access by visiting the URL: http:/ /status.aws.amazon.com/?
A. Amazon Cloud Watch
B. Status of the Amazon RDS DB
C. AWS Service Health Dashboard
D. AWS Cloud Monitor
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 453
Please select the Amazon EC2 resource which cannot be tagged.
A. images (AM|s, kernels, RAM disks)
B. Amazon EBS volumes
C. Elastic IP addresses
D. VPCs
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 454
Can the string value of 'Key' be prefixed with :aws:"?
A. Only in GovC|oud
B. Only for S3 not EC2
C. Yes
D. No
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 455
Because of the extensibility limitations of striped storage attached to Windows Sewer, Amazon RDS does not
currently support increasing storage on a _ DB Instance.
A. SQL Sewer
B. MySQL
C. Oracle
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 456
Through which of the following interfaces is AWS Identity and Access Management available? A) AWS
Management Console
B) Command line interface (CLI}
C) IAM Query API
D) Existing libraries
A. Only through Command line interface (CLI )
B. A, Band C
C. A and C
D. All of the above
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 457
Select the instatement
A. In Amazon EC2, the private IP addresses only returned to Amazon EC2 when the instance is stopped or
terminated
B. In Amazon VPC, an instance retains its private IP addresses when the instance is stopped.
C. In Amazon VPC, an instance does NOT retain its private IP addresses when the instance is stopped.
D. In Amazon EC2, the private IP address is associated exclusive ly with the instance for its lifetime
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 458
How are the EBS snapshots saved on Amazon S3?
A. Exponentially
B. Incrementally
C. EBS snapshots are not stored in the Amazon S3
D. Decrementally
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 459
What is the type of monitoring data (for Amazon EBS volumes) which is available automatically in 5- minute
periods at no charge called?
A. Basic
B. Primary
C. Detailed
D. Local
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 460
The new DB Instance that is created when you promote a Read Replica retains the backup window penod.
A. TRUE
B. FALSE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 461
What happens when you create a topic on Amazon SNS?
A. The topic is created, and it has the name you specified for it.
B. An ARN (Amazon Resource Name) is created.
C. You can create a topic on Amazon SQS, not on Amazon SNS.
D. This question doesn't make sense.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 462
Can I delete a snapshot of the root device of an EBS volume used by a registered AMI?
A. Only via API
B. Only via Console
C. Yes
D. No
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 463
Can I test my DB Instance against a new version before upgrading?
A. Only in VPC
B. No
C. Yes
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 464
What is the maximum response time for a Business level Premium Support case?
A. 120 seconds
B. 1 hour
C. 10 minutes
D. 12 hours
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 465
The _ service is targeted at organizations with multiple users or systems that use AWS products such as
Amazon EC2, Amazon SimpIeDB, and the AWS Management Console.
A. Amazon RDS
B. AWS Integrity Management
C. AWS Identity and Access Management
D. Amazon EMR
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 466
True or False: Without IAM, you cannot control the tasks a particular user or system can do and what AWS
resources they might use.
A. FALSE
B. TRUE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 467
When you use the AWS Management Console to delete an IAM user, IAM also deletes any signing certificates
and any access keys belonging to the user.
A. FALSE
B. This is configurable
C. TRUE
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 468
When automatic failover occurs, Amazon RDS will emit a DB Instance event to inform you that automatic
failover occurred. You can use the to ret urn information about events related to your DB Instance
A. FetchFai|ure
B. DescriveFai|ure
C. DescribeEvents
D. FetchEvents
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 469
What is the default maximum number of MFA devices in use per AWS account (at the root account level)?
A. 1
B. 5
C. 15
D. 10
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 470
D0 the Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?
A. Only if instructed to when created
B. Yes
C. No
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 471
Can we attach an EBS volume to more than one EC2 instance at the same time?
A. Yes.
B. No
C. Only EC2-optimized EBS volumes.
D. Only in read mode.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 472
Select the set of options. These are the initial settings for the default security group:
A. Allow no inbound traffic, Allow all outbound traffic and Allow instances associated with this security group to
talk to each other
B. Allow all inbound traffic, Allow no outbound traffic and Allow instances associated with this security group to
talk to each other
C. Allow no inbound traffic, Allow all outbound traffic and Does NOT allow instances associated with this
security group to talk to each other
D. AI low all inbound traffic, Allow all outbound traffic and Does NOT allow instances associated with this
security group to talk to each other
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 473
What does Amazon Route53 provide?
A. A global Content Delivery Network.
B. None of these.
C. A scalable Domain Name System.
D. An SSH endpoint for Amazon EC2.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 474
What does Amazon E|astiCache provide?
A. A senrice by this name doesn't exist. Perhaps you mean Amazon C|oudCache.
B. A virtual server with a huge amount of memory.
C. A managed In-memory cache service.
D. An Amazon EC2 instance with the Memcached software already pre-installed.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 475
How many Elastic IP by default in Amazon Account?
A. 1 Elastic IP
B. 3 Elastic IP
C. 5 Elastic IP
D. 0 Elastic IP
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 476
What is a Security Group?
A. None of these.
B. A list of users that can access Amazon EC2 instances.
C. An Access Control List (ACL) for AWS resources.
D. A firewall for inbound traffic, built-in around every Amazon EC2 instance.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 477
The one-time payment for Reserved Instances is _ _ refundable if the reservation is cancelled.
A. always
B. in some circumstances
C. never
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 478
Please select the Amazon EC2 resource which can be tagged.
A. key pairs
B. Elastic IP addresses
C. placement groups
D. Amazon EBS snapshots
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 479
If an Amazon EBS volume is the root device of an instance, can I detach it without stopping the instance?
A. Yes but only if Windows instance
B. No
C. Yes
D. Yes but only if a Linux instance
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 480
If you are using Amazon RDS Provisioned IOPS storage with MySQL and Oracle database engines, you can
scale the throughput of your database Instance by specifying the IOPS rate f rom _ _
A. 1,000 to 1,00,000
B. 100 to 1, 000
C. 10,000to 1,00,000
D. 1, 000 to 10, 000
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 481
Every user you create in the IAM system starts with _ _
A. full permissions
B. no permissions
C. partial permissions
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 482
After an Amazon VPC instance is launched, can I change the VPC security groups it belongs to?
A. Only if the tag "VPC_Change_Group" is true
B. Yes. You can.
C. No. You cannot.
D. Only if the tag "VPC Change Group" is true
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 483
A, _ is an indMdual, system, or application that interacts with AWS programmatically.
A. user
B. AWS Account
C. Group
D. Role
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 484
Select the statement:
A. You don't need not specify the resource identifier while stopping a resource
B. You can terminate, stop, or delete a resource based solely on its tags
C. You can't terminate, stop, or delete a resource based solely on its tags
D. You don't need to specify the resource identifier while terminating a resource
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 485
Amazon EC2 has no Amazon Resource Names (ARNs) because you can't specify a particular Amazon EC2
resource in an IAM policy.
A. TRUE
B. FALSE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 486
Can I initiate a "forced failover" for my MySQL Multi-AZ DB Instance deployment?
A. Only in certain regions
B. Only in VPC
C. Yes
D. No
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 487
A group can contain many users. Can a user belong to multiple groups?
A. Yes always
B. No
C. Yes but only if they are using two factor authentication
D. Yes but only in VPC
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 488
Is the encryption of connections between my application and my DB Instance using SSL for the MySQL server
engines available?
A. Yes
B. Only in VPC
C. Only in certain regions
D. No
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 489
Which AWS instance address has the following characteristics? :" If you stop an instance, its Elastic IP address
is unmapped, and you must remap it when you restart the instance."
A. Both A and B
B. None of these
C. VPC Addresses
D. EC2 Addresses
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 490
True or False: Common points of failures like generators and cooling equipment are shared across Availability
Zones.
A. TRUE
B. FALSE
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 491
Please select the most answer regarding the persistence of the Amazon Instance Store
A. The data on an instance store volume persists only during the life of the associated Amazon EC2 instance
B. The data on an instance store volume is lost when the security group rule of the associated instance is
changed.
C. The data on an instance store volume persists even after associated Amazon EC2 instance is deleted
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 492
Multi-AZ deployment _ supported for Microsoft SQL Server DB Instances.
A. is not currently
B. is as of 2013
C. is planned to be in 2014
D. will never be
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 493
Security groups act like a firewall at the instance level, whereas _ are an additional layer of security that act at
the subnet level.
A. DB Security Groups
B. VPC Security Groups
C. network ACLs
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 494
What does Amazon Elastic Beanstalk provide?
A. An application container on top of Amazon Web Services.
B. A scalable storage appliance on top of Amazon Web Services.
C. A scalable cluster of EC2 instances.
D. A service by this name doesn't exist.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 495
Is the SQL Server Audit feature supported in the Amazon RDS SQL Server engine?
A. No
B. Yes
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 496
Are you able to integrate a multi-factor token service with the AWS Platform?
A. Yes, using the AWS multi-factor token devices to authenticate users on the AWS platform.
B. No, you cannot integrate multi-factor token devices with the AWS platform.
C. Yes, you can integrate private multi-factor token devices to authenticate users to the AWS platform.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 497
My Read Replica appears "stuck" after a MuIti-AZ failover and is unable to obtain or apply updates from the
source DB Instance. What do I do?
A. You will need to delete the Read Replica and create a new one to rep lace it.
B. You will need to disassociate the DB Engine and re associate it.
C. The instance should be deployed to Single AZ and then moved to MuIti- AZ once again
D. You will need to delete the DB Instance and create a new one to replace it.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 498
Which DNS name can only be resolved within Amazon EC2?
A. Internal DNS name
B. External DNS name
C. Global DNS name
D. Private DNS name
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 499
If your DB instance runs out of storage space or file system resources, its status will change to _ and your DB
Instance will no longer be available.
A. storage-overflow
B. storage-full
C. storage-exceed
D. storage-overage
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 500
Is it possible to access your EBS snapshots?
A. Yes, through the Amazon S3 APIs.
B. Yes, through the Amazon EC2 APIs.
C. No, EBS snapshots cannot be accessed; they can only be used to create a new EBS volume.
D. EBS doesn't provide snapshots.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 501
Does Amazon RDS for SQL Server currently support importing data into the msdb database'?
A. No
B. Yes
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 502
Does Route 53 support MX Records?
A. Yes.
B. It supports CNAME records, but not MX records.
C. No
D. Only Primary MX records. Secondary MX records are not supported.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 503
Because of the extensibility limitations of striped storage attached to Windows Server, Amazon RDS does not
currently support increasing storage on a _ DB Instance.
A. SQL Server
B. MySQL
C. Oracle
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 504
Which Amazon storage do you think is the best for my database-style applications that frequently encounter
many random reads and writes across the dataset?
A. None of these.
B. Amazon Instance Storage
C. Any of these
D. Amazon EBS
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 505
Select the set of steps for exposing the snapshot only to specific AWS accounts
A. Select public for all the accounts and check mark t hose accounts with whom you want to expose the
snapshots and cl ick save.
B. Select Private, enter the IDs oft hose AWS accounts, and click Save.
C. Select Public, enter the IDs of those AWS accounts, and click Save.
D. Select Public, mark the IDs of those AWS accounts as private, and click Save.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 506
Is decreasing the storage size of a DB Instance permitted?
A. Depends on the ROMS used
B. Yes
C. No
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 507
When should I choose Provisioned IOPS over Standard RDS storage?
A. If you use production online transaction processing (OLTP) workloads.
B. If you have batch-oriented workloads
C. If you have workloads that are not sensitive to consistent performance
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 508
In the context of MySQL, version numbers are organized as MySQL version = X.Y.Z. What does X denote
here?
A. release level
B. minor version
C. version number
D. major version
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 509
In the 'Detailed ' monitoring data available for your Amazon EBS volumes, Provisioned IOPS volumes
automatically send _ minute metrics to Amazon C|oudWatch.
A. 5
B. 2
C. 1
D. 3
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 510
It is advised that you watch the Amazon C|oudWatch " _ " metric (available via the AWS Management Console
or Amazon Cloud Watch APIs) carefully and recreate the Read Replica should it fall behind due to replication
errors.
A. Write Lag
B. Read Replica
C. Replica Lag
D. Single Replica
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 511
Can the string value of 'Key' be prefixed with laws'?
A. No
B. Only for EC2 not S3
C. Yes
D. Only for S3 not EC
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 512
By default what are ENIs that are automatically created and attached to instances using the EC2 console set to
do when the attached instance terminates?
A. Remain as is
B. Terminate
C. Hibernate
D. Pause
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 513
Are you able to integrate a multi-factor token service with the AW5 Platform?
A. Yes, you can integrate private multi-factor token devices to authenticate users to the AW5 platform.
B. No, you cannot integrate multi-factor token devices with the AW5 platform.
C. Yes, using the AW5 multi-factor token devices to authenticate users on the AW5 platform.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 514
You can use _ and _ to help secure the instances in your VPC,
A. security groups and multi-factor authentication
B. security groups and 2-Factor authentication
C. security groups and biometric authentication
D. security groups and network ACLs
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 515
Fill in the blanks: _ is a durable, block-level storage volume that you can attach to a single, running Amazon
EC2 instance.
A. Amazon S3
B. Amazon EBS
C. None of these
D. All of these
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 516
Do the Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?
A. No
B. Only if instructed to when created
C. Yes
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 517
If I want my instance to run on a single-tenant hardware, which value do I have to set the instance's tenancy
attribute to?
A. dedicated
B. isolated
C. one
D. reserved
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 518
What does Amazon RDS stand for?
A. Regional Data Sewer.
B. Relational Database Service.
C. Nothing.
D. Regional Database Service.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 519
What is the maximum response time for a Business level Premium Support case?
A. 30 minutes
B. You always get instant responses (within a few seconds).
C. 10 minutes
D. 1 hour
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 520
What does Amazon ELB stand for?
A. Elastic Linux Box.
B. Encrypted Linux Box.
C. Encrypted Load Balancing.
D. Elastic Load Balancing.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 521
What does Amazon Cloud Formation provide?
A. None of these.
B. The ability to setup Autoscaling for Amazon EC2 instances.
C. A template to map network resources for Amazon Web Services.
D. A templated resource creation for Amazon Web Services.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 522
Is there a limit to the number of groups you can have?
A. Yes for all users except root
B. No
C. Yes unless special permission granted
D. Yes for all users
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 523
Location of Insta nces are -----
A. Regional
B. based on Availability Zone
C. Global
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 524
Is there any way to own a direct connection to Amazon Web Services'?
A. You can create an encrypted tunnel to VPC, but you don't own the connection.
B. Yes, it's called Amazon Dedicated Connection.
C. No, AWS only allows access from the public Internet.
D. Yes, it's called Direct Connect.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 525
What is the maximum response time for a Business level Premium Support case?
A. 30 minutes
B. 1 hour
C. 12 hours
D. 10 minutes
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 526
Does Dynamic DB support in-place atomic updates?
A. It is not defined
B. No
C. Yes
D. It does support in-place non-atomic updates
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 527
Is there a method in the IAM system to al low or deny access to a specific instance?
A. Only for VPC based instances
B. Yes
C. No
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 528
What is an isolated database environment running in the cloud (Amazon RDS) called?
A. DB Instance
B. DB Unit
C. DB Sen/er
D. DB Volume
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 529
What does Amazon SES stand for?
A. Simple Elastic Server
B. Simple Email Service
C. Software Email Solution
D. Software Enabled Sewer
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 530
Amazon S3 doesn't automatically give a user who creates _ permission to perform other actions on that bucket
or object.
A. a file
B. a bucket or object
C. a bucket orfile
D. a object or file
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 531
Can I attach more than one policy to a particular entity?
A. Yes always
B. Only if within GovC|oud
C. No
D. Only if within VPC
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 532
Fill in the blanks: A _ is a storage device that moves data in sequences of bytes or bits (blocks). Hint: These
devices support random access and generally use buffered 1/0.
A. block map
B. storage block
C. mapping device
D. block device
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 533
Can I detach the primary (ethO) network interface when the instance is running or stopped?
A. Yes, You can.
B. No. You cannot
C. Depends on the state of the interface at the time
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 534
What's an ECU?
A. Extended Cluster User.
B. None of these.
C. Elastic Computer Usage.
D. Elastic Compute Unit.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 535
REST or Query requests are HTIP or HTIPS requests that use an HTIP verb (such as GET or POST) and a
parameter named Action or Operation that specifies the API you are calling.
A. FALSE
B. TRUE
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 536
What is the charge for the data transfer incurred in replicating data between your primary and standby?
A. No charge. It is free.
B. Double the standard data transfer charge
C. Same as the standard data transfer charge
D. Half of the standard data transfer charge
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 537
Does AWS Direct Connect allow you access to all Availabilities Zones within a Region?
A. Depends on the type of connection
B. No
C. Yes
D. Only when there's just one availability zone in a region. If there are more than one, only one availability zone
can be accessed directly.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 538
What does the "Server Side Encryption" option on Amazon S3 provide?
A. It provides an encrypted virtual disk in the Cloud.
B. It doesn't exist for Amazon S3, but only for Amazon EC2.
C. It encrypts the files that you send to Amazon S3, on the server side.
D. It allows to upload fi les using an SSL endpoint, for a secure transfer.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 539
What does Amazon EBS stand for?
A. Elastic Block Storage
B. Elastic Business Server
C. Elastic Blade Server
D. Elastic Block Store
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 540
Within the IAM service a GROUP is regarded as a:
A. A collection of AWS accounts
B. |t's the group of EC2 machines that gain t he permissions specified in the GROUP.
C. There's no GROUP in IAM, but only USERS and RESOURCES.
D. A collection of users.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 541
A _ is the concept of allowing (or disallowing) an entity such as a user, group, or role some type of access to
one or more resources.
A. user
B. AWS Account
C. resource
D. permission
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 542
After an Amazon VPC instance is launched, can I change the VPC security groups it belongs to?
A. No. You cannot.
B. Yes. You can.
C. Only if you are the root user
D. Only if the tag "VPC_Change_Group" is true
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 543
Do the system resources on the Micro instance meet the recommended configuration for Oracle?
A. Yes completely
B. Yes but only for certain situations
C. Not in any circumstance
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 544
Willi be charged if the DB instance is idle?
A. No
B. Yes
C. Only is running in GovC|oud
D. Only if running in VPC
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 545
To help you manage your Amazon EC2 instances, images, and other Amazon EC2 resources, you can assign
your own metadata to each resource in the form of _ _
A. special filters
B. functions
C. tags
D. wildcards
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 546
Are you able to integrate a multi-factor token service with the AWS Platform?
A. No, you cannot integrate multi-factor token devices with the AWS platform.
B. Yes, you can integrate private multi-factor token devices to authenticate users to the AWS platform.
C. Yes, using the AWS multi-factor token devices to authenticate users on the AWS platform.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 547
True or False: When you add a rule to a DB security group, you do not need to specify port number or protocol.
A. Depends on the ROMS used
B. TRUE
C. FALSE
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 548
Is there a limit to the number of groups you can have?
A. Yes for all users
B. Yes for all users except root
C. No
D. Yes unless special permission granted
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 549
Can I initiate a "forced failover" for my Oracle Multi-AZ DB Instance deployment?
A. Yes
B. Only in certain regions
C. Only in VPC
D. No
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 550
Amazon EC2 provides a repository of public data sets that can be seamlessly integrated into AWS cloud-based
applications. What is the monthly charge for using the public data sets?
A. A 1 time charge of 10$ for all the datasets.
B. 1$ per dataset per month
C. 10$ per month for all the datasets
D. There is no charge for using the public data sets
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 551
In the Amazon RDS Oracle DB engine, the Database Diagnostic Pack and the Database Tuning Pack are only
available with _ _
A. Oracle Standard Edition
B. Oracle Express Edition
C. Oracle Enterprise Edition
D. None of these
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 552
Without -' you must either create multiple AWS accounts-each with its own billing and subscriptions to AWS
products-or your employees must share the security credentials of a single AWS account.
A. Amazon RDS
B. Amazon Glacier
C. Amazon EMR
D. Amazon IAM
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 553
Amazon RDS supports SOAP only through _ _
A. HTTP or HTTPS
B. TCP/IP
C. HTIP
D. HTIPS
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 554
The Amazon EC2 web service can be accessed using the _ web services messaging protocol. This interface is
described by a Web Services Description Language (WSDL) document.
A. SOAP
B. DCOM
C. CORBA
D. XML-RPC
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 555
Is creating a Read Replica of another Read Replica supported?
A. Only in VPC
B. Yes
C. Only in certain regions
D. No
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 556
What is the charge for the data transfer incurred in replicating data between your primary and standby?
A. Same as the standard data transfer charge
B. Double the standard data transfer charge
C. No charge. It is free
D. Half of the standard data transfer charge
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 557
HTIP Query-based requests are HTIP requests that use the HTIP verb GET or POST and a Query parameter
named _ _
A. Action
B. Value
C. Reset
D. Retrieve
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 558
What happens to the 1/0 operations while you take a database snapshot?
A. 1/0 operations to the database are suspended for an hour while the backup is in progress.
B. 1/0 operations to the database are sent to a Replica (if available) for a few minutes while the backup is in
progress.
C. 1/0 operations will be functioning normally
D. 1/0 operations to the database are suspended for a few minutes while the backup is in progress.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 559
Amazon RDS creates an SSL certificate and installs the certificate on the DB Instance when Amazon RDS
provisions the instance. These certificates are signed by a certificate authority. The _ is stored at https://
rds.amazonaws.com/doc/rds-ssl-ca-cert.pem.
A. private key
B. foreign key
C. public key
D. protected key
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 560
embodies the "share-nothing" architecture and essentially involves breaking a large database into several
smaller databases. Common ways to split a database include
1) splitting tables that are notjoined in the same query onto different hosts or
2) duplicating a table across multiple hosts and then using a hashing algorithm to determine which host
receives a given update.
A. $harding
B. Fai lure recovery
C. Federation
D. DOL operations
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 561
What is the name of licensing model in which I can use your existing Oracle Database licenses to run Oracle
deployments on Amazon RDS?
A. Bring Your Own License
B. Role Bases License
C. Enterprise License
D. License Included
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 562
When you resize the Amazon RDS DB instance, Amazon RDS will perform the upgrade during the next
maintenance window. If you want the upgrade to be performed now, rather than waiting for the maintenance
window, specify the _ option.
A. Apply Now
B. Apply Soon
C. Apply This
D. Apply Immediately
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 563
Does Amazon Route 53 support NS Records?
A. Yes, it supports Name Service records.
B. No
C. It supports only MX records.
D. Yes, it supports Name Sewer records.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 564
The SQL Server _ feature is an efficient means of copying data from a source database to your DB Instance. It
writes the data that you specify to a data file, such as an ASCII file.
A. bulk copy
B. group copy
C. dual copy
D. mass copy
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 565
When using consolidated billing there are two account types. What are they?
A. Paying account and Linked account
B. Parent account and Child account
C. Main account and Sub account.
D. Main account and Secondary account.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 566
A _ is a document that provides a formal statement of one or more permissions.
A. policy
B. permission
C. Role
D. resource
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 567
In the Amazon RDS which uses the SQL Server engine, what is the maximum size for a Microsoft SQL Server
DB Instance with SQL Sewer Express edition?
A. 10GB per DB
B. 100GB per DB
C. 2 TB per DB
D. 1TB per DB
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 568
Regarding the attaching of ENI to an instance, what does 'warm attach' refer to?
A. Attaching an ENI to an instance when it is stopped.
B. This question doesn't make sense.
C. Attaching an ENI to an instance when it is running
D. Attaching an ENI to an instance during the launch process
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 569
If I scale the storage capacity provisioned to my DB Instance by mid of a billing month, how will I be charged?
A. You will be charged for the highest storage capacity you have used
B. On a proration basis
C. You will be charged for the lowest storage capacity you have used
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 570
You can modify the backup retention period; valid values are 0 (for no backup retention) to a maximum of days.
A. 45
B. 35
C. 15
D. 5
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 571
A Provisioned IOPS volume must be at |east_ GB in size
A. 1
B. 50
C. 20
D. 10
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 572
Willi be alerted when automatic fail over occurs?
A. Only if SNS configured
B. No
C. Yes
D. Only if Cloudwatch configured
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 573
How can an EBS volume that is currently attached to an EC2 instance be migrated from one Availability Zone
to another?
A. Detach the volume and attach it to another EC2 instance in the other AZ.
B. Simply create a new volume in the other AZ and specify the original volume as the source.
C. Create a snapshot of the volume, and create a new volume from the snapshot in the other AZ.
D. Detach the volume, then use the ec2-migrate-voiume command to move it to another AZ.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 574
If you' re unable to connect via SSH to your EC2 instance, which of the following should you check and
possibly to restore connectMty?
A. Adjust Security Group to permit egress traffic over TCP port 443 from your IP.
B. Configure the JAM role to permit changes to security group settings.
C. Modify the instance security group to allow ingress of ICMP packets from your IP.
D. Adjust the instance's Security Group to permit ingress traffic over port 22 from your IP.
E. Apply the most recently released Operating System security patches.
Correct Answer: D
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.htmI
QUESTION 575
Which of the following features ensures even distribution of traffic to Amazon EC2 instances in multiple
Availability Zones registered with a load balancer?
A. Elastic Load Balancing request routing
B. An Amazon Route 53 weighted routing policy
C. Elastic Load Balancing cross-zone load balancing
D. An Amazon Route 53 latency routing pol icy
Correct Answer: A
Explanation
Explanation/Reference:
http://aws.amazon.com/eIasticIoadba|ancing/
QUESTION 576
You are using an m1.smaII EC2 Instance with one 300GB EBS volume to host a relational database. You
determined that write throughput to the database needs to be increased. Which of the following approaches
can help achieve this? Choose 2 answers
A. Use an array of EBS volumes.
B. Enable Multi-AZ mode.
C. Place the instance in an Auto Scaling Groups
D. Add an EBS volume and place into RAID 5.
E. Increase the size of the EC2 Instance.
F. Put the database behind an Elastic Load Balancer.
Correct Answer: DE
Explanation
Explanation/Reference:
QUESTION 577
After launching an instance that you intend to serve as a NAT (Network Address Translation) device in a public
subnet you modify your route tables to have the NAT device be the target of internet bound traffic of your
private subnet. When you try and make an outbound connection to the internet from an instance in the private
subnet, you are not successful. Which of the following steps could resolve the issue?
A. Disabling the Source/Destination Check attribute on the NAT instance
B. Attaching an Elastic IP address to the instance in the private subnet
C. Attaching a second Elastic Network Interface (EN I) to the NAT instance, and placing it in the private sub net
D. Attaching a second Elastic Network Interface (ENI) to the instance in the private subnet, and placing it in the
public subnet
Correct Answer: A
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/workspaces/latest/adminguide/gsg_create_vpc.html
QUESTION 578
You are building a solution for a customer to extend their on-premises data center to AWS. The customer
requires a 50-Mbps dedicated and private connection to their VPC. Which AWS product or feature satisfies this
requirement?
A. Amazon VPC peering
B. Elastic IP Addresses
C. AWS Direct Connect
D. Amazon VPC virtual private gateway
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 579
You nave multiple Amazon EC2 instances running in a cluster across multiple Availability Zones within the
same region. What combination of the following should be used to ensure the highest network performance
(packets per second), lowest latency, and Iowestjitter? Choose 3 answers
A. Amazon EC2 placement groups
B. Enhanced networking
C. Amazon PV AMI
D. Amazon HVM AM
E. Amazon Linux
F. Amazon VPC
Correct Answer: ABE
Explanation
Explanation/Reference:
QUESTION 580
When using the following AWS services, which should be implemented in multiple Availability Zones for high
availability solutions? Choose 2 answers
A. Amazon DynamoDB
B. Amazon Elastic Compute Cloud (EC2)
C. Amazon Elastic Load Balancing
D. Amazon Simple Notification Service (SNS)
E. Amazon Simple Storage Service {S3)
Correct Answer: BC
Explanation
Explanation/Reference:
QUESTION 581
You have a video transcoding application running on Amazon EC2. Each instance pol Is a queue to find out
which video should be transcoded, and then runs a transcoding process. If this process is interrupted, the
video will be transcoded by another instance based on the queuing system. You have a large backlog of videos
which need to be transcoded and would like to reduce this backlog by adding more instances. You will need
these instances only until the backlog is reduced. Which type of Amazon EC2 instances should you use to
reduce the backlog in the most cost efficient way?
A. Reserved instances
B. Spot instances
C. Dedicated instances
D. On-demand instances
Correct Answer: B
Explanation
Explanation/Reference:
http://aws.amazon.com/ec2/purchasing-options/spot-instances/
QUESTION 582
You have an EC2 Security Group with several running EC2 instances. You change the Security Group rules to
allow inbound traffic on a new port and protocol, and launch several new instances in the same Security
Group. The new rules apply:
A. Immediately to all instances in the security group.
B. Immediately to the new instances only.
C. Immediately to the new instances, but old instances must be stopped and restarted before the new rules
apply.
D. To all instances, but it may take several minutes for old instances to see the changes.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 583
Which services allow the customer to retain full administrative prMleges of the underlying EC2 instances?
Choose 2 answers
A. Amazon Relational Database Service
B. Amazon Elastic Map Reduce
C. Amazon EIastiCache
D. Amazon DynamoDB
E. AWS Elastic Beanstalk
Correct Answer: BE
Explanation
Explanation/Reference:
QUESTION 584
A company is building a two-tier web application to serve dynamic transaction-based content. The data tier is
leveraging an Online Transactional Processing (OLTP) database. What services should you leverage to enable
an elastic and scalable web tier?
A. Elastic Load Balancing, Amazon EC2, and Auto Scaling
B. Elastic Load Balancing, Amazon RDS with Multi-AZ, and Amazon S3
C. Amazon RDS with MuIti-AZ and Auto Scaling
D. Amazon EC2, Amazon DynamoDB, and Amazon S3
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 585
Your application provides data transformation services. Files containing data to be transformed are first
uploaded to Amazon S3 and then transformed by a fileet of spot EC2 instances. Fi les submitted by your
premium customers must be transformed with the highest priority. How should you implement such a system?
A. Use a DynamoDB table with an attribute defining the priority level. Transformation instances will scan the
table for tasks, sorting the results by priority level.
B. Use Route 53 latency based-routing to send high priority tasks to the closest transformation instances.
C. Use two SQS queues, one for high priority messages, the other for default priority. Transformation instances
first poll the high priority queue; if there is no message, they poll the default priority queue.
D. Use a single SQS queue. Each message contains the priority level. Transformation instances poll highpriority
messages first.
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 586
Which technique can be used to integrate AWS IAM (Identity and Access Management) with an on-premise
LDAP (Lightweight Directory Access Protocol) directory service?
A. Use an IAM policy that references the LDAP account identifiers and the AWS credentials.
B. Use SANIL (Security Assertion Markup Language) to enable single sign-on between AWS and LDAP.
C. Use AWS Security Token Service from an identity broker to issue short-lived AWS credentials.
D. Use IAM roles to automatically rotate the IAM credentials when LDAP credentials are updated.
E. Use the LDAP credentials to restrict a group of users from launching specific EC2 instance types.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 587
Which of the following are characteristics of Amazon VPC subnets? Choose 2 answers
A. Each subnet spans at least 2 Availability Zones to provide a high-availability environment.
B. Each subnet maps to a single Availability Zone.
C. CIDR block mask of/25 is the smallest range supported.
D. By default, all subnets can route between each other, whether they are private or public.
E. Instances in a private subnet can communicate with the Internet only if they have an Elastic IP.
Correct Answer: BE
Explanation
Explanation/Reference:
QUESTION 588
A customer is leveraging Amazon Simple Storage Service in eu-west-1 to store static content for a web-based
property. The customer is storing objects using the Standard Storage class. Where are the customers objects
replicated?
A. A single facility in eu-west-I and a single facility in eu-central-1
B. A single facility in eu-west-I and a single facility in us-east-I
C. IV|u|tip|e facilities in eu-west-I
D. A single facility in eu-west-1
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 589
Your web application front end consists of multiple EC2 instances behind an Elastic Load Balancer. You
configured ELB to perform health checks on these EC2 instances, if an instance fails to pass health checks,
which statement will be true?
A. The instance gets terminated automatically by the ELB
B. The instance gets quarantined by the ELB for root cause analysis.
C. The instance is replaced automatically by the ELB
D. The ELB stops sending traffic to the instance that failed its health check.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 590
In AWS, which security aspects are the customer's responsibility? Choose 4 answers
A. Security Group and ACL {Access Control List} settings
B. Decommissioning storage devices
C. Patch management on the EC2 instance's operating system
D. Life-cycle management of IAM credentials
E. Controlling physical access to compute resources
F. Encryption of EBS {Elastic Block Storage} volumes
Correct Answer: ACDF
Explanation
Explanation/Reference:
http://media.amazonwebservices.com/AWS_Security_Best_Practices.pdf
QUESTION 591
You have a web application running on six Amazon EC2 instances, consuming about 45% of resources on
each instance. You are using auto-scaling to make sure that six instances are running at all times. The number
of requests this application processes is consistent and does not experience spikes. The application is critical
to your business and you want high availability at all times. You want the load to be distributed evenly between
all instances. You also want to use the same Amazon Machine Image (AMI) for all instances. Which of the
following architectural choices should you make?
A. Deploy 6 EC2 instances in one availability zone and use Amazon Elastic Load Balancer.
B. Deploy 3 EC2 instances in one region and 3 in another region and use Amazon Elastic Load Balancer.
C. Deploy 3 EC2 instances in one availability zone and 3 in another availability zone and use Amazon Elastic
Load Balancer.
D. Deploy 2 EC2 instances in three regions and use Amazon Elastic Load Balancer.
Correct Answer: C
Explanation
Explanation/Reference:
https://media.amazonwebservices.com/pdf/AWS_Security_Whitepaper.pdf (page 8)
QUESTION 592
You have decided to change the instance type for instances running in your application tier that is using Auto
Scaling. In which area below would you change the instance type definition?
A. Auto Scaling policy
B. Auto Scaling group
C. Auto Scaling tags
D. Auto Scaling launch configuration
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 593
When an EC2 EBS-backed (EBS root} instance is stopped, what happens to the data on any ephemeral store
volumes?
A. Data is automatically saved in an EBS volume.
B. Data is unavailable until the instance is restarted.
C. Data will be deleted and will no longer be accessible.
D. Data is automatically saved as an EBS snapshot.
Correct Answer: B
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/Iatest/UserGuide/ComponentsA|V|is.html
QUESTION 594
Which of the following items are required to allow an application deployed on an EC2 instance to write data to
a DynamoDB table? Assume that no security keys are allowed to be stored on the EC2 instance.
(Choose 2 answers)
A. Create an IAM Role that allows write access to the DynamoDB tab Ie.
B. Add an IAM Role to a running EC2 instance.
C. Create an IAM User that al lows write access to the Dynamo DB tab Ie.
D. Add an IAM User to a running EC2 instance.
E. launch an EC2 Instance with the IAM Role included in the launch configuration.
Correct Answer: AE
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.Phase3.htmI
QUESTION 595
When you put objects in Amazon S3, what is the indication that an object was successfully stored?
A. A HTIP 200 result code and MDS checksum, taken together, indicate that the operation was successful.
B. Amazon S3 is engineered for 99.999999999% durability. Therefore there is no need to confirm that data
was inserted.
C. A success code is inserted into the S3 object metadata.
D. Each S3 account has a special bucket named _s3_1ogs. Success codes are written to this bucket with a
timestamp and checksum.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 596
What is one key difference between an Amazon EBS-backed and an instance-store backed instance?
A. Amazon EBS-backed instances can be stopped and restarted.
B. Instance-store backed instances can be stopped and restarted.
C. Auto scaling requires using Amazon EBS-backed instances.
D. Virtual Private Cloud requires EBS backed instances.
Correct Answer: A
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAIV|is.htmI#storage-for-theroot-devi ce
QUESTION 597
A company wants to implement their website in a virtual private cloud (VPC). The web tier will use an Auto
Scaling group across multiple Availability Zones (AZs). The database will use MuIti-AZ RDS MySQL and
should not be publicly accessible. What is the minimum number of subnets that need to be configured in the
VPC?
A. 1
B. 2
C. 3
D. 4
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 598
You have launched an Amazon Elastic Compute Cloud (EC2) instance into a public subnet with a primary
private I P address assigned, an internet gateway is attached to the VPC, and the public route table is
configured to send all Internet-based traffic to the Internet gateway. The instance security group is set to allow
all outbound traffic but cannot access the internet. Why is the Internet unreachable from this instance?
A. The instance does not have a public IP address.
B. The internet gateway security group must allow all outbound traffic.
C. The instance security group must allow all inbound traffic.
D. The instance "Source/Destination check" property must be enabled.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 599
You launch an Amazon EC2 instance without an assigned AVVS identity and Access Management (IAM) role.
Later, you decide that the instance should be running with an IAM role. Which action must you take in order to
have a running Amazon EC2 instance with an IAM role assigned to it?
A. Create an image of the instance, and register the image with an IAM role assigned and an Amazon EBS
volume mapping.
B. Create a new IAM role with the same permissions as an existing IAM role, and assign it to the running
instance.
C. Create an image of the instance, add a new IAM role with the same permissions as the desired IAM role,
and deregister the image with the new role assigned.
D. Create an image of the instance, and use this image to launch a new instance with the desired Lam role
assigned.
Correct Answer: D
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-usingroIe-ec2instanee.htm|
QUESTION 600
How can the domain's zone apex, for example, "myzoneapexdomain.com", be pointed towards an Elastic Load
Balancer?
A. By using an Amazon Route 53 Alias record
B. By using an AAAA record
C. By using an Amazon Route 53 CNAME record
D. By using an A record
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 601
An instance is launched into a VPC subnet with the network ACL configured to al low all inbound traffic and
deny all outbound traffic. The instance's security group is configured to allow SSH from any IP address and
deny all outbound traffic. What changes need to be made to allow SSH access to the instance?
A. The out bound security group needs to be modified to allow out bound traffic.
B. The outbound network ACL needs to be modified to allow outbound traffic.
C. Nothing, it can be accessed from any IP address using SSH.
D. Both the outbound security group and outbound network ACL need to be modified to allow outbound traffic.
Correct Answer: B
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AmazonVPC/|atest/UserGuide/VPC_ACLs.htm|
QUESTION 602
For which of the following use cases are Simple Workflow Service (SWF) and Amazon EC2 an appropriate
solution? Choose 2 answers
A. Using as an endpoint to collect thousands of data points per hourfrom a distributed fileet of sensors
B. Managing a multi-step and multi-decision checkout process of an e-commerce website
C. Orchestrating the execution of distributed and auditable business processes
D. Using as an SNS (Simple Notification Service) endpoint to trigger execution of video transcoding jobs
E. Using as a distributed session store for your web application
Correct Answer: AB
Explanation
Explanation/Reference:
QUESTION 603
A customer wants to leverage Amazon Simple Storage Service (S3) and Amazon Glacier as part of their
backup and archive infrastructure. The customer plans to use third-party software to support this integration.
Which approach will limit the access of the third party software to only the Amazon S3 bucket named
"company-backup"?
A. A custom bucket policy limited to the Amazon S3 API in the Amazon Glacier archive "company backup"
B. A custom bucket policy limited to the Amazon S3 API in "company-backup"
C. A custom IAM user policy limited to the Amazon S3 API for the Amazon Glacier archive "company backup?
D. A custom IAM user policy limited to the Amazon S3 API in "company-backup".
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 604
A client application requires operating system prMleges on a relational database server. What is an appropriate
configuration for a highly available database architecture?
A. A standalone Amazon EC2 instance
B. Amazon RDS in a Mu|ti-AZ configuration
C. Amazon EC2 instances in a replication configuration utilizing a single Availability Zone
D. Amazon EC2 instances in a replication configuration utilizing two different Availability Zones
Correct Answer: D
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/Iatest/UserGuide/using-regions-avaiIability-zones.html
QUESTION 605
What is a placement group?
A. A collection of Auto Scaling groups in the same region
B. A feature that enables EC2 instances to interact with each other via high bandwidth, low latency
connections
C. A collection of authorized CIoudFront edge locations for a distribution
D. A collection of Elastic Load Balancers in the same Region or Availability Zone
Correct Answer: B
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html
QUESTION 606
A company has a workflow that sends video files from their on-premise system to AWS for transcoding. They
use EC2 worker instances that pull transcoding jobs from SQS. Why is SQS an appropriate service for this
scenario?
A. SQS guarantees the order of the messages.
B. SQS synchronously provides transcoding output.
C. SQS checks the health of the worker instances.
D. SQS helps to facilitate horizontal scaling of encoding tasks.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 607
When creation of an EBS snapshot is initiated, but not completed, the EBS volume:
A. Can be used while the snapshot is in progress.
B. Cannot be detached or attached to an EC2 instance until the snapshot completes
C. Can be used in read-only mode while the snapshot is in progress.
D. Cannot be used until the snapshot completes.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 608
What are characteristics of Amazon S3? Choose 2 answers
A. S3 allows you to store objects of virtually unlimited size.
B. S3 offers Provisioned IOPS.
C. S3 allows you to store unlimited amounts of data.
D. S3 should be used to host a relational database.
E. Objects are directly accessible via a URL.
Correct Answer: CE
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AmazonCioudFront/latest/DeveIoperGuide/private-contentrestricting-access -tos3.
htmI
QUESTION 609
Per the AWS Acceptable Use Policy, penetration testing of EC2 instances:
A. May be performed by AWS, and will be performed by AWS upon customer request.
B. May be performed by AWS, and is periodically performed by AWS.
C. Are expressly prohibited under all circumstances.
D. May be performed by the customer on their own instances with prior authorization from AWS.
E. May be performed by the customer on their own instances, only if performed from EC2 instances
Correct Answer: B
Explanation
Explanation/Reference:
http://aws.amazon.com/security/penetration-testing/
QUESTION 610
You are working with a customer who has 10 TB of archival data that they want to migrate to Amazon Glacier.
The customer has a 1-Mbps connection to the Internet. Which service or feature provides the fastest method of
getting the data into Amazon Glacier?
A. Amazon Glacier multipart upload
B. AWS Storage Gateway
C. VM Import/Export
D. AWS Import/Export
Correct Answer: A
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html
QUESTION 611
How can you secure data at rest on an EBS volume?
A. Attach the volume to an instance using EC2's SSL interface.
B. Write the data randomly instead of sequentially.
C. Encrypt the volume using the S3 server-side encryption service.
D. Create an IAM policy that restricts read and write access to the volume.
E. Use an encrypted file system on top of the EBS volume.
Correct Answer: E
Explanation
Explanation/Reference:
https://aws.amazon.com/blogs/aws/protect-your-data-with-new-ebs-encryption/
QUESTION 612
A customer needs to capture all client connection information from their load balancer every five minutes. The
company wants to use this data for analyzing traffic patterns and troubleshooting their applications. Which of
the following options meets the customer requirements?
A. Enable AWS CIoudTraiI for the load balancer.
B. Enable access logs on the load balancer.
C. Install the Amazon CIoudWatch Logs agent on the load balancer.
D. Enable Amazon CIoudWatch metrics on the load balancer.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 613
If you want to launch Amazon Elastic Compute Cloud (EC2) instances and assign each instance a
predetermined private IP address you should:
A. Launch the instance from a private Amazon Machine Image (AMI).
B. Assign a group of sequential Elastic IP address to the instances.
C. Launch the instances in the Amazon Virtual Private Cloud (VPC).
D. Launch the instances in a Placement Group.
E. Use standard EC2 instances since each instance gets a private Domain Name Service (DNS) already.
Correct Answer: B
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.htmI
QUESTION 614
You need to configure an Amazon S3 bucket to serve static assets for your public-facing web application.
Which methods ensure that all objects uploaded to the bucket are set to public read? Choose 2 answers
A. Set permissions on the object to public read during upload.
B. Configure the bucket ACL to set all objects to public read.
C. Configure the bucket policy to set all objects to public read.
D. Use AWS Identity and Access Management roles to set the bucket to public read.
E. Amazon S3 objects default to public read, so no action is needed.
Correct Answer: AC
Explanation
Explanation/Reference:
QUESTION 615
A company is storing data on Amazon Simple Storage Service (S3). The company's security policy mandates
that data is encrypted at rest. Which of the following methods can achieve this? Choose 3 answers
A. Use Amazon S3 server-side encryption with AWS Key Management Service managed keys.
B. Use Amazon S3 server-side encryption with customer-provided keys.
C. Use Amazon S3 server-side encryption with EC2 key pair.
D. Use Amazon S3 bucket policies to restrict access to the data at rest.
E. Encrypt the data on the client-side before ingesting to Amazon S3 using their own master key.
F. Use SSL to encrypt the data while in transit to Amazon S3.
Correct Answer: ABE
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/Amazon$3/Iatest/dev/UsingKMSEncryption.htmI
QUESTION 616
Which procedure for backing up a relational database on EC2 that is using a set of RAIDed EBS volumes for
storage minimizes the time during which the database cannot be written to and results in a consistent backup?
A. 1. Detach EBS volumes, 2. Start EBS snapshot of volumes, 3. Re-attach EBS volumes
B. 1. Stop the EC2 Instance. 2. Snapshot the EBS volumes
C. 1. Suspend disk 1/0, 2. Create an image ofthe EC2 Instance, 3. Resume disk 1/0
D. 1. Suspend disk 1/0,2. Start EBS snapshot of volumes, 3. Resume disk 1/0
E. 1. Suspend disk 1/0, 2. Start EBS snapshot of volumes, 3. Wait for snapshots to complete, 4. Resume disk
1/0
Correct Answer: A
Explanation
Explanation/Reference:
http://media.amazonwebservices.com/AWS_Storage_Options.pdf (page 11)
QUESTION 617
A company needs to deploy virtual desktops to its customers in a virtual private cloud, leveraging existing
security controls. Which set of AWS services and features will meet the company's requirements?
A. Virtual Private Network connection. AWS Directory Services, and Classic link
B. Virtual Private Network connection. AWS Di rectory Services, and Amazon Workspaces
C. AWS Directory Service, Amazon Workspaces, and AWS Identity and Access Management
D. Amazon Elastic Compute Cloud, and AWS Identity and Access Management
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 618
After creating a new IAM user which of the following must be done before they can successfully make API
calls?
A. Add a password to the user.
B. Enable Multi-Factor Authentication for the user.
C. Assign a Password Policy to the user.
D. Create a set of Access Keys for the user.
Correct Answer: D
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_SettingUpUser.htmI
QUESTION 619
Which of the following are valid statements about Amazon S3? Choose 2 answers
A. S3 provides read-after-write consistency for any type of PUT or DELETE
B. Consistency is not guaranteed for any type of PUT or DELETE
C. A successful response to a PUT request only occurs when a complete object is saved.
D. Partially saved objects are immediately readable with a GET after an overwrite PUT.
E. S3 provides eventual consistency for overwrite PUTS and DELETES.
Correct Answer: CE
Explanation
Explanation/Reference:
http://api-portal.anypoint.mulesoft.com/amazon/api/amazon-s3-api/docs/concepts#DataConsistencyNIod el
QUESTION 620
You are configuring your company's application to use Auto Scaling and need to move user state information.
Which of the following AWS services provides a shared data store with durability and low latency?
A. AWS EIastiCache Memcached
B. Amazon Simple Storage Service
C. Amazon EC2 instance storage
D. Amazon DynamoDB
Correct Answer: B
Explanation
Explanation/Reference:
https://d36cz9buwruItt.cIoudfront.net/AWS_Overview.pdf (page 13, aws storage gateway)
QUESTION 621
Which features can be used to restrict access to data in S3? Choose 2 answers
A. Set an S3 ACL on the bucket or the object.
B. Create a Cloud Front distribution for the bucket.
C. Set an S3 bucket policy.
D. Enable IAM Identity Federation
E. Use S3 Virtua I Hosting
Correct Answer: CD
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AmazonCioudFront/latest/DeveIoperGuide/private-contentrestricting-access -tos3.
html
QUESTION 622
Which of the following are characteristics of a reserved instance? Choose 3 answers
A. It can be migrated across Availability Zones
B. It is specific to an Amazon Machine Image (AMI)
C. It can be applied to instances launched by Auto Scaling
D. It is specific to an instance Type
E. It can be used to lower Total Cost of Ownership (TCO) of a system
Correct Answer: CDE
Explanation
Explanation/Reference:
QUESTION 623
Which Amazon Elastic Compute Cloud feature can you query from within the instance to access instance
properties?
A. Instance user data
B. Resource tags
C. Instance metadata
D. Amazon Machine Image
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 624
Which of the following requires a custom Cloud Watch metric to monitor?
A. Memory Utilization of an EC2 instance
B. CPU Utilization of an EC2 instance
C. Disk usage actMty of an EC2 instance
D. Data transfer of an EC2 instance
Correct Answer: C
Explanation
Explanation/Reference:
http://aws.amazon.com/cIoudwatch/
QUESTION 625
You are tasked with setting up a Linux bastion host for access to Amazon EC2 instances running in your VPC.
Only clients connecting from the corporate external public IP address 72.34.51.100 should have SSH access to
the host. Which option will meet the customer requirement?
A. Security Group Inbound Rule: Protocol - TCP. Port Range- 22, Source 72.34.51. 100/32
B. Security Group Inbound Rule: Protocol - UDP, Port Range- 22, Source 72.34.51.100/32
C. Network ACL Inbound Rule: Protocol - UDP, Port Range- 22, Source 72.34.51.100/32
D. Network ACL Inbound Rule: Protocol - TCP, Port Range-22, Source 72.34.51.100/0
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 626
A customer needs corporate IT governance and cost oversight of all AWS resources consumed by its dMsions.
The dMsions want to maintain administrative control of the discrete AWS resources they consume and keep
those resources separate from the resources of other dMsions. Which of the following options, when used
together will support the autonomy/control of dMsions while enabling corporate IT to maintain governance and
cost oversight? Choose 2 answers
A. Use AWS Consolidated Billing and disable AWS root account access for the child accounts.
B. Enable IAM cross-account access for all corporate IT administrators in each child account.
C. Create separate VPCs for each dMsion within the corporate IT AWS account.
D. Use AWS Consolidated Billing to link the dMsions' accounts to a parent corporate account.
E. Write all child AWS CIoudTraiI and Amazon CIoudWatch logs to each child account's Amazon S3 'Log'
bucket.
Correct Answer: DE
Explanation
Explanation/Reference:
QUESTION 627
You run an ad-supported photo sharing website using S3 to serve photos to visitors of your site. At some point
you find out that other sites have been linking to the photos on your site, causing loss to your business. What is
an effective method to mitigate this?
A. Remove public read access and use signed URLs with expiry dates.
B. Use Cloud Front distributions for static content.
C. Block the IPs of the offending websites in Security Groups.
D. Store photos on an EBS volume of the web server.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 628
You are working with a customer who is using Chef configuration management in their data center. Which
service is designed to let the customer leverage existing Chef recipes in AWS?
A. Amazon Simple Workflow Service
B. AWS Elastic Beanstalk
C. AWS CIoudFormation
D. AWS OpsWorks
Correct Answer: D
Explanation
Explanation/Reference:
http://aws.amazon.com/opsworks/
QUESTION 629
An Auto-Scaling group spans 3 AZs and currently has 4 running EC2 instances. When Auto Scaling needs to
terminate an EC2 instance by default, AutoScaIing will: Choose 2 answers
A. Allow at least five minutes for Windows/Linux shutdown scripts to complete, before terminating the instance.
B. Terminate the instance with the least active network connections. If multiple instances meet this criterion,
one will be randomly selected.
C. Send an SNS notification, if configured to do so.
D. Terminate an instance in the AZ which currently has 2 running EC2 instances.
E. Randomly select one of the 3 AZs, and then terminate an instance in that AZ.
Correct Answer: CE
Explanation
Explanation/Reference:
QUESTION 630
When an EC2 instance that is backed by an S3-based AMI is terminated, what happens to the data on the root
volume?
A. Data is automatically saved as an EBS snapshot.
B. Data is automatically saved as an EBS volume.
C. Data is unavailable until the instance is restarted.
D. Data is automatically deleted.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 631
In order to optimize performance for a compute cluster that requires low inter-node latency, which of the
following feature should you use?
A. MuItipIe Availability Zones
B. AWS Direct Connect
C. EC2 Dedicated Instances
D. Placement Groups
E. VPC private subnets
Correct Answer: D
Explanation
Explanation/Reference:
http://aws.amazon.com/ec2/faqs/ (enhanced networking)
QUESTION 632
You have an environment that consists of a public subnet using Amazon VPC and 3 instances that are running
in this subnet. These three instances can successfully communicate with other hosts on the Internet. You
launch a fourth instance in the same subnet, using the same AM and security group configuration you used for
the others, but find that this instance cannot be accessed from the internet.
What should you do to enable Internet access?
A. Deploy a NAT instance into the public subnet.
B. Assign an Elastic IP address to the fourth instance.
C. Configure a publically routable IP Address in the host OS of the fourth instance.
D. Modify the routing table for the public subnet.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 633
You have a distributed application that periodically processes large volumes of data across multiple Amazon
EC2 Instances. The application is designed to recover gracefully from Amazon EC2 instance failures. You are
required to accomplish this task in the most cost-effective way.
Which of the following will meet your requirements?
A. Spot Instances
B. Reserved instances
C. Dedicated instances
D. On-Demand instances
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 634
Which of the following are t rue regarding AWS CIoudTraiI? Choose 3 answers
A. CIoudTraiI is enabled globally
B. CIoudTraiI is enabled by default
C. CIoudTraiI is enabled on a per-region basis
D. CIoudTraiI is enabled on a per-service basis.
E. Logs can be delivered to a single Amazon S3 bucket for aggregation.
F. CIoudTraiI is enabled for all available services within a region.
G. Logs can only be processed and delivered to the region in which they are generated.
Correct Answer: CDE
Explanation
Explanation/Reference:
http://aws.amazon.com/c|oudtraiI/faqs/
QUESTION 635
You have a content management system running on an Amazon EC2 instance that is approaching 100% CPU
utilization. Which option will reduce load on the Amazon EC2 instance?
A. Create a load balancer, and register the Amazon EC2 instance with it
B. Create a Cloud Front distribution, and configure the Amazon EC2 instance as the origin
C. Create an Auto Scaling group from the instance using the Create AutoScaIing Group action
D. Create a launch configuration from the instance using the Create launch Configuration action
Correct Answer: B
Explanation
Explanation/Reference:
https://aws.amazon.com/blogs/aws/new-amazon-ec2-micro-instances/
QUESTION 636
You have a load balancer configured for VPC, and all back-end Amazon EC2 instances are in service.
However, your web browser times out when connecting to the load baIancer's DNS name. Which options are
probable causes of this behavior? Choose 2 answers
A. The load balancer was not configured to use a public sub net with an Internet gateway configured
B. The Amazon EC2 instances do not have a dynamically allocated private IP address
C. The security groups or network ACLs are not property configured for web traffic.
D. The load balancer is not configured in a private subnet with a NAT instance.
E. The VPC does not have a VGW configured.
Correct Answer: AC
Explanation
Explanation/Reference:
QUESTION 637
A company needs to deploy services to an AWS region which they have not previously used. The company
currently has an AWS identity and Access Management (IAM) role for the Amazon EC2 instances, which
permits the instance to have access to Amazon DynamoDB. The company wants their EC2 instances in the
new region to have the same prMleges. How should the company achieve this?
A. Create a new IAM role and associated policies within the new region
B. Assign the existing IAM role to the Amazon EC2 instances in the new region
C. Copy the IAM role and associated policies to the new region and attach it to the instances
D. Create an Amazon Machine Image (AMI) of the instance and copy it to the desired region using the AMI
Copy feature
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 638
Which of the following notification endpoints or clients are supported by Amazon Simple Notification Service?
Choose 2 answers
A. Email
B. Cloud Front distribution
C. Fi Ie Transfer Protocol
D. Short Message Service
E. Simple Network Management Protocol
Correct Answer: AD
Explanation
Explanation/Reference:
http://docs.aws.a mazon.com/sns/latest/dg/welcome.htmI
QUESTION 639
Which set of Amazon S3 features helps to prevent and recoverfrom accidental data loss?
A. Object lifecycle and service access logging
B. Object versioning and Multi-factor authentication
C. Access controls and server-side encryption
D. Website hosting and Amazon S3 policies
Correct Answer: B
Explanation
Explanation/Reference:
http://media.amazonwebservices.com/AWS Security_Best_Practices.pdf
QUESTION 640
A company needs to monitor the read and write IOPs metrics for their AWS MySQL RDS instance and send
real-time alerts to their operations team. Which AWS services can accomplish this? Choose 2 answers
A. Amazon Simple Email Service
B. Amazon CIoudWatch
C. Amazon Simple Queue Service
D. Amazon Route 53
E. Amazon Simple Notification Service
Correct Answer: BE
Explanation
Explanation/Reference:
QUESTION 641
A company is preparing to give AWS Management Console access to developers Company policy mandates
identity federation and role-based access control. Roles are currently assigned using groups in the corporate
Active Directory. What combination of the following will give developers access to the AWS console? {Select 2}
Choose 2 answers
A. AWS Directory Service AD Connector
B. AWS Directory Service Simple AD
C. AWS Identity and Access Management groups
D. AWS identity and Access Management roles
E. AWS identity and Access Management users
Correct Answer: AD
Explanation
Explanation/Reference:
QUESTION 642
You are deploying an application to collect votes for a very popular television show. Millions of users will submit
votes using mobile devices. The votes must be collected into a durable, scalable, and highly available data
store for real-time public tabulation. Which service should you use?
A. Amazon DynamoDB
B. Amazon Redshift
C. Amazon Kinesis
D. Amazon Simple Queue Service
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 643
The Trusted Advisor service provides insight regarding which four categories of an AWS account?
A. Security, fault tolerance, high availability, and connectMty
B. Security, access control, high availability, and performance
C. Performance, cost optimization, security, and fault tolerance
D. Performance, cost optimization, access control, and connectMty
Correct Answer: C
Explanation
Explanation/Reference:
https://aws.amazon.com/blogs/aws/category/aws-trusted-advisor/
QUESTION 644
You are deploying an application to track GPS coordinates of delivery trucks in the United States. Coordinates
are transmitted from each delivery t ruck once every three seconds. You need to design an architecture that
will enable real-time processing of these coordinates from multiple consumers.
Which service should you use to implement data ingestion?
A. Amazon Kinesis
B. AWS Data Pipeline
C. Amazon AppStream
D. Amazon Simple Queue Sen/ice
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 645
A photo-sharing service stores pictures in Amazon Simple Storage Service (S3) and allows application sign-in
using an OpenID Connect-compatible identity provider. Which AWS Security Token Service approach to
temporary access should you use for the Amazon S3 operations?
A. SANIL-based Identity Federation
B. Cross-Account Access
C. AWS Identity and Access Management roles
D. Web Identity Federation
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 646
You have an application running on an Amazon Elastic Compute Cloud instance, that uploads 5 GB video
objects to Amazon Simple Storage Service (S3). Video uploads are taking longer than expected, resulting in
poor application performance. Which method will help improve performance of your application?
A. Enable enhanced networking
B. Use Amazon S3 multipart upload
C. Leveraging Amazon CIoudFront, use the HTIP POST method to reduce latency.
D. Use Amazon Elastic Block Store Provisioned IOPs and use an Amazon EBS-optimized instance
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 647
A customer wants to track access to their Amazon Simple Storage Service (S3) buckets and also use this
information for their internal security and access audits. Which of the following will meet the Customer
requirement?
A. Enable AW5 CIoudTraiI to audit all Amazon S3 bucket access.
B. Enable server access logging for all required Amazon S3 buckets.
C. Enable the Requester Pays option to track access via AWS Billing
D. Enable Amazon S3 event notifications for Put and Post.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 648
A company is deploying a two-tier, highly available web application to AWS. Which service provides durable
storage for static content while utilizing lower Overall CPU resources for the web tier?
A. Amazon EBS volume
B. Amazon S3
C. Amazon EC2 instance store
D. Amazon RD5 instance
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 649
You are designing a web application that stores static assets in an Amazon Simple Storage Service (S3)
bucket. You expect this bucket to immediately receive over 150 PUT requests per second. What should you do
to ensure optimal performance?
A. Use multi-part upload.
B. Add a random prefix to the key names.
C. Amazon S3 will automatically manage performance at this scale.
D. Use a predictable naming scheme, such as sequential numbers or date time sequences, in the key names
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 650
When will you incur costs with an Elastic IP address (EIP)?
A. When an EIP is allocated.
B. When it is allocated and associated with a running instance.
C. When it is allocated and associated with a stopped instance.
D. Costs are incurred regardless of whether the EIP is associated with a running instance.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 651
A company has an AWS account that contains three VPCs (Dev, Test, and Prod) in the same region. Test is
peered to both Prod and Dev. All VPCs have non-overlapping CIDR blocks. The company wants to push minor
code releases from Dev to Prod to speed up time to market . Which of the following options helps the company
accomplish this?
A. Create a new peering connection Between Prod and Dev along with appropriate routes.
B. Create a new entry to Prod in the Dev route table using the peering connection as the target.
C. Attach a second gateway to Dev. Add a new entry in the Prod route table identifying the gateway as the
target.
D. The VPCs have non-overlapping CI DR blocks in the same account. The route tables contain local routes
for all VPCs.
Correct Answer: D
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AmazonVPC/Iatest/PeeringGuide/vpc-pg.pdf
QUESTION 652
Which of the following instance types are available as Amazon EBS-backed only? Choose 2 answers
A. General purpose T2
B. General purpose M3
C. Compute-optimized C4
D. Compute-optimized C3
E. Storage-optimized 12
Correct Answer: DE
Explanation
Explanation/Reference:
QUESTION 653
A customer is hosting t heir company website on a cluster of web servers that are behind a public facing load
balancer. The customer also uses Amazon Route 53 to manage their public DNS. How should the customer
configure the DNS zone apex record to point to the load balancer?
A. Create an A record pointing to the IP address of the load balancer
B. Create a CNAME record pointing to the load balancer DNS name.
C. Create a CNAME record aliased to the load balancer DNS name.
D. Create an A record aliased to the load balancer DNS name
Correct Answer: C
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/EiasticIoadBaIancing/latest/Deve|operGuide/using-domain-names-with-elb.
html
QUESTION 654
You try to connect via SSH to a newly created Amazon EC2 instance and get one of the following error
messages:
"Network error: Connection timed out" or "Error connecting to [instance], reason: -> Connection timed out:
connect,"
You have confirmed that the network and security group rules are configured correctly and the instance is
passing status checks. What steps should you take to identify the source of the behavior? Choose 2 answers
A. Verify that the private key file corresponds to the Amazon EC2 key pair assigned at launch.
B. Verify that your IAM user policy has permission to launch Amazon EC2 instances.
C. Verify that you are connecting with the appropriate user name for your AMI.
D. Verify that the Amazon EC2 Instance was launched with the proper IAM role.
E. Verify that your federation trust to AWS has been established.
Correct Answer: AC
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/Iatest/UserGuide/Troubleshooting|nstancesConnecting.htmI
QUESTION 655
A customer is running a multi-tier web application farm in a virtual private cloud (VPC) that is not connected to
their corporate network. They are connecting to the VPC over the Internet to manage all of their Amazon EC2
instances running in both the public and private subnets. They have only authorized the bastion-security-group
with Mcrosoft Remote Desktop Protocol (RDP) access to the application instance security groups, but the
company wants to further limit administrative access to all of the instances in the VPC. Which of the following
Bastion deployment scenarios will meet this requirement?
A. Deploy a Windows Bastion host on the corporate network that has RDP access to all instances in the VPC.
B. Deploy a Windows Bastion host with an Elastic IP address in the public subnet and allow SSH access to the
bastion from anywhere.
C. Deploy a Windows Bastion host with an Elastic IP address in the private subnet, and restrict RDP access to
the bastion from only the corporate public IP addresses.
D. Deploy a Windows Bastion host with an auto-assigned Public IP address in the public subnet, and allow
RDP access to the bastion from only the corporate public IP addresses.
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 656
A customer has a single 3-TB volume on-premises that is used to hold a large repository of images and print
layout files. This repository is growing at 500 GB a year and must be presented as a single logical volume. The
customer is becoming increasingly constrained with their local storage capacity and wants an off-site backup of
this data, while maintaining low-latency access to their frequently accessed data. Which AWS Storage
Gateway configuration meets the customer requirements?
A. Gateway-Cached volumes with snapshots scheduled to Amazon S3
B. Gateway-Stored volumes with snapshots scheduled to Amazon S3
C. Gateway-Virtual Tape Library with snapshots to Amazon S3
D. Gateway-Virtual Tape Library with snapshots to Amazon Glacier
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 657
You are building an automated transcription service in which Amazon EC2 worker instances process an
uploaded audio file and generate a text file. You must store both of these files in the same durable storage until
the text file is retrieved. You do not know what the storage capacity requirements are.
Which storage option is both cost-efficient and scalable?
A. Multiple Amazon EBS volume with snapshots
B. A single Amazon Glacier vault
C. A single Amazon S3 bucket
D. Multiple instance stores
Correct Answer: C
Explanation
Explanation/Reference:
QUESTION 658
You need to pass a custom script to new Amazon Linux instances created in your Auto Scaling group.
Which feature allows you to accomplish this?
A. User data
B. EC2Config service
C. IAM roles
D. AWS Config
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 659
Which of the following services natively encrypts data at rest within an AWS region? Choose 2 answers
A. AWS Storage Gateway
B. Amazon DynamoDB
C. Amazon C|oudFront
D. Amazon Glacier
E. Amazon Simple Queue Senrice
Correct Answer: AD
Explanation
Explanation/Reference:
https://media.amazonwebservices.com/AWS_Securing_Data_ at_Rest_ with_E ncryption. pdf (page 12)
QUESTION 660
A company is building software on AWS that requires access to various AWS services. Which configuration
should be used to ensure mat AWS credentials (i.e ., Access Key ID/Secret Access Key combination) are not
compromised?
A. Enable Multi-Factor Authentication for your AWS root account.
B. Assign an IAM role to the Amazon EC2 instance.
C. Store the AWS Access Key ID/Secret Access Key combination in software comments.
D. Assign an IAM user to the Amazon EC2 Instance.
Correct Answer: A
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/IAM/Iatest/UserGuide/IAMBestPractices.htm|
QUESTION 661
Which of the following are true regarding encrypted Amazon Elastic Block Store (EBS) volumes? Choose 2
answers
A. Supported on all Amazon EBS volume types
B. Snapshots are automatically encrypted
C. Available to all instance types
D. Existing volumes can be encrypted
E. shared volumes can be encrypted
Correct Answer: AB
Explanation
Explanation/Reference:
This feature is supported on all Amazon EBS volume types (General Purpose (SSD), Provisioned Lops (SSD),
and Magnetic). You can access encrypted Amazon EBS volumes the same way you access existing volumes;
encryption and decryption are handled transparently and they require no additional action from you, your
Amazon EC2 instance, or your application. Snapshots of encrypted Amazon EBS volumes are automatically
encrypted, and volumes that are created from encrypted Amazon EBS snapshots are also automatically
encrypted.
http://docs.aws.a mazon.com/kms/latest/developerguide/services-ebs.htmI
QUESTION 662
A company is deploying a new two-tier web application in AWS. The company has limited staff and requires
high availability, and the application requires complex queries and table joins. Which configuration provides the
solution for the company's requirements?
A. MySQL Installed on two Amazon EC2 Instances in a single Availability Zone
B. Amazon RDS for MySQL with Multi-AZ
C. Amazon EIastiCache
D. Amazon DynamoDB
Correct Answer: D
Explanation
Explanation/Reference:
http://www.aIithingsdistributed.com/2013/03/dyna mod b-one-year-Iater.htmI
QUESTION 663
A t2.medium EC2 instance type must be launched with what type of Amazon Machine Image (AMI)?
A. An Instance store Hardware Virtual Machine AMI
B. An Instance store Paravirtual AMI
C. An Amazon EBS-backed Hardware Virtual Machine AMI
D. An Amazon EBS-backed Paravirtual AMI
Correct Answer: A
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/AWSEC2/Iatest/UserGuide/ec2-instanee-resize.htmI
QUESTION 664
You manually launch a NAT AMI in a public subnet. The network is properly configured. Security groups and
network access control lists are property configured. Instances in a private subnet can access the NAT. The
NAT can access the Internet. However, private instances cannot access the Internet. What additional step is
required to allow access from the private instances?
A. Enable Source/Destination Check on the private Instances.
B. Enable Source/Destination Check on the NAT instance.
C. Disable Source/Destination Check on the private instances.
D. Disable Source/Destination Check on the NAT instance.
Correct Answer: B
Explanation
Explanation/Reference:
QUESTION 665
Which of the following approaches provides the lowest cost for Amazon Elastic Block Store snapshots while
gMng you the ability to fully restore data?
A. Maintain two snapshots: the original snapshot and the latest incremental snapshot.
B. Maintain a volume snapshot; subsequent snapshots will overwrite one another
C. Maintain a single snapshot the latest snapshot is both Incremental and complete.
D. Maintain the most current snapshot, archive the original and incremental to Amazon Glacier.
Correct Answer: A
Explanation
Explanation/Reference:
QUESTION 666
An existing application stores sensitive information on a non-boot Amazon EBS data volume attached to an
Amazon Elastic Compute Cloud instance. Which of the following approaches would protect the sensitive data
on an Amazon EBS volume?
A. Upload your customer keys to AWS CIoudHSM. Associate the Amazon EBS volume with AWS C|oudHSM.
Re-mount the Amazon EBS volume.
B. Create and mount a new, encrypted Amazon EBS volume. Move the data to the new volume. Delete the old
Amazon EBS volume.
C. Unmount the EBS volume. Toggle the encryption attribute to True. Re-mount the Amazon EBS volume.
D. Snapshot the current Amazon EBS volume. Restore the snapshot to a new, encrypted Amazon EBS
volume. Mount the Amazon EBS volume
Correct Answer: D
Explanation
Explanation/Reference:
QUESTION 667
A US-based company is expanding their web presence into Europe. The company wants to extend their AWS
infrastructure from Northern Virginia (us-east-1) into the Dublin (eu-west-1) region. Which of the following
options would enable an equivalent experience for users on both continents?
A. Use a public-facing load balancer per region to load-balance web traffic, and enable HTIP health checks.
B. Use a public-facing load balancer per region to load-balance web traffic, and enable sticky sessions.
C. Use Amazon Route 53, and apply a geolocation routing policy to distribute traffic across both regions.
D. Use Amazon Route 53, and apply a weighted routing policy to distribute traffic across both regions.
Correct Answer: D
Explanation
Explanation/Reference:
http://docs.aws.amazon.com/Route53/latest/DeveIoperGuide/routing-policy.html
QUESTION 668
Which of the following are use cases for Amazon DynamoDB? Choose 3 answers
A. Storing BLOB data.
B. Managing web sessions.
C. Storing JSON documents.
D. Storing metadata for Amazon S3 objects.
E. Running relational joins and complex updates.
F. Storing large amounts of infrequently accessed data.
Correct Answer: CEF
Explanation
Explanation/Reference:
QUESTION 669
A customer implemented AWS Storage Gateway with a gateway-cached volume at their main office. An event
takes the link between the main and branch office offline. Which methods will enable the branch office to
access their data? Choose 3 answers
A. Use a HTTPS GET to the Amazon S3 bucket where the files are located.
B. Restore by implementing a lifecycle policy on the Amazon S3 bucket.
C. IV|ake an Amazon Glacier Restore API ca II to load the files into another Amazon S3 bucket within four to
six hours.
D. Launch a new AWS Storage Gateway instance AM in Amazon EC2, and restore from a gateway snapshot
E. Create an Amazon EBS volume from a gateway snapshot, and mount it to an Amazon EC2 instance.
F. Launch an AWS Storage Gateway virtual iSCSI device at the branch office, and restore from a gateway
snapshot
Correct Answer: ADF
Explanation
Explanation/Reference:
QUESTION 670
A company has configured and peered two VPCs: VPC-1 and VPC-2. VPC-1 contains only private subnets,
and VPC-2 contains only public subnets. The company uses a single AWS Direct Connect connection and
private virtual interface to connect their on-premises network with VPC-1. Which two methods increases the
fault tolerance of the connection to VPC-1 ? Choose 2 answers
A. Establish a hardware VPN over the internet between VPC-2 and the on-premises network.
B. Establish a hardware VPN overt he internet between VPC-1 and the on-premises network.
C. Establish a new AWS Direct Connect connection and private virtual interface in the same region as VPC-2.
D. Establish a new AWS Direct Connect connection and private virtual interface in a different AWS region than
VPC-1.
E. Establish a new AWS Direct Connect connection and private virtual interface in the same AWS region as
VPC-1
Correct Answer: BC
Explanation
Explanation/Reference:
QUESTION 671
What is the minimum time Interval for the data that Amazon CIoudWatch receives and aggregates?
A. One second
B. Five seconds
C. One minute
D. Three minutes
E. Five minutes
Correct Answer: C
Explanation
Explanation/Reference:
Many metrics are received and aggregated at 1-minute intervals. Some are at 3-minute or 5-minute intervals.
QUESTION 672
Which of the following statements are t rue about Amazon Route 53 resource records? Choose 2 answers
A. An Alias record can map one DNS name to another Amazon Route 53 DNS name.
B. A CNAME record can be created for your zone apex.
C. An Amazon Route 53 CNAME record can point to any DNS record hosted anywhere.
D. TIL can be set for an Alias record in Amazon Route 53.
E. An Amazon Route 53 Alias record can point to any DNS record hosted anywhere.
Correct Answer: AC
Explanation
Explanation/Reference:
http://d0cs.aws.amazon.c0m/R0uteS3/latest/Deve|0perGuide/resource-record-sets-chccsing-aIiasnon-ali
as.htmI
