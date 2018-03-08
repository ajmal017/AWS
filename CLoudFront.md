> [**CloudFront:**](https://aws.amazon.com/cloudfront/)

Amazon CloudFront is a global content delivery network (CDN) service that accelerates delivery of your websites, APIs, video content or other web assets.  
  

-   Edge Location is the location where content will be cached, separate from an AWS Region/AZ
-   Origin is the origin of all files, can be S3, EC2 instance, a ELB, or Route53
-   Distribution is the name given to the CDN which consists a collection of edge locations
-   Web Distributions are used for websites
-   RTMP - (Real-Time Messaging Protocol) used for streaming media typically around adobe flash files
-   Edge locations can be R/W and will accept a PUT request on an edge location, which then will replicate the file back to the origin
-   Objects are cached for the life of the TTL (24 hours by default)
-   You can clear objects from edge locations, but you will be charged
-   When enabling cloudfront from an S3 origin, you have the option to restrict bucket access; this will disable the direct link to the file in the S3 bucket, and ensure that the content is only served from cloudfront
-   The path pattern uses regular expressions
-   You can restrict access to your distributions using signed URLS
-   You can assign Web Application Firewall rules to your distributions
-   Distribution URLs are going to be non-pretty names such as random_characters.cloudfront.com; you can create a CNAME that points to the cloudfront name to make the URL user friendly
-   You can restrict content based on geographical locations in the behaviors tab
-   You can create custom error pages via the error pages tab
-   Purging content is handled in the Invalidations tab
