## URL Shortner toy project

This project implements simple tiny url using python with Flask, sqlalchemy

### How to run

1. Checkout the source from the git repo
   `git clone git@github.com:srsakhamuri\urlshort`
2. Then change directory
   `cd urlshort`
3. Create env
   `make env`
4. activate the sandbox
   `source .env/bin/activate`
5. Create the database
   `./manage.py createdb`
6. Run the server
   `./manage.py server`
7. Check out the following section for running the curl API or run it via the browser by hitting
   `http://localhost:5000`

### Example commands

`curl -XPOST http://localhost:5000/shorten?long_url=http://google.com -H "Accept: application/json"`

`curl http://localhost:5000/<short_code>` redirects to corresponding URL associated with this short URL

### Few other things

1. Scalability
  The solution currently uses an ORM since it doesn't have a complex relational model this should scale
  well with any clustered RDBMS. Since this will be an read heavy application, Along with RDBMS we could use
  an in memory database like redis/memcached for heavily used URLs as an LRU cache.

2. Availability
  Setup a loadbalancer like haproxy with healthchecks to make sure hosts are healthy.
  Round robin to send requests equally among healthy hosts. Also haproxy itself is prone to failure
  so would prefer setting up as a cluster with pacemaker and corosync using floating ip.
  
3. Deployment automation
  Prefer doing an ansible playbooks for deployment automation for easy maintainability. Check
  deploy/playbook.yml for simple deployment steps

4. Security
  Currently no implemented but a solution with OAuth with API tokens for access management should be simple
  to implment with Flask-login extension

5. Testing
  Will use unit tests (pytest)to get maximum coverage. And also loadrunner or locust or jmeter for performance
  for each release to make sure the performance is not deteriorated over the time

6. Internal doc
  Will depend on docstrings for API documentation. Use Sphinx for doc generation.


### Deploy log
```

11:06 $ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'bento/ubuntu-16.04' is up to date...
==> default: A newer version of the box 'bento/ubuntu-16.04' is available! You currently
==> default: have version '2.3.1'. The latest is version '2.3.4'. Run
==> default: `vagrant box update` to update.
==> default: Setting the name of the VM: urlshort_default_1491577642200_37934
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 5000 (guest) => 5050 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /vagrant => /Users/srisakha/src/urlshort
==> default: Running provisioner: ansible...
    default: Running ansible-playbook...
```
### Provision log
```
PLAY [all] *********************************************************************

TASK [setup] *******************************************************************
ok: [default]

TASK [Copy the urlshort repo] **************************************************
changed: [default]

TASK [install make] ************************************************************
changed: [default]

TASK [Kill existing process] ***************************************************
fatal: [default]: FAILED! => {"changed": true, "failed": true, "rc": 1, "stderr": "Shared connection to 127.0.0.1 closed.\r\n", "stdout": "pkill: pidfile not valid\r\nTry `pkill --help' for more information.\r\n", "stdout_lines": ["pkill: pidfile not valid", "Try `pkill --help' for more information."]}
...ignoring

TASK [setup env] ***************************************************************
changed: [default]

TASK [Creae database] **********************************************************
changed: [default]

TASK [Start application] *******************************************************
changed: [default]

PLAY RECAP *********************************************************************
default                    : ok=7    changed=6    unreachable=0    failed=0
```
### Sample commands
```
(.env) ✔ ~/src/urlshort [master|✚ 2]
11:10 $ curl -XPOST http://localhost:5050/shorten?long_url=http://google.com -H "Content-Type: application/json"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>URL Shortner</title>
</head>
<body>
<form>
    Long URL: <input type="text" name="long_url" value=http://google.com>
    <input type="submit" formaction="/shorten">
    <div><a href=http://localhost:5050/b>http://localhost:5050/b</a></div>
</form>
</body>
</html>

(.env) ✔ ~/src/urlshort [master|✚ 2]
11:11 $ curl -XPOST http://localhost:5050/shorten?long_url=http://google.com -H "Accept: application/json"
{
  "long_url": "http://google.com",
  "short_url": "http://localhost:5050/c"
}

(.env) ✔ ~/src/urlshort [master|✚ 2]
11:11 $ curl -XPOST http://localhost:5050/shorten?long_url=http://citrix.com -H "Accept: application/json"
{
  "long_url": "http://citrix.com",
  "short_url": "http://localhost:5050/d"
}

(.env) ✔ ~/src/urlshort [master|✚ 2]
11:11 $ curl http://localhost:5050/d
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="http://citrix.com">http://citrix.com</a>.  If not click the link.
```
