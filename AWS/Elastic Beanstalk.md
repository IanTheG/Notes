brb# Elastic Beanstalk

> _Quickly deploy and manage web-apps on AWS without worrying about the underlying infrastructure_

</br>

## EB is a **Platform as a Service**

> A platform allowing customers to develop, run, and manage apps without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app.

- Similar to Heroku, but for AWS.
- Not recommended for "Production" applications, warning meant for large companies
- Includes template setups
  - Elastic load balancer (ELB), auto scaling groups (ASG)
  - RDS database
  - EC2 instances with pre-configured or custom platforms (Docker, many supported languages)
  - Monitoring on CloudWatch or SNS
  - Can run Dockerized environments

### Supported Languages and Platforms

- Duby => Rails
- Python => Django
- PHP => Laravel
- Tomcat => Java Spring
- NodeJS => ExpressJS
- Also supports ASP.NET and Docker containers

</br>

### Web vs Worker Environment

Often you need both to be interconnected for a complicated web app.

> Web => Web backend, creates ASG and ELB  
> Worker => background tasks, creates ASG and SQS queue

### Web Env Types

**Load balanced Env**

- Uses ASG and set to scale and...
- Uses an ELB => designed to scale

**Single-instance Env**

- Public IP address to route traffic to server
- Uses an ASG but desired capacity is set to 1 to ensure server is always running
- No ELB, saves cost

</br>

### Development Policies

| Deployment Policy             | Load Balanced Env | Single Instance Env |
| ----------------------------- | ----------------- | ------------------- |
| All at once                   | Yes               | Yes                 |
| Rolling                       | Yes               | No                  |
| Rolling with additional batch | Yes               | No                  |
| Immutable                     | Yes               | Yes                 |

All at once – Deploy the new version to all instances simultaneously. All instances in your environment are out of service for a short time while the deployment occurs.

Rolling – Deploy the new version in batches. Each batch is taken out of service during the deployment phase, reducing your environment's capacity by the number of instances in a batch.

Rolling with additional batch – Deploy the new version in batches, but first launch a new batch of instances to ensure full capacity during the deployment process. Does NOT reduce capacity!

Immutable – Deploy the new version to a fresh group of instances by performing an immutable update. Safest way to deploy critical applications.

</br>

### Deployment Methods

| Method                        | Impact of failed deployment                       | Deploy time | Downtime? | DNS Change? | Rollback process | Code deployed to instances |
| ----------------------------- | ------------------------------------------------- | ----------- | --------- | ----------- | ---------------- | -------------------------- |
| All at once                   | Downtime!                                         | Shortest    | Yes       | No          | Manual           | Existing                   |
| Rolling                       | Single batch out of service                       | Short       | No        | No          | Manual           | Existing                   |
| Rolling with additional batch | Minimal impact if batch fails, similar to Rolling | Medium      | No        | No          | Manual           | New and existing           |
| Immutable                     | Minimal                                           | Long        | No        | Yes         | Terminate new    | New                        |
| Blue / green                  | Minimal                                           | Long        | No        | Yes         | Swap URL         | New                        |

### In Place vs Blue / Green Deployment

The definitions can change based on context and scope.

**_EXAMS REFER TO THIS DEFINITION OF IN-PLACE:_**  
In-place could mean within the _scope of the Elastic Beanstalk Env_:  
All deployment policies provided by EB could be considered in-place since they are within the scope of a single EB environment.

In-place could mean within the _scope of the same server_:  
Deployment policies that do not involve the replaced server. Use All at Once or Rolling.

In-place could mean within the _scope of an uninterrupted server_:  
Traffic is never routed away from the server, zero-downtime deploys where Blue/Green occurs on the server. Use Capistrano, Ruby on Rails, or Unicorn - EB can't do this!
