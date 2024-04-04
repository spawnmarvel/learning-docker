# https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-5.1

$url = "http://localhost:8983/solr/aspenTech/select?q=*:*"

try
{
    $rv = Invoke-WebRequest -URI $url
    write-host $rv.StatusCode
    write-host $rv.Headers
    # get all properties
    # $rv | Get-Member
    # 
  
}
catch
{
    $StatusCode = $_.Exception.Response.StatusCode.value__
    
}
write-host @StatusCode