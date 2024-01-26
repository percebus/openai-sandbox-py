az cognitiveservices account create \
    --subscription ${AZ_SUBSCRIPTION_ID} \
    --location ${AZ_REGION_NAME} \
    --resource-group ${AZ_RESOURCE_GROUP_NAME} \
    --kind ${OPENAI_API_KIND} \
    --sku ${OPENAI_API_SKU} \
    --name ${OPENAI_API_NAME}
