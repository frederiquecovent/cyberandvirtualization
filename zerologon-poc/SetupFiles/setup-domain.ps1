Import-Module ServerManager
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools

Import-Module ADDSDeployment
Install-ADDSForest `
    -DomainName "zerolab.local" `
    -DomainNetbiosName "ZEROLAB" `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "Wachtwoord123!" -AsPlainText -Force) `
    -InstallDNS:$true -Force:$true