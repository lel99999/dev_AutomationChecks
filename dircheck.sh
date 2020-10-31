#!/bin/bash

## Environment Checks

## Installation Checks

## User-Specific Checks
# id -u <name>
if id "$1" >/dev/null 2>&1; then
  echo "User has been created"
else
  echo "User has not been created"
fi

for USER in /home/org/user
do
  if [[ -f $USER/Desktop ]]
  then
    echo "User has been initialized"
  else
    echo "User has not been initialized"
  fi
done

do
  if [[ -f /home/<org>/<user>/.bash_profile
  then
    if [[ grep -i ".local" "$USER/.bash_profile" ]]
    then
      echo "bash_profile PATH correct"
    else
      echo "bash_profile PATH incoorrect"
    fi
  fi
done

# Grep for Additions in .bashrc
for USER in /home/org/*
do
  if [ grep -i "STATTMP" "$USER/.bashrc" ]]
  then
    echo "$USER, STATATMP found"
  else
    echo "$USER, STATATMP not found"
  fi
done

## If USER not in /home/<org>/ directory, run a creation script copying over /etc/skel
## or do initial SSH
##
## SKEL= in /etc/default/useradd
## contents ... .bash_logout .bash_profile .bashrc

## $ssh-keygen -t rsa -b 2048
## Generating public/private rsa key pair.
## Enter file in which to save the key (/home/username/.ssh/id_rsa): 
## Enter passphrase (empty for no passphrase): 
## Enter same passphrase again: 
## Your identification has been saved in /home/username/.ssh/id_rsa.
## Your public key has been saved in /home/username/.ssh/id_rsa.pub. 

## $ssh-copy-id id@server
## id@server's password:
## try $ssh id@server to see if password prompt

for i in $(ls -d /home/<user_specific_path>/*)
do
echo ${i%%/};
if [[ -f $i/.bashrc ]];
 then
  echo $i >> /tmp/bashrc_exists.txt
else
  echo $i >> /tmp/bashrc_noexists.txt
fi
done

# Check mounts
MOUNTS=( $(awk '$1 !~ /^#/ && $2 ~ /^[/]/ {print $2}' /etc/fstab) )
for mount in ${MOUNTS[@]};
do
   if ! findmnt "$mount" &> /dev/null; then
      echo "$mount is declared in fstab but not mounted"
   fi
done

# Check file permissions
for filename in *;
do
   if [ $(stat -c "%a" "$filename") == "755" ]
   then
      echo "File with correct permission: $filename"
   else
      echo "File with incorrect permision: $filename"
      chmod 755 "$filename"
   fi
done 

curl -s http://api.example.com/stats > api-stats.txt
awk 'BEGIN { print "<table>" }
     { print "<tr><td>" $1 "</td><td>" $2 "</td></tr>" }
     END   { print "</table>" }' api-stats.txt > api-stats.html
