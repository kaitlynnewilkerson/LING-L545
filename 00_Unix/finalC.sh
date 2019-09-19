sed 's/[^a-zA-Z]\+/\n/g' |\
grep -i '^[a-z]' |\
sed 's/[a-zA-Z]*[aeiouyAEIOUY]//g' |\
sort |\
uniq -c |\
sort -nr
