#!/bin/bash
for i in $(ls -d /home/<user_specific_path>/*)
do
echo ${i%%/};
if [[ -f $i/.bashrc ]]; then
  echo $i >> /tmp/bashrc_exists.txt
else
  echo $i >> /tmp/bashrc_noexists.txt
fi
done

# Check mounts
mountpoints=( $(awk '$1 !~ /^#/ && $2 ~ /^[/]/ {print $2}' /etc/fstab) )
for mount in ${mountpoints[@]}; do
   if ! findmnt "$mount" &> /dev/null; then
      echo "$mount is declared in fstab but not mounted"
   fi
done
