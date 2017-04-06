- Scalability

- Availability
  Setup a loadbalancer like haproxy with healthchecks to make sure hosts are healthy.
  Round robin to send requests equally among healthy hosts. Also haproxy itself is prone to failure
  so would prefer setting up as a cluster with pacemaker and corosync using floating ip or DNS.
- Deployment automation
- Security
- Coding style
- Testing
- Internal doc
- User doc
- Performance