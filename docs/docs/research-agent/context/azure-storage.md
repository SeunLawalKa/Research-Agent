# Azure Storage

If you want to use Azure Blob Storage as the source for your Research Agent report context, follow these steps:

> **Step 1** - Set these environment variables with a .env file in the root folder

```bash
AZURE_CONNECTION_STRING=
AZURE_CONTAINER_NAME=
```

> **Step 2** - Add the `azure-storage-blob` dependency to your requirements.txt file

```bash
azure-storage-blob
```

> **Step 3** - When running the ResearchAgent class, pass the `report_source` as `azure`

```python
report = ResearchAgent(
    query="What happened in the latest burning man floods?",
    report_type="research_report",
    report_source="azure",
)
```