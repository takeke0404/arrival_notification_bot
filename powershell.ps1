python $PSScriptRoot/scraping.py | sv x
cd $PSScriptRoot
foreach($y in $x){
  $y | Out-File "text.txt" -Encoding "UTF8"
  curl.exe -X POST -H "Authorization: Bearer 7IWK98uDYpM2E6pNeopcAWhovDYH9xBmwV0MIAbrBuH" -F "message=<text.txt" https://notify-api.line.me/api/notify
}
