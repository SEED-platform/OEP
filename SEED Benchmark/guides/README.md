![](oep.png)

# **Benchmark User Guide**

Last Updated: 2019

# **Table of Contents**

[1: Introduction 3](#_Toc534373141)

[2: Automated Updates 4](#_Toc534373142)

[Record Setup in Salesforce 4](#_Toc534373143)

[View Results in Salesforce 5](#_Toc534373144)

[3: Error Log Email 7](#_Toc534373145)

[Errors 7](#_Toc534373146)

[Example Error Log Email 8](#_Toc534373147)

[4: References 9](#_Toc534373148)

# **1: Introduction**

This document is a user guide to support Benchmark programs by automating benchmark record data updates from the Standard Energy Efficiency Data (SEED) Platform to Salesforce.com. The automation is provided via MuleSoft Anypoint Platform Community Edition API. The MuleSoft API provides one-way data flow, with Property records in SEED updating records in a Salesforce managed package called "OEI Package".

This automation was developed to support a pilot project with the City of San Francisco. It is an open source solution that can be configured to meet the needs of other organizations interested in benchmarking data management using SEED and Salesforce. Prior to using this guide, the OEP Benchmark Implementation Guide should be followed to setup an implementation of the OEP Benchmark solution [1].

This document describes how to trigger automated updates from SEED to Salesforce, how to use error log emails to troubleshoot errors, and provides references for additional resources. Each section identifies configuration elements and how the City of San Francisco configured the solution to meet their use case.

# **2: Automated Updates**

This section describes how to trigger automated updates and what to expect of those updates. There are two different types of update which are each triggered by a different Label from SEED. One type of API update updates fields from SEED Label and Property to Salesforce, the other API update updates fields from the SEED Label. The City of San Francisco uses both of these API updates depending on the Label value being either "Complied" or "Violation – Insufficient Data".

Automated updates occur periodically. For the City of San Francisco, the update is configured to occur every 60 minutes.

## Record Setup in Salesforce

**Premises:** Using the OEI App, create a Premises record. Enter the Name field value based on the SEED field mapping in the OEP Data Model [3] on the Premises tab. If the Premises record already exists in Salesforce, skip this step.

**Benchmark:** Using the OEI App, create a child Benchmark record with an assigned Premises Name. Enter the Name field values. For the City of San Francisco the Benchmark name is manually entered combining the SEED Property Name and Cycle.

When the Benchmark record is open, copy the "Benchmark Salesforce ID" from the URL. Example Benchmark Salesforce ID is the bolded section of the example URL: https://sitename.lightning.force.com/lightning/r/oei\_\_Benchmark\_\_c/ **a0D3C000001aOi0UAG** /view

**Account: \*Optional step\*** Using Salesforce standard objects, create an Account record. When creating an Account record, select the Account type specified for your use case. For the City of San Francisco, the Account record type is "Commercial". Enter the Name field value based on the SEED field mapping in the OEP Data Model [2] on the Account tab.

**Contact: \*Optional step\*** In Salesforce, using Salesforce standard objects, create a child Contact record. Enter the Name field value based on the SEED field mapping in the OEP Data Model [2] on the Contact tab. Be sure to data enter the Email address that matches the SEED Property Email field.

**\*** Creating Account and Contact records manually is an optional step. If there is no Contact with a matching email or Account with a matching Name, then a new record will be created in the automated API update.

#### Trigger API Update in SEED

##### Update Option 1: Trigger Label Update in SEED

Navigate: Select "Inventory", select the Property record, select "Edit".

**Step 1:** Data enter the value for the "Benchmark Salesforce ID" field, select "Save Changes". If the Benchmark Salesforce ID is already entered, delete it, select "Save Changes", select edit, enter it, select "Save Changes" so that the record is updated. The record must be updated in the duration since the last update in order for the record to be trigged to be updated in Salesforce.

Navigate: In Property record, select "Add/Remove Labels"

**Step 2:** For the Label name that is configured to trigger Label Update, select "Add", select "Done". For the City of San Francisco, the Label for this update is named "Violation - Insufficient Data".

**Step 3:** When ready to trigger update to Salesforce.com: For "Add to Salesforce" Label, select "Add", select "Done".

##### Update Option 2: Trigger Label & Property Update in SEED

Navigate: Select "Inventory", select the Property record, select "Edit".

**Step 1:** Data enter the value for the "Benchmark Salesforce ID" field, select "Save Changes". If the Benchmark Salesforce ID is already entered, delete it, select "Save Changes", select edit, enter it, select "Save Changes" so that the record is updated. The record must be updated in the duration since the last update in order for the record to be trigged to be updated in Salesforce.

Navigate: In Property record, select "Add/Remove Labels".

**Step 2:** For the Label name that is configured to trigger Label & Property Update, select "Add", select "Done". For the City of San Francisco, this Label for this update is named "Complied".

**Step 3:** When ready to trigger update: For "Add to Salesforce" Label, select "Add", select "Done".

## View Results in Salesforce

##### Update Option 1: Label Fields Updated in Salesforce

**Premises:** No update to Premises record.

**Benchmark:** Label Updates made to Benchmark record where it's Salesforce ID field is equal to the Benchmark Salesforce ID in SEED. Fields in Salesforce that are updated are Fields with values from the Label in SEED. Fields that are not updates remain unchanged, if they previously had values they continue to do so. Fields updated are identified in the OEP Data Model, Benchmark tab, "Update Label" column [2].

**Account:** If the name doesn't match an existing Account record, then a new Account record is created. Fields updated are identified in the OEP Data Model, Account tab, "Update Label" column [2].

**Contact:** If the email doesn't match an existing Contact record, then a new Contact record is created for that Account. Fields created are identified in the OEP Data Model, Contact "Update Label" column [2]. The Contact record does not update if the email matches an existing Contact record email.

##### Update Option 2: Label & Property Fields Updated in Salesforce

**Premises:** No update to Premises record.

**Benchmark:** Label & Property Updates made to Benchmark record where it's Salesforce ID field is equal to the Benchmark Salesforce ID in SEED. Fields in Salesforce that are update are Fields with values from the Label and Property in SEED. Fields updated are identified in the OEP Data Model, Benchmark tab, "Update Property & Label" column [2].

**Account:** If the name doesn't match an existing Account record, then a new Account record is created. Fields updated are identified in the OEP Data Model, Account tab, "Update Property & Label" column [2].

**Contact:** If the email doesn't match an existing Contact record, then a new Contact record is created for that Account. Fields created are identified in the OEP Data Model, Contact "Update Property & Label" column [2]. The Contact record does not update if the email matches an existing Contact record email.

# 3: Error Log Email

When an error occurs in MuleSoft the user can have an error log email configured to be sent to them. An error log email is sent for each update where there is an error, all errors for that update are listed in one email.

**Step 1:** Read the Error Log Email

For the errors associated with a property record the format is: [Error Code] SEED property: [Property Name], SEED Id: [Property View Id]. [Description of error].

**Step 2:** Resolve the Error

In SEED, open the Property record for that Property Name. Use the Description of the error in the error message and for the Error Code see the hints in the Error Reference Table below to identify and resolve the error. Make sure you have edited/saved the record in SEED so that it will be triggered for update.

**Step 3:** Confirm Update

After the update duration has passed (default configured to 60 minutes) confirm that the record has updated in Salesforce. If it failed to update the error message will reoccur on the next Error Log Email.

## Errors

| **Error Reference Table** |
| --- |
| **Error Code** | **Error Details and User Hints** |
| [Error1] | _ **Missing Update Label:** _ No labels that trigger updates have been applied to this property, so no records are updated. The user can resolve this error by applying a Label, in SEED to the identified Property, that will trigger an update. For City of San Francisco this is either "Complied" or "Violation – Insufficient Data".OR_ **Multiple Update Label:** _ Two different labels that trigger updates have been applied to this property, so no records are updated to avoid the incorrect type of update from occurring.The user can resolve this error by removing one of the Labels, in SEED to the identified Property, that will trigger an update. For City of San Francisco this is either "Complied" or "Violation – Insufficient Data". |
| [Error2] | _ **Missing Benchmark Salesforce ID** __:_ Benchmark Salesforce ID field is missing for this property, so no records are updated.The user can resolve this error by data entering the Salesforce Benchmark ID, in SEED to the identified Property. |
| [Error3] | _ **Data Error in Salesforce Update:** _ There is an error in a field value coming from SEED.The user can resolve this error by looking at the message in the error. It will point to the error, resolve error. |
| [Info1] | _ **MuleSoft instance exception error** __:_ The user can confirm whether recent updates have occurred as expected. If they have not, the user can retrigger the SEED property record by editing it. The user cannot directly resolve this error as it is caused by a system exception. Contact a system administrator if it persists. |

## Example Error Log Email

**Subject:** Error log for SEED to Salesforce Mule process

**Email Body:**

[Error1] SEED property: 1600 Jackson Street, SEED Id: 513157. Both 'Complied' AND 'Violation - Insufficient Data' labels have been applied to this property so no action will be taken.

[Error1] SEED property: Market Lytton, LLC, SEED Id: 519265. Neither 'Complied' or 'Violation - Insufficient Data' labels have been applied to this property so no action will be taken.

[Error2] SEED property: DPR Construction, SEED property ID: 530455 'Benchmark Salesforce ID' field is missing, there is no Salesforce object destination so no action will be taken

[Error3] For SEED property: 639 Front Street, SEED Id: 513004 There was an error when updating Salesforce, which returned the following message:

Record ID: id value of incorrect type: wrong ID

[Error3] For SEED property: 140 9TH ST, SEED Id: 515401 There was an error when updating Salesforce, which returned the following message:

Total GHG Emissions Intensity (kgCO2e/ft: invalid number: sdf

[Info1] There was an error: MuleEvent: 0-debb2522-e8ed-11e8-a4db-00059a3c7a00, stop processing=false, polling://-1912630717with the following details: org.codehaus.groovy.runtime.typehandling.GroovyCastException: Cannot cast object '2018-11-06 12:05:58.000' with class 'java.lang.String' to class 'java.util.Date'

# 4: References

Find documentation about OEP at the [GitHub site](/OEP)

Relevant documentation for the SEED Benchmark use case that this User Guide supports can be found at in the OEP github site:

- [1] [OEP Benchmark Implementation Guide](/SEED%20Benchmark/guides/OEP%20Benchmark%20Implementation%20Guide.md)

- [2] [OEP Data Model](/Salesforce%20Package/OEP%20Data%20Model.xlsx)

