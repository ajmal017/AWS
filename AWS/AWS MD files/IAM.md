
# AWS Identity and Access Management (IAM)
***
### **Definition** 

-   AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their       access to AWS resources

-   Users      - End users / people.
    
-   Groups     - Users having one set of permissions.
    
-   Roles      - Create set of permissions and assign them to AWS resources.
    
-   Policies   - Document (JSON format) that defines one or more permissions – assign to user or groups
    
***
### **IAM Features** 

-   **Fine-grained access control to AWS resources :** IAM enables your users to control access to AWS service APIs and to specific resources. IAM also enables you to add specific conditions such as time of day to control how a user can use AWS, their originating IP address, whether they are using SSL, or whether they have authenticated with a multi-factor authentication device.

-   **Multi-factor authentication for highly privileged users :** Protect your AWS environment by using AWS MFA, a security feature available at no extra cost that augments user name and password credentials. MFA requires users to prove physical possession of a hardware MFA token or MFA-enabled mobile device by providing a valid MFA code.

-   **Manage access control for mobile applications with Web Identity Providers :** You can enable your mobile and browser-based applications to securely access AWS resources by requesting temporary security credentials that grant access only to specific AWS resources for a configurable period of time.

-   **Integrate with your corporate directory :** IAM can be used to grant your employees and applications federated access to the AWS Management Console and AWS service APIs, using your existing identity systems such as Microsoft Active Directory. You can use any identity management solution that supports SAML 2.0, or feel free to use one of our federation samples (AWS Console SSO or API federation).
***
### **Important Points** 
-   IAM is a global service. It is not region specific
    
-   Root account is the email address you use to sign up for AWS
    
-   AWS recommends very limited usage of root account
    
-   Setup MFA on root account.
    
-   You can attach permissions to individual users and groups.
    
-   Secret access key can be retrieved only once during user creation. In case you lose it then you can re-generate it.
    
-   IAM Password policy can be set to access the admin console.
    
-   New users have no permissions when first created. Everything has to be explicitly added.
    
-   Power User Access allows Access to all AWS services except the management of groups and users within IAM.

-   Using Access Key ID and Secret Access Key – can be used only via accessing programmatically. Likewise username and password can only be used while accessing the console
  
-   A user can belong to multiple groups.
  
-   Groups cannot belong to other groups

-   IAM users can be email address

-   IAM role vs IAM user : An IAM user has permanent long-term credentials and is used to directly interact with AWS services. An IAM role does not have any credentials and cannot make direct requests to AWS services. IAM roles are meant to be assumed by authorized entities, such as IAM users, applications, or an AWS service such as EC2.

-   Can not add an IAM role to an IAM group

-   IAM roles for EC2 instances enables your applications running on EC2 to make requests to AWS services such as Amazon S3, Amazon SQS, and Amazon SNS without you having to copy AWS access keys to every instance

-   You can use same IAM role on multiple EC2 instances

-   Role can also be assigned to an EC2 instance that is already running.

-   You can associate an IAM role with an Auto Scaling group

-    Can not associate more than one IAM role with an EC2 instance

-   You must grant an IAM user two distinct permissions to successfully launch EC2 instances with roles:

    -   Permission to launch EC2 instances.
    -   Permission to associate an IAM role with EC2 instances.
-   A service-linked role is a type of role that links to an AWS service (also known as a linked service) such that only the linked service can assume the role. Using these roles, you can delegate permissions to AWS services to create and manage AWS resources on your behalf.

-   Managed policy: Set of permissions which are managed by you or AWS

-   Use IAM groups to collect IAM users and define common permissions for those users. Use managed policies to share permissions across IAM users, groups, and roles

-   Managed policies can only be attached to IAM users, groups, or roles. You cannot use them as resource-based policies.

-   Only the AWS account owner can manage the access keys for the root account

-   The AWS account alias is a name you define to make it more convenient to identify your account

-   AWS multi-factor authentication (AWS MFA) provides an extra level of security that you can apply to your AWS environment

-   With identity federation, external identities are granted secure access to resources in your AWS account without having to create IAM users

-   Federated users (external identities) are users you manage outside of AWS in your corporate directory, but to whom you grant access to your AWS account using temporary security credentials   

-   Federated users can access AWS APIs

-   Federated users can access the AWS Management Console

-   Web identity federation allows you to create AWS-powered mobile apps that use public identity providers (such as Amazon Cognito, Login with Amazon, Facebook, Google, or any OpenID Connect-compatible provider) for authentication.
***
### **Best Practices** 

-   Users – Create individual users.

-   Groups – Manage permissions with groups.

-   Permissions – Grant least privilege.

-   Auditing – Turn on AWS CloudTrail.

-   Password – Configure a strong password policy.

-   MFA – Enable MFA for privileged users.

-   Roles – Use IAM roles for Amazon EC2 instances.

-   Sharing – Use IAM roles to share access.

-   Rotate – Rotate security credentials regularly.

-   Conditions – Restrict privileged access further with conditions.

-   Root – Reduce or remove use of root.
***

## Video Presentation About IAM Best Practices<a name="top-practices-video"></a>

[![AWS Videos](http://img.youtube.com/vi/_wiGpBQGCjU/0.jpg)](http://www.youtube.com/watch?v=_wiGpBQGCjU)
