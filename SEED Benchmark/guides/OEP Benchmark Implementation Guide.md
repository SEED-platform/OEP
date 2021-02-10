![](oep.png)

# **Benchmark Implementation Guide**

Last Updated: 2019

# **Table of Contents**

[1: Introduction 3](#_Toc534371569)

[2: Salesforce Managed Package &quot;OEI Platform&quot; 4](#_Toc534371570)

[3: Docker MuleSoft solution 5](#_Toc534371571)

[4: Setup Email Server 6](#_Toc534371572)

[5: Configure MuleSoft solution 7](#_Toc534371573)

[Edit Configuration Properties 7](#_Toc534371574)

[Edit Field Mappings 7](#_Toc534371575)

[6: Modify MuleSoft solution 8](#_Toc534371576)

[7: References 9](#_Toc534371577)

# **1: Introduction**

This document is an implementation guide to support Benchmark programs by automating benchmark record data updates from the Standard Energy Efficiency Data (SEED) Platform to Salesforce.com. The automation is provided via MuleSoft Anypoint Platform Community Edition API. The MuleSoft API provides one-way data flow, with Property records in SEED updating records in a Salesforce managed package called the &quot;OEI Platform&quot;.

This automation was developed to support a pilot project with the City of San Francisco. It is an open source solution that can be configured to meet the needs of other organizations interested in benchmarking data management using SEED and Salesforce.

This guide, the OEP Benchmark Implementation Guide, should be followed to setup an implementation of the OEP Benchmark solution.

This document describes how to install the Salesforce managed package in your organization&#39;s Salesforce instance, how to install the dockered MuleSoft solution, how to configure the MuleSoft solution for your instance, and how to modify the MuleSoft solution for your instance.

# 2: Salesforce Managed Package &quot;OEI Platform&quot;

Login to your organizations Salesforce instance. If you do not already have an instance, go to Salesforce.com to learn more about Salesforce and its licensing options.

Navigate to the app selecting the URL below depending on if the instance is a Sandbox or Production site:

Sandbox: [https://test.salesforce.com/packaging/installPackage.apexp?p0=04t1N000000GnV8](https://test.salesforce.com/packaging/installPackage.apexp?p0=04t1N000000GnV8)

Production: [https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1N000000GnV8](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1N000000GnV8)

For either URL enter the password: MLLk7aCPvz2cBTP3pV3Y

Select &quot;Install for all Users&quot;

Go to Setup, search for Installed Packages, confirm &quot;OEI Platform&quot; is installed

In App launcher, select &quot;OEI&quot; App, view the tabs. The &quot;Premises&quot;, &quot;Benchmark&quot;, &quot;Account&quot;, and &quot;Contacts&quot; tabs/objects are used for the Benchmark use case. They are documented at the field level in the OEP Data Model [1]. The OEP Data Model includes field level mappings from ENERGY STAR Portfolio Manager and SEED to Salesforce. It also includes identification of which fields are updated for the &quot;Update Label &amp; Properties&quot; and &quot;Update Label&quot; updates via MuleSoft API.

# 3: Docker MuleSoft solution

# 4: Setup Email Server

To receive Mule error emails, an email server must be setup. This is optional, but without it your organization will not receive notifications of errors in updating from SEED to Salesforce.

Free cloud-based email server services are available online and support levels of service that are appropriate for error log emails. One example service provider is SendGrid. Their free option includes 100 emails per day which is sufficient for logging errors from updates on an hourly basis.

# 5: Configure MuleSoft solution

There are two primary file **s** to edit for configuration. Configuration Properties has the properties set for the instance and must be edited for new instances. Field Mappings can optionally be edited based on the use case.

## Edit Configuration Properties

Configuration can be edited in the Oei.properties file. It is found in [github](/SEED%20Benchmark/conf)

Edit, save, commit changes to this file. The instance must be reloaded for it to run using the updated Oei.properties file. All new instances will require updating: Mule host configuration, SEED user configuration, Salesforce user configuration, and Mule error email configuration. Some instances may choose to update: SEED trigger update label name configuration, and update timer configuration.

## Edit Field Mappings

Field mappings can be edited, deleted, and added in the groovy files. The groovy files are found in the github site at: [https://github.com/OpenEfficiencyPlatform/OEP/tree/master/SEED%20Benchmark/mulesoft/src/main/groovy](https://github.com/OpenEfficiencyPlatform/OEP/tree/master/SEED%20Benchmark/mulesoft/src/main/groovy)

AccountToSalesforce.groovy can be edited to configure the field mappings for the Salesforce Account object.

ContactToSalesforce.groovy can be edited to configure the field mappings for the Salesforce Contact object.

SEEDPropertyToSFBenchmark.groovy can be edited to configure the field mappings for the Salesforce Benchmark object.

# 6: Modify MuleSoft solution

The MuleSoft code is open source and has been made available in the github site: [https://github.com/OpenEfficiencyPlatform/OEP/tree/master/SEED%20Benchmark/mulesoft](https://github.com/OpenEfficiencyPlatform/OEP/tree/master/SEED%20Benchmark/mulesoft).

# 7: References

Find documentation about OEP at the github site: [https://github.com/OpenEfficiencyPlatform/OEP](https://github.com/OpenEfficiencyPlatform/OEP)

Relevant documentation in the OEP github site includes:

- [1] OEP Data Model

[https://github.com/OpenEfficiencyPlatform/OEP/blob/master/Salesforce%20Package/OEP%20Data%20Model.xlsx](https://github.com/OpenEfficiencyPlatform/OEP/blob/master/Salesforce%20Package/OEP%20Data%20Model.xlsx)

- [2] OEP Benchmark User Guide: [https://github.com/OpenEfficiencyPlatform/OEP/blob/master/SEED%20Benchmark/guides/OEP%20Benchmark%20User%20Guide.docx](https://github.com/OpenEfficiencyPlatform/OEP/blob/master/SEED%20Benchmark/guides/OEP%20Benchmark%20User%20Guide.docx)