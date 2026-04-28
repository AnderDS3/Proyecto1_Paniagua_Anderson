# proyecto1_Paniagua_Anderson

Calculadora de fracciones con interfaz gráfica, desarrollada en Python usando el patrón MVC.

---

## ¿Qué hace?

Permite al usuario ingresar fracciones y realizar las siguientes operaciones:

- Sumar, restar, multiplicar y dividir todas las fracciones ingresadas
- Encontrar la fracción mayor y la menor
- Ordenar las fracciones de mayor a menor
- Simplificar fracciones automáticamente
- Limpiar la lista de fracciones

---

## Estructura del proyecto

```
Proyecto1_Paniagua_Anderson/
├── README.md          ← instrucciones de ejecución
├── requirements.txt   ← librerías necesarias (ninguna en este caso)
├── datos/
│   └── fracciones.json  ← datos de prueba
├── src/               ← código fuente principal
│   ├── main.py        ← punto de entrada, arranca la app
│   ├── models/
│   │   └── model.py   ← lógica de las fracciones
│   ├── views/
│   │   └── view.py    ← interfaz gráfica
│   └── controllers/
│       └── controller.py ← conecta modelo y vista
├── tests/
│   └── test_fracciones.py ← pruebas automáticas
└── venv/              ← entorno virtual (no se entrega)

```

---

## Requisitos

No requiere librerías externas. Solo necesitas tener **Python 3** instalado.

---

## ¿Cómo ejecutar?

Desde la terminal del proyecto, corre:

```bash ejecutar:
python src/main.py
```

---

## ¿Cómo correr los tests?

Desde la terminal del proyecto, corre:

```bash ejecutar:
python -m unittest discover tests
```

---

## Autor

Anderson Paniagua Dany
