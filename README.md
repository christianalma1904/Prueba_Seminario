{
  "info": {
    "_postman_id": "platos-collection-001",
    "name": "API - Platos Restaurante",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    {
      "key": "base_url",
      "value": "http://127.0.0.1:8000/api"
    },
    {
      "key": "token",
      "value": ""
    }
  ],
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Login - Obtener Token",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"username\": \"admin\",\n  \"password\": \"admin123\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/auth/login/",
              "host": ["{{base_url}}"],
              "path": ["auth", "login", ""]
            }
          },
          "response": [],
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "var json = pm.response.json();",
                  "if (json.token) {",
                  "    pm.collectionVariables.set(\"token\", json.token);",
                  "}",
                  "pm.test(\"Login exitoso\", function () {",
                  "    pm.response.to.have.status(200);",
                  "});"
                ],
                "type": "text/javascript"
              }
            }
          ]
        }
      ]
    },
    {
      "name": "Platos",
      "item": [
        {
          "name": "Listar Platos",
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{base_url}}/platos/",
              "host": ["{{base_url}}"],
              "path": ["platos", ""]
            }
          },
          "response": []
        },
        {
          "name": "Crear Plato",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Authorization",
                "value": "Token {{token}}"
              },
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"codigo\": \"PLT-001\",\n  \"nombre\": \"Hamburguesa Doble\",\n  \"descripcion\": \"Carne doble, queso, vegetales y salsa especial\",\n  \"categoria\": \"PRINCIPAL\",\n  \"precio\": \"8.50\",\n  \"disponible\": true,\n  \"tiempo_preparacion_min\": 15,\n  \"calorias\": 900,\n  \"es_vegetariano\": false,\n  \"nivel_picante\": 1\n}"
            },
            "url": {
              "raw": "{{base_url}}/platos/",
              "host": ["{{base_url}}"],
              "path": ["platos", ""]
            }
          },
          "response": []
        },
        {
          "name": "Detalle Plato (id)",
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{base_url}}/platos/1/",
              "host": ["{{base_url}}"],
              "path": ["platos", "1", ""]
            }
          },
          "response": []
        },
        {
          "name": "Actualizar Plato (PUT)",
          "request": {
            "method": "PUT",
            "header": [
              {
                "key": "Authorization",
                "value": "Token {{token}}"
              },
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"id\": 1,\n  \"codigo\": \"PLT-001\",\n  \"nombre\": \"Hamburguesa Doble Especial\",\n  \"descripcion\": \"Versión mejorada con pan brioche y salsa premium\",\n  \"categoria\": \"PRINCIPAL\",\n  \"precio\": \"9.50\",\n  \"disponible\": true,\n  \"tiempo_preparacion_min\": 14,\n  \"calorias\": 950,\n  \"es_vegetariano\": false,\n  \"nivel_picante\": 2\n}"
            },
            "url": {
              "raw": "{{base_url}}/platos/1/",
              "host": ["{{base_url}}"],
              "path": ["platos", "1", ""]
            }
          },
          "response": []
        },
        {
          "name": "Eliminar Plato",
          "request": {
            "method": "DELETE",
            "header": [
              {
                "key": "Authorization",
                "value": "Token {{token}}"
              }
            ],
            "url": {
              "raw": "{{base_url}}/platos/1/",
              "host": ["{{base_url}}"],
              "path": ["platos", "1", ""]
            }
          },
          "response": []
        }
      ]
    }
  ]
}