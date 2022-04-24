# 

## Basic
```text
httrack "http://www.all.net/" -O "/tmp/www.all.net" "+*.all.net/*" -v
```

httrack --mirror N4 "http://www.all.net/" -O "/tmp/www.all.net" 


## How to search in all HTML files on a website

httrack --skeleton http://localhost/ -V "if grep -iE \"TITLE\" \"\$0\">/dev/null; then echo \"Match found at \$0\"; fi"
rm -rf tmpget

Same thing but matches only the first file:
httrack --skeleton http://localhost/ -V "if grep -iE \"TITLE\" \"\$0\">/dev/null; then echo \"Match found at \$0\"; kill -9 \$PPID; fi"
rm -rf tmpget


## 参考
1. [Httrack Users Guide](http://www.httrack.com/html/fcguide.html)  
2. [HTTrack Programming page](http://www.httrack.com/html/dev.html)