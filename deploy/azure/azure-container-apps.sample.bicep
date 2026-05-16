// Sample Azure Container Apps skeleton for review only.
// Do not deploy as-is. No secrets are included in this file.
//
// This assumes:
// - a Container Apps managed environment already exists;
// - the image is in a private registry you control;
// - a private storage mount named by indexStorageName is configured on the
//   managed environment and contains .math_rag_index/index.json;
// - authentication, HTTPS, and direct-ingress restrictions are configured
//   before connecting ChatGPT.
//
// SECURITY NOTE:
// The ingress block below uses external: true only as a placeholder for early
// fixture-index tests. This is not safe for the real research index unless APIM
// or equivalent network policy prevents direct bypass. Prefer private ingress
// or IP/network restrictions that allow only the gateway to reach the backend.

param location string = resourceGroup().location
param appName string = 'math-rag-remote-mcp'
param managedEnvironmentId string
param containerImage string
param apiTokenSecretName string = 'math-rag-api-token'
@secure()
param apiToken string
param indexStorageName string = 'math-rag-index'

resource app 'Microsoft.App/containerApps@2024-03-01' = {
  name: appName
  location: location
  properties: {
    managedEnvironmentId: managedEnvironmentId
    configuration: {
      secrets: [
        {
          name: apiTokenSecretName
          value: apiToken
        }
      ]
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
              name: 'MATH_RAG_AUTH_MODE'
              value: 'bearer'
            }
            {
              name: 'MATH_RAG_API_TOKEN'
              secretRef: apiTokenSecretName
            }
            {
              name: 'MATH_RAG_TOOL_MODE'
              value: 'chatgpt'
            }
            {
              name: 'MATH_RAG_HOST'
              value: '0.0.0.0'
            }
            {
              name: 'PORT'
              value: '8000'
            }
            {
              name: 'MATH_RAG_REMOTE_TRANSPORT'
              value: 'streamable-http'
            }
            {
              name: 'MATH_RAG_REMOTE_PATH'
              value: '/mcp'
            }
            {
              name: 'MATH_RAG_MCP_ALLOW_WRITE_TOOLS'
              value: 'false'
            }
            {
              name: 'MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC'
              value: 'false'
            }
            {
              name: 'MATH_RAG_PROTECT_HEALTH'
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
