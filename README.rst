- Scalability
  The solution currently uses an ORM since it doesn't have a complex relational model this should scale
  with any clustered RDBMS. Since this will be an read heavy application, Along with RDBMS we could use
  an in memory database like redis/memcached for heavily used URLs as an LRU cache.

- Availability
  Setup a loadbalancer like haproxy with healthchecks to make sure hosts are healthy.
  Round robin to send requests equally among healthy hosts. Also haproxy itself is prone to failure
  so would prefer setting up as a cluster with pacemaker and corosync using floating ip.
  .
- Deployment automation
  Prefer doing an ansible playbooks for deployment automation for easy maintainability.

- Security
  Currently no implemented but a solution with OAuth with API tokens for access management.

- Coding style

- Testing
  Will use unit tests to get maximum coverage. And also loadrunner or locust or jmeter for performance
  for each release to make sure the performance is not deteriorated over the time

- Internal doc
  Will depend on docstrings for API documentation. Use Sphinx for doc generation.

- User doc

- Performance
