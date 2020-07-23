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
