#!/bin/bash
request='http://localhost'
ret_code=`/usr/bin/curl -so /dev/null -w "%{http_code}" $request`

if [ $ret_code -eq 200  ];then
        echo "Success";
        exit 0
fi

echo "Got failed"
exit 1

