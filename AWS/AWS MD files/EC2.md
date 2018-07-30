
# Elastic Cloud Compute (EC2) 
***
### **Definition** 

-   Amazon Elastic Block Store (Amazon EBS) provides persistent block storage volumes for use with Amazon EC2 instances in the AWS Cloud.

***
### **IAM Features** 

-   **High Performance Volumes :** Choose between SSD-backed or HDD-backed volumes that can deliver the performance you need for your most demanding applications.

-   **Availability :** Each Amazon EBS volume is designed for 99.999% availability and automatically replicates within its Availability Zone to protect your applications from component failure

-   **Encryption :** Amazon EBS encryption provides seamless support for data-at-rest and data-in-transit between EC2 instances and EBS volumes.

-   **Access Management :** Amazon’s flexible access control policies allow you to specify who can access which EBS volumes ensuring secure access to your data.

-   **Snapshots :** Protect your data by creating point-in-time snapshots of EBS volumes, which are backed up to Amazon S3 for long-term durability.

-   **Elastic Volumes :** Dynamically increase capacity, tune performance, and change the type of live EBS volumes. 
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
