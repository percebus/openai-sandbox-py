az cognitiveservices account deployment create \
    --resource-group ${AZ_RESOURCE_GROUP_NAME} \
    --name ${AZ_OPENAI_NAME} \
    --deployment-name ${AZ_OPENAI_DEPLOYMENT_NAME} \
    --model-name ${AZ_OPENAI_MODEL_NAME} \
    --model-version ${AZ_OPENAI_MODEL_VERSION}  \
    --model-format ${AZ_OPENAI_MODEL_FORMAT} \
    --scale-settings-scale-type ${AZ_OPENAI_SCALING}
