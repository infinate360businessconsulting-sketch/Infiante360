# Adobe Experience Platform basics
Adobe Experience Platform (AEP) is a platform for collecting, unifying and activating customer data. Data is described with XDM (Experience Data Model) schemas and stored in datasets.

## XDM schemas
An XDM schema defines the structure of data. Record schemas describe attributes such as name or email; event schemas describe time-stamped behaviour such as a page view. Field groups let you reuse standard fields.

## Identity and profile
Identity namespaces label identifiers such as email or a CRM id. The identity graph links identifiers that belong to one person. Real-Time Customer Profile merges attributes and events from enabled datasets into a profile for segmentation and activation.

## Ingestion
Data reaches AEP through batch sources, streaming ingestion, and the Web SDK for browser and app events. Validate schema, identity and dataset settings before enabling a dataset for profile.
