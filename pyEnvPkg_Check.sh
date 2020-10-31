#!/bin/bash

declare -a aCMD=("python -c 'import numpy;print(numpy.__version__)'" "python -c 'import scipy;print(scipy.__version__)'" "python -c 'import pandas;print(pandas.__version__)'")

python -c "import numpy;print(numpy.__version__)"

echo "Native Python 2.7"
echo `which python`
for i in "${aCMD[@]}";do
#  echo "$i"
  	eval "$i | echo "$i" failed"
done
