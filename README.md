# FastAPI Library API 📚

Esta es una API REST desarrollada con **FastAPI** para gestionar una biblioteca de libros. Permite realizar operaciones como agregar, listar, obtener y eliminar libros utilizando una base de datos SQLite.

## **Requisitos** ⚙️

- Python 3.7 o superior.
- Dependencias de Python (FastAPI, Uvicorn, SQLAlchemy, Pydantic).

## **Instrucciones de Instalación** 🚀

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/JuannIM/IITA-API
   cd IITA-API
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**
   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - En **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Inicia la base de datos:**
   Para crear las tablas en la base de datos SQLite, corre el siguiente comando en Python:
   ```bash
   python -c "from app.database import init_db; init_db()"
   ```

6. **Ejecuta el servidor:**
   ```bash
   uvicorn app.main:app --reload
   ```

   Esto iniciará el servidor de desarrollo en **http://127.0.0.1:8000**.

---

## **Endpoints Disponibles** 🔧

La API tiene los siguientes endpoints para gestionar los libros:

### 1. **Crear un libro** ✍️
   - **URL:** `/books`
   - **Método:** `POST`
   - **Descripción:** Crea un nuevo libro en la biblioteca.
   - **Cuerpo de la solicitud (JSON):**
     ```json
     {
       "title": "El Gran Libro",
       "author": "Autor Ejemplo",
       "category": "Ficción",
       "available": true
     }
     ```
   - **Respuesta (JSON):**
     ```json
     {
       "id": 1,
       "title": "El Gran Libro",
       "author": "Autor Ejemplo",
       "category": "Ficción",
       "available": true
     }
     ```

### 2. **Obtener todos los libros** 📖
   - **URL:** `/books`
   - **Método:** `GET`
   - **Descripción:** Lista todos los libros en la biblioteca.
   - **Respuesta (JSON):**
     ```json
     [
       {
         "id": 1,
         "title": "El Gran Libro",
         "author": "Autor Ejemplo",
         "category": "Ficción",
         "available": true
       },
       {
         "id": 2,
         "title": "Otro Libro",
         "author": "Otro Autor",
         "category": "No Ficción",
         "available": false
       }
     ]
     ```

### 3. **Obtener un libro por ID** 🔍
   - **URL:** `/books/{book_id}`
   - **Método:** `GET`
   - **Descripción:** Obtiene los detalles de un libro específico por su ID.
   - **Respuesta (JSON):**
     ```json
     {
       "id": 1,
       "title": "El Gran Libro",
       "author": "Autor Ejemplo",
       "category": "Ficción",
       "available": true
     }
     ```

### 4. **Eliminar un libro** ❌
   - **URL:** `/books/{book_id}`
   - **Método:** `DELETE`
   - **Descripción:** Elimina un libro específico por su ID.
   - **Respuesta (JSON):**
     ```json
     {
       "message": "Book deleted"
     }
     ```

---

## **Pruebas con Swagger** 🧪

Puedes probar los endpoints de la API utilizando **Swagger UI**:

1. Abre tu navegador y dirígete a:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

2. Desde allí podrás interactuar con la API y probar todos los endpoints disponibles.

---

## **Notas** 📝

- La base de datos utilizada es **SQLite**, y el archivo de base de datos se crea automáticamente en la carpeta raíz del proyecto (`library.db`).
- Los datos no se persisten entre reinicios del servidor si no se realizan cambios en la base de datos.

---
