az cognitiveservices account create \
    --subscription ${AZ_SUBSCRIPTION_ID} \
    --location ${AZ_REGION_NAME} \
    --resource-group ${AZ_RESOURCE_GROUP_NAME} \
    --kind ${AZ_OPENAI_KIND} \
    --sku ${AZ_OPENAI_SKU} \
    --name ${AZ_OPENAI_NAME}
