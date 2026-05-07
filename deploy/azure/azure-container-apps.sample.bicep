// Sample Azure Container Apps skeleton for review only.
// Do not deploy as-is. No secrets are included in this file.
//
// This assumes:
// - a Container Apps managed environment already exists;
// - the image is in a private registry you control;
// - a private storage mount named by indexStorageName is configured on the
//   managed environment and contains .math_rag_index/index.json;
// - authentication and HTTPS are configured before connecting ChatGPT.

param location string = resourceGroup().location
param appName string = 'math-rag-remote-mcp'
param managedEnvironmentId string
param containerImage string
param publicBaseUrl string
param indexStorageName string = 'math-rag-index'

resource app 'Microsoft.App/containerApps@2024-03-01' = {
  name: appName
  location: location
  properties: {
    managedEnvironmentId: managedEnvironmentId
    configuration: {
      ingress: {
        external: true
        targetPort: 8000
        transport: 'auto'
      }
    }
    template: {
      containers: [
        {
          name: 'math-rag-remote-mcp'
          image: containerImage
          env: [
            {
              name: 'MATH_RAG_INDEX_DIR'
              value: '/data/.math_rag_index'
            }
            {
              name: 'MATH_RAG_REMOTE_MCP_READ_ONLY'
              value: 'true'
            }
            {
              name: 'MATH_RAG_REMOTE_PUBLIC_BASE_URL'
              value: publicBaseUrl
            }
            {
              name: 'MATH_RAG_REMOTE_HOST'
              value: '0.0.0.0'
            }
            {
              name: 'MATH_RAG_REMOTE_PORT'
              value: '8000'
            }
            {
              name: 'MATH_RAG_REMOTE_TRANSPORT'
              value: 'http'
            }
            {
              name: 'MATH_RAG_REMOTE_PATH'
              value: '/mcp/'
            }
            {
              name: 'MATH_RAG_MCP_ALLOW_WRITE_TOOLS'
              value: 'false'
            }
          ]
          volumeMounts: [
            {
              volumeName: 'math-rag-index'
              mountPath: '/data/.math_rag_index'
            }
          ]
          resources: {
            cpu: json('0.5')
            memory: '1Gi'
          }
        }
      ]
      volumes: [
        {
          name: 'math-rag-index'
          storageType: 'AzureFile'
          storageName: indexStorageName
        }
      ]
      scale: {
        minReplicas: 0
        maxReplicas: 1
      }
    }
  }
}
