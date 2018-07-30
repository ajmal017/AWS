
# Elastic Cloud Compute (EC2) 
***
### **Definition** 

-   Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale computing easier for developers.
***
### **EC2 Features** 

-   **ELASTIC WEB-SCALE COMPUTING:**  Amazon EC2 enables you to increase or decrease capacity within minutes, not hours or days. You can commission one, hundreds, or even thousands of server instances simultaneously. You can also use Amazon EC2 Auto Scaling to maintain availability of your EC2 fleet and automatically scale your fleet up and down depending on its needs in order to maximize performance and minimize cost. To scale multiple services, you can use AWS Auto Scaling.

-   **COMPLETELY CONTROLLED :** You have complete control of your instances including root access and the ability to interact with them as you would any machine. You can stop any instance while retaining the data on the boot partition, and then subsequently restart the same instance using web service APIs. Instances can be rebooted remotely using web service APIs, and you also have access to their console output.

-   **FLEXIBLE CLOUD HOSTING SERVICES :** You have the choice of multiple instance types, operating systems, and software packages. Amazon EC2 allows you to select a configuration of memory, CPU, instance storage, and the boot partition size that is optimal for your choice of operating system and application. For example, choice of operating systems includes numerous Linux distributions and Microsoft Windows Server.

-   **INTEGRATED :** Amazon EC2 is integrated with most AWS services such as Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS), and Amazon Virtual Private Cloud (Amazon VPC) to provide a complete, secure solution for computing, query processing, and cloud storage across a wide range of applications.

-   **RELIABLE :** Amazon EC2 offers a highly reliable environment where replacement instances can be rapidly and predictably commissioned. The service runs within Amazon’s proven network infrastructure and data centers. The Amazon EC2 Service Level Agreement commitment is 99.99% availability for each Amazon EC2 Region.

-   **SECURE :** Cloud security at AWS is the highest priority. As an AWS customer, you will benefit from a data center and network architecture built to meet the requirements of the most security-sensitive organizations. Amazon EC2 works in conjunction with Amazon VPC to provide security and robust networking functionality for your compute resources.

-   **INEXPENSIVE :** Amazon EC2 passes on to you the financial benefits of Amazon’s scale. You pay a very low rate for the compute capacity you actually consume. See Amazon EC2 Instance Purchasing Options for more details.

-   **EASY TO START :** There are several ways to get started with Amazon EC2. You can use the AWS Management Console, the AWS Command Line Tools (CLI), or AWS SDKs. AWS is free to get started. To learn more, please visit our tutorials.


***
### **Important Points** 
-   If you are using an Amazon EBS volume as a root partition, set the Delete on termination flag to "No" if you want your Amazon EBS volume to persist outside the life of the instance.
    
-   EBS provides four current generation volume types: Provisioned IOPS SSD (io1), General Purpose SSD (gp2), Throughput Optimized HDD (st1) and Cold HDD (sc1)
    
-   SSD-backed volumes are designed for transactional, IOPS-intensive database workloads, boot volumes, and workloads that require high IOPS. SSD-backed volumes include Provisioned IOPS SSD (io1) and General Purpose SSD (gp2).
    
-   HDD-backed volumes are designed for throughput-intensive and big-data workloads, large I/O sizes, and sequential I/O patterns. HDD-backed volumes include Throughput Optimized HDD (st1) and Cold HDD (sc1)
    
-   Changing a EBS volume configuration is easy. The Elastic Volumes feature allows you to increase capacity, tune performance, or change your volume type with a single CLI call, API call or a few console clicks
    
-   When attached to EBS-optimized instances, Provisioned IOPS volumes can achieve single digit millisecond latencies
    
-   Snapshots are only available through the Amazon EC2 API and are not availbale via Amazon S3 API
    
-   Snapshots can be done in real time while the volume is attached and in use
    
-   Each snapshot is given a unique identifier, and customers can create volumes based on any of their existing snapshots.
    
-   You can share the snapshot locally or globally
    
-   Amazon EBS encryption offers seamless encryption of EBS data volumes, boot volumes and snapshots, eliminating the need to build and maintain a secure key management infrastructure
    
-   You can mount multiple volumes on the same instance, but each volume can be attached to only one instance at a time. You can dynamically change the configuration of a volume attached to an instance

-   EBS volumes behave like raw, unformatted block devices. You can create a file system on top of these volumes, or use them in any other way you would use a block device (like a hard drive)

-   EBS encryption supports boot volumes

-   You can create an encrypted data volume at the time of instance launch by using customer master keys (CMKs) that are either AWS-managed or customer-managed

-   Yes, you will be billed for the IOPS provisioned when it is disconnected from an instance. When a volume is detached, we recommend you consider creating a snapshot and deleting the volume to reduce costs.

-   EBS volumes can only be attached to one EC2 instance at a time. In contrast, EFS can be shared but has a much higher price point

-   ⏱A single EBS volume allows 10k IOPS max. To get the maximum performance out of an EBS volume, it has to be of a maximum size and attached to an EBS-optimized EC2 instance.

-   When restoring a snapshot to create an EBS volume, blocks are lazily read from S3 the first time they're referenced. To avoid an initial period of high latency, you may wish to use dd or fio

-   A standard block size for an EBS volume is 16kb.
  
-   Public snapshots of encrypted volumes are not supported, but you can share an encrypted snapshot with specific accounts


***
### **Best Practices** 

-   Ensure all AWS EBS volumes for app tier are encrypted

-   Ensure that existing Elastic Block Store (EBS) attached volumes are encrypted to meet security and compliance requirements.

-   Ensure EBS volumes are encrypted with KMS CMKs in order to have full control over data encryption and decryption.

-   Ensure that your Amazon EBS volume snapshots are not accessible to all AWS accounts

-   Ensure AWS Elastic Block Store (EBS) volumes have recent snapshots available for point-in-time recovery.

-   Identify and remove old AWS Elastic Block Store (EBS) volume snapshots for cost optimization

-   Ensure all AWS EBS volumes for web tier are encrypted.
***
