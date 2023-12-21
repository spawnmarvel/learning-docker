## Mount fileshare on VM Better use a disk, not fileshare....args

Storage account staccvmdocker01

Fileshare dockershare01

Test 445
```bash
# cp each line
RESOURCE_GROUP_NAME="<your-resource-group>"
STORAGE_ACCOUNT_NAME="<your-storage-account>"

# This command assumes you have logged in with az login
HTTP_ENDPOINT=$(az storage account show --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --query "primaryEndpoints.file" --output tsv | tr -d '"')
SMBPATH=$(echo $HTTP_ENDPOINT | cut -c7-${#HTTP_ENDPOINT})
FILE_HOST=$(echo $SMBPATH | tr -d "/")

nc -zvw3 $FILE_HOST 445

# Connection to .file.core.windows.net (xx.xxx.xx.xxx) 445 port [tcp/microsoft-ds] succeeded!

```

Mount it

```bash

# https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-linux?tabs=Ubuntu%2Csmb311

# https://follow-e-lo.com/2023/11/09/ubuntu-az-cli-and-mount-fileshare/

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

az upgrade
az version
# azure-cli 2.55.0


sudo apt install cifs-utils

sudo apt install -y linux-modules-extra-azure

az login --tenant
# To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code

# cp each line
# Step 1
RESOURCE_GROUP_NAME="<resource-group-name>"
STORAGE_ACCOUNT_NAME="<storage-account-name>"
FILE_SHARE_NAME="<file-share-name>"

MNT_ROOT="/media"
MNT_PATH="$MNT_ROOT/$STORAGE_ACCOUNT_NAME/$FILE_SHARE_NAME"

sudo mkdir -p $MNT_PATH

# cd to /media, then pwd
/media/staccvmdocker01/dockershare01

# This command assumes you have logged in with az login
HTTP_ENDPOINT=$(az storage account show --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --query "primaryEndpoints.file" --output tsv | tr -d '"')
SMB_PATH=$(echo $HTTP_ENDPOINT | cut -c7-${#HTTP_ENDPOINT})$FILE_SHARE_NAME

STORAGE_ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv | tr -d '"')

sudo mount -t cifs $SMB_PATH $MNT_PATH -o username=$STORAGE_ACCOUNT_NAME,password=$STORAGE_ACCOUNT_KEY,serverino,nosharesock,actimeo=30,mfsymlinks

# Create a folder on the fileshare on the vm
# cd, sudo mkdir test01, pwd
/media/staccvmdocker01/dockershare01/test01

# Verify the folder on the storage account
# Storage accounts > name > File shares > sharename
test01
# Restart the vm and verify the folder and make a file in the folder
ssh

mount

# and no share args

# Went to the fileshare and copied the Connect script
touch connect_fileshare.sh

sudo bash connect_fileshare.sh

cd /mnt
ls
# 
# DATALOSS_WARNING_README.txt  dockershare01  lost+found
cd dockershare01
ls
# test01

# Restart vm and all gone, so back to the initial step 1 code.

```

https://learn.microsoft.com/en-us/answers/questions/1410701/linux-image-6-2-0-1016-azure-cifs-is-not-supported

## Use the portal to attach a data disk to a Linux VM

Create standard sdd, e8 in the same rg

```bash

```

https://learn.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal?tabs=ubuntu

https://github.com/spawnmarvel/azure-automation/blob/main/azure-extra-linux-vm/READMEQuickstartsLinuxMS.md