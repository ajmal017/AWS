#  AWS Certification Notes:
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
IAM : Identity and Access Management
-	IAM is used to control who is authenticated (signed in) and authorized (has permissions) to use AWS resources.
-	IAM allows you to manage users and thier level of access to the AWS console using groups and policies

- Critical Terms
	 -  IAM consists of the following
	 --  Users    :  End users / people.
	 --  Groups   :  Collection of users. Users having one set of permissions.
	 --  Roles    :  An AWS identity with permission policies that determine what the identity can and cannot do in AWS.
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
	 -  Use Roles for Applications That Run on Amazon EC2 Instances
 

   
=================================================================================
  


