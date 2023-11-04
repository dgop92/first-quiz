# Security audit

To improve our security, we should first focus on checking for possible SQL injection risks. To do this, we need to make sure we use libraries or tools like sqlalchemy and SQLModel to write statements in a safe way that prevents SQL attacks.


For our authentication system, we can make it stronger by enforcing strong password rules, using two-factor authentication, and considering using external services for authentication. If we can't use external services due to company policies,  it is imperative that we employ the latest cryptographic algorithms for password hashing, complemented by the use of salts to enhance the security of stored credentials. 


Access control for the 12 software engineers should be tailored to grant them access only to resources essential to their roles. A well-defined permissions structure will mitigate risks such as human error data deletion and facilitate the identification of individuals responsible for specific issues. 


In the context of utilizing APIs or logging mechanisms, we must have caution with serialized data within our application. Sensitive information such as credit card details and passwords should never be serialized to mitigate potential security breaches.


In our technology stack it is necessary to ensure we are running the most up-to-date and secure versions of each component, library, and dependencies. Investing in a vulnerability scanning tool would be a valuable asset in this task.

We're using various technologies, so it's crucial to set up our containers, web interfaces, and backends correctly. We need to ensure we're not running unnecessary services,  safeguard our environment variables, and turn off any ports we don't need to reduce security risks.
