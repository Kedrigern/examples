# Azure

**Note:** *StorageAccount is not the same as Azure Account. A StorageAccount is specific to storage services and has its own settings like redundancy and access privileges.*

## StorageAccount

- **Redundancy policy:** Determines how and where the data is replicated to ensure high availability and fault tolerance.
- **Access privileges:** Defines the permission levels (read, write, delete) for accessing and managing the stored data.

## Storage Types

- **Blob:** For unstructured or binary data.
  - **[Tiers:](https://learn.microsoft.com/en-in/azure/storage/blobs/access-tiers-overview)**
    - *hot:* For frequently accessed data.
    - *cool:* For infrequently accessed data with rapid access needs.
    - *cold:* For rarely accessed data.
    - *archive:* For long-term archival with the lowest access frequency.
- **Files:** Shared file storage with support for SMB and NFS protocols; ideal for lift and shift scenarios.
- **[Tables:](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-design-guide)** NoSQL storage for structured data, leveraging partition key and row ID with a default timestamp.
- **Queue:** Messaging service similar to RabbitMQ for asynchronous communication (not intended to replace Kafka).
- **DataLake:** A specialized Blob storage with namespace support for big data analytics and file system-like operations.

## [Concurrency in Blob Storage](https://learn.microsoft.com/en-in/azure/storage/blobs/concurrency-manage)

- **Last writer wins:** The default mode where the last write operation takes precedence.
- **Optimistic concurrency:** Uses the `if-match` header to ensure data integrity; returns error 412 (precondition failed) if there is a version mismatch.
- **Pessimistic concurrency:** Implements a lease mechanism on a blob (from 15 to 60 seconds) to prevent concurrent write conflicts.
  
**Snapshot isolation for read:** Allows the creation of snapshots ensuring a consistent view of the data during reads.

## [Data Redundancy in Storage](https://docs.microsoft.com/en-in/azure/storage/common/storage-redundancy)

- **LRS (Locally Redundant Storage):** Keeps 3 copies of data within a single zone.
   
   ![azure-lrs](https://github.com/user-attachments/assets/6f17cdef-539d-4694-ab48-7cda1159169d)
- **ZRS (Zone Redundant Storage):** Distributes 3 copies across multiple zones within a region.
  ![azure-zrs](https://github.com/user-attachments/assets/59039a69-eded-459f-babc-1040b581373d)
- **GRS (Geo Redundant Storage):** Maintains 3 copies in a primary region with an additional replication in a secondary region.
  ![azure-grs](https://github.com/user-attachments/assets/84e05ab9-7a0f-490d-9709-860667d4431e)
- **GZRS (Geo Zone Redundant Storage):** Combines the benefits of ZRS with geo-replication (additional copy in another region).
  ![azure-gzrs](https://github.com/user-attachments/assets/70be63be-a8b2-4290-8ac6-3a6a9ad27eac)

**Note:** Data redundancy is not the same as CDN.

## RPO and RTO

- **RPO (Recovery Point Objective):** Maximum acceptable data loss, typically less than 15 minutes.
- **RTO (Recovery Time Objective):** Target time to restore services after an outage.

## Azure Services

- **CDN (Content Delivery Network):** Provides global dynamic caching for faster content delivery.
- **Functions:** Serverless compute platform for event-driven applications.
- **Container:** Services like Azure Container Instances for deploying containerized applications.
- **Kubernetes Service (AKS):** Managed Kubernetes for container orchestration.
- **Load Balancer:** Distributes incoming traffic to optimize resource utilization and availability.
- **Databricks:** Managed Apache Spark-based analytics platform for big data processing and machine learning.
- **SQL:** Managed relational database service for both operational and analytical workloads.

## Key Terms

- **ACID:** Atomicity, Consistency, Isolation, Durability – core properties of database transactions.
- **OLTP (Online Transaction Processing):** Real-time transactional processing.
- **OLAP (Online Analytical Processing):** Complex analytical queries for business intelligence.
- **RBAC (Role-Based Access Control):** Access control based on user roles.
- **ACL (Access Control List):** List defining specific permissions for users or groups.
- **[SAS](https://learn.microsoft.com/en-in/azure/storage/common/storage-sas-overview) (Shared Access Signature):** Tokens that delegate restricted access to storage resources without sharing primary keys.

## Protocols

- **REST:** Architectural style using HTTP methods for communication.
- **GraphQL:** Query language that allows clients to request only the data they need.
- **GRPC:** A high-performance communication framework based on HTTP/2 for low latency and efficient data transfer.
