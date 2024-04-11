import streamlit as st
from azure.storage.blob import BlobServiceClient

# Azure storage account url
storage_account_url = "https://meddocsearchsa.blob.core.windows.net/"
# BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient(account_url=storage_account_url)

# Name of your container
container_name = "med-docs"
# Get a client to interact with a specific container - though it won't do anything yet
container_client = blob_service_client.get_container_client(container_name)

st.title('Hello, Azure!')
st.write('This is a basic Streamlit app deployed on Azure.')

# List all blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    st.write(blob.name)