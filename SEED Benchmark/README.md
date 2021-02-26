# SEED Benchmark

[![Build Status](https://travis-ci.com/SEED-platform/OEP.svg?branch=Dev)](https://travis-ci.com/SEED-platform/OEP)

The OEP SEED Benchmark supports Benchmark programs by automting benchmark record data updadates from the Standard Energy Efficiency Data (SEED) Platform in Salesforce.com. The automation is provided via MuleSoft Anypoint Platform Community Edition API. The MuleSoft API provides one-way data flow, with Property records in SEED updating Benchmark records, and creating Account and Contract records in a Salesforce managed package called the "OEI Package". The OEI Package includes example Benchmark reports and email templates.

This automation was developed to support a pilot project with the City of San Francisco. It is an open source solution that can be configured to meet the needs of other organizations interested in benchmarking data management using SEED and Salesforce.

Get started [here](/SEED%20Benchmark/guides/). This includes the User Guide (which is the README) and the Benchmark Implementation Guide.

"OEI" folder holds the self extracting zip MuleSoft files to be used for Docker.

# SEED Benchmark Salesforce

The SEED Benchmark use case, leverages the OEP Salesforce managed package "OEI Package".
Documentation for installing the managaged package and referencing the OEP Data Model can be found [here](/Salesforce%20Package)

The SEED Benchmark uses the Premises and Benchmark managed package objects and uses the standard Account, and Contact objects. It includes reports in the OEI Reports folder and email templates in the OEI Email Templates folder with the name "Benchmark in them.

## Deployment

The preferred method of deployment is to use docker and docker stack deploy. The docker containers are provided on [Docker Hub](https://cloud.docker.com/u/seedplatform/repository/docker/seedplatform/oep) but can also be built locally for development and testing. In order to use docker, it is recommended to follow the instructions in the [docker folder](docker/README.md). The instructions include how to configure the configuration files for deployment.

## Development Notes

* The Docker version uses the versions in the OEI/*.xml directory. For some reason, when developing in Eclipse it appears that the OEI/classes/*.xml are used. It is important that both these files are "in-sync".

# TODO

* Remove spaces from directory names. It can cause some trivial issues with Docker.
* Add Docker instructions to Benchmark Implementation Guide.
