Prueba Seminario

{
	"info": {
		"_postman_id": "4b6c8d9e-1f2a-4c9b-b2d3-1e4f5g6h7i8j",
		"name": "CRUD de Platos (Django Vistas)",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"description": "Colección para probar las vistas CRUD de Platos implementadas con Class-Based Views de Django. La URL base es http://127.0.0.1:8000. Advertencia: las peticiones POST/DELETE requieren manejo del token CSRF o la exención de su protección en las vistas para Postman."
	},
	"item": [
		{
			"name": "1. [R] READ - LISTA de Platos (GET)",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/platos/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"platos",
						""
					]
				},
				"description": "Obtiene la lista completa de platos. Devuelve el HTML renderizado (PlatoListView)."
			},
			"response": []
		},
		{
			"name": "2. [R] READ - DETALLE de Plato (GET)",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/platos/1/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"platos",
						"1",
						""
					]
				},
				"description": "Obtiene los detalles de un plato específico. Sustituye '1' por el ID/PK del plato. Devuelve el HTML renderizado (PlatoDetailView)."
			},
			"response": []
		},
		{
			"name": "3. [C] CREATE - Crear Nuevo Plato (POST)",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "urlencoded",
					"urlencoded": [
						{
							"key": "codigo",
							"value": "POST-001",
							"type": "text",
							"description": "Máximo 10 caracteres"
						},
						{
							"key": "nombre",
							"value": "Tarta de Prueba",
							"type": "text"
						},
						{
							"key": "descripcion",
							"value": "Postre de prueba enviado desde Postman.",
							"type": "text"
						},
						{
							"key": "categoria",
							"value": "Postre",
							"type": "text"
						},
						{
							"key": "precio",
							"value": "8.50",
							"type": "text"
						},
						{
							"key": "disponible",
							"value": "on",
							"type": "text",
							"description": "Para booleanos en formulario: 'on' (True) o dejar vacío (False)"
						},
						{
							"key": "tiempo_preparacion_min",
							"value": "10",
							"type": "text"
						},
						{
							"key": "calorias",
							"value": "450",
							"type": "text"
						},
						{
							"key": "es_vegetariano",
							"value": "on",
							"type": "text",
							"description": "Para booleanos en formulario: 'on' (True) o dejar vacío (False)"
						},
						{
							"key": "nivel_picante",
							"value": "1",
							"type": "text",
							"description": "Valor entre 1 y 5"
						}
					]
				},
				"url": {
					"raw": "http://127.0.0.1:8000/platos/nuevo/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"platos",
						"nuevo",
						""
					]
				},
				"description": "Crea un nuevo plato (PlatoCreateView). **Requiere el token CSRF**."
			},
			"response": []
		},
		{
			"name": "4. [U] UPDATE - Editar Plato (POST)",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "urlencoded",
					"urlencoded": [
						{
							"key": "codigo",
							"value": "POST-ACTUALIZADO",
							"type": "text"
						},
						{
							"key": "nombre",
							"value": "Tarta Actualizada",
							"type": "text"
						},
						{
							"key": "precio",
							"value": "9.50",
							"type": "text"
						},
						{
							"key": "disponible",
							"value": "on",
							"type": "text"
						},
						{
							"key": "descripcion",
							"value": "Descripción actualizada desde Postman.",
							"type": "text"
						},
						{
							"key": "categoria",
							"value": "Postre",
							"type": "text"
						},
						{
							"key": "tiempo_preparacion_min",
							"value": "15",
							"type": "text"
						},
						{
							"key": "calorias",
							"value": "500",
							"type": "text"
						},
						{
							"key": "es_vegetariano",
							"value": "off",
							"type": "text",
							"description": "Ejemplo de False"
						},
						{
							"key": "nivel_picante",
							"value": "1",
							"type": "text"
						}
					]
				},
				"url": {
					"raw": "http://127.0.0.1:8000/platos/1/editar/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"platos",
						"1",
						"editar",
						""
					]
				},
				"description": "Actualiza un plato existente (PlatoUpdateView). Sustituye '1' por el ID/PK. **Requiere el token CSRF**."
			},
			"response": []
		},
		{
			"name": "5. [D] DELETE - Eliminar Plato (POST)",
			"request": {
				"method": "POST",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/platos/1/eliminar/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"platos",
						"1",
						"eliminar",
						""
					]
				},
				"description": "Solicita la eliminación de un plato (PlatoDeleteView). Sustituye '1' por el ID/PK. **Requiere el token CSRF**."
			},
			"response": []
		}
	]
}
