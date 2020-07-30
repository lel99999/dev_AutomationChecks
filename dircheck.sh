#!/bin/bash
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
