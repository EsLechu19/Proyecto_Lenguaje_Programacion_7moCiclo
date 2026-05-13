# StockWise - Sistema de Gestión de Inventario

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0.5-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple.svg)
![Chart.js](https://img.shields.io/badge/Chart.js-4.x-orange.svg)

Sistema web de gestión de inventario desarrollado como proyecto académico para el curso de **Lenguajes de Programación**. El sistema permite administrar productos, categorías, entradas y salidas de stock mediante una interfaz moderna tipo dashboard SaaS.

---

# Descripción General

StockWise es una aplicación web construida con Django siguiendo la arquitectura **MTV (Model - Template - View)**. El proyecto fue diseñado para ayudar a pequeñas tiendas y negocios a llevar un control organizado de su inventario.

El sistema incluye:

* Gestión de productos
* Gestión de categorías
* Registro de entradas y salidas
* Dashboard interactivo
* Reportes visuales
* Alertas de stock bajo
* Sistema de autenticación
* Visualización gráfica de movimientos

---

# Características Principales

| Módulo        | Funcionalidad                           |
| ------------- | --------------------------------------- |
| Autenticación | Login y logout de usuarios              |
| Dashboard     | Estadísticas generales del inventario   |
| Productos     | CRUD completo de productos              |
| Categorías    | CRUD completo de categorías             |
| Inventario    | Registro de entradas y salidas          |
| Alertas       | Detección automática de stock bajo      |
| Reportes      | Vista general de métricas y movimientos |
| Búsqueda      | Filtro de productos por nombre          |
| Seguridad     | Protección de rutas con login           |
| Visualización | Gráficos con Chart.js                   |

---

# Tecnologías Utilizadas

| Categoría         | Tecnología                    |
| ----------------- | ----------------------------- |
| Lenguaje          | Python 3.14                   |
| Framework Backend | Django 6.0.5                  |
| Base de Datos     | SQLite3                       |
| Frontend          | HTML5 + CSS3                  |
| Framework CSS     | Bootstrap 5.3.3               |
| Iconos            | Font Awesome                  |
| Gráficos          | Chart.js                      |
| Arquitectura      | MTV (Model - Template - View) |

---

# Arquitectura del Proyecto

El proyecto sigue la arquitectura MTV de Django:

```text
stockwise/
│
├── config/                 # Configuración principal del proyecto
├── productos/              # Gestión de productos y categorías
├── inventario/             # Entradas y salidas de stock
├── usuarios/               # Login y autenticación
├── reportes/               # Estadísticas y reportes
├── templates/              # Templates HTML
├── static/                 # Archivos CSS e imágenes
├── db.sqlite3              # Base de datos SQLite
└── manage.py
```

---

# Funcionalidades del Sistema

## Dashboard Principal

El dashboard muestra:

* Total de productos
* Total de entradas
* Total de salidas
* Productos con stock bajo
* Últimos movimientos registrados
* Gráfico estadístico de movimientos
* Acciones rápidas

---

## Gestión de Productos

El sistema permite:

* Crear productos
* Editar productos
* Eliminar productos
* Buscar productos
* Asociar categorías
* Controlar stock mínimo

---

## Gestión de Inventario

### Entradas

Las entradas incrementan automáticamente el stock del producto.

### Salidas

Las salidas reducen automáticamente el stock del producto.

El sistema valida que no se pueda registrar una salida si no existe suficiente stock disponible.

---

## Reportes

La sección de reportes permite visualizar:

* Total de productos
* Total de categorías
* Total de movimientos
* Productos con stock bajo
* Últimos movimientos realizados

---

# Seguridad Implementada

El sistema implementa:

* Protección de rutas mediante `@login_required`
* Sistema de autenticación nativo de Django
* Protección CSRF en formularios
* Validación de formularios con Django Forms
* Control de sesiones de usuario

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd stockwise
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Aplicar migraciones

```bash
python manage.py migrate
```

---

## 5. Crear superusuario

```bash
python manage.py createsuperuser
```

---

## 6. Ejecutar servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

---

# Flujo de Uso del Sistema

## 1. Iniciar sesión

Ingresar mediante:

```text
/login/
```

---

## 2. Gestionar categorías

Crear categorías para organizar los productos.

Ejemplos:

* Bebidas
* Alimentos
* Electrónicos
* Limpieza

---

## 3. Registrar productos

Registrar:

* Nombre
* Descripción
* Precio
* Stock
* Stock mínimo
* Categoría

---

## 4. Registrar entradas y salidas

Las entradas y salidas modifican automáticamente el stock.

Cada movimiento queda asociado al usuario autenticado.

---

## 5. Consultar reportes

Visualizar estadísticas, alertas y exportar información del inventario.

---

# Capturas del Sistema

## Login

*Agregar captura del login aquí.*

---

## Dashboard

*Agregar captura del dashboard aquí.*

---

## Productos

*Agregar captura del módulo productos aquí.*

---

## Reportes

*Agregar captura del módulo reportes aquí.*

---

# Posibles Mejoras Futuras

El proyecto fue diseñado con posibilidad de escalabilidad. Algunas mejoras futuras podrían ser:

* Sidebar colapsable
* Modo oscuro
* Dashboard analítico avanzado
* Integración con PostgreSQL
* API REST con Django REST Framework
* Sistema de roles y permisos
* Notificaciones en tiempo real
* Integración con APIs externas
* Sistema multiempresa

---

# Integrantes del Proyecto

* Integrante 1
* Integrante 2
* Integrante 3
* Integrante 4

---

# Estado del Proyecto

Proyecto funcional con:

* Dashboard interactivo
* CRUD completo
* Sistema de autenticación
* Reportes PDF y Excel
* Filtros y paginación
* Control automático de inventario
* Trazabilidad de movimientos por usuario
* Dashboard analítico
* Deploy en Render
* Interfaz moderna responsive

---

# Conclusión

StockWise permitió aplicar conceptos fundamentales de:

* Programación Orientada a Objetos (POO)
* Arquitectura MTV
* Desarrollo web con Django
* Gestión de bases de datos
* Diseño frontend responsive
* Seguridad web básica
* CRUD y lógica de negocio
* Visualización de datos
* Deploy cloud

El proyecto fue desarrollado con un enfoque escalable y modular, permitiendo futuras mejoras y ampliaciones.
 