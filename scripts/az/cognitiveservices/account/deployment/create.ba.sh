az cognitiveservices account deployment create \
    --resource-group ${AZ_RESOURCE_GROUP_NAME} \
    --name ${OPENAI_API_NAME} \
    --deployment-name ${OPENAI_API_DEPLOYMENT_NAME} \
    --model-name ${OPENAI_API_MODEL} \
    --model-version ${OPENAI_API_MODEL_VERSION}  \
    --model-format ${OPENAI_API_MODEL_FORMAT} \
    --scale-settings-scale-type ${OPENAI_API_SCALING}
