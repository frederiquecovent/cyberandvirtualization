$vmName = "DC-Server"
$isoPath = "$env:USERPROFILE\Downloads\zerologon-poc\ISO\server_2019_build_17763.737.iso"
$autoIso = "$env:USERPROFILE\Downloads\zerologon-poc\autounattend.iso"
$vmFolder = "$env:USERPROFILE\VirtualBox VMs\$vmName"

& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createvm --name $vmName --ostype Windows2016_64 --register
& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm $vmName --memory 4096 --cpus 2 --nic1 intnet --intnet1 "ZerologonNet" --boot1 dvd
& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createhd --filename "$vmFolder\$vmName.vdi" --size 30000

& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storagectl $vmName --name "SATA Controller" --add sata
& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storageattach $vmName --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$vmFolder\$vmName.vdi"
& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storageattach $vmName --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium $isoPath
& "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storageattach $vmName --storagectl "SATA Controller" --port 2 --device 0 --type dvddrive --medium $autoIso

#PS C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\amd64\Oscdimg> .\oscdimg.exe -n -m C:\Users\Frederique\Downloads\zerologon-poc\SetupFiles C:\Users\Frederique\Downloads\zerologon-poc\autounattend.iso