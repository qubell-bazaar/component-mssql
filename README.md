MSSQL Server
===============

Version 2.0-36p
---------------

![](http://www.arvixe.com/images/landing_pages/mssql_2008_hosting.png)

Installs and configures MSSQL Server 2008R2/2012

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-mssql/2.0-36p/meta.yml)
------------------------------------------------

Features
--------
 - Install and configure MSSQL Server 2008R2/2012 Express or Full version
 - Create databases
 - Manage users and grants
 - Execute arbitrary SQL on a database

Configurations
--------------
 - MSSQL Server 2008R2, MS Windows 2012-R2 Server (us-east-1/ami-ba13abd2), AWS EC2 m3.medium, Administrator
 - MSSQL Server 2012, MS Windows 2012-R2 Server (us-east-1/ami-ba13abd2), AWS EC2 m3.medium, Administrator

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under Administrator
 - Either installed Cygwin on target compute OR launch under Administrator
 - Internet access from target compute:
   - Microsoft SQL server distribution and additions
   - S3 bucket with Chef recipes: qubell-starter-kit-artifacts

Implementation notes
--------------------
 - Installation is based on Chef recipes from https://github.com/qubell-bazaar/cookbook_qubell_mssql

Configuration parameters
------------------------
 - input.server-os: List of available Amazon AMI ID and user identity
 - input.server-os-password: Administrator's password
 - input.server-instance-size:  Amazon instance type
 - input.instance-prefix: Custom Prefix for AWS console Name tag
 - input.recipe-url: URL to chef cookbooks tarball
 - input.mssql-version: List of available MSSQL versions to install
 - input.mssql-key: MSSQL Product Key (When specified will be installed full MSSQL Server version instead of Express)
 - input.mssql-sa-password: MSSQL SA user password
 - input.mssql-port: MSSQL Server listen port
