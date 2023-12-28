
## Fileshare not supported

https://learn.microsoft.com/en-us/answers/questions/1410701/linux-image-6-2-0-1016-azure-cifs-is-not-supported

## Use the portal to attach a data disk to a Linux VM

* Find the virtual machine
* Attach a new disk
* Connect to the Linux VM to mount the new disk

```bash

# Find the disk
lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"

# sda     0:0:0:0       30G
# ├─sda1              29.9G /
# ├─sda14                4M
# └─sda15              106M /boot/efi
# sdb     0:0:0:1        8G
# └─sdb1                 8G /mnt
# sdc     1:0:0:0        4G

# In this example, the disk that was added was sdc. It's a LUN 0 and is 4GB.

```
Prepare a new empty disk

If you are using an existing disk that contains data, skip to mounting the disk. The following instructions will delete data on the disk.

```bash
# The following example uses parted on /dev/sdc, which is where the first data disk will typically be on most VMs. Replace sdc with the correct option for your disk. 

sudo parted /dev/sdc --script mklabel gpt mkpart xfspart xfs 0% 100%

sudo mkfs.xfs /dev/sdc1

sudo partprobe /dev/sdc1

# Use the partprobe utility to make sure the kernel is aware of the new partition and filesystem. 


```
Mount the disk

```bash
sudo mkdir /datadrive

sudo mount /dev/sdc1 /datadrive

# To ensure that the drive is remounted automatically after a reboot, it must be added to the /etc/fstab file. It's also highly recommended that the UUID (Universally Unique Identifier) is used in /etc/fstab to refer to the drive rather than just the device name (such as, /dev/sdc1).

sudo blkid
# /dev/sdc1: UUID="cb692e40-6029-4c17-9476-277006ea5ab5" BLOCK_SIZE="4096" TYPE="xfs" PARTLABEL="xfspart" PARTUUID="2b7e9afb-4126-478f-820d-37a9e9d755ca"

# Next, open the /etc/fstab file in a text editor. Add a line to the end of the file, using the UUID value for the /dev/sdc1 device that was created in the previous steps, and the mountpoint of /datadrive. Using the example from this article, the new line would look like the following:

UUID=cb692e40-6029-4c17-9476-277006ea5ab5   /datadrive   xfs   defaults,nofail   1   2

sudo nano /etc/fstab

```
Verify the disk

```bash
lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"
# sda     0:0:0:0       30G
# ├─sda1              29.9G /
# ├─sda14                4M
# └─sda15              106M /boot/efi
# sdb     0:0:0:1        8G
# └─sdb1                 8G /mnt
# sdc     1:0:0:0        4G
# └─sdc1                 4G /datadrive

# You can see that sdc is now mounted at /datadrive.

```

Create file and restart vm
```bash
cd /datadrive

sudo mkdir test01

# Reboot and verify disk

```
https://learn.microsoft.com/en-us/azure/virtual-machines/linux/attach-disk-portal?tabs=ubuntu

https://github.com/spawnmarvel/azure-automation/blob/main/azure-extra-linux-vm/READMEQuickstartsLinuxMS.md