# dev_AutomationChecks
Exploratory Development with Automated System Checks and Reporting
#### Frameworks to Review
- [ ] BATS (Bash Automated Testing System) - [https://github.com/sstephenson/bats](https://github.com/sstephenson/bats) 
- [ ] Ansible RSpec = [https://github.com/volanja/ansible_spec](https://github.com/volanja/ansible_spec)
- [ ] Spock = [https://spockframework.org/](https://spockframework.org/)

#### Add Environment Specific Checks
- Check Python 2.x, 3.x versions
- Check SCL Python 3.x
- Check VirtualEnv 
- Check if Python Packages have been installed
  - numpy
  - scipy
  - pandas

#### Add User Specific Checks
- User Exists <br/>
- User Creation <br/>
  - in correct AD groups <br/>
  - getfacl/setfacl has correct ACLs <br/>
- User .bashrc and other information created/exits <br/>
  - within .bashrc STATATMP and crk variables are set <br/>
  - within .bash_profile include correct PATH additions <br/>

Issue #142 <br/>
- Confirm STATA serers are running<br/>
- Confirm <org>, data,work,work2 mounts are function on _adml06<br/>
- Check no 0kb duplicate files exists<br/>
- Check SASStudio is funcioning correctly<br/>
- Check RStudio is functioning correctly<br/>
- Check mounts on _adml06'<br/>

Issue #159 <br/>
- Check .bashrc for existence/defined crk and STATATMP <br/>


#### Add Directory Checks
- Check mounts from /etc/fstab <br/>

#### Headless Client Testing
https://docs.travis-ci.com/user/gui-and-headless-browsers/

#### Add HTML Output

#### Add Selenium Testing
  
#### Add Infrastructure Code
