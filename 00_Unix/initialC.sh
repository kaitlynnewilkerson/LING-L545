sed 's/[^a-zA-Z]\+/\n/g' |\
grep -i '^[^aeiouy]' |\
sed 's/[aeiouyAEIOUY][^aeiouyAEIOUY]*//g' |\
sort |\
uniq -c |\
sort -nr
